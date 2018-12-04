FROM ubuntu:18.04

#  
# -- if you are using docker behind proxy, please set ENV --
#

#ENV http_proxy "http://proxy.yourdomain.com:8080/"
#ENV https_proxy "http://proxy.yourdomain.com:8080/"

ENV DEBIAN_FRONTEND nonineractive

#
# -- build tools --
#
RUN apt update && apt upgrade -y

RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install python3-dev -y
RUN python3 -V
RUN pip3 -V
RUN pip3 install --upgrade pip
RUN pip -V

RUN apt install pkg-config -y
RUN apt install libavdevice-dev -y
RUN apt install libavfilter-dev -y
RUN apt install libopus-dev -y
RUN apt install libvpx-dev -y
RUN apt install libffi-dev -y
RUN apt install libssl-dev -y
RUN apt install libopencv-dev -y

RUN mkdir /root/work 
WORKDIR /root/work/

RUN apt install git -y
RUN git clone https://github.com/jlaine/aiortc.git

RUN pip install aiohttp
RUN pip install aiortc 
RUN pip install opencv-python

# --- for running --
EXPOSE 8080

WORKDIR /root/work/aiortc/examples/server/
CMD [ "python3", "server.py", "-v" ]
