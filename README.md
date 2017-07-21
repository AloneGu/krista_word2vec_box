# krista_word2vec_box

play with word2vec, this project used py3

## notes

看起来skip效果更好

unicode 有奇怪的问题 载入模型时使用 ignore

## 自己训练一遍，先准备好数据

1. trans wiki:

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

2. 简繁转换:

```
sudo apt-get install opencc

cd data

opencc -i wiki_org.zh.text -o wiki.zh.text.simple -c zht2zhs.ini
```

3. word cut:

```
cd data

python3 word_cut.py wiki.zh.text.simple

output:
input wiki.zh.text.simple out jieba_cut_wiki.zh.text.simple
Building prefix dict from /usr/local/lib/python3.5/dist-packages/jieba/dict.txt ...
Loading model from cache /tmp/jieba.cache
Loading model cost 2.40177583694458 seconds.
Prefix dict has been built succesfully.
2017-07-21T15:05:58.301916+08:00 20000
2017-07-21T15:10:19.473602+08:00 40000
2017-07-21T15:14:27.135009+08:00 60000
2017-07-21T15:18:27.877135+08:00 80000
2017-07-21T15:22:15.421795+08:00 100000
2017-07-21T15:25:28.591771+08:00 120000
2017-07-21T15:28:34.029554+08:00 140000
2017-07-21T15:31:54.928105+08:00 160000
2017-07-21T15:34:54.735939+08:00 180000
2017-07-21T15:37:35.695462+08:00 200000
2017-07-21T15:40:23.367567+08:00 220000
2017-07-21T15:43:13.425890+08:00 240000
2017-07-21T15:46:09.265424+08:00 260000
2017-07-21T15:48:47.738941+08:00 280000

```

此时 ls data -lh

```
total 4.6G
-rw-rw-r-- 1 jac jac 1.4G 7月  21 15:50 jieba_cut_wiki.zh.text.simple
-rw-rw-r-- 1 jac jac 1008 7月  21 12:18 trans_wiki.py
-rw-rw-r-- 1 jac jac 965M 7月  21 14:17 wiki_org.zh.text
-rw-rw-r-- 1 jac jac 965M 7月  21 14:44 wiki.zh.text.simple
-rw-rw-r-- 1 jac jac  763 7月  21 14:59 word_cut.py
-rwxrwx--- 1 jac jac 1.4G 7月  21 10:57 zhwiki-latest-pages-articles.xml.bz2
```

4. train

```
python3 train_model.py data/jieba_cut_wiki.zh.text.simple models/my_wiki_cn.model models/my_wiki_cn.vector

output:

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
