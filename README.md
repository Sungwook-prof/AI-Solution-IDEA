# AI-Solution-IDEA
2024 AI 솔루션 아이디어 경진대회 &amp; 창업캠프

# 공지 #
- 대회 일정이 겹치는 연세대 다른 캠프 또는 대회 관련 참가자 동시 참여 불가함
  (대회 당일 타 대회 참여자 목록 비교 후 참여제한 조치 시행 예정)
- 대학원생 참여가능함 (단, 팀 선정에서 대학생팀 우선 배정 원칙을 적용함)
- 카메라, 드론 기반 솔루션 개발은 즉시 진행가능하며, 장비 요청의 경우 아래 안내된 메일로 신청 가능함.
- 멘토링도 메일로 신청하여 스케줄 협의후 진행가능함. 

# 사전 학습
1) 카메라 기반 Object Detection
- 데이터 셋 : [다운로드](https://drive.google.com/file/d/1ND6HWbIJuINC-0-7XrJu2XzZoCtCbuFz/view?usp=drive_link)
- YOLOv9 학습 노트북 : train_yolov9.ipynb
- YOLOv9 학습 교재 : YOLOv9 Training.pdf
- YOLOv9 OpenVINO 모델 변환 노트북 : convert_yolov9.ipynb
- YOLOv9 추론 교재 : YOLOv9 Inferencing.pdf
- YOLOv9 OpenVINO 모델 경량화 노트북 :  quantize_yolov9.ipynb
- 인식 코드 : [camera.zip](https://drive.google.com/file/d/1cNEbD9QCJ0d7-ucSsMlSvD3JWBVOkyOt/view?usp=drive_link)
- 카메라 또는 동영상 파일 기반 인식 프로그램을 변형하여, 아이디어를 구현한 AI 솔루션으로 변경해야 함.
- 동영상 강좌1 [YOLOv9 colab 학습](https://youtu.be/eHtbDfvnKu8)
- 동영상 강좌2 [동영상 추론 프로그램 강좌](https://youtu.be/WlE58lXgXgM)

2) Drone 기반 Image Classification
- 데이터 셋 : [데이터 다운로드](https://drive.google.com/file/d/1hdAZOkMQq-1fZBh-VsxZNYim1XERT8AD/view?usp=sharing)
- mobilenet 학습 노트북 : AI_Hackaton.ipynb
- mobilenet 추론 노트북 : AI_Hackaton2.ipynb
- mobilenet 학습 교재 : AI Training and Inferencing.pdf
- mobilenet 추론 교재 : Drone Classification.pdf
- 인식 프로그램 : drone.zip
- 드론 기반 인식 프로그램을 변형하여 드론을 활용하여 인식하는 솔루션으로 변경해야 함.
- 동영상 강좌1 [이미지 인식](https://youtu.be/fomZdMWF0W0?feature=shared)
- 동영상 강좌2 [인식 프로그램 강좌](https://youtu.be/MVNxox1S6pI)

# 팀별 지원
- Colab GPU 사용료 지원, 팀당 최대 2개 계정 지원 (대회 기간 중 사용료 영수증 증빙 후 통장 입금 처리함)
- 카메라 또는 드론 지원
- 매주 멘토링 지원(문제 해결, 코딩, 아디이어 등)
- 증빙 제출, 장비 요청, 멘토링 요청 : fpga@yonsei.ac.kr

# 지원 목록
- 지원장비는 필수는 아닙니다. 폰이나 다른 촬영장비로 mp4파일을 만들 수 있는 경우 팀내 장비활용가능합니다.
- 카메라의 경우 iptime 카메라로 sd 카드로 기록하고, 해당 파일을 컴퓨터로 옮겨와 작업가능합니다.
- 드론의 경우는 intel Tello 드론으로 지원되면 tello의 경우도 폰으로 녹화한 후 해당 mp4 파일을 활용하거나, 실시간으로 구동되는 영상을 다시 녹화하여 발표시 활용해야 합니다.
- 멘토링 시간의 경우 협의후 아래 테이블에 수정 반영할 예정입니다. 멘토링 회수나 멘토링 유무가 점수로 반영되는 것은 아니므로, 필수 절차는 아닙니다. 

|팀명|contact|지원장비|멘토링1|멘토링2|멘토링3|
|-|-|-|-|-|-|
|이글스|정제원|드론|10/16 17:00|||
|BOAA|최승현|카메라|10/14 13:00||10:28 17:00|
|DenAI|송혜인||10/17 17:00|||
|두어스|권기범||10/14 14:00|||
|포워드|이희진||10/17 18:00|10/28 18:00||

# FAQ
[Q] 기존 드론 대회같은 방식인가요?

[A] 이번 대회는 인공지능 솔루션 아이디어를 발표하고, 해당 아이디어로 객체 인식 솔루션이나 객체 분류 솔루션에 따라서 코드로 구현한 솔루션을 평가받는 대회입니다. 카메라나, 드론으로 촬영한 mp4 비디오 파일을 활용해서 인식되는 것을 시각화하거나 인식된 것을 이용해서 아이디어를 구체화하는 것을 평가받습니다. 

[Q] 일반 아이디어 대회와 차이점은 무엇인가요?

[A] 전체 평가 점수중 일반 아이디어와 같이 신규성, 진보성, 과제 착안점, 개발 가능성 등 일반적인 점수가 50점이고, 나머지 50점은 아이디어 구현 정도를 평가 받습니다. 

[Q] 다른 곳에 논문이나 제출한 아이디어도 가능한가요? 

[A] 이번 대회는 OpenVINO를 활용한 솔루션 구현 정도를 보는 것으로 제출한 코드에 대해서 심사를 거칩니다. 해외 컨퍼런스 특전이 있는 대상과 금상은 반드시 구현된 코드가 있어야 하며, 단순 아이디어 발표의 경우 50점을 받을 수 없습니다. 

[Q] 본인 카드로 구글 게정 결제가 아닌 경우, 증빙은 어떻게 할 수 있나요?

[A] 부모님이나 가족관계 증명서에 있는 분의 카드로 결제 후, 가족관계증명서, 해당 가족 카드 결제 영수증, 본인 통장 사본으로 제출가능합니다. 

[Q] 카메라나 드론를 필수로 신청해야 하나요?

[A] 필수는 아니면 팀내 영상 촬영장비로 촬영한 mp4 파일로 인식하거나 분석하는 솔루션으로 구현 가능합니다. 실시간 처리인 경우, 실시간 처리 프로그램을 다시 녹화해서 발표시에 활용하면 됩니다. 

- 추가적인 메일로 질문한 질의 내용에 대해서 FAQ로 반영할 예정입니다. 

![poster](https://github.com/Sungwook-prof/AI-Solution-IDEA/blob/main/POSTER.jpg)
