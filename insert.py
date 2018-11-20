import pymysql
import requests
from bs4 import BeautifulSoup 
req = requests.get('http://campusmon.jobkorea.co.kr/')
html = req.content
soup = BeautifulSoup(html, 'html.parser')

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='djfudnsekf', db='withpk', charset='utf8')

find1 = soup.find("div", {"class":"ctsBest"} )
findimg = find1.find_all('img')

finddt = find1.find_all('dt')
finddd = find1.find_all('dd')
count = 0
find = 1
num = 1

try:
    for b in range(0,18):
        gongmo = finddt[b].get_text()
        host = finddd[count].get_text()
        count = count +1
        dayday = finddd[count].get_text()
        img = findimg[find].get('src')
        with db.cursor() as cursor:
            sql = '''
                INSERT INTO info (number, title, org, dday, image) VALUES(%s, %s, %s, %s, %s)
            '''
            cursor.execute(sql,(num, gongmo.rstrip('\n').rstrip('\n').rstrip('\n'), host, dayday, img))
            db.commit()
            num = num+1
            count = count +2
            find = find+2
            
finally:
    db.close()

