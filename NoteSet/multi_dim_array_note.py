"""
多维数组的测试
:return: 无
"""

import numpy as np

# a = np.array([[[[]]]])

# 定义一个5*4*3*2的四维数组
a = np.array([[[[0.0 for i in range(2)] for j in range(3)] for m in range(4)] for n in range(5)])
a[0][0][0][0] = 12
# print(len(a))            # 5
# print(len(a[0]))         # 4
# print(len(a[0][0]))      # 3
# print(len(a[0][0][0]))   # 2
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(a[0][0])):
            for l in range(len(a[0][0][0])):
                print(a[i][j][k][l])
