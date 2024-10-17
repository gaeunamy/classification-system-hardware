# YOLOv5를 이용한 과일 분류 시스템
<br/>

## 📝 프로젝트 설명  
이 프로젝트는 YOLOv5 딥러닝 모델을 활용하여 정상과 불량 과일을 자동으로 분류하는 시스템을 개발한 것입니다. OpenCV와 PyTorch를 이용하여 이미지 및 영상을 실시간으로 처리하고, Socket과 Linux 기반의 서버-클라이언트 구조로 데이터를 송수신하며 하드웨어 제어를 통해 분류 작업을 자동화합니다.
<br/>
<br/>

## 🌊 시스템 구성도
![000](https://github.com/user-attachments/assets/ee3d88d6-c89f-4bb2-8caf-0d11f109b767)

<br/>

- ## 전체 워크플로우
![mermaid-diagram-2024-10-03-203631](https://github.com/user-attachments/assets/394142d3-0640-4528-bdc7-6d091284155c)

<br/>

## ⭐ 주요 기능

### YOLOv5를 이용한 사과 상태 판별  
- 7,434장의 정상 및 불량 사과 이미지 수집, 전처리 및 라벨링  
- YOLOv5s 모델을 사용하여 하이퍼파라미터 최적화 및 모델 학습  
- 자상, 압상, 병충해 등을 인식하여 불량 또는 정상으로 처리
  
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/ac8c4604-d773-48a9-8a20-d097361a3423" width="75%" />
    </td>
  </tr>
  <tr>
    <td align="center" style="border: none;">
      <p align="center">모델 학습 데이터셋</p>
    </td>
</table>

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/bdeefd08-ca25-456f-b644-bf4840227fe2" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/46d2c09a-91e9-4698-b721-65da79548074" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" style="border: none;">
      <p align="center">정상 사과 판별</p>
    </td>
    <td align="center" style="border: none;">
      <p align="center">불량 사과 판별</p>
    </td>
  </tr>
</table>
<br/>

### 실시간 캡처 및 저장  
- OpenCV를 활용해 실시간 비디오 스트림 캡처 및 사용자에게 영상 제공  
- 사과 감지 시 이미지를 캡처하여 로컬 폴더 내에 저장, 폴더를 1초마다 확인하고 새로운 JPG 파일을 감지하여 Firebase Storage로 업로드  
- Socket 통신을 이용한 서버와 클라이언트 간 실시간 데이터 송수신 처리
  
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/ef1d16b2-768c-4c27-8402-cccb482f3227" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/e545252a-3da8-4a9e-90be-06deaab889d7" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" style="border: none;">
      <p align="center">정상 사과 이미지 업로드</p>
    </td>
    <td align="center" style="border: none;">
      <p align="center">불량 사과 이미지 업로드</p>
    </td>
  </tr>
</table>
<br/>

### 분류 시스템 제어  
- 분류 시스템의 하드웨어 설계 및 임베디드 시스템 개발  
- 컨베이어 벨트(DC 모터, 서보 모터, 초음파 센서로 구성)의 동작을 제어하여 정상/불량 판별 결과에 따라 과일을 분류
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/19bc07fe-f1f8-49eb-89a2-29eb163cabca" width="75%" />
    </td>
  </tr>
  <tr>
    <td align="center" style="border: none;">
      <p align="center">분류 시스템</p>
    </td>
</table>
<br/>

## ⚙️ 트러블 슈팅

### 정상과 불량 판별 오류  
- **문제점**: 정상 사과를 불량으로 잘못 판별하는 현상 발생  
- **원인**: 모델이 특정 조명 조건이나 각도에서 정상 사과를 불량으로 잘못 판별  
- **해결 방법**: 데이터셋에 다양한 조명 조건과 각도의 이미지를 추가하여 모델의 일반화 능력 향상 및 추가적인 데이터 증강 기법을 적용하여 판별 정확도 개선

### 영상 전송 시의 프레임 딜레이  
- **문제점**: 영상 처리 시, 프레임 딜레이가 20초 이상으로 길게 나타나는 문제 발생  
- **원인**: 라즈베리파이가 영상 분석 및 분류 시스템 제어를 동시에 처리하면서 과부하 발생  
- **해결 방법**: Socket 모듈을 이용해 영상 분석과 분류 시스템 제어를 클라이언트와 서버로 분리하여 프레임 딜레이를 20초 이상에서 5초 이내로 줄임

<br/>

## 🔧 Stack  
**Language**  
- Python  

**Libraries & Frameworks**  
- YOLOv5, OpenCV, PyTorch, Socket, Torch/TorchVision  

**Tools & OS**  
- Roboflow, Linux(Debian GNU/Linux 11  (bullseye))

  **Storage**
  - Firebase(Storage, Real-Time Database)
 
**Hardware**  
- Raspberry Pi 4 4GB, DC 기어 모터(모델명), 서보 모터(모델명), 초음파 센서(HC-SR04), 웹캠(720p)  

<br/>

## 🙋‍♂️ Developer  
| Fullstack |  
| :--------: |  
| [김가은](https://github.com/gaeunamy) |
