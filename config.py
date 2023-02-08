'''
author: yuyuyuj1e 807152541@qq.com
github: https://github.com/yuyuyuj1e
csdn: https://blog.csdn.net/yuyuyuj1e
date: 2023-02-07 16:21:12
last_edit_time: 2023-02-08 21:55:04
file_path: /Conference-Deadlines/config.py
description: 头部注释配置模板
'''
# -*- coding: utf-8 -*-
# @Author     : yuyuyuj1e
# @GitHub     : https://github.com/yuyuyuj1e
# @CSDN       : https://blog.csdn.net/yuyuyuj1e
# @Time       : 2023/1/30 11:29
# @File       : config.py
# @Software   : PyCharm
# @Description: 配置文件

# 配置数据库信息
HOSTNAME = "127.0.0.1"  # MySQL 所在主机名
PORT = 3306  # MySQL 监听端口号
USERNAME = "root"  # 账号
PASSWORD = "123456"  # 密码
DATABASE = "ddl"  # 连接的数据库

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}" \
                                        f"?charset=utf8mb4"

# 分页配置
per_page = 5  # 每页显示数据数
max_pages = 5  # 分页最多显示页数
