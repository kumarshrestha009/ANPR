import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)

p = GPIO.PWM(17, 50) #connect to pin 11



def move():
    try:
        p.start(7.5)
        p.ChangeDutyCycle(7.5)                   # change duty cycle for getting the servo position to 90
        time.sleep(10)                                      # sleep for 1 second
        #p.ChangeDutyCycle(12.5)                  # change duty cycle for getting the servo position to 180
        #time.sleep(1)                                     # sleep for 1 second
        p.ChangeDutyCycle(2.5)                  # change duty cycle for getting the servo position to 0
        time.sleep(1)                                     # sleep for 1 second
        p.stop()

    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()




