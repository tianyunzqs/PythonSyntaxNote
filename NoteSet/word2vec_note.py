"""
.wv.syn0.npy文件和.syn1neg.npy文件不能删除，否则load出错
"""

from gensim.models import word2vec

model = word2vec.Word2Vec.load("D:/jianxun/word2vec4.model")
print(model.similar_by_word("安全", topn=20))
