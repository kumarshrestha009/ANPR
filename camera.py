from picamera import PiCamera
from time import sleep
def capture():    
    camera = PiCamera()
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
    #camera.capture('/home/pi/Desktop/files/image.jpg')
    camera.capture('image.jpg')

#capture()



