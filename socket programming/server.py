import socket
import cv2
import pickle
import struct
import pigpio
import time
from threading import Thread
import os
from datetime import datetime

# GPIO 초기화 및 설정
ENA_PIN = 27  # Enable A 핀
IN1_PIN = 17  # Input 1 핀
IN2_PIN = 22  # Input 2 핀
TRIG_PIN = 24  # 초음파 센서의 TRIG 핀 번호
ECHO_PIN = 23  # 초음파 센서의 ECHO 핀 번호
SERVO_PIN = 18  # 서보모터 핀 번호

# 초음파 센서 초기화
pi = pigpio.pi()
if not pi.connected:
    exit()  # pigpio 데몬이 실행되지 않았으면 종료

pi.set_mode(TRIG_PIN, pigpio.OUTPUT)
pi.set_mode(ECHO_PIN, pigpio.INPUT)

# DC 모터 제어 함수 (80% 속도, 전진만)
def control_motor(state):
    if state == 1:  # 전진
        pi.write(IN1_PIN, 1)
        pi.write(IN2_PIN, 0)
        pi.set_PWM_dutycycle(ENA_PIN, 255)  # 80% 속도 (255 * 0.8 = 204)
    elif state == 0:  # 정지
        pi.write(IN1_PIN, 0)
        pi.write(IN2_PIN, 0)
        pi.set_PWM_dutycycle(ENA_PIN, 0)

# 서보모터 제어 함수
def rotate_servo(angle):
    duty = angle / 180 * 2000 + 500
    pi.set_servo_pulsewidth(SERVO_PIN, duty)

# 초음파 센서로 거리 측정 함수
def measure_distance():
    pi.write(TRIG_PIN, 1)
    time.sleep(0.00001)
    pi.write(TRIG_PIN, 0)

    start_time = time.time()
    while pi.read(ECHO_PIN) == 0:
        if time.time() - start_time > 1:
            return None

    pulse_start = time.time()
    while pi.read(ECHO_PIN) == 1:
        if time.time() - pulse_start > 1:
            return None

    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # cm 단위

    return distance

# 클라이언트로 이미지 전송 및 결과 수신 함수
def send_frame_and_receive_result(client_socket, frame):
    data = pickle.dumps(frame)
    message_size = struct.pack("Q", len(data))
    client_socket.sendall(message_size + data)
    result = client_socket.recv(1024).decode()
    return result

# 객체 감지 및 웹캠 화면 표시 함수
def object_detection(client_socket):
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Object Detection', cv2.WINDOW_NORMAL)
    control_motor(1)  # 모터 전진 시작

    save_path = "/home/kge/captured_images"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            distance = measure_distance()
            if distance is not None:
                print(f"Measured Distance = {distance:.2f} cm")
            else:
                print("Error measuring distance")

            if distance is not None and distance < 30:  # 예시로 30cm 이내에 물체가 감지되면
                control_motor(0)  # 모터 정지

                result = send_frame_and_receive_result(client_socket, frame)
                current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

                if result == "defective":
                    img_name = os.path.join(save_path, f"rotten_apple_{current_time}.jpg")
                    rotate_servo(180)  # 서보모터 회전
                    time.sleep(3)  # 회전 후 3초 대기
                    rotate_servo(0)  # 원래 위치로 회전
                else:
                    img_name = os.path.join(save_path, f"normal_apple_{current_time}.jpg")

                cv2.imwrite(img_name, frame)
                #time.sleep(3)  # 3초 대기 후 다시 모터 동작
                control_motor(1)  # 모터 다시 동작
                time.sleep(5)  # 3초 동안 모터가 무조건 동작

            cv2.imshow('Object Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        control_motor(0)  # 프로그램 종료 시 모터 정지
        cap.release()
        cv2.destroyAllWindows()
        client_socket.close()

# 소켓 서버 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.161.25'  # 라즈베리 파이의 IP 주소
port = 8888
server_socket.bind((host_ip, port))
server_socket.listen(5)
print('서버 대기 중...')

try:
    while True:
        client_socket, addr = server_socket.accept()
        print('클라이언트 연결됨:', addr)

        # 객체 감지 및 웹캠 화면 표시 스레드 시작
        object_detection_thread = Thread(target=object_detection, args=(client_socket,))
        object_detection_thread.start()
except KeyboardInterrupt:
    print("서버 종료 중...")
finally:
    server_socket.close()
    pi.stop()  # pigpio 종료