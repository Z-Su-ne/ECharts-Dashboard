# coding=utf-8
"""
    @author：邹宇鹏 32105531
    @email: zou.yp@qq.com
    @date：2024/1/11
"""
import pandas as pd

# 读取CSV文件
df = pd.read_csv('江浙沪67.csv')

# 按照[working, emp_income]筛选出硕士的数据
filtered_data = df[df['cfps2020edu'] == '硕士'][['workingyear', 'emp_income']].values.tolist()

# 打印筛选结果
print(filtered_data)
