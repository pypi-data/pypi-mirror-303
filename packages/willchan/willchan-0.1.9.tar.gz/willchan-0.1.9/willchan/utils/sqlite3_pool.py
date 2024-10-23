import sqlite3
import time


# 创建连接池
def create_connection_pool(database, pool_size):
    # 创建一个连接池列表
    connection_pool = []
    for _ in range(pool_size):
        # 创建连接并加入连接池
        connection = sqlite3.connect(database)
        connection_pool.append(connection)
    return connection_pool


# 从连接池中获取连接
def get_connection(connection_pool):
    while True:
        if len(connection_pool) > 0:
            # 弹出连接池中的一个连接
            connection = connection_pool.pop()
            return connection
        else:
            # 连接池为空，等待并重新尝试获取连接
            time.sleep(1)


# 执行SQL语句
def execute_sql(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    # 关闭游标
    cursor.close()
    connection.commit()
    return results


# 执行SQL语句
def execute_sql(connection, sql, params=()):
    cursor = connection.cursor()
    cursor.execute(sql, params)
    results = cursor.fetchall()
    # 关闭游标
    cursor.close()
    connection.commit()
    return results


# 释放连接
def release_connection(connection_pool, connection):
    connection_pool.append(connection)


# 示例代码
if __name__ == "__main__":
    # 创建连接池
    connection_pool = create_connection_pool("database.db", 5)

    # 从连接池获取连接
    connection = get_connection(connection_pool)

    # 执行SQL语句
    results = execute_sql(connection, "SELECT * FROM users")

    # 输出查询结果
    for row in results:
        print(row)

    # 释放连接
    release_connection(connection_pool, connection)
