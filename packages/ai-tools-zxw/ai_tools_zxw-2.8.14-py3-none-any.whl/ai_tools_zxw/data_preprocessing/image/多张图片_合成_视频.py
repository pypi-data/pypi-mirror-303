"""
pip install opencv-python
"""
import cv2
import numpy as np
from pathlib import Path


class 单帧图片2视频:
    视频图像 = []  # shape = (fps,height,width,channel)

    def step1_accumulate_img(self, img: np.ndarray):
        if len(img.shape) != 3:
            raise ValueError("输入图片必须是三通道的")
        elif img.shape[2] != 3:
            raise ValueError("输入图片数组形状必须是（高，宽，3）")
        self.视频图像.append(img)

    def step2_save_video_mp4(self, fps: int, out_path: Path):
        # 创建视频
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(
            str(out_path),
            fourcc,
            fps,
            (self.视频图像[0].shape[1], self.视频图像[0].shape[0])
        )
        # 写入视频
        for i in self.视频图像:
            out.write(i)
        # 释放
        out.release()
        print(f"视频已保存至{out_path}")
        self.视频图像 = []
        print("视频图像已清空")
