import os
import picamera
import picamera.array
import datetime
from fractions import Fraction
import time
import numpy as np

oldImage = np.zeros((256, 192, 3), dtype=np.uint8)
newImage = np.zeros((256, 192, 3), dtype=np.uint8)
color_offset = 15
image_path = os.getcwd() + '/public/images/'

with picamera.PiCamera() as camera:
  camera.rotation = 180
  camera.resolution = (256, 192)
  camera.start_preview()
  time.sleep(.5)
  camera.stop_preview()
  camera.capture(image_path + 'old-image.jpg')
  camera.capture(oldImage, "rgb")



  a = True
  while a:
    x = 0
    y = 0
    different = 0
    time.sleep(1)
    camera.start_preview()
    time.sleep(2)
    camera.stop_preview()
    camera.capture(image_path + 'new-image.jpg')
    camera.capture(newImage, "rgb")
    
    print(oldImage[128, 96])
    print(newImage[128, 96])

    while(x < np.size(newImage, 0)):
      while(y < np.size(newImage, 1)):
        #print(str(x) + ", " + str(y))
        #print(oldImage[x,y])
        #print(newImage[x,y])
        #print("")
        for z in range(0, 3):
          oip = oldImage[x,y,z].item()
          nip = newImage[x,y,z].item()
          if (abs(oip - nip) > color_offset):
            different += 1
            break
        y += 1
      y = 0
      x += 1

    print("Total pixels:")
    print(256 * 192)
    print("Pixels that are different:")
    print(different)
    
    oldImage = np.copy(newImage)