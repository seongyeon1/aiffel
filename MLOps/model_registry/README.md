# MlOps 실습
- Data Generator on Docker

## 목표
- 모델을 학습하고 저장하는 기본적인 파이프라인을 작성합니다.

<br>

## 스펙 명세서
### 1. 학습 및 평가 데이터 선정
- `scikit-learn` 에서 제공하는 iris 데이터를 불러옵니다.
- 불러온 데이터를 학습 데이터와 평가 데이터로 분리합니다. 
- 이 때 분리된 데이터는 추후에 재현이 되어야 합니다.

<br>

### 2. 모델 개발 및 학습
- `scikit-learn` 에서 제공하는 Standard Scaler 와 SVC를 사용합니다.
- `1. 학습 및 평가 데이터 선정` 에서 나눈 학습 데이터를 이용하여 모델을 학습합니다.
- 학습된 모델을 이용하여 학습 데이터와 평가 데이터의 정확도를 계산합니다.

<br>

### 3. 학습된 모델 저장
- 학습된 모델을 joblib , pickle , dill 등의 패키지를 이용해 저장합니다.

<br>

### 4. 저장된 모델 불러오기
- 모델이 정상적으로 저장 되었는지 확인하기 위해 모델을 불러옵니다.
- 불러온 모델로 학습 데이터와 평가 데이터의 정확도를 계산합니다.
- `1. 학습 및 평가 데이터 선정` 에서 나눈 Validation 데이터를 이용하여 학습이 잘 되었는지 확인합니다.

해당 파트의 전체 코드는 [mlops-for-mle/part2/](https://github.com/mlops-for-mle/mlops-for-mle/tree/main/part2) 에서 확인할 수 있습니다.

### 파일 설치
```bash
$ make init
```
### 컨테이너 생성
```bash
$ make server
```
### 모든 서비스 컨테이너와 이미지를 한 번에 정지시키고 삭제 
```bash
$ make server-clean
```

### 컨테이너 안으로 들어가기 (container 안에서는 이 명령어 사용불가)
```bash
$ make go-container
```

### DB 연결 -> query로 db 확인
```bash
$ make db-connection
```
