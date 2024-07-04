import RPi.GPIO as GPIO
import time


ENA = 17   # ENA 핀에 연결된 GPIO 핀 번호
IN1 = 27   # IN1 핀에 연결된 GPIO 핀 번호
IN2 = 22  # IN2 핀에 연결된 GPIO 핀 번호

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)

def motor_forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm = GPIO.PWM(ENA, 100)
    pwm.start(speed)
    time.sleep(2)
    
    
def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.cleaup()
    
if __name__ == "__main__":
    try:
        setup()
        print("DC start")
        
        
        motor_forward(50)
        
        
    except KeyboardInterrupt:
        pass
    finally:
        motor_stop()