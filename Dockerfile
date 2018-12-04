FROM ubuntu:18.04

ENV DEBIAN_FRONTEND nonineractive

RUN mkdir /app/
WORKDIR /app/
COPY . /app

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

RUN apt install git -y
#RUN git clone https://github.com/psolanke/p2pConnection.git
RUN pip install -r requirements.txt

# --- for running --
EXPOSE 8080

WORKDIR /app/server/
CMD [ "python3", "flask_server.py"]
