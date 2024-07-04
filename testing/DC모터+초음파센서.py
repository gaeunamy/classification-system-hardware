import RPi.GPIO as GPIO
import time

IN1 = 6  # DC 모터 드라이버 IN1 핀
IN2 = 7  # DC 모터 드라이버 IN2 핀
ENA = 14 # ENA
trig_1 = 2 # 초음파 센서 트리거 핀
echo_1 = 3  # 초음파 센서 에코 핀

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(trig_1, GPIO.OUT)
    GPIO.setup(echo_1, GPIO.IN)

def motor_go():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

def distance_return():
    GPIO.output(trig_1, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(trig_1, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_1, GPIO.LOW)

    pulse_start_time = time.time()
    pulse_end_time = time.time()

    while GPIO.input(echo_1) == 0:
        pulse_start_time = time.time()

    while GPIO.input(echo_1) == 1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = pulse_duration * 343 / 2
    return distance

def sensor_print(distance):
    print(f"거리: {distance:.2f}mm")
    time.sleep(0.5)

if __name__ == "__main__":
    setup()

    try:
        print("초음파 센서 시작")
        while True:
            new_distance = distance_return()
            sensor_print(new_distance)

            if new_distance > 100:
                motor_go()
            else:
                motor_stop()

    except KeyboardInterrupt:
        pass
    #finally:
        #GPIO.cleanup()