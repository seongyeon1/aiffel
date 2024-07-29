#FROM --platform=$BUILDPLATFORM python:3.9-slim
FROM --platform=linux/arm64 python:3.9-slim

RUN apt-get update && apt-get install -y \
	postgresql-client \
    make \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app

#RUN pip install -U pip && \
#    pip install scikit-learn pandas psycopg2-binary

COPY Makefile-docker Makefile
COPY data_generator.py data_generator.py

RUN make init

ENTRYPOINT ["python", "data_generator.py", "--db-host"]
# Change CMD to solve host finding error
CMD ["localhost"]