import pandas as pd
import numpy as np
import os
import re
from nltk.tokenize import sent_tokenize
import json

languages = {
    0: 'Danish', 1: 'German',
    2: 'Greek', 3: 'English',
    4: 'Spanish', 5: 'Finnish',
    6: 'French', 7: 'Italian',
    8: 'Dutch', 9: 'Portuguese',
    10: 'Swedish', 11: 'Bulgarian',
    12: 'Czech', 13: 'Estonian',
    14: 'Hungarian', 15: 'Lithuanian',
    16: 'Latvian', 17: 'Polish',
    18: 'Romanian', 19: 'Slovak',
    20: 'Slovenian'
}

def extract_language(language):
    with open(os.getcwd() + '/dataset/' + language +".txt") as outfile:
        lang = outfile.read()
    return lang

def clean(language):
    pattern = r'<(!?).*>'

    language = re.sub(pattern, '', language)

    language = ''.join([i for i in language if not i.isdigit()])
    language = ''.join([i for i in language if i not in "(){}[]\n,'"])

    language = sent_tokenize(language)
    language = [i for i in language if len(i)> 4]
    return language

def stack(sentences, langauge_id, language):
    length = len(sentences)

    target = [langauge_id] * length
    lang = [language] * length

    df = pd.DataFrame(np.c_[sentences, target, lang], columns=['Sentences','Target', 'Language'])
    return df

def shuffle(dataframe):
    return dataframe.sample(frac=1).reset_index(drop=True)

def preprocess():
    data = pd.DataFrame([])
    for code,language in languages.items():
        extracted = extract_language(language.lower())
        cleaned = clean(extracted)
        dataframe = stack(cleaned, code, language)

        data = data.append(dataframe, ignore_index=True)
    data = shuffle(data)
    data['Target'] = data['Target'].astype(int)
    return data

data = preprocess()

import tensorflow as tf

tok = tf.keras.preprocessing.text.Tokenizer(char_level=True, oov_token='UNK')
tok.fit_on_texts(list(data['Sentences']))
X_train = tok.texts_to_sequences(list(data['Sentences']))
X_train = np.array(X_train)

X_train = tf.keras.preprocessing.sequence.pad_sequences(X_train, maxlen=500,
 padding='post',
 truncating='post')

vocab = len(tok.word_index)+1

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim= vocab,
                             output_dim=200,
                             input_length=500),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1000, activation=tf.nn.relu),
    tf.keras.layers.Dense(1000, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(250, activation=tf.nn.relu),
    tf.keras.layers.Dense(21, activation=tf.nn.softmax),
])

model.compile(optimizer='adam', loss=tf.keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])

es = tf.keras.callbacks.EarlyStopping()

model.fit(X_train, data['Target'], batch_size=32, epochs=10, callbacks=[es], validation_split=0.1)

model.save('language_char_level.h5')

with open('tokenizer.json','w') as file:
    json.dump(dict(tok.word_index), file, indent=4)
