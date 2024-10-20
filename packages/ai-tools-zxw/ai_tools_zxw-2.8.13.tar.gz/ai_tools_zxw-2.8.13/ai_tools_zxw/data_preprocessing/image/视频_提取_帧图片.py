"""
pip install opencv-python tqdm
"""
import cv2
from pathlib import Path
from tqdm import tqdm


def video_to_jpg(video_path: Path = Path('/Volumes/AI175125410/AI/行车记录/VID_800.MOV'),
                 out_root_path: Path = Path('/Volumes/AI175125410/AI/行车记录jpg'),
                 out_img_suffix="jpg",
                 抽帧间隔_秒: int = 60
                 ):
    # 安全判断
    if not video_path.is_file():
        raise FileNotFoundError(f"【警告】{video_path}：视频文件不存在")
    elif video_path.suffix not in ['.MOV', '.mp4', '.avi']:
        raise FileNotFoundError(f"【警告】{video_path}：不是视频文件")

    # 读取视频
    cap = cv2.VideoCapture(str(video_path))

    # 获取视频信息：帧数、时长、帧率、分辨率
    总帧数 = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    帧率 = int(cap.get(cv2.CAP_PROP_FPS))
    # 总时长 = int(总帧数 / 帧率)
    # print(f"{i视频文件=}\n{总帧数=}fp,{帧率=}fps,{总时长=}s")

    # 安全判断
    if 抽帧间隔_秒 * 帧率 >= 总帧数:
        print(f"【警告】{video_path.stem}：抽帧间隔过大，已超过视频总帧数")
        return None

    # 提取固定帧
    for ifp in tqdm(range(0, 总帧数, 帧率 * 抽帧间隔_秒)):
        # 设置帧数
        cap.set(cv2.CAP_PROP_POS_FRAMES, ifp)
        # 提取frame
        ret, frame = cap.read()
        if ret is True:
            # 整理输出路径
            out_path: Path = out_root_path / f"{video_path.stem}_{ifp}.{out_img_suffix}"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            # 输出img
            cv2.imwrite(str(out_path), frame)


def videos_to_jpg(videos_root_path: str = '/Volumes/AI175125410/AI/行车记录',
                  videos_suffix='*.MOV',
                  out_path: str = '/Volumes/AI175125410/AI/行车记录jpg2',
                  out_img_suffix="jpg",
                  抽帧间隔_秒: int = 60):
    # 超参数设置
    视频路径 = Path(videos_root_path)
    jpg数据路径 = Path(out_path)

    # 扫描视频文件
    视频文件列表 = 视频路径.glob(videos_suffix)  # 此时文件名是乱序排列
    视频文件列表 = sorted(视频文件列表)  # 按名称，排序

    # 取第一条视频
    for i视频文件 in 视频文件列表:
        # 读取视频
        cap = cv2.VideoCapture(str(i视频文件))

        # 获取视频信息：帧数、时长、帧率、分辨率
        总帧数 = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        帧率 = int(cap.get(cv2.CAP_PROP_FPS))
        # 总时长 = int(总帧数 / 帧率)
        # print(f"{i视频文件=}\n{总帧数=}fp,{帧率=}fps,{总时长=}s")

        # 安全判断
        if 抽帧间隔_秒 * 帧率 >= 总帧数:
            print(f"【警告】{i视频文件.stem}：抽帧间隔过大，已超过视频总帧数")
            continue

        # 提取固定帧
        for ifp in tqdm(range(0, 总帧数, 帧率 * 抽帧间隔_秒)):
            # 设置帧数
            cap.set(cv2.CAP_PROP_POS_FRAMES, ifp)
            # 提取frame
            ret, frame = cap.read()
            if ret is True:
                # 整理输出路径
                out_path: Path = jpg数据路径 / f"{i视频文件.stem}_{ifp}.{out_img_suffix}"
                out_path.parent.mkdir(parents=True, exist_ok=True)
                # 输出img
                cv2.imwrite(str(out_path), frame)


if __name__ == '__main__':
    video_to_jpg(抽帧间隔_秒=1)
