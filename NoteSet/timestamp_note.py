# -*- coding= utf-8 -*-

"""
时间戳转换成规定的日期时间格式
:param timestamp: 时间戳，如：1451577606
:return: 转换后的日期时间格式，如：2016-05-05 20:28:54
"""

import time

timestamp = 1451577606
# 转换成localtime
time_local = time.localtime(timestamp)
# 转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
print(dt)
