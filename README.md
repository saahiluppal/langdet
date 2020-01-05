# Language Detection System
This repo provides a clean implementation of Language Detection System in TensorFlow using all best practices.

## Usage
### Installation
#### Conda (Recommended)
```bash
# Tensorflow CPU
conda activate (import tensorflow as tf)

# Tensorflow GPU
conda activate (import tensorflow-gpu as tf)
```
### pip
```bash
pip install -r requirements.txt
```
### Nvidia Driver (For GPU)

```bash
# Ubuntu 18.04
sudo apt-add-repository -r ppa:graphics-drivers/ppa
sudo apt install nvidia-driver-430
# Windows/Other
https://www.nvidia.com/Download/index.aspx
```

### Downloading pre-trained weights
<a href='https://github.com/saahiluppal/langdet/blob/master/model_one.h5'>Model_one</a>&emsp;(Almost 97.04% accuracy)
#### Or hit wget on terminal (linux)
```bash
# Model_one
wget https://github.com/saahiluppal/langdet/blob/master/model_one.h5
```
## Action
```bash
# wanna detect language (we recommend using more than 5 words for better accuracy)
# file dependencies soon to be added
detect.py

# Training custom model (we recommend setting code which better suits your needs)
manual_tokens.py
# jupyter notebook for same
manual_tokens.ipynb
```
