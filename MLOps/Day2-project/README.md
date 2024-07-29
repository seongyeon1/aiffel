# MlOps 실습
- Data Generator on Docker

## 목표
- DB 컨테이너와 Data Generator 컨테이너를 함께 띄우기 위한 Docker Compose 파일을 작성한다.
- DB 안에 데이터가 계속해서 삽입되고 있는지 확인한다.


## 스펙 명세서
1. Docker Compose 파일을 작성.
   - Postgres Server
     - Service name : postgres-server 
     - Image : postgres:14.0 
     - Container name : postgres-server 
     - Environment 
       - POSTGRES_USER : myuser
       - POSTGRES_PASSWORD : mypassword
       - POSTGRES_DB : mydatabase
     - Port forwarding : 5432:5432

   - Data Generator
     - Service name : data-generator
     - Image : Dockerfile
     - Container name : data-generator
     - Command : ["postgres-server"]

      
> - Postgres Server 서비스와 Data Generator 서비스를 띄울 때 어떤 서비스가 먼저 
> 생성되어야 하는지 생각해보고, 그 기능을 Compose 파일에 추가.
> - depends_on 으로 서비스 간의 종속성은 정했지만, 
> 실제로 postgres server 가 띄워진 뒤에 곧바로 Data Generator 가 띄워지게 되면 Postgres server 는 아직 준비가 되어있지 않은데 Data Generator 가 띄워져서 DB 에 연결을 하려다보니 Data Generator 가 Exited 되는 문제가 발생한다.
> - postgres server 가 사용 가능한 상태가 되어있는지 체크를 한 뒤에 Data Generator 를 띄워야 한다.
> - 이를 해결하기 위한 방법으로 [Docker Compose Healthcheck](https://github.com/peter-evans/docker-compose-healthcheck) 를 사용한다.

2. Docker Compose 파일 실행
3. psql 을 이용하여 DB 에 데이터가 계속해서 쌓이고 있는지 확인
   - Local 에서 확인
    ```bash
    $ make db-connection
    mydatabase=# select * from iris_data;
    ```
   - Data Generator server 에서 확인
   ```bash
    $ docker exec -it data-generator /bin/bash
    root@354b29f212f6:/usr/app# PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase
    mydatabase=# select * from iris_data;
    id |         timestamp          | sepal_length | sepal_width | petal_length | petal_width | target 
    ----+----------------------------+--------------+-------------+--------------+-------------+--------
      1 | 2024-07-29 07:35:03.546737 |          6.4 |         2.8 |          5.6 |         2.1 |      2
      2 | 2024-07-29 07:35:04.555192 |            5 |         3.2 |          1.2 |         0.2 |      0
      3 | 2024-07-29 07:35:05.560515 |          5.8 |         2.7 |          5.1 |         1.9 |      2
      4 | 2024-07-29 07:35:06.568681 |            6 |         2.7 |          5.1 |         1.6 |      1
      5 | 2024-07-29 07:35:07.573374 |          6.2 |         2.9 |          4.3 |         1.3 |      1
      6 | 2024-07-29 07:35:08.579074 |          7.4 |         2.8 |          6.1 |         1.9 |      2
      7 | 2024-07-29 07:35:09.589246 |          5.6 |         2.9 |          3.6 |         1.3 |      1
    ```

## Makefile 활용

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

### DB 연결 -> query로 db 확인
```bash
$ make db-connection
```
