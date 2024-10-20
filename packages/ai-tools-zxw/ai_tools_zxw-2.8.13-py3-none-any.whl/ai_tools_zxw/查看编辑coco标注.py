"""
# File       : 查看编辑coco标注.py
# Time       ：2024/7/18 上午8:52
# Author     ：张鑫
# Email      ：
# version    ：python 3.12
# Description：查看COCO数据集的标注信息

pip install pycocotools
"""
from pycocotools.coco import COCO
from pathlib import Path


class COCO数据集:

    def __init__(self, dateset_path: Path):
        # 初始化 COCO API
        self.coco = COCO(dateset_path)
        # 获取所有类别
        self.class_ids = self.coco.getCatIds()
        self.class_names = [self.coco.loadCats(class_id)[0]['name'] for class_id in self.class_ids]

    def 显示类别(self, class_id: int) -> str:
        print(f"类别ID：{class_id}, 类别名称：{self.coco.loadCats(class_id)[0]['name']}")
        return self.coco.loadCats(class_id)[0]['name']

    def 显示所有类别(self) -> tuple[list[int], list[str]]:
        print(f"类别总数：{len(self.class_ids)}")
        print(f"类别名称：{self.class_names}")
        return self.class_ids, self.class_names


if __name__ == '__main__':
    path = "/Volumes/zhang_娱乐大型数/AI数据/coco-2017-full"
    dateset_path = Path(path) / "raw/instances_train2017.json"
    coco数据集 = COCO数据集(dateset_path)
    coco数据集.显示所有类别()
