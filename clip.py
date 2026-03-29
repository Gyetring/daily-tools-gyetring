from moviepy import VideoFileClip

def parse_time(t_str):
    """
    将 'mm:ss' 或 'hh:mm:ss' 转换为秒数(float)
    例如：
        '1:23' -> 83
        '0:02:10' -> 130
    """
    parts = [float(p) for p in t_str.split(':')]
    if len(parts) == 2:  # mm:ss
        minutes, seconds = parts
        return minutes * 60 + seconds
    elif len(parts) == 3:  # hh:mm:ss
        hours, minutes, seconds = parts
        return hours * 3600 + minutes * 60 + seconds
    else:
        raise ValueError(f"无效的时间格式: {t_str}")

def cut_video(input_path, output_path, start_time, end_time):
    """
    从视频中截取指定时间段并保存为新文件。
    start_time 和 end_time 可以是 'mm:ss' 或 'hh:mm:ss'。
    """
    start_sec = parse_time(start_time)
    end_sec = parse_time(end_time)

    video = VideoFileClip(input_path)
    duration = video.duration

    if start_sec < 0 or end_sec > duration or start_sec >= end_sec:
        raise ValueError(f"无效的时间范围: 0 <= start < end <= {duration:.2f}")

    subclip = video.subclipped(start_sec, end_sec)
    subclip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    print(f"✅ 已保存剪辑视频: {output_path}")

if __name__ == "__main__":
    # 示例：截取从 1:23 到 2:45 的片段
    input_video = "input_2.mp4"
    output_video = "output_clip.mp4"
    cut_video(input_video, output_video, start_time="5:00", end_time="10:50")