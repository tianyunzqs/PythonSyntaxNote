# -*- coding: utf-8 -*-

import re

"""
    字符串分割测试，split函数后面的数字表示分割次数
    :return: 无
    """
s = "个人标签：    php,java：    python"
parts = re.split(r'：|:', s, 1)  # 1表示只分割1次
for p in parts:
    print(p)

for p in s.split("：", 1):
    print(p)
