FROM docker-register-registry-vpc.cn-shanghai.cr.aliyuncs.com/ai/pytorch:1.13.1-cuda11.6-cudnn8-devel

WORKDIR /app

COPY requirements.txt .

ARG DEBIAN_FRONTEND=noninteractive

ENV HTTP_PROXY=10.18.252.1:6152 HTTPS_PROXY=10.18.252.1:6152

RUN apt update && apt install -y git vim wget sudo ffmpeg libsm6 libxext6 build-essential

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-x86_64.sh \
    && chmod +x ./Miniconda3-py37_4.10.3-Linux-x86_64.sh \
    && ./Miniconda3-py37_4.10.3-Linux-x86_64.sh -b -p /root/anaconda
ENV PATH="/root/anaconda/bin:$PATH"

ENV CUDA_HOME /usr/local/cuda-11.6/

RUN apt-get update && apt-get install -y wget git make vim tmux
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
RUN pip3 install /root/.ssh/keras-contrib-master.zip

ENV HTTP_PROXY="" HTTPS_PROXY=""
