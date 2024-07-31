# Docker Hub에서 MySQL 이미지를 기본 이미지로 사용합니다
FROM mysql:8.2.0

# 환경변수 설정
ENV MYSQL_ROOT_PASSWORD=1234

# 파일 복사
COPY exam.sql /docker-entrypoint-initdb.d/