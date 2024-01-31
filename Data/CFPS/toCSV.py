import pandas as pd

# 读取 .dta 文件
# data = pd.read_stata('江浙沪数据.dta')
data = pd.read_stata('全国567.dta')
# 将数据保存为 utf-8 编码的 .csv 文件
data.to_csv('全国567.csv', encoding='utf-8', index=False)
