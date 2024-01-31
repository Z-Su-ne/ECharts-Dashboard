import csv
import json

# 定义映射关系
edu_mapping = {
    '文盲/半文盲': 1,
    '小学': 2,
    '初中': 3,
    '高中/中专/技校/职高': 4,
    '大专': 1,
    '大学本科': 2,
    '硕士': 3,
    '博士': 8
}

# 读取CSV文件
with open('全国567.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []

    # 提取列标题
    headers = ['gender', 'emp_income', 'cfps2020edu', 'workingyear']
    data.append(headers)

    for row in reader:
        # 转换性别为数字表示
        gender_value = 1 if row['gender'] == '男' else 0

        # 转换教育程度为相应数字
        edu_value = edu_mapping.get(row['cfps2020edu'], 0)  # 默认为0
        # 处理工资数据
        emp_income = min(float(row['emp_income']), 400000)  # 如果超过400000则设为400000
        workingyear = min(float(row['workingyear']), 40)

        # 提取所需的列数据
        extracted_data = [
            gender_value,
            emp_income,
            edu_value,
            float(row['workingyear'])
            # 如果有其他列也想提取，可以在这里添加相应的数据
        ]
        data.append(extracted_data)

# 将提取的数据保存为JSON文件
with open('全国数据567.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4, ensure_ascii=False)
