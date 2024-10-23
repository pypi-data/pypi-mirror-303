
import subprocess
subprocess.run(["wget", "-O" "/usr/local/lib/python3.10/dist-packages/controlnet_aux/open_pose/util.py", "https://huggingface.co/flatyplus/fdc/raw/main/util.py"])
import numpy as np
import cv2
import torch
import matplotlib
import matplotlib.cm
import numpy as np
from PIL import Image
from pathlib import Path
import random
import os
from controlnet_aux import HEDdetector, OpenposeDetector
from rembg import remove
from diffusers.utils import load_image


mode_control = None
processor_openpose = None
processor_scribble = None
model_zoe_n = None

def init(mode):
    global mode_control
    global processor_openpose
    global processor_scribble
    global model_zoe_n
    mode_control = mode
    for m in mode_control:
        if m == "openpose":
             processor_openpose = OpenposeDetector.from_pretrained('lllyasviel/ControlNet')
        if m == "zoe-depth":
             torch.hub.help("intel-isl/MiDaS", "DPT_BEiT_L_384", force_reload=True)  # Triggers fresh download of MiDaS repo
             model_zoe_n = torch.hub.load("isl-org/ZoeDepth", "ZoeD_NK", pretrained=True).eval()
             model_zoe_n = model_zoe_n.to("cuda")
        if m == "scribble":
             processor_scribble = HEDdetector.from_pretrained('lllyasviel/Annotators')

def nms(x, t, s):
    x = cv2.GaussianBlur(x.astype(np.float32), (0, 0), s)
    f1 = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]], dtype=np.uint8)
    f2 = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]], dtype=np.uint8)
    f3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.uint8)
    f4 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=np.uint8)
    y = np.zeros_like(x)
    for f in [f1, f2, f3, f4]:
        np.putmask(y, cv2.dilate(x, kernel=f) == x, x)
    z = np.zeros_like(y, dtype=np.uint8)
    z[y > t] = 255
    return z

def openpose(img, resize):
    controlnet_img = processor_openpose(img, hand_and_face=False)
    img = controlnet_img.resize(resize)
    return img

def scribble(img, resize):
    controlnet_img = processor_scribble(img, scribble=False)
    controlnet_img = np.array(controlnet_img)
    controlnet_img = nms(controlnet_img, 127, 3)
    controlnet_img = cv2.GaussianBlur(controlnet_img, (0, 0), 3)
    random_val = int(round(random.uniform(0.01, 0.10), 2) * 255)
    controlnet_img[controlnet_img > random_val] = 255
    controlnet_img[controlnet_img < 255] = 0
    controlnet_img = Image.fromarray(controlnet_img)
    img = controlnet_img.resize(resize)
    return img

def colorize(value, vmin=None, vmax=None, cmap='gray_r', invalid_val=-99, invalid_mask=None, background_color=(128, 128, 128, 255), gamma_corrected=False, value_transform=None):
    if isinstance(value, torch.Tensor):
        value = value.detach().cpu().numpy()

    value = value.squeeze()
    if invalid_mask is None:
        invalid_mask = value == invalid_val
    mask = np.logical_not(invalid_mask)

    # normalize
    vmin = np.percentile(value[mask],2) if vmin is None else vmin
    vmax = np.percentile(value[mask],85) if vmax is None else vmax
    if vmin != vmax:
        value = (value - vmin) / (vmax - vmin)  # vmin..vmax
    else:
        # Avoid 0-division
        value = value * 0.

    # squeeze last dim if it exists
    # grey out the invalid values

    value[invalid_mask] = np.nan
    cmapper = matplotlib.cm.get_cmap(cmap)
    if value_transform:
        value = value_transform(value)
        # value = value / value.max()
    value = cmapper(value, bytes=True)  # (nxmx4)

    # img = value[:, :, :]
    img = value[...]
    img[invalid_mask] = background_color

    # gamma correction
    img = img / 255
    img = np.power(img, 2.2)
    img = img * 255
    img = img.astype(np.uint8)
    img = Image.fromarray(img)
    return img


def zoe_depth(img, resize):
    with torch.autocast("cuda", enabled=True):
        depth = model_zoe_n.infer_pil(img)
    depth = colorize(depth, cmap="gray_r")
    img = depth.resize(resize)
    return img

def canny(img, resize):
    img = np.array(img)
    img = cv2.Canny(img, 100, 200)
    img = img[:, :, None]
    img = np.concatenate([img, img, img], axis=2)
    img = Image.fromarray(img)
    img = img.resize(resize)
    return img

def image(path, resize, output=None, rembg=False):
    torch.cuda.empty_cache()
    img = path
    if isinstance(path, str):
        img = load_image(path)
    img = img.resize(resize)
    img_output = []
    for m in mode_control:
        if m == "openpose":
              img_output.append(openpose(img, resize))
        elif m == "scribble":
              img_output.append(scribble(img, resize))
        elif m == "zoe-depth":
              img_output.append(zoe_depth(img, resize))
        elif m == "canny":
              img_output.append(canny(img, resize))
    if rembg == True:
        imgbg = remove(img)
        data = []
        for pix in list(imgbg.getdata()):
              if pix[3] > 140:
                   data.append((0, 0, 0, 0))
              else:
                   data.append((0, 0, 0, 255))
        imgbg.putdata(data)
        for i in range(0, len(img_output)):
              img_output[i].paste(imgbg, (0, 0), imgbg)
    if output != None:
        output = output+"/"
        for i in range(0, len(img_output)):
              img_output[i].save(output+mode_control[i]+".png")
    torch.cuda.empty_cache()
    return img_output

def video(path, resize, nskip, rembg=False, output=None):
    if output == None:
        output = Path(path).stem+"-control"
    output = output+"/"
    if os.path.exists(output) == False:
        os.mkdir(output)
    for m in mode_control:
        if os.path.exists(output+m) == False:
              os.mkdir(output+m)
    vidcap = cv2.VideoCapture(path)
    success,imgcv = vidcap.read()
    totalframe = int((int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))/nskip)-1)
    count = 0
    num = 0
    while success:
        if count%nskip == 0:
              imgcv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2RGB)
              imgcv = Image.fromarray(imgcv)
              img = imgcv.resize(resize)
              img_output = image(img, resize, rembg=rembg)
              for i in range(0, len(mode_control)):
                   output_path = output+mode_control[i]+"/"
                   img_output[i].save(output_path+str(num)+".png")
              num += 1
              print("\rextract control: "+str(num), end=" ")
        success,imgcv = vidcap.read()
        count += 1
    print("finish")

def frame(path, resize, rembg=False, output=None):
    if output == None:
        output = Path(path).stem+"-control"
    output = output+"/"
    if os.path.exists(output) == False:
        os.mkdir(output)
    for m in mode_control:
        if os.path.exists(output+m) == False:
              os.mkdir(output+m)
    last = len(os.listdir(path))
    for i in range(0, last):
         imgcv = cv2.imread(path+"/"+str(i)+".png")
         imgcv = cv2.cvtColor(imgcv, cv2.COLOR_BGR2RGB)
         imgcv = Image.fromarray(imgcv)
         img = imgcv.resize(resize)
         img_output = image(img, resize, rembg=rembg)
         for k in range(0, len(mode_control)):
              output_path = output+mode_control[k]+"/"
              img_output[k].save(output_path+str(i)+".png")
         print("\rextract control: "+str(i), end=" ")
    print("finish")
