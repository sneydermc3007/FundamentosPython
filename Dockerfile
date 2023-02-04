FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl

RUN pip3 install jupyter

WORKDIR /app

COPY . .

ENV JUPYTER_ENABLE_LAB yes

EXPOSE 8888

CMD ["jupyter", "lab", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]