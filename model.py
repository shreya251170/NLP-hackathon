from keras import backend as K
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional, Dropout,Activation
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

#LSTM using woth random weight initialization
def create_model1(max_sequence_len, total_words):
    input_len = max_sequence_len - 1
    model = Sequential()
    # ----------Add Input Embedding Layer
    model.add(Embedding(total_words, 10, input_length=input_len))
    # ----------Add Hidden Layer 1 - LSTM Layer
    model.add(LSTM(100))
    model.add(Dropout(0.1))
    # ----------Add Output Layer
    model.add(Dense(total_words, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

#Bidirectional LSTM using word2vec architecture for word representations
def create_model2(total_unique_words, embeddings_matrix, max_seq_length):
    K.clear_session()
    model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim = total_unique_words, output_dim=100, weights=[embeddings_matrix], input_length=max_seq_length-1, trainable=False),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(256, return_sequences=True)),
    tf.keras.layers.Dropout(0.2), 
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(256)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(total_unique_words , activation='softmax')])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    return model
