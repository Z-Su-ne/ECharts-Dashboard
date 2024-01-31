# coding=utf-8
"""
    @author：邹宇鹏 32105531
    @email: zou.yp@qq.com
    @date：2024/1/6
"""
import json

# 打开并读取TXT文件
with open('jobs2.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# 将 JSON 数据解析为 Python 对象
job_data = json.loads(data)

# 提取所需信息
job_info = []
for job in job_data:
    job_info.append({
        'jobName': job['jobName'],
        'salaryDesc': job['salaryDesc'],
        'cityName': job['cityName'],
        'areaDistrict': job['areaDistrict'],
        'jobExperience': job['jobExperience'],
        'jobDegree': job['jobDegree'],
        'brandName': job['brandName'],
        'brandIndustry': job['brandIndustry'],
        'leastMonthDesc': job['leastMonthDesc']
    })

# 输出提取的信息
for info in job_info:
    print(info)

# 创建一个用于存储信息的列表
job_info = []
for job in job_data:
    job_info.append({
        'jobName': job['jobName'],
        'salaryDesc': job['salaryDesc'],
        'cityName': job['cityName'],
        'areaDistrict': job['areaDistrict'],
        'jobExperience': job['jobExperience'],
        'jobDegree': job['jobDegree'],
        'brandName': job['brandName'],
        'brandIndustry': job['brandIndustry'],
        'leastMonthDesc': job['leastMonthDesc']
    })

# 指定要保存的文件名
output_file = 'extracted_jobs2.json'

# 将提取的信息写入 JSON 文件
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(job_info, f, ensure_ascii=False, indent=4)

print(f"提取的信息已保存至文件: '{output_file}'")