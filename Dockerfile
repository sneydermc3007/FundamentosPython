FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3-pip

RUN rm -rf /app && mkdir /app

COPY ./entregables /app/entregables

WORKDIR /app/entregables

CMD ["python3", "exercise1.py"]
