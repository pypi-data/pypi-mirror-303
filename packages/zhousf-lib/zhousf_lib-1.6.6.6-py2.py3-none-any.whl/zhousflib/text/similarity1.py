# -*- coding: utf-8 -*-
# @Author  : zhousf
# @Function: 相似度计算
# pip install datasketch
import jieba
import numpy as np
from typing import List
from functools import lru_cache
from zhousflib.util import re_util
from zhousflib.metrics.cosine import Cosine
from zhousflib.ml.feature_vector import FeatureVector, TypeFeatureVector

"""
字符串匹配算法：这是最基本的文本相似度计算方法，主要通过将两个文本字符串进行逐个字符的比较，计算相同字符的数量占总字符数的比例来判断文本的相似度。但是，这种方法对于大量文本的比对速度较慢，且只能检测出完全相同的文本
哈希算法：哈希算法可以快速计算出文本的哈希值，然后通过比对哈希值来判断文本的相似度。但是，哈希算法存在哈希冲突的问题，即不同的文本可能会产生相同的哈希值，从而导致误判
N-gram算法：N-gram算法是一种基于文本分词的方法，将文本分成N个连续的词组，然后比对词组的相似度来判断文本的相似度。N-gram算法可以识别出部分相似的文本，相对于字符串匹配算法和哈希算法，其检测精度更高。
向量空间模型算法：向量空间模型算法是一种基于文本向量化的方法，将文本转换成向量，然后计算向量之间的相似度来判断文本的相似度。这种方法可以识别出语义相似的文本，相对于其他算法，其检测精度更高。

MinHash算法：MinHash算法是一种基于哈希的文本查重方法，它通过随机排列文档中的词项并使用哈希函数来比较文档的相似性。
SimHash算法：

运行速度：KSentence > Simhash > Minhash
准确率：KSentence > Minhash > Simhash
召回率：Simhash > Minhash > KSentence
工程应用上，海量文本用Simhash，短文本用Minhash，追求速度用KSentence。
"""

"""
余弦相似度：from sklearn.metrics.pairwise import cosine_similarity   
欧氏距离：  from sklearn.metrics.pairwise import euclidean_distances
曼哈顿距离：from sklearn.metrics.pairwise import manhattan_distances
"""


class Similarity:

    def __init__(self, vector_type=TypeFeatureVector.TYPE_COUNT_VECTOR):
        self.cosine = Cosine()
        self.feature_vector = FeatureVector(vector_type=vector_type)
        jieba.lcut("This is test script")

    @staticmethod
    @lru_cache(maxsize=int(1e6))
    def jieba_lcut_with_cache(txt, cut_all=True):
        return str(jieba.lcut(txt, cut_all=cut_all))

    def text_to_vector(self, text: List[str]):
        return self.feature_vector.fit_transform(text)

    def compute_similarity(self, text: List[str], filter_punctuation=True, cut_all=True):
        _text = []
        for txt in text:
            if filter_punctuation:
                txt = re_util.get_digit_letter_chinese(str(txt))
            # _text.append(self.jieba_lcut_with_cache(txt, cut_all=cut_all))
            _text.append(str(jieba.lcut(txt, cut_all=cut_all)))

        vector = self.text_to_vector(_text,)
        similarity_matrix = self.cosine.cosine_vector_with_matrix(vector)
        return similarity_matrix

    def compute_similarity_filter(self, text: List[str], filter_threshold: float = 0, filter_punctuation=True, cut_all=True):
        similarity_matrix = self.compute_similarity(text, filter_punctuation, cut_all)
        filter_indexes = np.where(similarity_matrix >= filter_threshold)
        tmp = []
        results_ = []
        for k in range(len(filter_indexes[0])):
            file_name1 = text[int(filter_indexes[0][k])]
            file_name2 = text[int(filter_indexes[1][k])]
            # same file
            if filter_indexes[0][k] == filter_indexes[1][k]:
                continue
            # same file of different order
            sim_score = similarity_matrix[filter_indexes[0][k]][filter_indexes[1][k]]
            if (filter_indexes[0][k], filter_indexes[1][k]) not in tmp and (filter_indexes[1][k], filter_indexes[0][k]) not in tmp:
                tmp.append((filter_indexes[0][k], filter_indexes[1][k]))
                results_.append(dict(index=[filter_indexes[0][k], filter_indexes[1][k]], text=[file_name1, file_name2],
                                     score=sim_score))
        tmp.clear()
        return results_


if __name__ == "__main__":
    import time
    similarity = Similarity(vector_type=TypeFeatureVector.TYPE_COUNT_VECTOR)
    documents = [
        "This is the first document",
        "This document is the second document",
        "This is the third document",
    ]
    count = 1
    start = time.time()
    for i in range(count):
        results = similarity.compute_similarity(text=documents, filter_punctuation=True, cut_all=False)
        print(results)
        # for item in results:
        #     print(item)
    print("耗时", (time.time() - start)/count)
    start = time.time()
    for i in range(count):
        results = similarity.compute_similarity(text=documents, filter_punctuation=True, cut_all=False)
        print(results)
    print("耗时", (time.time() - start)/count)

