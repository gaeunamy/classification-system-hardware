import socket
import cv2
import pickle
import struct
import torch
import threading

# YOLOv5 커스텀 모델 로드
model = torch.hub.load('C:/Users/사용자/Desktop/yolov5', 'custom', path='C:/Users/사용자/Desktop/yolov5/runs/train/exp/weights/best.pt', source='local')
labels = {0: '정상', 1: '불량'}  # 클래스 인덱스에 대응되는 라벨

# 프레임 수신 스레드
def receive_frames(client_socket):
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K
            if not packet:
                return None
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)

        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        return frame

# YOLOv5 예측 스레드
def predict_frame(frame):
    results = model(frame)
    return results

# 메인 클라이언트 함수
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = '192.168.161.25'  # 라즈베리 파이의 IP 주소
    port = 8888

    client_socket.connect((host_ip, port))

    while True:
        frame = receive_frames(client_socket)
        if frame is None:
            break

        # YOLOv5 모델을 사용하여 객체 감지
        results = predict_frame(frame)

        # 결과를 이미지에 렌더링
        result_img = results.render()[0]
        cv2.imshow('YOLOv5 Object Detection', result_img)

        # 객체 분류 결과 전송
        if '불량' in [labels[int(pred[-1])] for pred in results.pred[0]]:
            client_socket.send(b"defective")
        else:
            client_socket.send(b"normal")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_client()
