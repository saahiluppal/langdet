import tensorflow as tf
import pickle
import warnings

warnings.filterwarnings('ignore')

tokenizer_path = 'tokenizer_two.json'
model_path = 'model_two.h5'

with open(tokenizer_path,'rb') as handle:
    tokenizer = pickle.load(handle)

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

model = tf.keras.models.load_model(model_path)

text = input('\nEnter Language You Want to Detect: (Enter at least 5 words So the model can predict Accurately)\n:').strip()
if len(text) == 0:
    print('Can you please write Something')
    exit()
    
text = tokenizer.texts_to_sequences([text])
text = tf.keras.preprocessing.sequence.pad_sequences(text, maxlen=100)

num = model.predict_classes(text)[0]

print('I Think This is', languages.get(num))