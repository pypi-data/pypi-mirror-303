"""
pip install tqdm ultralytics
"""
from typing import List
from pathlib import Path
from ultralytics import YOLO
from ultralytics.engine.results import Results


# from ai_tools_zxw.yolo.yolo_results保存 import SAVE_YOLO_RESULTS


class AutoLabeling:
    def __init__(self,
                 yolo_weight_path: str =
                 "/Users/zhangxuewei/Documents/GitHub/myLib/ai_tools_zxw/ai_tools_zxw/yolo/weights/yolov10m.pt",
                 device='cpu'):
        self.yolo_weight_path = yolo_weight_path
        self.model = YOLO(yolo_weight_path)
        self.model.to(device)
        # print所有类别
        print("origin labels = \n", self.model.names)
        print(self.model.names.values())

    def 标注单张图片(self, img_path: Path, class_ids: List[int] = None):
        """
        :param img_path:
        :param class_ids: 为None时，标注所有类别
        :return:
        """
        # 检查总类别txt文件是否存在
        classes_path = img_path.parent / "classes.txt"
        if not classes_path.exists():
            with open(classes_path, 'w') as f:
                f.write('\n'.join(list(self.model.names.values())))

        #
        results: List[Results] = self.model(img_path, classes=class_ids)
        for result in results:
            result.save_txt(str(img_path.with_suffix('.txt')))

    def 批量标注图片(self, img_dir: Path, class_ids: List[int] = None):
        """
        :param img_dir:
        :param class_ids: 为None时，标注所有类别
        :return:
        """
        for img_file_path in img_dir.glob("*.jpg"):
            self.标注单张图片(img_file_path, class_ids)

    def coco标注类别_转_自定义类别(self, 标注目录: Path, 自定义类别: List[str]):
        """
        :param 自定义类别:
        :return:
        """
        # 1. 读取coco标注类别
        coco_classes: dict = self.model.names
        # 2. 读取根目录下所有文件类别
        labels_path = 标注目录.glob("*.txt")
        # 3. 遍历类别文件，替换为自定义类别
        for label in labels_path:
            with open(label, 'r') as f:
                lines = f.readlines()
            with open(label, 'w') as f:
                for line in lines:
                    coco_class: int = int(line.split(' ')[0])
                    if coco_class in coco_classes:
                        f.write(f"{自定义类别[coco_classes[coco_class]]} {' '.join(line.split(' ')[1:])}")
                    else:
                        print(f"类别{coco_class}不存在")


# def 试试():
#     # 参数  8n推理速度大概是8x的十倍
#     图片路径 = Path("/Volumes/AI175125410/AI/行车记录_测试jpg/VID_758_3600.jpg")
#
#     # 8n, 8s, 8m, 8l, 8x的模型参数量分别为 43M, 64M, 89M, 138M, 224M
#     model_root = Path("/Users/zhangxuewei/Documents/GitHub/myLib/ai_tools_zxw/ai_tools_zxw/yolo/weights")
#     # model_name = "yolov8s"
#     model_name = "yolov10m"
#
#     # 加载预训练的 YOLOv8 模型，
#     model = YOLO(model_root / f'{model_name}.pt')
#     print(model.names)  # 类别名称
#     # model.to('mps')  # 使用cuda
#
#     # 在视频上进行目标检测
#     # save_yolo_results = SAVE_YOLO_RESULTS(图片路径, isVideo=True)
#     results: List[Results] = model(图片路径)
#
#     #
#     out_path = 图片路径.parent / f"{图片路径.stem}_{model_name}_results.txt"
#     print(out_path)
#     results[0].save(out_path.with_suffix('.jpg'))
#     results[0].save_txt(str(out_path))
#     # results[0].tojson()


if __name__ == '__main__':
    # img_path = Path("/Volumes/AI175125410/AI/行车记录jpg/VID_800_3600.jpg")
    auto_labeling = AutoLabeling(
        yolo_weight_path="/ai_tools_zxw/yolo/weights/yolov10m.pt",
        device='cpu')
    auto_labeling.批量标注图片(Path("/Volumes/AI175125410/AI/行车记录jpg"),
                               class_ids=[0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11])

    # auto_labeling.批量标注图片(Path("/Volumes/AI175125410/AI/行车记录jpg"))
    auto_labeling.coco标注类别_转_自定义类别(Path("/Volumes/AI175125410/AI/行车记录jpg"),
                                             自定义类别=["行人", "车辆", "摩托车", "自行车"])
