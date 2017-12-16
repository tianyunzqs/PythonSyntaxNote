"""
    有序字典测试及字典排序测试
"""
from collections import OrderedDict

d = OrderedDict()
d["c"] = 90
d["c++"] = 70
d["matlab"] = 86
d["java"] = 85
d["python"] = 76

print("字典原序输出1：")
for key in d:
    print(key + "\t" + str(d[key]))

print("字典原序输出2：")
for key, value in d.items():
    print(key + "\t" + str(value))

# 字典排序
d_sorted = sorted(d.items(), key=lambda s: s[1], reverse=True)
# 排序后输出list，进行遍历
print("字典排序后输出：")
for k in d_sorted:  # list的遍历
    for index in range(len(k)):  # tuple的遍历
        print(str(k[index]) + "\t")
    print()
