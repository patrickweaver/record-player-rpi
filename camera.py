import os
import picamera
import picamera.array
import datetime
from fractions import Fraction
import time
import numpy as np

width = 256
height = 192

oldImage = np.zeros((width, height, 3), dtype=np.uint8)
newImage = np.zeros((width, height, 3), dtype=np.uint8)
defaultBackground = np.zeros((width, height, 3), dtype=np.uint8)
color_offset = 15
pixel_offset = 0.10
image_path = os.getcwd() + '/public/images/'

r_start = 0
r_end = 0

g_start = 0
g_end = 0

b_start = 0
b_end = 0


def capture_new_image_and_compare(old_image):
    camera.start_preview()
    time.sleep(1)
    camera.stop_preview()
    camera.capture(image_path + 'new-image.jpg')
    camera.capture(newImage, "rgb")

    #print(oldImage[128, 96])
    #print(newImage[128, 96])

    default_change = compare(defaultBackground, newImage)
    print(default_change)
    if (default_change > pixel_offset) {
      return ["default", np.copy(newImage)]
    }

    change = compare(oldImage, newImage)
    print(change)

    if (change > pixel_offset) {
      return ["previous", np.copy(newImage)]
    }
    #print("Total pixels:")
    #print(256 * 192)
    #print("Pixels that are different:")
    #print(different)

    return ["new", np.copy(newImage)]

def compare(old_image_array, new_image_array):
    x = 0
    y = 0
    different = 0
    while(x < np.size(new_image_array, 0)):
        while(y < np.size(new_image_array, 1)):
            #print(str(x) + ", " + str(y))
            #print(oldImage[x,y])
            #print(newImage[x,y])
            #print("")
            for z in range(0, 3):
                oip = old_image_array[x,y,z].item()
                nip = new_image_array[x,y,z].item()
                if (abs(oip - nip) > color_offset):
                    different += 1
                    break
            y += 1
        y = 0
        x += 1

    total_pixels = height * width
    change = different / float(total_pixels)

    print("Done Comparing:")
    print(different)
    print("of")
    print(total_pixels)
    print("")

    return change

def find_default(image_array, color):
    x = 0
    y = 0

    while(x < np.size(image_array, 0)):
        while(y < np.size(image_array, 1)):
            if image_array[x,y,color] > 150 and image_array[x,y,(color + 1) % 3] < 150 and image_array[x,y,(color + 2) % 3] < 150:
                print(x)
                print(y)
                print(image_array[x,y])
                print("")
            y += 1
        y = 0
        x += 1

        if x % 10 == 0:
            print(x)
            print("")

def playRecord():
     print("Play:")
     print(image_path + 'new-image.jpg')

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (256, 192)

    print("Getting Default image in:\n3")
    time.sleep(.1)
    print("2")
    time.sleep(.1)
    print("1")
    time.sleep(.1)
    camera.capture(defaultBackground, "rgb")

    #camera.start_preview()
    #time.sleep(.5)
    #camera.stop_preview()
    #camera.capture(image_path + 'old-image.jpg')
    #camera.capture(oldImage, "rgb")

    a = True
    while a:
        capture_result = capture_new_image_and_compare(oldImage)

        if capture_result[0] == "default":
            defaultBackground = ((defaultBackground + capture_result[1]) / 2)
        if capture_result[0] == "previous":
            oldImage = ((oldImage + capture_result[1]) / 2)
        else:
            playRecord()
            time.sleep(20)
    #find_default(oldImage, 0)
