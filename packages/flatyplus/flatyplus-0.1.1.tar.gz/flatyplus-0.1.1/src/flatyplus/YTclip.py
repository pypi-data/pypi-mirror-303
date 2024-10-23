
import os
import subprocess
import cv2
from yt_dlp import YoutubeDL

def getTitle(url):
    with YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        return video_title

def audio(url, clip=None, output=None):
    if output == None:
        output = getTitle(url)+".m4a"
    if os.path.exists(output) == True:
        os.remove(output)
    if os.path.exists("/tmp/audio.m4a") == True:
        os.remove("/tmp/audio.m4a")
    subprocess.run(["yt-dlp", "-o", "/tmp/audio.m4a", "-f", "ba", "-S", "aext:m4a", url])
    if clip == None:
        subprocess.run(["mv", "/tmp/audio.m4a", output])
    else:
        subprocess.run(["ffmpeg", "-ss", clip[0], "-to", clip[1], "-i", "/tmp/audio.m4a", "-c", "copy", output])
    print("save audio")

def video(url, short=False, clip=None, output=None):
    if output == None:
        output = getTitle(url)+".mp4"
    if os.path.exists(output) == True:
        os.remove(output)
    if os.path.exists("/tmp/video.mp4") == True:
        os.remove("/tmp/video.mp4")
    if short == True:
        subprocess.run(["yt-dlp", "-o", "/tmp/video.mp4", "-f", "bv", "-S", "width:1280,vext:mp4", url])
    else:
        subprocess.run(["yt-dlp", "-o", "/tmp/video.mp4", "-f", "bv", "-S", "height:1280,vext:mp4", url])
    if clip == None:
        subprocess.run(["mv", "/tmp/video.mp4", output])
    else:
        subprocess.run(["ffmpeg", "-ss", clip[0], "-to", clip[1], "-i", "/tmp/video.mp4", "-c", "copy", output])
    print("save video")

def audiovideo(url, short=False, clip=None, output=None):
    if output == None:
        output = getTitle(url)+".mp4"
    if os.path.exists(output) == True:
        os.remove(output)
    audio(url, clip=clip, output="/tmp/a.m4a")
    video(url, short=short, clip=clip, output="/tmp/v.mp4")
    subprocess.run(["ffmpeg", "-i", "/tmp/v.mp4", "-i", "/tmp/a.m4a", "-c:v", "libx264", "-preset", "slow", "-crf", "23", output])
    print("save audiovideo")

