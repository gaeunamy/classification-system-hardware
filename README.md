# YOLOv5를 이용한 과일 분류 시스템
<br/>

## 📝 작품 소개  
YOLOv5 기반 사과 자동 선별 시스템은 사과의 외형적 결함(압상, 자상, 병충해 등)을 인식하고 정상과 불량을 구별하여 최종적으로 사과의 품질 평가 작업을 수행하는 시스템이다.
시스템을 이용해 기존 수작업으로 진행되던 사과 품질 평가 작업을 자동화하여 고품질의 사과 생산과 효율성을 향상시킬 수 있을 것으로 기대한다.

- ## 소개 영상
[시스템 소개 영상 보기](https://youtu.be/dc5rjoLaHT0?si=LIahUHK1u_XYlSwK)

<br>

## 🌊 시스템 구성도
![000](https://github.com/user-attachments/assets/ee3d88d6-c89f-4bb2-8caf-0d11f109b767)

<br/>

- ## 전체 워크플로우
![mermaid-diagram-2024-10-03-203631](https://github.com/user-attachments/assets/394142d3-0640-4528-bdc7-6d091284155c)

<br/>

## ⭐ 주요 기능

### YOLOv5를 이용한 사과 상태 판별  
- 사과의 외형적 결함(자상, 압상, 병충해 등)을 인식하여 불량으로 분류
- 정상과 불량 사과를 판별하고 판별 정확도를 출력


- ## 모델 학습
  - 정상 사과 이미지 3,127장과 결점 사과 이미지 4,247장으로 데이터셋을 구성
  - 데이터의 다양성 확보와 모델의 일반화 능력을 향상하기 위해 회전, 좌우 반전, 밝기 조절, 대비 조절 등의 데이터 증강 기법을 적용
  - 모든 이미지는 416x416 픽셀로 조정하여 Roboflow를 통해 라벨링 작업 진행
  - 훈련 및 검증 데이터를 8:2 비율로 나누어 YOLOv5 모델 학습에 활용

<br>
    
<div align="center">
  <table>
    <tr>
      <th>분류</th>
      <th>이미지 수</th>
      <th>비율</th>
      <th>훈련 데이터</th>
      <th>검증 데이터</th>
    </tr>
    <tr>
      <td align="center">정상 사과</td>
      <td align="center">3,127</td>
      <td align="center">42.4%</td>
      <td align="center">2,502</td>
      <td align="center">625</td>
    </tr>
    <tr>
      <td align="center">결점 사과</td>
      <td align="center">4,247</td>
      <td align="center">57.6%</td>
      <td align="center">3,398</td>
      <td align="center">849</td>
    </tr>
    <tr>
      <td align="center"><strong>총계</strong></td>
      <td align="center"><strong>7,374</strong></td>
      <td align="center"><strong>100%</strong></td>
      <td align="center"><strong>5,900</strong></td>
      <td align="center"><strong>1,474</strong></td>
    </tr>
  </table>
</div>

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

 <br/>
 
- ## 실험 결과
  - 모델의 성능을 mAP, 정확도, 재현율, F1-Score을 통해 평가

<br>
  
<div align="center">
  <table style="border: 1px solid #ddd; border-collapse: collapse;">
    <tr>
      <th style="color: #fff; background-color: #333;">성능 지표</th>
      <th style="color: #fff; background-color: #333;">값</th>
      <th style="color: #fff; background-color: #333;">설명</th>
    </tr>
    <tr>
      <td align="center">mAP@0.5</td>
      <td align="center">0.991</td>
      <td align="center">IoU 임계값 0.5에서의 평균 정밀도</td>
    </tr>
    <tr>
      <td align="center">Precision</td>
      <td align="center">0.985</td>
      <td align="center">정확히 분류된 사과의 비율</td>
    </tr>
    <tr>
      <td align="center">Recall</td>
      <td align="center">0.982</td>
      <td align="center">정확히 검출된 사과의 비율</td>
    </tr>
    <tr>
      <td align="center">F1-score</td>
      <td align="center">0.970</td>
      <td align="center">Precision과 Recall의 조화 평균</td>
    </tr>
    <tr>
      <td align="center">Inference Time</td>
      <td align="center">0.015s</td>
      <td align="center">이미지당 평균 추론 시간</td>
    </tr>
  </table>
</div>

  
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/b95bfcee-a800-41d9-9fb1-14974479e36f" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/e3bba652-90f1-42f2-869f-597d280817b7" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" style="border: none;">
      <p align="center">정확도-재현율 그래프</p>
    </td>
    <td align="center" style="border: none;">
      <p align="center">F1-Score 그래프</p>
    </td>
  </tr>
<talbe/>

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
  <tr>
    <td align="center" colspan="2">
      <p align="center">실제 판별 결과</p>
    </td>
  </tr>
</table>
<br/>


### 실시간 캡처 및 저장  
- OpenCV를 활용해 실시간 비디오 스트림 캡처 및 사용자에게 영상 제공  
- 사과 감지 시 이미지를 캡처하여 서버(Rpi)의 로컬 폴더 내에 저장, 폴더를 1초마다 확인하고 새로운 JPG 파일을 감지하여 Firebase Storage로 업로드
  - 파일명은, 정상 사과는 normal_apple_YYYY-MM-DD_HH:MM:SS.jpg, 불량 사과는 rotten_apple_YYYY-MM-DD_HH:MM:SS.jpg로 자동 저장
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
   <tr>
    <td align="center" colspan="2">
      <p align="center">Firebase Storage에 저장</p>
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

- ## 작동 영상
  

https://github.com/user-attachments/assets/c24302dd-55c2-4657-a007-1b2105ec442e



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
| Fullstack | Hardware | Labeling |  
| :--------: | :--------: | :--------: |  
| [김가은](https://github.com/gaeunamy) | 정 * * | 맹 * * |
