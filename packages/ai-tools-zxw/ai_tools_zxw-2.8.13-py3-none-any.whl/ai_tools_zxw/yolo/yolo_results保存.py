"""
pip install tqdm ultralytics numpy opencv-python
"""
from typing import List
from pathlib import Path
from PIL import Image
import cv2
from ultralytics.engine.results import Results
from tqdm import tqdm
import numpy as np


class SAVE_YOLO_RESULTS:

    def __init__(self, 检测对象路径: Path, isVideo: bool = False):
        self.检测对象路径 = 检测对象路径
        # 获取原始对象信息
        if isVideo:
            # 视频
            self.原始对象 = cv2.VideoCapture(str(检测对象路径))
            self.原始对象_fps = self.原始对象.get(cv2.CAP_PROP_FPS)
            self.原始对象_frames = self.原始对象.get(cv2.CAP_PROP_FRAME_COUNT)
            self.原始对象_width = self.原始对象.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.原始对象_height = self.原始对象.get(cv2.CAP_PROP_FRAME_HEIGHT)
        else:
            # 图片
            self.原始对象 = Image.open(检测对象路径)
            self.原始对象_width, self.原始对象_height = self.原始对象.size

    @staticmethod
    def 保存为TXT_YOLO标注(results: List[Results], 文件输出路径: Path):
        # 输出文件路径
        文件输出路径.parent.mkdir(parents=True, exist_ok=True)
        # 保存txt
        if len(results) == 1:
            results[0].save_txt(str(文件输出路径))
        else:
            for i, r in enumerate(results):
                out_path = 文件输出路径.parent / f'{文件输出路径.stem}_frame_{i}.txt'
                r.save_txt(str(out_path))

    def 保存为图片(self, results: List[Results], 图片输出路径: Path = None, use_PIL_Save: bool = False):
        if 图片输出路径 is None:
            保存根路径 = self.检测对象路径.parent
            图片输出路径 = 保存根路径 / 'yolo_detected'

        #
        for i, r in enumerate(results):
            # 输出文件路径
            out_path = 图片输出路径 / f'{self.检测对象路径.stem}_{i}.png'
            out_path.parent.mkdir(parents=True, exist_ok=True)
            # 保存图片
            if not use_PIL_Save:
                r.save(filename=str(out_path))
            else:
                im_bgr = r.plot()
                im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image
                im_rgb.save(out_path.with_suffix('.jpg'))

    def 保存为视频(self, results: List[Results], 视频输出路径: Path = None):
        # save_video = 单帧图片2视频()
        if 视频输出路径 is None:
            保存根路径 = self.检测对象路径.parent
            视频输出路径 = 保存根路径 / 'yolo_detected' / f'{self.检测对象路径.stem}.mp4'

        # 输出文件路径
        视频输出路径.parent.mkdir(parents=True, exist_ok=True)

        # 创建MOV格式视频
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(
            str(视频输出路径),
            fourcc,
            self.原始对象_fps,
            (results[0].orig_shape[1], results[0].orig_shape[0])
        )
        # 遍历每一帧识别结果，并保存
        for i, r in tqdm(enumerate(results)):
            im_bgr = r.plot()
            out.write(np.array(im_bgr))
        # 释放内存
        out.release()
        print(f"视频已保存至{视频输出路径}")
