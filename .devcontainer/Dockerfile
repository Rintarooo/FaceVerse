# https://pytorch.org/get-started/previous-versions/
ARG TORCH_VER=1.11.0
ARG TORCH_VISON_VER=0.12.0
ARG CUDA_VER=11.3.1
ARG UBUNTU_VER=20.04


# Requirements for v1&v2
# Python 3.9
# PyTorch 1.11.0
# torchvision 0.11.1
# PyTorch3D 0.6.0
# Cuda 11.3
# ONNX Runtime
# OpenCV
# Numpy
# tqdm
# ninja
# You need to compile the ops provided by stylegan2-pytorch using ninja:

# Requirements
# jittor
# mediapipe
# opencv-python
# numpy
# tqdm
# onnxruntime

# check whether the base image exists in dockerhub repo
# https://hub.docker.com/r/nvidia/cuda
# FROM nvidia/cuda:${CUDA_VER}-base-ubuntu${UBUNTU_VER}
# FROM nvidia/cuda:${CUDA_VER}-cudnn8-runtime-ubuntu${UBUNTU_VER}
FROM nvidia/cuda:${CUDA_VER}-cudnn8-devel-ubuntu${UBUNTU_VER}


ARG DEBIAN_FRONTEND=noninteractive

ENV WORK_DIR /app
WORKDIR ${WORK_DIR}

ARG TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone

# Install some basic utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    sudo \
    wget \
    curl \
    vim \
    git \
    bzip2 \
    build-essential \
    vim \
    libgl1-mesa-glx \
    x11-apps \
    libglib2.0-0 \
    zlib1g-dev \
    libffi-dev \
    libssl-dev \
    python3-pip \
    python3-dev \
    cmake \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# https://freak-da.hatenablog.com/entry/2020/03/31/094140
ARG TORCH_VER
ARG TORCH_VISON_VER
ARG UBUNTU_VER
ARG PYTHON_VER=3.9.0
ARG PYTHON_VER_MAJOR=39
ARG CUDA_VER_MAJOR=113
ARG TORCH3D_VER=0.6.2
ENV PYTHON_INSTALL_DIR /my_python/

# Install Python
RUN mkdir -p ${PYTHON_INSTALL_DIR} \
    &&  cd ${PYTHON_INSTALL_DIR} \
    &&  wget https://www.python.org/ftp/python/$PYTHON_VER/Python-$PYTHON_VER.tgz \
    &&  tar -xf Python-$PYTHON_VER.tgz \
    &&  rm Python-$PYTHON_VER.tgz \
    &&  cd Python-$PYTHON_VER/ \
    &&  ./configure --enable-optimizations \
    &&  make -j$(nproc) \
    &&  make install

RUN ln -fs ${PYTHON_INSTALL_DIR}/Python-${PYTHON_VER}/python /usr/bin/python \
    && curl -kL https://bootstrap.pypa.io/get-pip.py | python 

# Install pip packages
# RUN ln -s /usr/bin/python3 /usr/bin/python \
#     &&  pip3 install --upgrade pip setuptools wheel \
#     &&  pip3 install --no-cache-dir cmake \
#     &&  pip3 install torch==${TORCH_VER}+cu${CUDA_VER_MAJOR} torchvision==${TORCH_VISON_VER}+cu${CUDA_VER_MAJOR} --index-url https://download.pytorch.org/whl/cu${CUDA_VER_MAJOR} \
#     &&  pip3 install opencv-python numpy tqdm ninja mediapipe jittor onnxruntime-gpu

# RUN ln -s /usr/bin/python3 /usr/bin/python \
RUN pip3 install --upgrade pip setuptools wheel \
    &&  pip3 install torch==${TORCH_VER}+cu${CUDA_VER_MAJOR} torchvision==${TORCH_VISON_VER}+cu${CUDA_VER_MAJOR} --index-url https://download.pytorch.org/whl/cu${CUDA_VER_MAJOR} \
    &&  pip3 install opencv-python numpy tqdm ninja mediapipe jittor onnxruntime-gpu
    # &&  pip install --no-cache-dir cmake \
 
    # torch-2.0.1+cu117.with.pypi.cudnn-cp310-cp310-linux_x86_64.whl
    # pip install torch==${TORCH_VER}+cu${CUDA_VER_MAJOR} torchvision==0.15.1+cu{CUDA_VER_MAJOR} --index-url https://download.pytorch.org/whl/cu117 \
    # pip install torch torchvision \

# Install ONNX Runtime
# https://self-development.info/onnx-runtime%EF%BC%88gpu%E7%89%88%EF%BC%89%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB/
# RUN pip3 install onnxruntime-gpu

# Install pytorch3d
# https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md#3-install-wheels-for-linux
# https://github.com/facebookresearch/pytorch3d/tags
# torch3d:0.6.0, torch:1.9.0, cu111
# https://github.com/facebookresearch/pytorch3d/blob/2bd65027ca5c3b87b77d4f05b8eacae58d8d106f/.circleci/regenerate.py#L32
# torch3d:0.6.0, torch:1.11.0, cu113
# https://github.com/facebookresearch/pytorch3d/blob/9585a58d10cb2efcd159b058fa4af914203c1d0d/.circleci/regenerate.py#L29

# RUN echo $CUDA_HOME \
#     && export CUDA_HOME="/usr/local/cuda" \
# RUN export FORCE_CUDA="1" \


# RUN export CUDA_HOME="/usr/local/cuda" \
#     && export FORCE_CUDA="1" \

# ARG CUDA_HOME="/usr/local/cuda-11.3"
# RUN export FORCE_CUDA="1" \
#     && pip3 install "git+https://github.com/facebookresearch/pytorch3d.git@v${TORCH3D_VER}"

# RUN git clone https://github.com/facebookresearch/pytorch3d.git \
#     && cd pytorch3d \
#     && git checkout -q v${TORCH3D_VER}\
#     && pip install -e .

RUN pip install "git+https://github.com/facebookresearch/pytorch3d.git@v${TORCH3D_VER}"

# RUN pip install --no-index --no-cache-dir pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py${PYTHON_VER_MAJOR}_cu${CUDA_VER_MAJOR}_pyt${CUDA_VER_MAJOR}1/download.html
# pip3 install --no-index --no-cache-dir pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py38_cu${CUDA_VER_MAJOR}_pyt1110/download.html

# # requirements.txtの場合
# COPY requirements.txt ${WORK_DIR}
# COPY requirements.txt /
# # COPY environment.yml ${WORK_DIR}

# # https://qiita.com/Sicut_study/items/b612174caab6d0e2c9bf
# ARG CRYPTOGRAPHY_DONT_BUILD_RUST=1


# RUN ln -s /usr/bin/python3 /usr/bin/python \
#     &&  pip3 install --upgrade pip setuptools wheel \
#     &&  pip3 install --no-cache-dir cmake \
#     &&  pip3 install --no-cache-dir -r requirements.txt
    # &&  pip install cryptacular \



# # Create a working directory
# RUN mkdir ${WORK_DIR}
# WORKDIR ${WORK_DIR}

# # this is heavy if your current folder is a big data storage
# # COPY . ${WORK_DIR}

# # # Install Miniconda and Python 3.x
# # ENV CONDA_AUTO_UPDATE_CONDA=false
# # ENV PATH=/home/user/miniconda/bin:$PATH
# # RUN curl -sLo ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
# #  && chmod +x ~/miniconda.sh \
# #  && ~/miniconda.sh -b -p ~/miniconda \
# #  && rm ~/miniconda.sh \
# #  && conda install -y python==$PYTHON_VERSION numpy scipy pandas matplotlib tqdm \
# #  && conda clean -ya


# # https://qiita.com/junkor-1011/items/cd7c0e626aedc335011d
# # ローカルuser作成
# # ARG USER_NAME=user
# # ARG USER_UID=1000
# # ARG PASSWD=password
# # RUN useradd -m -s /bin/bash -u ${USER_UID} ${USER_NAME} && \
# #     gpasswd -a ${USER_NAME} sudo && \
# #     echo "${USER_NAME}:${PASSWD}" | chpasswd && \
# #     echo "${USER_NAME} ALL=(ALL) ALL" >> /etc/sudoers && \
# #     chmod g+w /etc/passwd


# # conda用準備
# ENV CONDA_DIR=/opt/conda \
#     CONDA_TMP_DIR=/tmp/conda \
#     HOME=/home/$USER_NAME \
#     SHELL=/bin/bash
# RUN mkdir -p $CONDA_DIR && \
#     mkdir -p $CONDA_TMP_DIR
#     # && \
#     # chown $USER_NAME:$USER_UID $CONDA_DIR && \
#     # chown $USER_NAME:$USER_UID $CONDA_TMP_DIR

# # yamlファイルの取り込み
# ARG CONDA_YAML="./environment.yml"
# COPY $CONDA_YAML /tmp/conda_packages.yml

# # USER ${USER_NAME}

# # WORKDIR $HOME

# # miniconda
# # https://repo.anaconda.com/miniconda/
# ARG MINICONDA_VERSION=py${PYTHON_VER_MAJOR}_23.3.1-0-Linux-x86_64
# # latest-Linux-x86_64
# # py37_4.8.3-Linux-x86_64
# # ARG MINICONDA_MD5=751786b92c00b1aeae3f017b781018df
# ENV PATH=${CONDA_DIR}/bin:$PATH

# RUN cd /tmp && \
#     wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}.sh && \
#     /bin/bash Miniconda3-${MINICONDA_VERSION}.sh -f -b -p $CONDA_TMP_DIR && \
#     rm Miniconda3-${MINICONDA_VERSION}.sh && \
#     $CONDA_TMP_DIR/bin/conda env create -f /tmp/conda_packages.yml -p $CONDA_DIR && \
#     rm -rf $HOME/.cache/* && \
#     rm -rf $CONDA_TMP_DIR/*
#     # echo "${MINICONDA_MD5} *Miniconda3-${MINICONDA_VERSION}.sh" | md5sum -c - && \
#     # 