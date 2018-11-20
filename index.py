from flask import Flask, render_template, request, redirect, url_for, session
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
number = 1

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
            cursor.execute(sql,(number, gongmo.rstrip('\n').rstrip('\n').rstrip('\n'), host, dayday, img))
            db.commit()
            count = count +2
            find = find+2
            number = number+1
            
finally:
    db.close()
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='djfudnsekf', db='withpk', charset='utf8')
try:
    with db.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = '''
            select * from info where number=1;
        '''
        cursor.execute(sql)
        rows=cursor.fetchall()
        for row in rows:
            title1=row['title']
            org1=row['org']
            dday1=row['dday']
            image1=row['image']
        sql = '''
            select * from info where number=2;
        '''
        cursor.execute(sql)
        rows=cursor.fetchall()
        for row in rows:
            title2=row['title']
            org2=row['org']
            dday2=row['dday']
            image2=row['image']
        sql = '''
            select * from info where number=3;
        '''
        cursor.execute(sql)
        rows=cursor.fetchall()
        for row in rows:
            title3=row['title']
            org3=row['org']
            dday3=row['dday']
            image3=row['image']

finally:
    db.close()
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/conlist", methods=['GET','POST'])
def conlist() -> 'html':
    return render_template('conlist.html', title1=title1, image1=image1, title2=title2, image2=image2, title3=title3, image3=image3)

@app.route("/coninfo1", methods=['GET','POST'])
def coninfo1() -> 'html':
    return render_template('coninfo1.html', title1=title1, org1=org1, dday1=dday1, image1=image1)

if __name__ == "__main__":
    app.run(port = 8000)