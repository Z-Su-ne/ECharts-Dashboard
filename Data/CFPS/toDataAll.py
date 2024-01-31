import pandas as pd

# 读取CSV文件
data = pd.read_csv('全国数据.csv')

# 筛选出'cfps2020edu'字段值为6（大学本科）的数据
undergrad_data = data[data['cfps2020edu'] == '大学本科']

# 按照'provcd20'和'gender'字段进行分类
grouped = undergrad_data.groupby(['provcd20'])

# 对每个分类下的'emp_income'求平均值和中位数
result = grouped['emp_income'].agg(['median'])

# 将结果保存为CSV文件
result.to_csv('undergrad_result.csv')

# 输出结果
print("大学本科数据的结果已保存为 undergrad_result.csv")