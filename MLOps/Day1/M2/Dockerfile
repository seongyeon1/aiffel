#Dockerfile
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /code

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

#현재 디렉토리의 모든 파일을 컨테이너의 /code 디렉토리로 복사
COPY . /code

ENTRYPOINT ["python3"]
CMD ["app.py"]


FROM builder as dev-envs

#git,bash
RUN <<EOF
apk update
apk add git bash
EOF

#dockergroup
RUN <<EOF
addgroup -S docker
adduser -S --shell /bin/bash --ingroup docker vscode
EOF
# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /