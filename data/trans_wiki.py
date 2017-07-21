#!/usr/bin/env python
# encoding: utf-8


"""
@author: Jackling Gu
@file: trans_wiki.py
@time: 17-7-21 12:16
"""

import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    inp, outp = 'zhwiki-latest-pages-articles.xml.bz2', 'wiki_org.zh.text'

    space = " "
    i = 0
    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    texts = wiki.get_texts()
    for text in texts:
        # print((text[0]).decode("utf-8"))
        # exit()
        output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles")