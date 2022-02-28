from pymysql import *

# 자기소개서 db에서 가져오기
def db_showme_sangmin(db):
    with db.cursor() as cursor:
        query = '''
        SELECT *
        FROM SHOWME;
        '''
        cursor.execute(query)
        result = cursor.fetchall()
    
    return result

# 수상내역 db에서 가져오기
def db_showme_price(db):
    with db.cursor() as cursor:
        query = '''
        SELECT *
        FROM price;
        '''
        cursor.execute(query)
        result = cursor.fetchall()

    return result

# 활동내역 db에서 가져오기
def db_showme_activity(db):
    with db.cursor() as cursor:
        query = '''
        SELECT *
        FROM ACTIVITY;
        '''
        cursor.execute(query)
        result = cursor.fetchall()

    return result