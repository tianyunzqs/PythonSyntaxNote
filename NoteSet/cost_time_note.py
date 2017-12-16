# -*- coding: utf-8 -*-

import datetime

"""
程序运行时间的实例
:return: 无
"""

t1 = datetime.datetime.now()
s = [0 for i in range(100000)]
t2 = datetime.datetime.now()
print((t2-t1).microseconds)
