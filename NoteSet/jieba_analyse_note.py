"""
结巴分词中analyse包测试，textrank提取关键词
"""

import jieba.posseg as pseg
import jieba.analyse

sentence = "具备系统集成、需求分析、文档制作、项目管理的工作经验，有着大量的与政府及学校之间成功沟通经验，" \
           "习惯于为客户在技术范围内及客户所需之间寻找平衡点，擅长现场问题的应对，有丰富的跨部门合作经验，" \
           "学习能力及动手能力强，希望有个好的工作环境，大家能团结一致应对难题。"
a = jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'v', 'nv'))
print(a)

seg = pseg.cut("我们变而以书会友，以书结缘，把欧美、港台流行的食品类图谱、画册、工具书汇集一堂")
for w in seg:
    print(w.word, w.flag)
