import RPi.GPIO as GPIO
import time

pin = 21
pin2 =  3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

pin_pwm = GPIO.PWM(pin, 100)  #(pin, frequency)
pin_pwm2 = GPIO.PWM(pin2, 100)  #(pin, frequency)

pin_pwm.start(0)    #(dutycycle)
pin_pwm2.start(0)    #(dutycycle)
i=0
i2=0
start_time = 0

while True:

    try:

        #pwm

        GPIO.output(pin, 0)
        time.sleep(0.00001)
        GPIO.output(pin, 1)
        time.sleep(0.00001)




        #time.sleep(0.1)
        """
        i = (i+5) % 105 #0 ~ 100
        i2 = ( i2 + 10) % 105

        print("pin21:{}".format(i))
        print("pin2:{}".format(i2))

        pin_pwm.ChangeDutyCycle(i)
        pin_pwm2.ChangeDutyCycle(i2)

        time.sleep(0.5)
        """




    except:
        print("finish!!")
        GPIO.cleanup()
        GPIO.output(pin, 0)
        GPIO.output(pin2, 0)
        pin_pwm.stop()
        pin_pwm2.stop()
        exit(1)


"""
while True:
    try:
        print('start!')
        GPIO.output(pin, 1)

        #time.sleep(0.1)

        #GPIO.output(pin, 0)
        #time.sleep(0.1)

    except:
        print('stop!!')
        GPIO.output(pin,0)
        GPIO.cleanup()
        exit(1)
"""