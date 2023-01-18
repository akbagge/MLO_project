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
COPY uploads/ uploads/
COPY templates/ templates/
COPY main.py main.py  
COPY models/ models/
COPY resources/ resources/

RUN conda create --name docker_env --file environment.yml
RUN pip3 install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_ENV=production

EXPOSE 8080

#CMD [ "python3", "data.py"]
#CMD flask run --host 0.0.0.0 --port 8080
CMD ['python3', 'src/models/train_model.py', '--data-dir', 'output', '--num_classes', '5', '--img-size', '224', '-b', '50', '--epochs', '10', '--pretrained', '--log-wandb', '--experiment', 'timm']
