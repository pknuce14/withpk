import pymysql
 
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='djfudnsekf', db='withpk', charset='utf8')
try:
    with db.cursor() as cursor:
        sql = '''
            CREATE TABLE info (
                   number VARCHAR(10),
                   title VARCHAR(50),
                   org VARCHAR(50),
                   dday VARCHAR(20),
                   image VARCHAR(500),
                   PRIMARY KEY(title)
            );
        '''
        cursor.execute(sql)
        db.commit()
finally:
    db.close()