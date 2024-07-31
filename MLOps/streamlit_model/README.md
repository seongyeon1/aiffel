# Model API (FastAPI, streamlit)
- MlOps 실습

## 목표
- Iris 데이터를 입력받아 예측값을 반환하는 API 를 작성합니다.
- 작성한 API 에 데이터를 전달하여 제대로 작동하는지 확인합니다.
- streamlit을 통해 예측결과를 웹에서 볼 수 있다.

## 결과
- streamlit을 통해 iris 종 예측결과를 확인하는 페이지입니다.
![Screenshot 2024-07-31 at 5 35 37 PM](https://github.com/user-attachments/assets/88044060-b76a-4334-a924-a73da8f1d2a8)


## 스펙 명세서

1. `03. Model Registry`  파트에서 모델을 학습한 후 저장한 MLflow 서버의 Model Registry 에서 모델을 로컬로 다운로드받는 스크립트 `download_model.py` 를 작성하고 실행합니다.
2. `POST /predict` 를 수행하면 학습한 모델의 inference 결과를 반환하는 API 의 명세서를 작성합니다.
3. `schemas.py` 에서 Pydantic 을 사용해 input schema 와 output schema 의 클래스를 작성합니다.
    - Input schema: `Class PredictIn(BaseModel)` 을 이용
        - Column 이름: 01. Database 파트에서 작성한 이름과 동일
    - Output schema: `Class PredictOut(BaseModel)` 을 이용
        - Column 이름: `iris_class`작성한 명세서를 FastAPI 를 이용해 `app.py` 에 구현합니다.작성한 API 에 데이터를 전달하여 잘 작동하는지 확인합니다.

해당 파트의 전체 코드는 [mlops-for-mle/part6/](https://github.com/mlops-for-mle/mlops-for-mle/tree/main/part6) 에서 확인할 수 있습니다.

---
## Makefile 구성

### 데이터 생성 
- 현재 폴더 실행전 꼭 먼저 실행
```bash
$ make dependency
```
### dependency clean
- 관련 이미지 및 컨테이너 모두 삭제
```bash
$ make dependency-clean
```

### 파일 설치
```bash
$ make init
```

### API 작동 확인
```bash
$ make app
```

### 컨테이너 생성
```bash
$ make server
```
### 모든 서비스 컨테이너와 이미지를 한 번에 정지시키고 삭제 
```bash
$ make server-clean
```

### 위에서 모든 과정(dependency, server 한 번에) 실행
```bash
$ make all
```
### 위에서 모든 과정(dependency, server 한 번에) 종료
```bash
$ make all-clean
```
