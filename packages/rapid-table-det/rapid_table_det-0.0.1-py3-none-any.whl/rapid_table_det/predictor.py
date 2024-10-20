import time

from rapid_table_det.utils import *

MODEL_STAGES_PATTERN = {
    "PPLCNet": ["blocks2", "blocks3", "blocks4", "blocks5", "blocks6"]
}
root_dir = Path(__file__).resolve().parent
root_dir_str = str(root_dir)
# https://github.com/RapidAI/TableStructureRec/releases/download/v0.0.0/lineless_table_rec_models.zip
# obj_model_path = f"{root_dir_str}/obj_det.onnx"
# dbnet_model_path = f"{root_dir_str}/edge_det.onnx"
# pplcnet_model_path = f"{root_dir_str}/cls_det.onnx"


class ObjectDetector:
    model_key = "obj_det"

    def __init__(self, model_path, **kwargs):
        self.model = OrtInferSession(model_path)
        self.img_loader = LoadImage()
        self.resize_shape = [928, 928]

    def __call__(self, img, **kwargs):
        start = time.time()
        score = kwargs.get("score", 0.4)
        img = self.img_loader(img)
        ori_h, ori_w = img.shape[:-1]
        img, im_shape, factor = self.img_preprocess(img, self.resize_shape)
        pre = self.model([img, factor])
        result = []
        for item in pre[0]:
            cls, value, xmin, ymin, xmax, ymax = list(item)
            if value < score:
                continue
            cls, xmin, ymin, xmax, ymax = [
                int(x) for x in [cls, xmin, ymin, xmax, ymax]
            ]
            xmin = max(xmin, 0)
            ymin = max(ymin, 0)
            xmax = min(xmax, ori_w)
            ymax = min(ymax, ori_h)
            result.append([value, np.array([xmin, ymin, xmax, ymax])])
        return result, time.time() - start

    def img_preprocess(self, img, resize_shape=[928, 928]):
        im_info = {
            "scale_factor": np.array([1.0, 1.0], dtype=np.float32),
            "im_shape": np.array(img.shape[:2], dtype=np.float32),
        }
        im, im_info = resize(img, im_info, resize_shape, False)
        im, im_info = pad(im, im_info, resize_shape)
        im = im / 255.0
        im = im.transpose((2, 0, 1)).copy()
        im = im[None, :]
        factor = im_info["scale_factor"].reshape((1, 2))
        im_shape = im_info["im_shape"].reshape((1, 2))
        return im, im_shape, factor


class DbNet:
    model_key = "edge_det"

    def __init__(self, model_path, **kwargs):
        self.model = OrtInferSession(model_path)
        self.img_loader = LoadImage()
        self.resize_shape = [800, 800]

    def __call__(self, img, **kwargs):
        start = time.time()
        img = self.img_loader(img)
        destHeight, destWidth = img.shape[:-1]
        img, resize_h, resize_w, left, top = self.img_preprocess(img, self.resize_shape)
        # with paddle.no_grad():
        predict_maps = self.model([img])
        # predict_maps = predicts.cpu()
        pred = np.squeeze(predict_maps[0])
        segmentation = pred > 0.7
        mask = np.array(segmentation).astype(np.uint8)
        # 找到最佳边缘box shape(4, 2)
        box = get_max_adjacent_bbox(mask)
        # todo 注意还有crop的偏移
        if box is not None:
            # 根据缩放调整坐标适配输入的img大小
            adjusted_box = self.adjust_coordinates(
                box, left, top, resize_w, resize_h, destWidth, destHeight
            )
            # 排序并裁剪负值
            lt, lb, rt, rb = self.sort_and_clip_coordinates(adjusted_box)
            return box, lt, lb, rt, rb, time.time() - start
        else:
            return None, None, None, None, None, time.time() - start

    def adjust_coordinates(
        self, box, left, top, resize_w, resize_h, destWidth, destHeight
    ):
        """
        调整边界框坐标，确保它们在合理范围内。

        参数:
        box (numpy.ndarray): 原始边界框坐标 (shape: (4, 2))
        left (int): 左侧偏移量
        top (int): 顶部偏移量
        resize_w (int): 缩放宽度
        resize_h (int): 缩放高度
        destWidth (int): 目标宽度
        destHeight (int): 目标高度
        xmin_a (int): 目标左上角横坐标
        ymin_a (int): 目标左上角纵坐标

        返回:
        numpy.ndarray: 调整后的边界框坐标
        """
        # 调整横坐标
        box[:, 0] = np.clip(
            (np.round(box[:, 0] - left) / resize_w * destWidth), 0, destWidth
        )

        # 调整纵坐标
        box[:, 1] = np.clip(
            (np.round(box[:, 1] - top) / resize_h * destHeight), 0, destHeight
        )
        return box

    def sort_and_clip_coordinates(self, box):
        """
        对边界框坐标进行排序并裁剪负值。

        参数:
        box (numpy.ndarray): 边界框坐标 (shape: (4, 2))

        返回:
        tuple: 左上角、左下角、右上角、右下角坐标
        """
        # 按横坐标排序
        x = box[:, 0]
        l_idx = x.argsort()
        l_box = np.array([box[l_idx[0]], box[l_idx[1]]])
        r_box = np.array([box[l_idx[2]], box[l_idx[3]]])

        # 左侧坐标按纵坐标排序
        l_idx_1 = np.array(l_box[:, 1]).argsort()
        lt = l_box[l_idx_1[0]]
        lb = l_box[l_idx_1[1]]

        # 右侧坐标按纵坐标排序
        r_idx_1 = np.array(r_box[:, 1]).argsort()
        rt = r_box[r_idx_1[0]]
        rb = r_box[r_idx_1[1]]

        # 裁剪负值
        lt[lt < 0] = 0
        lb[lb < 0] = 0
        rt[rt < 0] = 0
        rb[rb < 0] = 0

        return lt, lb, rt, rb

    def img_preprocess(self, img, resize_shape=[800, 800]):
        im, new_w, new_h, left, top = ResizePad(img, resize_shape[0])
        im = im / 255.0
        im = im.transpose((2, 0, 1)).copy()
        im = im[None, :].astype("float32")
        return im, new_h, new_w, left, top


class PPLCNet:
    model_key = "cls_det"

    def __init__(self, model_path, **kwargs):
        self.model = OrtInferSession(model_path)
        self.img_loader = LoadImage()
        self.resize_shape = [624, 624]

    def __call__(self, img, **kwargs):
        start = time.time()
        img = self.img_loader(img)
        img = self.img_preprocess(img, self.resize_shape)
        label = self.model([img])[0]
        label = label[None, :]
        mini_batch_result = np.argsort(label)
        mini_batch_result = mini_batch_result[0][-1]  # 把这些列标拿出来
        mini_batch_result = mini_batch_result.flatten()  # 拉平了，只吐出一个 array
        mini_batch_result = mini_batch_result[::-1]  # 逆序
        pred_label = mini_batch_result[0]
        return pred_label, time.time() - start

    def img_preprocess(self, img, resize_shape=[624, 624]):
        im, new_w, new_h, left, top = ResizePad(img, resize_shape[0])
        im = np.array(im).transpose((2, 0, 1)) / 255.0
        return im[None, :].astype("float32")
