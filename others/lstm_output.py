# -*- coding: utf-8 -*-
# ModuleName: lstm_output
# Author: dongyihua543
# Time: 2024/5/9 14:10

import tensorflow as tf
from tensorflow.keras.layers import LSTM, Bidirectional

"""
测试LSTM的输出
"""

# 开启 eager 模式 (TF 1.15)
tf.enable_eager_execution()

# (32, 128, 768)
bert_output = tf.random.normal(shape=[32, 128, 768])
print(bert_output.shape)

# (32, 128, 192)
lstm_out_1 = Bidirectional(LSTM(96, return_sequences=True, dropout=0.2, recurrent_dropout=0.2))(bert_output)
print(lstm_out_1.shape)

# (32, 192)
lstm_out_2 = Bidirectional(LSTM(96, return_sequences=False, dropout=0.2, recurrent_dropout=0.2))(bert_output)
print(lstm_out_2.shape)
