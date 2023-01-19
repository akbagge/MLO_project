FROM python:3.10
WORKDIR /model

RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

COPY requirements.txt requirements.txt
COPY environment.yml environment.yml
COPY src/ src/
COPY models/ models/

RUN conda create --name docker_env --file environment.yml
RUN pip3 install -r requirements.txt

WORKDIR /model/src
ENV FLASK_APP=api/main
ENV FLASK_ENV=production

EXPOSE 8080

CMD flask run --host 0.0.0.0 --port 8080
