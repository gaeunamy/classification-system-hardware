import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

ENA = 17   # ENA 핀에 연결된 GPIO 핀 번호
IN1 = 27   # IN1 핀에 연결된 GPIO 핀 번호
IN2 = 22   # IN2 핀에 연결된 GPIO 핀 번호

trig_1 = 2  # 초음파 센서 트리거 핀
echo_1 = 3  # 초음파 센서 에코 핀

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(trig_1, GPIO.OUT)
    GPIO.setup(echo_1, GPIO.IN)

def motor_forward(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm = GPIO.PWM(ENA, 100)
    pwm.start(speed)

def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.cleanup()

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

if __name__ == "__main__":
    try:
        setup()
        print("DC start")

        while True:
            new_distance = distance_return()
            print(f"현재 거리: {new_distance:.2f}mm")

            if new_distance <= 30:  # 거리가 3cm 이하인 경우
                motor_stop()
                print("거리가 3cm 이하입니다. 5초 동안 일시정지합니다.")
                time.sleep(5)  # 5초 동안 일시정지

            else:
                motor_forward(50)  # 거리가 3cm 이상이면 모터를 전진

    except KeyboardInterrupt:
        pass
    finally:
        motor_stop()
