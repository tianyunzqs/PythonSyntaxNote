# -*- coding: utf-8 -*-

"""
    编码格式的实例
"""
# 如果是下面情形，则直接print就行
s = '{"native_place": "\u60e0\u5dde", "highest_degree": "\u672c\u79d1", ' \
    '"edu_major_1": "\u8ba1\u7b97\u673a\u79d1\u5b66\u4e0e\u6280\u672f"}'
print(s.encode('utf-8').decode('unicode_escape'))  # 这样乱码
print(s)  # 正常输出

# 如果是下面情形(从文件中读取)，需要使用.encode('utf-8').decode('unicode_escape')
with open(r"D:/jianxun/anquan/all_resume_converted_info", "r+", encoding="utf-8") as fin:
    line = fin.readline()
    while line:
        line = line.strip()
        print(line.encode('utf-8').decode('unicode_escape'))
        break
