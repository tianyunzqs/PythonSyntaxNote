"""
测试字符串前面 u 和 r 的区别
"""

import re

print("this is a test string.\nthis is other test string.")
# 前面加 u 表示unicode字符
print(u"this is a test string.\nthis is other test string.")
# 前面加 r 表示不做转义处理（通常用于正则表达式）
print(r"this is a test string.\nthis is other test string.")

if re.search(r"\d+", "1234"):
    print("number string.")