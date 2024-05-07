# -*- coding: utf-8 -*-
# ModuleName: read_data
# Author: dongyihua543
# Time: 2024/5/7 14:53

from load_data import read_data

"""
sentences=['海钓比赛地点在厦门与金门之间的海域。', '这座依山傍水的博物馆由国内一流的设计师主持设计，整个建筑群精美而恢宏。', '但作为一个共产党员、人民公仆，应当胸怀宽阔，真正做到“先天下之忧而忧，后天下之乐而乐”，淡化个人的名利得失和宠辱悲喜，把改革大业摆在首位，这样才能超越自我，摆脱世俗，有所作为。']

tags=[['O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-LOC', 'I-LOC', 'O', 'B-LOC', 'I-LOC', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
"""

if __name__ == '__main__':
    path = '../data/example.train_mini'
    sentences, tags = read_data(path)
    print(sentences)
    print(tags)
    print('success')
