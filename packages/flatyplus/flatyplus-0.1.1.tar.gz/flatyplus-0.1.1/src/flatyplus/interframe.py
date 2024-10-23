
import os
import subprocess
import re
import cv2
from pathlib import Path


def interpolate(path, num=2, loop=False, output=None):
    path = path+"/"
    if output == None:
        output = Path(path).stem+"-interframe"
    output = output+"/"
    if os.path.exists(output) == False:
        os.mkdir(output)
    while(True):
        output_temp = "/tmp/interframe/"
        if os.path.exists(output_temp) == False:
             os.mkdir(output_temp)
        n = int((len(os.listdir(output)))/(2**num))
        if os.path.exists(path+str(n+1)+".png") == False:
             if loop == True:
                   subprocess.run(["interframe", "-i", path+str(n)+".png", path+str(0)+".png", "-o", output_temp, "-n", str(num)])
                   for f in os.listdir(output_temp):
                        os.rename(output_temp+f, output_temp+re.sub("(.*)_", "", f))
                   for f in range(0, (2**num)+1):
                        if f != 2**num:
                              subprocess.run(["mv", output_temp+str(f)+".png", output+str(len(os.listdir(output)))+".png"])
                   print("\rextract interpolation: "+str(n), end=" ")
             else:
                  subprocess.run(["cp", path+str(n)+".png", output+str(len(os.listdir(output)))+".png"])
             subprocess.run(["rm", "-r", output_temp])
             break
        subprocess.run(["interframe", "-i", path+str(n)+".png", path+str(n+1)+".png", "-o", output_temp, "-n", str(num)])
        for f in os.listdir(output_temp):
             os.rename(output_temp+f, output_temp+re.sub("(.*)_", "", f))
        for f in range(0, (2**num)+1):
             if f != 2**num:
                  subprocess.run(["mv", output_temp+str(f)+".png", output+str(len(os.listdir(output)))+".png"])
        subprocess.run(["rm", "-r", output_temp])
        print("\rextract interpolation: "+str(n), end=" ")
    print("save interpolation frame finish")
