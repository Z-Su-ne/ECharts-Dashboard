# coding=utf-8
"""
    @author：邹宇鹏 32105531
    @email: zou.yp@qq.com
    @date：2024/1/6
"""
import requests
import csv

f = open('boss.csv', mode='a', newline='', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(
    ['jobName', 'salaryDesc', 'cityName', 'areaDistrict', 'jobExperience', 'jobDegree', 'brandName', 'brandIndustry', 'leastMonthDesc'])

headers = {
    'Cookie': 'wd_guid=0f5ba78c-0ee1-4e67-932d-4ab8d1995383; historyState=state; _bl_uid=m3l0qq1pynksRCug00C254na6kL7; lastCity=101210100; wt2=D22JYDNBiPDvMUnSlEN4BVWz495wVNbvrsAagf7Ie2JX8hQj6CRQmAp-G8q25QbqtrcVGVZ8HQtjoG-S6GFmZMw~~; wbg=0; __zp_stoken__=e768fQkTDqcOFwoHDg0s2GB4VFBpIM0dEMz1LQjBLRE9CRElGUUJEUSRDMiDDicO2w5jCv2jDkHNGOURJTUZCSklETSlETcWCw4NFRzxKw4bDsMOawrhow5MTwosUw7DDgxMjw4kZwqrDhyHDlMOENTDDlcOJRUNPRS%2FDicKsw5FGw4TCrsONQMOJwq%2FDi0NHRUA7R2AWahtHR1BTZhVZbFBsa10TW1pYOUVNR0bCqcKPxIBBRB0fHh8hEhQZFBYVFxYYGhUXFhcZFRcWFxk6RMKrw4VdxY%2FFpMSMxI7EqcKkwr7CkmfCsmLDhFTEhFvEg19dasKywrjDimfCtMKwwrlXwqRXwqt9W3NbXcOPwo9UwotwcsOKd8KBU8KDeH8cHRshIWpHH17EgsOQ; geek_zp_token=V1R9kmFe350l1jVtRuzxkdKy-56TrQwSs~',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}
url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101210100&experience=108,102&payType=&partTime=&degree=203&industry=&scale=&stage=&position=&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page=1&pageSize=60'

response = requests.get(url=url, headers=headers)
# print(response)
# print(response.text)

json_data = response.json()
print(json_data)

jobList = json_data['zpData']['jobList']
print(jobList)

# for循环遍历列表
for job in jobList:
    # 工作名称
    jobName = job['jobName']
    # 工资
    salaryDesc = job['salaryDesc']
    # 工作城市
    cityName = job['cityName']
    # 工作城市-地区
    areaDistrict = job['areaDistrict']
    # 工作经验
    jobExperience = job['jobExperience']
    # 学历
    jobDegree = job['jobDegree']
    # 公司名称
    brandName = job['brandName']
    # 公司标签
    brandIndustry = job['brandIndustry']
    # 最短工作时间
    leastMonthDesc = job['leastMonthDesc']

    csv_writer.writerow([jobName, salaryDesc, cityName, areaDistrict, jobExperience, jobDegree, brandName, brandIndustry, leastMonthDesc])
