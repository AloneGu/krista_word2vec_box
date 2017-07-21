#!/usr/bin/env python
# encoding: utf-8


"""
@author: Jackling Gu
@file: word_cut.py
@time: 17-7-21 14:21
"""

import sys
import jieba
import arrow

def jieba_cut(text):
    tmp_res = ' '.join(jieba.cut(text,cut_all=True))
    return tmp_res.replace('  ',' ')  # change 2 space to 1 space

# python3 word_cut.py wiki.zh.text.simple
if __name__=='__main__':
    input_file = sys.argv[1]
    output_file = 'jieba_cut_' + input_file
    print('input',input_file,'out',output_file)
    i = 0
    with open(input_file) as fin:
        with open(output_file,'w') as fout:
            for line in fin.readlines():
                fout.write(jieba_cut(line.strip())+'\n')
                i += 1
                if i % 4000 == 0:
                    print(arrow.utcnow(),i)