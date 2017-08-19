# coding = utf-8

'''
This is a webscraping script for testing the possibility that
TOEFL official website can be entered successfully. The script will generate the
data table in csv form and a chart for the solution.
'''
# import scraping packages
import requests
import sys
from bs4 import BeautifulSoup

# packages used for analysis
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

url = 'https://toefl.etest.net.cn/cn/ViewScores'
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'WebBrokerSessionID=TaWVlhXeDIraIN2E',
    'Host':'toefl.etest.net.cn',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
} # this is the headers of Chrome browser for pretending

# initiation of original data and generation of a new csv document
total = 0
n_groups = 0
frequ = []
csvFile = open('csvFile.csv','w',newline='')
writer = csv.writer(csvFile)

while int(time.strftime('%H',time.localtime(time.time()))) < 20:
    for i in range(30):
        html = requests.get(url, headers = headers)
        bsObj = BeautifulSoup(html.content,'html5lib')
        if(str(bsObj.title) == '<title>教育部考试中心托福网考网上报名 - 登录</title>'): # if entering is successful, there will be a tag like this.
            print(str(i+1)+'-- ok --'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            total += 1
        else:
            print(str(i+1)+'-- failed --'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        time.sleep(30) # scrape every half minute to prevent error
    print(total)
    n_groups += 1
    frequ.append(total)
    writer.writerow([time.strftime('%H：%M',time.localtime(time.time())), total])
    total = 0

csvFile.close()

# plot the frequency chart
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
rect = plt.bar(index, frequ, bar_width, alpha=opacity, color = 'b')
plt.xlabel('Group')
plt.ylabel('frequency')
plt.title('possiblity of login in toefl website')
plt.ylim(0,30)
plt.legend()

plt.tight_layout()
plt.show()
