# -- coding: utf-8 --
# @Time    : 2024/2/10 15:27
# @Author  : TangKai
# @Team    : ZheChengData

import os
import pyproj
import numpy as np
import pandas as pd
import multiprocessing
import geopandas as gpd
from shapely.ops import linemerge
from shapely.ops import transform
import xml.etree.cElementTree as ET
from ..tools.group import cut_group
from ..WrapsFunc import function_time_cost
from shapely.geometry import LineString, Point, Polygon


"""SUMO路网转换的相关方法"""

EDGE_ID_KEY = 'id'
EDGE_FROM_KEY = 'from'
EDGE_TO_KEY = 'to'
EDGE_SPEED_KEY = 'speed'
EDGE_LANES_KEY = 'numLanes'
EDGE_PRIORITY_KEY = 'priority'
EDGE_SHAPE_KEY = 'shape'
EDGE_FUNCTION_KEY = 'function'

LANE_ID_KEY = 'id'
LANE_SPEED_KEY = 'speed'
LANE_LENGTH_KEY = 'length'
LANE_WIDTH_KEY = 'width'
LANE_INDEX_KEY = 'index'
LANE_SHAPE_KEY = 'shape'
DEFAULT_LANE_WIDTH = '3.2'
DEFAULT_LANE_SPEED = '9.0'

NODE_ID_KEY = 'id'
NODE_X_KEY = 'x'
NODE_Y_KEY = 'y'
NODE_TYPE_KEY = 'type'
NODE_COV_BOUND_KEY = 'convBoundary'

JUNCTION_ID_KEY = 'id'
JUNCTION_TYPE_KEY = 'type'
JUNCTION_X_KEY = 'x'
JUNCTION_Y_KEY = 'y'
JUNCTION_SHAPE_KEY = 'shape'

CONN_FROM_EDGE_KEY = 'from'
CONN_TO_EDGE_KEY = 'to'
CONN_FROM_LANE_KEY = 'fromLane'
CONN_TO_LANE_KEY = 'toLane'
CONN_VIA_KEY = 'via'

geometry_field = 'geometry'

class SumoConvert(object):
    def __init__(self):
        pass

    # 1.从解耦的node和edge文件生产shp层
    def get_plain_shp(self, plain_edge_path: str = None, plain_node_path: str = None, crs: str = None) -> \
            tuple[gpd.GeoDataFrame, gpd.GeoDataFrame]:
        """
        从解耦的node和edge文件生产shp层
        :param plain_edge_path:
        :param plain_node_path:
        :param crs:
        :return:
        """
        # 先解析节点
        node_tree = ET.parse(plain_node_path)
        node_root = node_tree.getroot()
        node_df = self.parse_node_plain(plain_node_root=node_root)

        node_loc_dict = {node_id: (x, y) for node_id, x, y in
                         zip(node_df[NODE_ID_KEY], node_df[NODE_X_KEY], node_df[NODE_Y_KEY])}

        node_df[geometry_field] = node_df.apply(lambda xy: Point((xy[NODE_X_KEY], xy[NODE_Y_KEY])), axis=1)
        node_df.drop(columns=[NODE_X_KEY, NODE_Y_KEY], axis=1, inplace=True)
        node_gdf = gpd.GeoDataFrame(node_df, geometry=geometry_field, crs=crs)
        del node_df

        # 再解析edge
        edge_tree = ET.parse(plain_edge_path)
        edge_root = edge_tree.getroot()
        edge_df = self.parse_edge_plain(plain_edge_root=edge_root, node_loc_dict=node_loc_dict)

        # 生产几何列
        edge_df[geometry_field] = edge_df[EDGE_SHAPE_KEY].apply(lambda shape: LineString(shape))
        edge_df.drop(columns=[EDGE_SHAPE_KEY], axis=1, inplace=True)

        edge_gdf = gpd.GeoDataFrame(edge_df, geometry=geometry_field, crs=crs)
        del edge_df

        return edge_gdf, node_gdf

    @staticmethod
    def parse_node_plain(plain_node_root: ET.Element = None) -> pd.DataFrame:
        """
        解析node文件
        :param plain_node_root:
        :return:
        """
        item_list: list[list[str, float, float, str]] = list()
        for child in plain_node_root:
            if child.tag == 'node':
                node_id, node_x, node_y, node_type = child.get(NODE_ID_KEY), float(child.get(NODE_X_KEY)), float(
                    child.get(
                        NODE_Y_KEY)), child.get(NODE_TYPE_KEY)
                item_list.append([node_id, node_x, node_y, node_type])
        return pd.DataFrame(item_list, columns=[NODE_ID_KEY, NODE_X_KEY, NODE_Y_KEY, NODE_TYPE_KEY])

    @staticmethod
    def parse_edge_plain(plain_edge_root: ET.Element = None, node_loc_dict: dict = None) -> pd.DataFrame:
        """
        解析edge文件
        :param plain_edge_root:
        :param node_loc_dict:
        :return:
        """
        edge_item_list = []
        for child in plain_edge_root:
            if child.tag == 'edge':
                edge_id, from_node, to_node, priority, lanes, speed, shape = child.get(EDGE_ID_KEY), child.get(
                    EDGE_FROM_KEY), child.get(
                    EDGE_TO_KEY), int(child.get(EDGE_PRIORITY_KEY)), int(child.get(EDGE_LANES_KEY)), \
                    float(child.get(EDGE_SPEED_KEY)), child.get(EDGE_SHAPE_KEY)
                if shape is None:
                    shape = [node_loc_dict[from_node], node_loc_dict[to_node]]
                else:
                    shape = [list(map(float, xy.split(','))) for xy in shape.split(' ')]
                edge_item_list.append([edge_id, from_node, to_node, priority, lanes, speed, shape])

        edge_df = pd.DataFrame(edge_item_list,
                               columns=[EDGE_ID_KEY, EDGE_FROM_KEY, EDGE_TO_KEY, EDGE_PRIORITY_KEY, EDGE_LANES_KEY,
                                        EDGE_SPEED_KEY, EDGE_SHAPE_KEY])
        return edge_df

    # 2.解析net.xml文件
    @function_time_cost
    def get_net_shp(self, net_path: str = None, crs: str = None, core_num: int = 1, l_threshold: float = 1.0) -> \
            tuple[gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, pd.DataFrame]:
        """
        从net.xml解析微观车道级路网
        :param net_path:
        :param crs:
        :param core_num
        :param l_threshold
        :return:
        """
        core_num = os.cpu_count() if core_num > os.cpu_count() else core_num
        net_tree = ET.parse(net_path)

        net_root = net_tree.getroot()
        location_ele = net_root.findall('location')[0]
        try:
            prj4_str = location_ele.get('projParameter')
        except:
            prj4_str = None

        if crs is None:
            assert prj4_str is not None
            crs = 'EPSG:' + prj4_2_crs(prj4_str=prj4_str)
        try:
            x_offset, y_offset = list(map(float, location_ele.get('netOffset').split(',')))
        except:
            x_offset, y_offset = 0, 0

        all_edge_ele = list(net_root.findall('edge'))
        all_junction_ele = list(net_root.findall('junction'))
        all_conn_ele = list(net_root.findall('connection'))

        if core_num > 1:
            # 分组
            edge_ele_group = cut_group(obj_list=all_edge_ele, n=core_num)
            junction_ele_group = cut_group(obj_list=all_junction_ele, n=core_num)
            conn_ele_group = cut_group(obj_list=all_conn_ele, n=core_num)

            edge_ele_group_len, junction_ele_group_len, conn_ele_group_len = \
                len(edge_ele_group), len(junction_ele_group), len(conn_ele_group)

            max_len = max([edge_ele_group_len, junction_ele_group_len, conn_ele_group_len])

            junction_ele_group.extend([] * (max_len - junction_ele_group_len))
            edge_ele_group.extend([] * (max_len - edge_ele_group_len))
            conn_ele_group.extend([] * (max_len - conn_ele_group_len))

            del all_edge_ele, all_junction_ele, all_conn_ele

            pool = multiprocessing.Pool(processes=core_num)
            result_list = []
            for i in range(len(edge_ele_group)):
                result = pool.apply_async(self.parse_elements,
                                          args=(edge_ele_group[i], junction_ele_group[i], conn_ele_group[i], x_offset, y_offset))
                result_list.append(result)
            pool.close()
            pool.join()

            # 车道线, edge中心线, 交叉口面域
            lane_gdf, avg_edge_gdf, junction_gdf, conn_df = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

            for res in result_list:
                _lane_df, _avg_edge_df, _junction_df, _conn_df = res.get()
                lane_gdf = pd.concat([lane_gdf, _lane_df])
                avg_edge_gdf = pd.concat([avg_edge_gdf, _avg_edge_df])
                junction_gdf = pd.concat([junction_gdf, _junction_df])
                conn_df = pd.concat([_conn_df, conn_df])
            lane_gdf.reset_index(inplace=True, drop=True)
            avg_edge_gdf.reset_index(inplace=True, drop=True)
            junction_gdf.reset_index(inplace=True, drop=True)
            conn_df.reset_index(inplace=True)
            del result_list
        else:
            lane_gdf, avg_edge_gdf, junction_gdf, conn_df = self.parse_elements(edge_ele_list=all_edge_ele,
                                                                                junction_ele_list=all_junction_ele,
                                                                                conn_ele_list=all_conn_ele,
                                                                                x_offset=x_offset, y_offset=y_offset)

        junction_gdf = gpd.GeoDataFrame(junction_gdf, geometry=geometry_field, crs=crs)
        lane_gdf = gpd.GeoDataFrame(lane_gdf, geometry=geometry_field, crs=crs)
        avg_edge_gdf.drop(index=avg_edge_gdf[avg_edge_gdf['function'] == 'internal'].index, axis=0, inplace=True)
        avg_edge_gdf = gpd.GeoDataFrame(avg_edge_gdf, geometry=geometry_field, crs=crs)

        try:
            lane_gdf[geometry_field] = lane_gdf[geometry_field].remove_repeated_points(l_threshold)
            avg_edge_gdf[geometry_field] = avg_edge_gdf[geometry_field].remove_repeated_points(l_threshold)
        except:
            lane_gdf[geometry_field] = lane_gdf[geometry_field].simplify(l_threshold / 5)
            avg_edge_gdf[geometry_field] = avg_edge_gdf[geometry_field].simplify(l_threshold / 5)
        try:
            lane_gdf[geometry_field] = lane_gdf[geometry_field].simplify(1e-5)
            avg_edge_gdf[geometry_field] = avg_edge_gdf[geometry_field].simplify(1e-5)
        except:
            pass

        lane_polygon_gdf = lane_gdf[lane_gdf['function'] != 'internal'].copy()
        lane_polygon_gdf[geometry_field] = \
            lane_polygon_gdf.apply(lambda item:
                                   get_off_polygon(l=item[geometry_field],
                                                   off_line_l=(item[
                                                                   LANE_WIDTH_KEY] - 0.01) / 2),
                                   axis=1)
        conn_df = self.process_conn(pre_conn_df=conn_df)

        conn_gdf = self.tess_lane(conn_df=conn_df, lane_gdf=lane_gdf)

        avg_conn = conn_gdf.drop_duplicates(subset=['from_edge', 'to_edge'], keep='first')[['from_edge', 'to_edge']]
        avg_edge_geo_map = {edge: geo for edge, geo in zip(avg_edge_gdf['edge_id'], avg_edge_gdf[geometry_field])}
        avg_conn[geometry_field] = avg_conn.apply(
            lambda row: LineString([list(avg_edge_geo_map[row['from_edge']].coords)[-1],
                                    list(avg_edge_geo_map[row['to_edge']].coords)[0]]), axis=1,
            result_type='expand')
        del avg_conn['from_edge'], avg_conn['to_edge']
        avg_conn['function'] = 'conn'
        avg_conn = gpd.GeoDataFrame(avg_conn, geometry=geometry_field, crs=avg_edge_gdf.crs)
        avg_edge_gdf = pd.concat([avg_edge_gdf, avg_conn])
        avg_edge_gdf.reset_index(inplace=True, drop=True)
        return lane_gdf, junction_gdf, lane_polygon_gdf, avg_edge_gdf, conn_gdf

    @staticmethod
    def tess_lane(conn_df: pd.DataFrame = None, lane_gdf: gpd.GeoDataFrame = None) -> gpd.GeoDataFrame:
        normal_lane = lane_gdf[~lane_gdf['edge_id'].str.startswith(':')].copy()
        conn_lane = lane_gdf[lane_gdf['edge_id'].str.startswith(':')].copy()
        # print(normal_lane)
        # print(conn_lane)
        conn_df = conn_df.explode(column=['via'], ignore_index=True)
        conn_lane['lane_id'] = conn_lane['edge_id'].astype(str) + '_' + conn_lane['index'].astype(str)

        conn_df = pd.merge(conn_df, conn_lane[['lane_id', geometry_field]], left_on='via', right_on=['lane_id'])
        conn_df = conn_df.groupby(['from_edge', 'from_lane_index',
                                   'to_edge', 'to_lane_index']).agg({geometry_field: list}).reset_index(drop=False)
        conn_df[geometry_field] = conn_df[geometry_field].apply(lambda x: linemerge(x))
        conn_gdf = gpd.GeoDataFrame(conn_df, geometry=geometry_field, crs=lane_gdf.crs)
        return conn_gdf

    def parse_elements(self, edge_ele_list: list[ET.Element] = None, junction_ele_list: list[ET.Element] = None,
                       conn_ele_list: list[ET.Element] = None, x_offset: float = 0.0, y_offset: float = 0.0) \
            -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """
        :param edge_ele_list:
        :param junction_ele_list
        :param conn_ele_list
        :param x_offset
        :param y_offset
        :return:
        """
        lane_item_list, avg_edge_item_list = list(), list()
        for edge_ele in edge_ele_list:
            _lane_item_list, avg_edge_item = self.parse_net_edge(net_edge_obj=edge_ele, x_offset=x_offset,
                                                                 y_offset=y_offset)
            lane_item_list.extend(_lane_item_list)
            avg_edge_item_list.append(avg_edge_item)
        lane_df = pd.DataFrame(lane_item_list,
                               columns=['edge_' + EDGE_ID_KEY, EDGE_FROM_KEY, EDGE_TO_KEY, EDGE_FUNCTION_KEY,
                                        LANE_INDEX_KEY, LANE_SPEED_KEY, LANE_LENGTH_KEY, LANE_WIDTH_KEY,
                                        LANE_SHAPE_KEY, 'allow'])
        avg_edge_df = pd.DataFrame(avg_edge_item_list,
                                   columns=['edge_' + EDGE_ID_KEY, EDGE_FROM_KEY, EDGE_TO_KEY, EDGE_FUNCTION_KEY,
                                            EDGE_SHAPE_KEY, EDGE_SPEED_KEY])
        lane_df.rename(columns={EDGE_SHAPE_KEY: geometry_field}, inplace=True)
        avg_edge_df.rename(columns={EDGE_SHAPE_KEY: geometry_field}, inplace=True)

        junction_item_list = list()
        for junction_ele in junction_ele_list:
            junction_item = self.parse_net_junction(junction_obj=junction_ele)
            junction_item_list.append(junction_item)

        junction_df = pd.DataFrame(junction_item_list, columns=[JUNCTION_ID_KEY, JUNCTION_TYPE_KEY,
                                                                JUNCTION_X_KEY, JUNCTION_Y_KEY, JUNCTION_SHAPE_KEY])
        junction_df.rename(columns={JUNCTION_SHAPE_KEY: geometry_field}, inplace=True)

        conn_item_list = list()
        for conn_ele in conn_ele_list:
            conn_item_list.append(self.parse_connection(conn_ele))
        conn_df = pd.DataFrame(conn_item_list, columns=[CONN_FROM_EDGE_KEY, CONN_TO_EDGE_KEY, CONN_FROM_LANE_KEY,
                                                        CONN_TO_LANE_KEY, CONN_VIA_KEY])
        return lane_df, avg_edge_df, junction_df, conn_df

    @staticmethod
    def parse_net_edge(net_edge_obj: ET.Element = None, x_offset: float = 0.0, y_offset: float = 0.0) -> \
            tuple[
                list[list[str, str, str, str, int, float, float, float, LineString, str]],
                list[str, str, str, str, LineString, float]
            ]:
        """

        :param net_edge_obj:
        :param x_offset
        :param y_offset
        :return:
        """
        edge_id = net_edge_obj.get(EDGE_ID_KEY)
        edge_from, edge_to = net_edge_obj.get(EDGE_FROM_KEY), net_edge_obj.get(EDGE_TO_KEY)
        lane_item_list: list[list[str, str, str, str, int, float, float, float, LineString]] = []

        edge_function = net_edge_obj.get(EDGE_FUNCTION_KEY)
        edge_function = 'normal' if edge_function is None else edge_function
        lane_speed_list = list()
        avg_line_shape_list = []
        for lane_obj in net_edge_obj:

            lane_id, lane_index, lane_shape, lane_length, = lane_obj.get(LANE_ID_KEY), \
                lane_obj.get(LANE_INDEX_KEY), lane_obj.get(
                LANE_SHAPE_KEY), lane_obj.get(LANE_LENGTH_KEY)

            lane_allow = lane_obj.get('allow')
            if lane_allow is None:
                lane_allow = 'passenger'

            if lane_id is None or lane_index is None:
                # print(net_edge_obj.get(EDGE_ID_KEY))
                continue

            lane_speed, lane_width = float(try_get_v(lane_obj, LANE_SPEED_KEY, DEFAULT_LANE_SPEED)), \
                float(try_get_v(lane_obj, LANE_WIDTH_KEY, DEFAULT_LANE_WIDTH))
            lane_speed_list.append(lane_speed)
            lane_shape = [list(map(float, xy.split(','))) for xy in lane_shape.split(' ')]
            lane_shape = np.array(lane_shape) - np.array([x_offset, y_offset])
            avg_line_shape_list.append(lane_shape)
            lane_shape = LineString(lane_shape)

            if lane_length is None:
                lane_length = lane_shape.length

            lane_item_list.append(
                [edge_id, edge_from, edge_to, edge_function, int(lane_index), float(lane_speed),
                 float(lane_length), float(lane_width), lane_shape, lane_allow])

        avg_center_line = LineString()
        avg_speed = DEFAULT_LANE_SPEED
        if edge_function == 'normal':
            try:
                avg_center_line = LineString(
                    np.array(avg_line_shape_list).mean(axis=0))
            except Exception as e:
                print(repr(e))
                _l = len(avg_line_shape_list)
                select_line = [avg_line_shape_list[int(_l / 2)]]
                avg_center_line = LineString(
                    np.array(select_line).mean(axis=0))

            avg_speed = np.array(lane_speed_list).mean()

        return lane_item_list, [edge_id, edge_from, edge_to, edge_function, avg_center_line, avg_speed]

    @staticmethod
    def parse_net_junction(junction_obj: ET.Element = None) -> list[str, str, float, float, Polygon]:
        """

        :param junction_obj:
        :return:
        """
        junction_id, junction_type, junction_x, junction_y, junction_shape = \
            junction_obj.get(JUNCTION_ID_KEY), junction_obj.get(JUNCTION_TYPE_KEY), junction_obj.get(JUNCTION_X_KEY), \
            junction_obj.get(JUNCTION_Y_KEY), junction_obj.get(JUNCTION_SHAPE_KEY)
        try:
            junction_x, junction_y = float(junction_x), float(junction_y)
        except TypeError:
            pass
        if junction_type == 'internal':
            junction_shape = Polygon(list(Point(junction_x, junction_y).buffer(1.5).exterior.coords))
        else:
            junction_shape = [list(map(float, xy.split(','))) for xy in junction_shape.split(' ')]
            _l = len(junction_shape)
            if _l >= 3:
                junction_shape = Polygon(junction_shape)
            elif _l == 2:
                junction_shape = LineString(junction_shape).buffer(1.0)
            else:
                junction_shape = LineString(list(Point(junction_x, junction_y).buffer(1.5).exterior.coords))

        return [junction_id, junction_type, junction_x, junction_y, junction_shape]

    @staticmethod
    def parse_connection(conn_obj: ET.Element = None) -> tuple[str, str, str, str, str]:
        from_edge, to_edge, from_lane, to_lane, via_lane = \
            conn_obj.get(CONN_FROM_EDGE_KEY), conn_obj.get(CONN_TO_EDGE_KEY), conn_obj.get(CONN_FROM_LANE_KEY), \
            conn_obj.get(CONN_TO_LANE_KEY), None
        try:
            via_lane = conn_obj.get(CONN_VIA_KEY)
        except Exception:
            pass
        return from_edge, to_edge, from_lane, to_lane, via_lane

    @staticmethod
    def process_conn(pre_conn_df: pd.DataFrame = None):
        pre_conn_df['from_lane_id'] = pre_conn_df[CONN_FROM_EDGE_KEY] + '_' + pre_conn_df[CONN_FROM_LANE_KEY]
        pre_conn_df['to_lane_id'] = pre_conn_df[CONN_TO_EDGE_KEY] + '_' + pre_conn_df[CONN_TO_LANE_KEY]

        cm = pre_conn_df['from_lane_id'].str.startswith(':')
        a_pre_conn_df = pre_conn_df[~cm].copy()
        b_pre_conn_df = pre_conn_df[cm].copy()
        entrance_exit_list = []
        turn_list = []
        a_pre_conn_df.reset_index(inplace=True, drop=True)
        a_pre_conn_df['from_edge'] = a_pre_conn_df[EDGE_FROM_KEY]
        for row in a_pre_conn_df.itertuples():
            from_lane_id, to_lane_id, via_lane_id = getattr(row, 'from_lane_id'), getattr(row, 'to_lane_id'), \
                getattr(row, 'via')
            from_edge, from_lane_index, to_edge, to_lane_index = getattr(row, 'from_edge'), \
                getattr(row, CONN_FROM_LANE_KEY), getattr(row, CONN_TO_EDGE_KEY), getattr(row, CONN_TO_LANE_KEY)
            entrance_exit_list.append([from_edge, from_lane_index, to_edge, to_lane_index])
            _turn = []
            _x = b_pre_conn_df[b_pre_conn_df['from_lane_id'] == via_lane_id]
            while not _x.empty:
                _turn.append(via_lane_id)
                via_lane_id = _x.at[_x.index[0], 'via']
                _x = b_pre_conn_df[b_pre_conn_df['from_lane_id'] == via_lane_id]
            turn_list.append(_turn)
        res = pd.DataFrame(entrance_exit_list, columns=['from_edge', 'from_lane_index', 'to_edge', 'to_lane_index'])
        res['via'] = turn_list
        return res

    # 转换plain edge和plain node文件的坐标系
    def convert_plain_crs(self, plain_edge_path: str = None, plain_node_path: str = None, from_crs='EPSG:4326',
                          to_crs='EPSG:32650') -> tuple[ET.ElementTree, ET.ElementTree]:
        node_tree = ET.parse(plain_node_path)
        node_root = node_tree.getroot()

        edge_tree = ET.parse(plain_edge_path)
        edge_root = edge_tree.getroot()

        self.convert_plain_node_crs(node_root, from_crs=from_crs, to_crs=to_crs)
        self.convert_plain_edge_crs(edge_root, from_crs=from_crs, to_crs=to_crs)

        return node_tree, edge_tree

    # 转换plain_edge
    @staticmethod
    def convert_plain_edge_crs(plain_edge_root: ET.Element = None,
                               from_crs='EPSG:4326', to_crs='EPSG:32650'):

        for child in plain_edge_root:
            if child.tag == 'edge':
                shape = child.get(EDGE_SHAPE_KEY)
                if shape is None:
                    pass
                else:
                    shape = [list(map(float, xy.split(','))) for xy in shape.split(' ')]
                    origin_p = [Point(loc) for loc in shape]
                    xfer_p = [prj_xfer(origin_p=p, from_crs=from_crs, to_crs=to_crs) for p in origin_p]
                    xfer_shape = [[_xfer_p.x, _xfer_p.y] for _xfer_p in xfer_p]
                    child.set(EDGE_SHAPE_KEY, ' '.join([','.join(list(map(str, loc))) for loc in xfer_shape]))

    @staticmethod
    def convert_plain_node_crs(plain_node_root: ET.Element = None, from_crs='EPSG:4326',
                               to_crs='EPSG:32650') -> None:
        for child in plain_node_root:
            if child.tag == 'node':
                node_x, node_y = float(child.get(NODE_X_KEY)), float(child.get(NODE_Y_KEY))
                xfer_p = prj_xfer(from_crs=from_crs, to_crs=to_crs, origin_p=Point(node_x, node_y))
                child.set(NODE_X_KEY, str(xfer_p.x))
                child.set(NODE_Y_KEY, str(xfer_p.y))
            elif child.tag == 'location':
                # "120.29231071,31.60290186,120.29565375,31.60509861"
                conv_boundary = child.get(NODE_COV_BOUND_KEY).split(',')
                p1, p2 = Point(conv_boundary[0], conv_boundary[1]), Point(conv_boundary[2], conv_boundary[3])
                xfer_p1, xfer_p2 = prj_xfer(from_crs=from_crs, to_crs=to_crs, origin_p=p1), prj_xfer(
                    from_crs=from_crs, to_crs=to_crs, origin_p=p2)
                child.set(NODE_COV_BOUND_KEY, ','.join(list(map(str, [xfer_p1.x, xfer_p1.y, xfer_p2.x, xfer_p2.y]))))


def try_get_v(item_obj: ET.Element = None, k: str = None, default: str = None):
    res = item_obj.get(k)
    if res is None:
        return default
    else:
        return res


def get_off_polygon(l: LineString = None, off_line_l: float = 1.8):
    a = l.offset_curve(off_line_l)
    b = l.offset_curve(-off_line_l)
    a_list, b_list = list(a.coords), list(b.coords)
    return Polygon(a_list + b_list[::-1])


def prj4_2_crs(prj4_str: str = None) -> str:
    crs = pyproj.CRS(prj4_str)
    x = crs.to_epsg()
    return str(x)


def prj_xfer(from_crs: str = 'EPSG:32650', to_crs: str = 'EPSG:4326', origin_p: Point = None) -> Point:
    f = pyproj.CRS(from_crs)
    t = pyproj.CRS(to_crs)
    project = pyproj.Transformer.from_crs(f, t, always_xy=True).transform
    xfer_point = transform(project, origin_p)
    return xfer_point

