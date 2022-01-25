import mysql.connector

def connect_mysql():
    global cnx
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database=''
    )



# インサート
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


# カラム名を取得
def get_table_columns(table_name):
    cursor = cnx.cursor()
    cursor.execute("DESC " + table_name)
    columns_info = cursor.fetchall()
    cursor.close()
    column_names = []
    for column in columns_info: column_names.append(column[0])
    return column_names