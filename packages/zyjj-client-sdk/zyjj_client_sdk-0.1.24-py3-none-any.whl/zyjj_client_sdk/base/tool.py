import uuid
from io import BytesIO
import asyncio
import logging
import math
from pydub import AudioSegment


# 毫秒时间戳格式化
def format_ms(ms: int):
    hours = ms // 3600000
    minutes = (ms % 3600000) // 60000
    seconds = (ms % 60000) // 1000
    milliseconds = ms % 1000
    # 格式化字符串
    return "{:02d}:{:02d}:{:02d},{:03d}".format(int(hours), int(minutes), int(seconds), int(milliseconds))


# 音频分割
def audio_split(audio_file: str, chunk_length_s: int = 60, return_bytes: bool = True) -> list:
    audio = AudioSegment.from_mp3(audio_file)
    segments_list = []
    # 计算要切割多少段
    segment_duration = chunk_length_s * 1000
    num_segments = math.ceil(len(audio) / segment_duration)
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = start_time + segment_duration
        segment = audio[start_time:end_time]
        info = {"start": start_time, "end": end_time}
        # 保存切割后的音频
        if return_bytes:
            byte_io = BytesIO()
            segment.export(byte_io, format="mp3")
            byte_io.seek(0)  # 重置指针到开头
            info["data"] = byte_io.read()
        else:
            name = f"/tmp/{uuid.uuid4().hex}.mp3"
            segment.export(name, format="mp3")
            info["data"] = name
        segments_list.append(info)
    return segments_list


# 字幕转字节
def subtitles2srt(subtitles: list) -> bytes:
    srt = ""
    for i, subtitle in enumerate(subtitles):
        srt += f"{i + 1}\n"
        srt += f"{format_ms(subtitle['start'])} --> {format_ms(subtitle['end'])}\n"
        srt += f"{subtitle['text']}\n\n"
    return srt.encode()


async def _async_batch_run(data_list: list, split_size: int, async_fun, sleep: int, args: dict):
    num_segments = math.ceil(len(data_list) / split_size)
    logging.info(f"segments size {num_segments}")
    task_list = []
    # 把任务全部添加到任务组里面去
    async with asyncio.TaskGroup() as tg:
        for i in range(num_segments):
            logging.info(f"start task {i}")
            start = i * split_size
            end = min((i + 1) * split_size, len(data_list))
            data = data_list[start:end]
            task_list.append(tg.create_task(async_fun(data=data, **args)))
            # 延迟5s，避免并发太高
            await asyncio.sleep(sleep)
    # 等待所有任务完成
    return [await task for task in task_list]


def async_batch_run(data_list: list, async_func, split_size: int = 1, sleep: int = 1, args: dict = {}) -> list:
    return asyncio.run(_async_batch_run(data_list, split_size, async_func, sleep, args))
