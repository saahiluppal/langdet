import pandas as pd
import numpy as np
import os
import re
from nltk.tokenize import sent_tokenize

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

def total_lines():
    sum = 0
    for code, lang in languages.items():
        extracted = extract_language(lang.lower())
        cleaned = clean(extracted)
        sum += len(cleaned)
    return sum

data = preprocess()

import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

data['Target'].max()

y = tf.keras.utils.to_categorical(data['Target'], num_classes=21)
tok = tf.keras.preprocessing.text.Tokenizer()
tok.fit_on_texts(data['Sentences'])
x = tok.texts_to_sequences(data['Sentences'])

vocab = len(tok.word_index) + 1

pad = tf.keras.preprocessing.sequence.pad_sequences(x,maxlen=(100))



model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab,
                              output_dim=200,
                             input_length=120),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(21, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(pad, y, test_size=0.1, random_state=42)

model.fit(X_train,y_train,epochs=3)

#model.evaluate(X_test, y_test)

model.save('language2.h5')

