import pandas as pd

# 读取CSV文件
data = pd.read_csv('全国数据.csv')

# 筛选出'cfps2020edu'字段值为6（大学本科）的数据
undergrad_data = data[data['cfps2020edu'] == '硕士'].copy()

# 将'gender'列中的值替换为'男'和'女'的对应数字
gender_mapping = {'男': 4, '女': 5}
undergrad_data['gender'] = undergrad_data['gender'].replace(gender_mapping)

# 将'provcd20'列中的省份名称替换为对应的下标数字
regions = [
    '北京市', '天津市', '河北省', '山西省', '内蒙古自治区', '辽宁省', '吉林省', '黑龙江省',
    '上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省',
    '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '重庆市', '四川省',
    '贵州省', '云南省', '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区'
]
undergrad_data['provcd20'] = undergrad_data['provcd20'].replace(regions, range(len(regions)))

# 按照'provcd20'和'gender'字段进行分类
grouped = undergrad_data.groupby(['provcd20', 'gender'])

# 对每个分类下的'emp_income'求平均值和中位数
result = grouped['emp_income'].agg(['median'])

# 将结果保存为CSV文件
result.to_csv('undergrad_result.csv')

# 输出结果
print("大学本科数据的结果已保存为 undergrad_result.csv")
