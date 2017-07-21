# krista_word2vec_box

play with word2vec, this project used py3

## notes

看起来skip效果更好

unicode 有奇怪的问题 载入模型时使用 ignore

trans wiki:

```
cd data

python3 trans_wiki.py

output:
Using Theano backend.
2017-07-21 12:18:27,057: INFO: running trans_wiki.py
2017-07-21 12:21:03,429: INFO: Saved 10000 articles
2017-07-21 12:22:51,299: INFO: Saved 20000 articles
2017-07-21 12:24:41,928: INFO: Saved 30000 articles
2017-07-21 12:26:31,976: INFO: Saved 40000 articles
2017-07-21 12:28:40,667: INFO: Saved 50000 articles
2017-07-21 12:30:54,409: INFO: Saved 60000 articles
2017-07-21 12:32:37,709: INFO: Saved 70000 articles
2017-07-21 12:34:17,293: INFO: Saved 80000 articles
2017-07-21 12:35:56,816: INFO: Saved 90000 articles
2017-07-21 12:37:50,342: INFO: Saved 100000 articles
2017-07-21 12:42:39,179: INFO: Saved 110000 articles
2017-07-21 12:48:37,350: INFO: Saved 120000 articles
2017-07-21 12:52:49,601: INFO: Saved 130000 articles
2017-07-21 13:03:31,402: INFO: Saved 140000 articles
2017-07-21 13:08:32,960: INFO: Saved 150000 articles
2017-07-21 13:12:17,513: INFO: Saved 160000 articles
2017-07-21 13:18:15,291: INFO: Saved 170000 articles
2017-07-21 13:21:58,414: INFO: Saved 180000 articles
2017-07-21 13:38:42,441: INFO: Saved 190000 articles
2017-07-21 13:48:42,717: INFO: Saved 200000 articles
2017-07-21 13:54:46,107: INFO: Saved 210000 articles
2017-07-21 13:57:20,749: INFO: Saved 220000 articles
2017-07-21 14:00:43,035: INFO: Saved 230000 articles
2017-07-21 14:03:40,037: INFO: Saved 240000 articles
2017-07-21 14:06:06,000: INFO: Saved 250000 articles
2017-07-21 14:08:55,023: INFO: Saved 260000 articles
2017-07-21 14:11:48,002: INFO: Saved 270000 articles
2017-07-21 14:14:09,074: INFO: Saved 280000 articles
2017-07-21 14:16:50,286: INFO: Saved 290000 articles
2017-07-21 14:17:24,643: INFO: finished iterating over Wikipedia corpus of 292312 documents with 65734120 positions (total 2974751 articles, 78415596 positions before pruning articles shorter than 50 words)
2017-07-21 14:17:24,690: INFO: Finished Saved 292312 articles

```

简繁转换:

```
sudo apt-get install opencc

cd data

opencc -i wiki_org.zh.text -o wiki.zh.text.simple -c zht2zhs.ini
```


word cut:

```
cd data

python3 word_cut.py wiki.zh.text.simple
```

## download

把模型下载到 models 底下并且解压缩

下载地址 ： 

cbow http://pan.baidu.com/s/1eSd6zqa

skipgram http://pan.baidu.com/s/1hs02SD2

## data

维基百科训练数据 ： http://pan.baidu.com/s/1dEDQbZF

## next

自己训练一遍 skip word2vec

## links

感谢以下两个repo的作者

模型参考 : https://github.com/to-shimo/chinese-word2vec  百度云上的模型是从这里拷贝的

训练参考 : https://github.com/candlewill/Chinsese_word_vectors
