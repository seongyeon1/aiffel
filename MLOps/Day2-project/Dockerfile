#FROM --platform=$BUILDPLATFORM python:3.9-slim
FROM --platform=linux/amd64 python:3.9-slim

RUN apt-get update && apt-get install -y \
	postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app

#RUN pip install -U pip && \
#    pip install scikit-learn pandas psycopg2-binary
RUN make init

COPY data_generator.py data_generator.py
COPY Makefile Makefile

ENTRYPOINT ["python", "data_generator.py", "Makefile","--db-host"]
# Change CMD to solve host finding error
CMD ["localhost"]