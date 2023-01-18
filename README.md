# MLOPS_group3

### Project structure

------------

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── Rice_Image_Dataset <- External dataset
    │   ├── Arborio       
    │   ├── Basmati        
    │   ├── Ipsala
    │   ├── Jasmine        
    │   └── Karacadag
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    |
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    |
    |
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## Project Description

### Goal
This is the project description for group 3 in the 02476 Machine Learning Operations course on DTU. The overall goal of the project is to apply the material we have learned in the course to a machine learning problem, while using one of the given frameworks to do so. We will then finally present our findings in a short presentation as well as hand in the written code.

### Framework
The framework we have chosen for this project is the TIMM framework for Computer Vision (PyTorch Image Models). We will be using this framework to construct a deep learning model and apply it to our data. We expect to set up the framework as part of our environment, while writing organized and structured code with version control.

### Data
The data we have initially chosen to work with is a [Rice Image](https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset) dataset from Kaggle consisting of 75K images different types of rice. There are 5 total types of rice: Arborio, Basmati, Ipsala, Jasmine and Karacadag and there are 15K images of individual grains of rice for each type.

### Models
We intend to perform an image classification task on the rice data using some type of CNN. We expect to be using different models from the TIMM framework such as ConvNeXt, MobileNet V3, ResNet and VGG.
