# -*- coding: utf-8 -*-

import pandas as pd
import xlrd

data = xlrd.open_workbook('D:/verify/original/train_pass_by_man.xls')
table = data.sheets()[0]

nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
print(nrows, ncols)

with pd.ExcelWriter('newxls.xlsx') as writer:
    col = ['jobId', 'jobInfo']
    cnt = 0
    for r in range(nrows):
        cnt += 1
        if cnt % 10 == 0:
            print(cnt)
            break
        jobInfo = table.cell(r, 0).value
        row = [str(cnt-1), str(jobInfo)]
        row_dict = dict(zip(col, row))
        result = pd.DataFrame([row_dict], columns=col)
        result.to_excel(writer, startrow=cnt-1, header=False, index=False)
