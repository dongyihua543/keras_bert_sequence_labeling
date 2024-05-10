#FROM docker-register-registry-vpc.cn-shanghai.cr.aliyuncs.com/ai/starlab-base:v0.0.2
FROM docker-register-registry-vpc.cn-shanghai.cr.aliyuncs.com/ai/starlab-base:v0.0.3

WORKDIR /app

COPY requirements.txt .

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget git make vim tmux
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

