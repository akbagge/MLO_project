FROM python:3.8
WORKDIR /model


# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

COPY requirements.txt requirements.txt
COPY environment.yml environment.yml
COPY src/ src/
COPY data.py data.py

RUN conda create --name docker_env --file environment.yml
RUN pip3 install -r requirements.txt




CMD [ "python3", "data.py"]
