
import os
import subprocess
import re
from pathlib import Path
import time
import cv2
import numpy
from rembg import remove
from PIL import Image

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries","format=duration", "-of","default=noprint_wrappers=1:nokey=1", filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def get_hms(sec):
    hms = time.strftime('%H:%M:%S', time.gmtime(get_length(sec)))
    return hms


def write(path, duration=15, resize=None, soundpath=None, background=None, output=None):
    path = path+"/"
    if output == None:
        output = Path(path).stem+".mp4"
    if os.path.exists(output) == True:
        os.remove(output)
    fps = len(os.listdir(path))/duration
    imgs = Image.open(path+"/"+os.listdir(path)[0])
    width, height = imgs.size
    cv2flag = cv2.INTER_NEAREST
    if resize != None:
        if resize[0] > width:
             cv2flag = cv2.INTER_CUBIC
        width, height = resize
    video = cv2.VideoWriter("/tmp/video.avi", cv2.VideoWriter_fourcc(*"XVID"), fps, (width, height))
    last = len(os.listdir(path))
    if background != None:
        isimgbg = os.path.exists(background)
    for i in range(0, last):
        image = Image.open(path+str(i)+".png")
        pix = image.load()
        if background != None:
             image = remove(image)
             if isimgbg == True:
                  new_image = Image.open(background)
                  new_image = new_image.resize((width, height))
             else:
                  if background == "default":
                        background = pix[1, 1]
                  new_image = Image.new("RGBA", image.size, background)
             new_image.paste(image, (0, 0), image)
             image = new_image
        image = image.convert('RGB')
        image = numpy.array(image)
        image = image[:, :, ::-1].copy()
        if resize != None:
             image = cv2.resize(image, (width, height), interpolation=cv2flag)
        video.write(image)
        print("\r assignment frame: "+str(i)+"/"+str(last-1), end=" ")
    video.release()
    if soundpath == None:
        subprocess.run(["ffmpeg", "-i", "/tmp/video.avi", "-c:v", "libx264", "-preset", "slow", "-crf", "23", output])
    else:
        subprocess.run(["ffmpeg", "-i", "/tmp/video.avi", "-i", soundpath, "-c:v", "libx264", "-preset", "slow", "-crf", "23", output])
    print("save video finish")

def clip(path, start="00:00:00", end="00:00:00", crop=None, resize=None, output=None):
    if output == None:
        output = Path(path).stem+"-clip.mp4"
    if os.path.exists(output) == True:
        os.remove(output)
    vidcap = cv2.VideoCapture(path)
    totalframe = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    success,imgcv = vidcap.read()
    height, width, _ = imgcv.shape
    cv2flag = cv2.INTER_NEAREST
    if resize != None:
        if resize[0] > width:
             cv2flag = cv2.INTER_CUBIC
        width, height = resize
    duration = get_length(path)
    fps = totalframe/duration
    video = cv2.VideoWriter("/tmp/video.avi", cv2.VideoWriter_fourcc(*"XVID"), fps, (width, height))
    count = 0
    n = 0
    while success:
        if type(crop) is tuple:
             imgcv = imgcv[crop[1][1]:crop[1][1]+crop[0][1], crop[1][0]:crop[1][0]+crop[0][0]]
        if type(crop) is list:
             for c in crop:
                  if get_hms(c["start"]) <= n and n <= get_hms(c["start"])+c["duration"]:
                       imgcv = imgcv[c["crop"][1][1]:c["crop"][1][1]+c["crop"][0][1], c["crop"][1][0]:c["crop"][1][0]+c["crop"][0][0]]
        imgcv = cv2.resize(imgcv, (width, height), interpolation = cv2flag)
        video.write(imgcv)
        success,imgcv = vidcap.read()
        n += duration/totalframe
        count += 1
        print("\r assignment frame: "+str(count)+"/"+str(totalframe), end=" ")
    video.release()
    if end == "00:00:00":
        end = time.strftime('%H:%M:%S', time.gmtime(get_length(path)))
    subprocess.run(["ffmpeg", "-ss", start, "-to", end, "-i", "/tmp/video.avi", "-ss", start, "-to", end, "-i", path, "-map", "0:0", "-map", "1:a", "-c:v", "libx264", "-preset", "slow", "-crf", "23", output])
    print("save video clip finish")

def clipframe(path, clif, fps=7, nskip=1, output=None):
    if output == None:
        output = Path(path).stem+"-clip"
    if os.path.exists(output) == True:
        subprocess.run(["rm", "-r", output])
    if Path(output).suffix != ".mp4" and Path(output).suffix != ".avi":
        output= output+"/"
        if os.path.exists(output) == False:
              os.mkdir(output)
    vidcap = cv2.VideoCapture(path)
    duration = get_length(path)
    totalframe = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    success,imgcv = vidcap.read()
    height, width, _ = imgcv.shape
    duration = get_length(path)

    video = cv2.VideoWriter("/tmp/video.avi", cv2.VideoWriter_fourcc(*"XVID"), fps, (width, height))
    count = 0
    num = 0
    while success:
        if count%nskip == 0 and clif[0]<=count and count<=clif[1]:
              if Path(output).suffix != ".mp4" and Path(output).suffix != ".avi":
                    cv2.imwrite(output+str(num)+".png", imgcv),
              video.write(imgcv)
              print("\rextract control: "+str(num)+"/"+str((clif[1]-clif[0])/nskip), end=" ")
              num += 1
        success,imgcv = vidcap.read()
        count += 1
    video.release()
    if Path(output).suffix == ".avi":
        subprocess.run(["mv", "/tmp/video.avi", output])
    if Path(output).suffix == ".mp4":
        subprocess.run(["ffmpeg", "-i", "/tmp/video.avi", "-c:v", "libx264", "-preset", "slow", "-crf", "23", output])
    print("save video clipframe finish")


def loop(path, num, output=None):
    if output == None:
        output = Path(path).stem+"-loop.mp4"
    if os.path.exists(output) == True:
        os.remove(output)
    subprocess.run(["ffmpeg", "-stream_loop", str(num), "-i", path, "-c", "copy", output])
    print("save video loop finish")

