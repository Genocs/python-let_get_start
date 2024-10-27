# syntax=docker/dockerfile:1
FROM docker.io/continuumio/miniconda3:latest

WORKDIR /

COPY ./requirements.txt /requirements.txt

# gcc is for build psutil in MacOS
RUN apt-get update && apt-get install -y runit gcc

# create conda environment
RUN conda create -n uvicorn-serve python=3.11.9 pip=23.3.1 -q -y && \
    conda run -n uvicorn-serve \
    pip install -r /requirements.txt && \
    conda run -n uvicorn-serve pip cache purge && \
    conda clean -a -y

COPY ./src /src

EXPOSE 8000

# reset runsvdir
RUN rm -rf /var/runit
COPY ./runit /var/runit

# grant permission
RUN chmod -R +x /var/runit

COPY ./start.sh /
CMD ["bash", "./start.sh"]
