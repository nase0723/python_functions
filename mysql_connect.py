import mysql.connector


def connect_mysql():
    global cnx
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database=''
    )
    # if cnx.is_connected:
    #     print("Connected!")

def insert_mysql():
    cursor = cnx.cursor()
    sql = ('''
    INSERT INTO wp_kamo_customer_voice 
        (author, date, customer_voice)
    VALUES 
        (%s, %s, %s)
    ''')
    data = [
        ('2', '2001-03-12', '200'),
        ('1', '2001-03-12', '20'),
        ('3', '2001-03-12', '200')
    ]
    cursor.executemany(sql, data)
    cnx.commit()
    print(f"{cursor.rowcount} records inserted.")
    cursor.close()


def insert_into_mysql(table_name, columns, data):
    cursor = cnx.cursor()
    values = ["%s"] * len(columns)
    values = "(" + ", ".join(values) + ")"
    columns = "(" + ", ".join(columns) + ")"
    sql = "INSERT INTO " + table_name + " " + columns + " VALUES " + values
    cursor.executemany(sql, data)
    cnx.commit()
    print(f"{cursor.rowcount} records inserted.")
    cursor.close()
