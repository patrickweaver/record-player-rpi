import time
import picamera

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (256, 192)
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()
