import re

_pattern_date = re.compile(
    r'\d{4}学?年? *[-|/|.|到|至]? *(\d{4}学?年?)?|'
    r'\d{4}[年][0-1]\d{1}[月][0-3]\d{1}[日]|'
    r'\d{4}[年][0-1]\d{1}[月]|'
    r'[0-1]\d{1}[月]\d{4}[年]|'
    r'\d{4} *(-|/|.) *\d{1,2}\1\d{1,2}|'
    r'\d{4} *(-|/|.) *\d{1,2}|'
    r'\d{1,2} *(-|/|.) *\d{4}|至今|今'
)

re_date = re.finditer(_pattern_date, "    2009学年获得国家励志奖学金")
date_list = [_.group() for _ in re_date]
print(date_list)

'''
    __date是一个迭代器，迭代器只能迭代一次，如果需要多次迭代，参考下面方法
'''
date_list = []
__date = re.finditer(r'[1-2]\d{3}', "2009-2010学年获得国家励志奖学金")
__date_copy = list(__date)
for _ in __date:
    print(_.group())

print(__date)
print(next(__date).group())
date_list.append(__date.next().group() + "/09")
date_list.append(__date.next().group() + "/06")
print(date_list)
