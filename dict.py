import pymysql
 
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
            print(title1)
            print(org1)
            print(dday1)
            print(image1)

finally:
    db.close()