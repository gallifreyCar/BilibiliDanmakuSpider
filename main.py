# 哔哩哔哩弹幕爬虫
import requests
import re
import datetime

# 发起请求
cid = '1047927623'
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + cid
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                  'Safari/537.36 Edg/111.0.1661.44 '
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
'''
正则捕获数据
    弹幕出现时间,模式,字体大小,颜色,发送时间戳,弹幕池,用户Hash,数据库ID,page
    <d p="91.35700,1,25,16777215,1679280461,0,c61a3d4c,1276656055551609600,10">愿人类荣光永存</d>
'''
barrage_list = re.findall('<d p=".*?">(.*?)</d>', response.text)
results = re.findall('<d p="(.*?),.*?,(.*?),(.*?),(.*?),.*?">.*?</d>', response.text)
time_diff_list = [result[0] for result in results]
font_size_list = [result[1] for result in results]
color_list = [result[2] for result in results]
timestamp_list = [result[3] for result in results]

# 处理数据
time_diff_res = []
timestamp_res = []
color_res = []

for time_diff in time_diff_list:
    time_diff = str(datetime.timedelta(
        seconds=round(float(time_diff), 2))).strip("0:")
    time_diff_res.append(time_diff)
for timestamp in timestamp_list:
    timestamp = str(datetime.datetime.fromtimestamp(int(timestamp)))
    timestamp_res.append(timestamp)
for color in color_list:
    color = hex(int(color))[2:].upper()
    color_res.append(color)

# 保存到excel
import pandas as pd
import openpyxl

df = pd.DataFrame(
    {'弹幕内容': barrage_list, '弹幕发送时间': timestamp_res, '弹幕在视频中出现时间': time_diff_res, '弹幕颜色': color_res,
     '字体大小': font_size_list})
df.to_excel('output.xlsx', index=False)

# todo 转换成json乱码待处理
# df.to_json('output.json')
