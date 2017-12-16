# -*- coding= utf-8 -*-

import functools

"""
functools.reduce函数用法测试，此例functools.reduce的结果为全部的机器学习类别
对于普通的数字加法，也有效 
"""

ML_POSITION_ANALOG_LIST = [
    [r'数据挖掘', r'搜索算法', r'推荐算法', r'用户画像', r'深度学习'],
    [r'图像算法', r'语音算法', r'视频算法'],
    [r'自然语言处理'],
    [r'机器学习_其它'],
]
job_position = '数据挖掘'
print(functools.reduce(lambda x, y: x + y, ML_POSITION_ANALOG_LIST))
if job_position in functools.reduce(lambda x, y: x + y, ML_POSITION_ANALOG_LIST):
    for ml_position_class in ML_POSITION_ANALOG_LIST:
        # print(ml_position_class)
        if job_position in ml_position_class:
            analog_position = ml_position_class[:]
            print(analog_position)
            analog_position.remove(job_position)
            print(analog_position)