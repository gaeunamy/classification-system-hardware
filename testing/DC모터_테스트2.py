from gpiozero import Motor
import time

ENA = 17
IN1 = 27
IN2 = 22

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(ENA, GPIO.OUT)
    
def motor_forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    pwm = GPIO.PWM
