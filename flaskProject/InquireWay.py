# 万思昊
# 编写时间：2023/6/16 21:05
import Config

#获取第一行数字，返回结果是整型；
def inquire_one_num(sql):
    cursor = Config.conn.cursor()
    cursor.execute(sql)
    tup = cursor.fetchone()
    cache = tup[0]
    cursor.close()
    return cache
#获取操作行数，返回值是整数；
def inquire_rows_num(sql):
    cursor = Config.conn.cursor()
    rows = cursor.execute(sql)
    cursor.close()
    return rows
#获取列列数，返回值为列表；
def inquire_type_list_num(sql):
    cursor = Config.conn.cursor()
    cursor.execute(sql)
    temp = list(cursor.fetchall())
    ans = []
    for com in temp:
        ans.append(com[0])
    cursor.close()
    return ans

def over():
    Config.conn.close()