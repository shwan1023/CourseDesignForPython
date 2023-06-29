# 万思昊
# 编写时间：2023/6/15 16：48
import pymysql
#PyMySQL连接
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='1023',
                       database='computer college',
                       charset='utf8')