import time
import picamera

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (256, 192)
    camera.start_preview()
    time.sleep(4)
    #camera.stop_preview()

    camera.zoom = 0.1, 0.1, 0.3, 0.3
    #camera.start_preview()
    time.sleep(4)
    camera.stop_preview()


