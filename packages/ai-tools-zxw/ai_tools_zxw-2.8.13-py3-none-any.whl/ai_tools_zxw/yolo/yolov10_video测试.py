"""
pip install ultralytics
"""
from typing import List
from pathlib import Path
from ultralytics import YOLO
from ultralytics.engine.results import Results
from ai_tools_zxw.yolo.yolo_results保存 import SAVE_YOLO_RESULTS

# 待编辑参数
视频路径 = Path('/Volumes/AI175125410/AI/行车记录')
文件列表 = 视频路径.glob('*.MOV')  # 搜索的文件类型
model_root = Path("/ai_tools_zxw/yolo/weights")
model_name = "yolov10m"

# 加载预训练的 YOLOv8 模型，
model = YOLO(model_root / f'{model_name}.pt')
model.to('mps')  # 使用cuda、mps、cpu

文件列表 = sorted(文件列表)
for i0 in range(0, 86, 17):
    i单体文件 = 文件列表[i0]
    # for i0, i单体文件 in enumerate(文件列表):
    # 在视频上进行目标检测
    save_yolo_results = SAVE_YOLO_RESULTS(i单体文件, isVideo=True)
    results: List[Results] = model(i单体文件)
    print(f"{i单体文件=}, {len(results)=}")

    # 输出路径
    保存根路径 = i单体文件.parent.parent
    视频输出路径 = 保存根路径 / f'yolov10m_detected_{model_name}' / f'{i单体文件.stem}.mp4'

    # 处理结果列表
    save_yolo_results.保存为视频(results, 视频输出路径=视频输出路径)
    #
    results.clear()
    if i0 > 5:
        break
