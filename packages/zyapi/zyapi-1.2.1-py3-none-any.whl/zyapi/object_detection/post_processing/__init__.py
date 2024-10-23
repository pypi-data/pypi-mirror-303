# coding: utf-8
from ..utils import *


class ImageProcess(object):
    """图片处理类"""

    def __init__(self, image, result_boxes, mode, face_distinguish):
        self.dev_params = None
        self.face_boxes = None
        self.roi_list = None
        self.out_result = None  # 最后告警推送的时候使用
        self.alarm_info_dict = None
        self.behavior_result = {}
        self.image = image
        self.out_boxes = result_boxes  # 最后人数统计时使用
        self.ele_fence_mode = mode  # all_in /half_in /all_out/half_out
        self.face_distinguish = face_distinguish

    def point_in_polygon(self, x, y, verts):
        """
        PNPoly算法, 判断是否在区域内

        Args:
            x: x轴坐标
            y: y轴坐标
            verts: [(x1, y1), (x2, y2), (x3, y3), ...]
        Return:
            True or False
        """
        try:
            x, y = float(x), float(y)
        except:
            return False
        vertx = [xyvert[0] for xyvert in verts]
        verty = [xyvert[1] for xyvert in verts]
        if not verts or not min(vertx) <= x <= max(vertx) or not min(verty) <= y <= max(verty):
            return False

        nvert = len(verts)
        is_in = False
        for i in range(nvert):
            j = nvert - 1 if i == 0 else i - 1
            if ((verty[i] > y) != (verty[j] > y)) and (
                    x < (vertx[j] - vertx[i]) * (y - verty[i]) / (verty[j] - verty[i]) + vertx[i]):
                is_in = not is_in

        return is_in

    def overlap_in_area(self, bbox, roi, iou=0.8):
        """
        交并比算法, 通过判断重叠面积，判断bbox和roi是否重叠，且大于阈值

        Args:
            bbox: [x_min, y_min, x_max, y_max]
            roi: [x_min, y_min, x_max, y_max]
        Return:
            True or False
        """
        s_tl_x, s_tl_y, s_br_x, s_br_y = bbox[0], bbox[1], bbox[2], bbox[3]
        m_tl_x, m_tl_y, m_br_x, m_br_y = roi[0], roi[1], roi[2], roi[3]
        # 计算相交部分的坐标
        x_min = max(s_tl_x, m_tl_x)
        x_max = min(s_br_x, m_br_x)
        y_min = max(s_tl_y, m_tl_y)
        y_max = min(s_br_y, m_br_y)
        inter_h = max(y_max - y_min + 1, 0)
        inter_w = max(x_max - x_min + 1, 0)
        inter = inter_h * inter_w
        if inter == 0:
            return False
        else:
            if inter / ((s_br_y - s_tl_y) * (s_br_x - s_tl_x)) >= iou:
                return True
            else:
                return False

    def check_point_in_area(self, behavior_mode):
        """
        根据behavior_mode来筛选bbox

        Args:
            behavior_mode (str): in/out
        Return:
            boxes: 筛选后的bbox
            roi_info_list: [{'roi_name': str, roi: list, 'boxes': list, cls: list}, {}, {}]
        """
        boxes = []
        roi_info_list = []
        for rois in self.roi_list:
            roi_cls = []
            roi_boxes = []  # 符合该roi区域的bbox
            verts = []  # 多边形顶点列表
            is_in = 0
            for roi in rois['roi']:
                verts.append((float(roi[0]), float(roi[1])))
            for box in self.boxes:
                x1, y1, x2, y2 = box[0], (box[3] - box[1]) / 2 + box[1], box[2], (box[3] - box[1]) / 2 + box[
                    1]  # 获取bbox中线坐标
                cx = abs(x1 + x2) / 2
                if behavior_mode == "in":  # 标记为in，则为闯入检查，box在roi区域内，就输出结果
                    if self.ele_fence_mode == "all_in":  # box中线都在roi中
                        result = self.point_in_polygon(float(x1), float(y1), verts) and self.point_in_polygon(float(x2),
                                                                                                              float(y2),
                                                                                                              verts)
                    elif self.ele_fence_mode == "half_in":  # box中点坐标在roi中
                        result = self.point_in_polygon(float(cx), float(y1), verts)
                    elif self.ele_fence_mode == 'overlap_in':  # 通过面积判断
                        result = check_overlapped_area(verts, box, overlap=0.6)
                    if result:
                        boxes.append(box[:4])  # 符合条件的添加到返回列表
                        roi_boxes.append(box[:4])
                        roi_cls.append(box[-1])
                elif behavior_mode == "out":  # 标记为out，脱岗检测
                    if self.ele_fence_mode == "all_out":  # box与roi没有交集才算脱岗
                        result = check_overlapped_area(verts, box, overlap=1)
                    elif self.ele_fence_mode == "half_out":  # box中点没在roi才算脱岗
                        result = self.point_in_polygon(float(cx), float(y1), verts)
                    elif self.ele_fence_mode == "klx_out":  # 长时间无医护人员护理
                        result = self.point_in_polygon(float(cx), float(y1), verts)
                    if result:
                        is_in += 1
            if behavior_mode == "out":  # 脱岗需要检查此步骤
                if is_in == 0 and self.ele_fence_mode == "half_out":
                    rois['cls'] = ['out']
                    rois['boxes'] = [[0, 0, 5, 5]]
                    roi_info_list.append(rois)
                if is_in == 1 and self.ele_fence_mode == "klx_out":
                    rois['cls'] = ['out']
                    rois['boxes'] = [rois['roi']]
                    roi_info_list.append(rois)
            else:
                # bug修复：需确保区域内有boxes才添加到roi_info_list中, 防止累计一定此数后，返回的当前结果为[], 此后roi_info_list中有值，对应区域内才会计算ftime
                if len(roi_boxes):
                    rois['cls'] = roi_cls
                    rois['boxes'] = roi_boxes
                    roi_info_list.append(rois)
        return boxes, roi_info_list

    def roi_area(self):
        """
        计算设置区域的四边形面积

        Return:
            area: 多边形的面积
        """
        poly = Polygon(self.roi_list)
        area = poly.area
        return area

    def threshold_filter(self, index_list, out_scores, threshold):
        """
        阈值判断

        Args:
            index_list: 识别到的指定行为的多个索引
            out_scores: 识别到的所有阈值
            threshold: 阈值
        Return:
            阈值符合的索引结果列表
        """
        return [i for i in index_list if float(threshold) <= out_scores[i]]

    def label_contrary(self, label, out_class):
        """
        标签取反

        Args:
            label: 需要取反的标签
            out_class: 所有的识别结果
        Return:
            True: 代表out_class内无label标签
            False: 代表out_class内有label标签
        """
        return True if label not in out_class else False

    def target_size(self, setting_h, setting_w):
        """
        目标大小判断

        Args：
            setting_h: 设置的目标高
            setting_w: 设置的目标宽
        """
        return [box for box in self.boxes if box[3] - box[1] >= setting_h and box[2] - box[0] >= setting_w]