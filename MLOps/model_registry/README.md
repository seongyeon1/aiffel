# Model Registry
- MlOps 실습

## 목표
- Docker Compose 를 이용하여 실제 서비스 환경과 비슷한 형태로 MLflow 서버를 띄워봅니다.
- 서비스 상황을 가정하여 MLflow 의 구성 요소들을 이해합니다.

## 스펙 명세서
- Docker Compose 파일에 MLflow 의 운영 정보, 모델 결과 등을 저장할 물리적인 PostgreSQL DB 서버 스펙을 정의합니다.
    - POSTGRES_USER : mlflowuser
    - POSTGRES_PASSWORD : mlflowpassword
    - POSTGRES_DB : mlflowdatabase
- Docker Compose 파일에 학습된 모델을 저장할 물리적인 저장 공간인 MinIO 서버 스펙을 정의합니다.
    - MINIO_ROOT_USER : minio
    - MINO_ROOT_PASSWORD : miniostorage
    - Port forwarding :
        - api: 9000:9000
        - console: 9001:9001
- Docker Compose 파일에 모델과 모델의 결과들을 관리할 MLFlow 서버를 정의합니다.
    - 환경 변수를 이용하여 MLflow 서버에서 앞서 띄워둔 PostgreSQL DB 와 MinIO 두 가지 서버에 접근이 가능하도록 연결합니다.

    - Dockerfile
        - MLflow 에 관련된 패키지가 설치된 이미지를 생성하기 위한 Dockerfile 을 정의합니다.
        - MinIO 에 모델 저장을 위한 초기 버켓을 생성 하기 위해 MinIO Client 도 함께 설치되도록 합니다.
    - Docker Compose
        - MinIO 의 접속 정보를 AWS_ACCESS_KEY_ID , AWS_SECRET_ACCESS_KEY 환경 변수를 통해 적절하게 설정합니다.
        - MinIO Client 를 설치하고, MinIO 의 초기 버켓을 생성하도록 명령어를 작성합니다.
        - MLflow 서버를 띄우는 명령어를 작성합니다.
        - Port forwarding : 5001:5000
            - MLflow 에서는 기본값으로 5000 포트를 사용합니다.
            - 하지만 실습에서 MacOS 를 사용하는 경우 AirPlay 기능이 5000번 포트를 사용하기 때문에 중복을 피하기 위해 5001번 포트를 사용합니다.
            - 일반적인 경우 5000번 포트를 사용하면 됩니다.
    - 정의된 스펙에 따라 서비스들을 띄웁니다.
        - localhost:9001 에 접속하여 MinIO 로그인 페이지가 잘 동작하는지 확인합니다.
        - localhost:5001 에 접속하여 MLflow 페이지가 잘 동작하는지 확인합니다.

해당 파트의 전체 코드는 [mlops-for-mle/part3/](https://github.com/mlops-for-mle/mlops-for-mle/tree/main/part3) 에서 확인할 수 있습니다.

---
---
## Makefile 구성

### 현재 폴더 실행전 꼭 먼저 실행 
- 데이터 생성
```bash
$ make dependency
```
### 현재 폴더 실행전 꼭 먼저 실행 
- 관련 이미지 및 컨테이너 모두 삭제
```bash
$ make dependency
```

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

### 위에서 모든 과정(dependency, server 한 번에) 실행
```bash
$ make all
```
### 위에서 모든 과정(dependency, server 한 번에) 종료
```bash
$ make all-clean
```
