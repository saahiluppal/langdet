# Language Detection System
This repo provides clean implementation of Language Detection System in TensorFlow-2 using all best practices.
### Languages that Models can detect are:
- [x] Bulgarian
- [x] Czech
- [x] Danish
- [x] Dutch
- [x] English (Of course)
- [x] Estonian
- [x] Finnish
- [x] French
- [x] German
- [x] Greek 
- [x] Hungarian
- [x] Italian
- [x] Latvian
- [x] Lithuanian
- [x] Polish
- [x] Portuguese
- [x] Romanian
- [x] Slovak
- [x] Slovenian
- [x] Spanish
- [x] Swedish

## Usage
### Installation
#### Conda (Recommended)
```bash
# Tensorflow CPU
conda activate (import tensorflow as tf)
```
### pip
```bash
pip install -r requirements.txt
```

### Downloading pre-trained weights
<a href='https://github.com/saahiluppal/langdet/blob/master/model_one.h5'>Model_one</a>&emsp;(Almost 97.04% accuracy)
<br />
<a href='https://github.com/saahiluppal/langdet/blob/master/tokenizer_one.json'>Tokenizer</a>&emsp;(For Model One)
<br /><br />
<a href='https://github.com/saahiluppal/langdet/blob/master/model_two.h5'>Model_two</a>&emsp;(Almost 99.72% accuracy)
<br />
<a href='https://github.com/saahiluppal/langdet/blob/master/tokenizer_two.json'>Tokenizer</a>&emsp;(For Model Two)

NOTE: Models requires their respective tokenizers to work with; SO kindly download models along with their tokenizers
#### Or hit wget on terminal (linux)
```bash
# Model_one
wget https://github.com/saahiluppal/langdet/blob/master/model_one.h5
# Tokenizer_one
wget https://github.com/saahiluppal/langdet/blob/master/tokenizer_one.json

# Model_two
wget https://github.com/saahiluppal/langdet/blob/master/model_two.h5
# Tokenizer_two
wget https://github.com/saahiluppal/langdet/blob/master/tokenizer_two.json
```
Not sure which model to use, You can find information about models <a href='https://github.com/saahiluppal/langdet/blob/master/model_history'>here</a>

## Action
```bash
# wanna detect language (we recommend using more than 5 words for better accuracy)
# file dependencies soon to be added
detect.py

# Training custom model (we recommend setting code which better suits your needs)
manual_tokens.py
# jupyter notebook for same
manual_tokens.ipynb

# Wanna preprocess downloaded data for custom use
extraction.py
```
### Dataset Used
I used Dataset from European Parliament Parallel Corpus,which can be found <a href='http://www.statmt.org/europarl/'>here</a>
<br />
While full dataset is large (1.5 GB Unextracted) you might want to use smaller preprocessed dataset can be found <a href='https://github.com/saahiluppal/langdet/tree/master/dataset'>here</a> 

### LICENSE
<a href='https://github.com/saahiluppal/langdet/blob/master/LICENSE'>Apache License 2.0</a>
