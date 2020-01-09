#coding:utf-8

import pymysql

# 1.建立数据库连接 conn = pymysql.connect()
# 2.从连接建立操作游标 cur = conn.cursor()
# 3.使用游标执行sql（读/写） cur.execute(sql)
# 4.获取结果（读）/ 提交更改（写） cur.fetchall() / conn.commit()
# 5.关闭游标及连接 cur.close();conn.close()

# 1. 建立连接
conn = pymysql.connect(host='',
                       port=3306,
                       user='root',
                       passwd='123456',  # password也可以
                       db='',
                       charset='utf-8')  # 如果查询有中文需要指定数据库编码

# 2. 从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

# 3. 查询数据库（读）
cur.execute("sql语句")

# 4. 获取查询结果
result = cur.fetchall()
print(result)

# 3. 更改数据库（写）
cur.execute("")

# 4. 提交更改
conn.commit()  # 注意是用的conn不是cur

# 5. 关闭游标及连接
cur.close()
conn.close()