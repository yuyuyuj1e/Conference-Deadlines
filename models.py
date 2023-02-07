# -*- coding: utf-8 -*-
# @Author     : yuyuyuj1e
# @GitHub     : https://github.com/yuyuyuj1e
# @CSDN       : https://blog.csdn.net/yuyuyuj1e
# @Time       : 2023/1/30 11:35
# @File       : models.py
# @Software   : PyCharm
# @Description: 模型文件

from exts import db


# 表
class ConferenceModel(db.Model):
    __tablename__ = "conference"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="序号")
    name = db.Column(db.String(255), comment="会议名称")
    sname = db.Column(db.String(255), comment="会议简称")
    website = db.Column(db.String(255), comment="会议网址")
    dblp = db.Column(db.String(255), comment="dblp")
    deadline_cst = db.Column(db.DateTime, comment="截止时间")
    year = db.Column(db.String(255), comment="会议年份")
    date = db.Column(db.String(255), comment="会议日期")
    location = db.Column(db.String(255), comment="会议地址")
    CCF = db.Column(db.String(255), comment="A/B/C/Non")
    publisher = db.Column(db.String(255), comment="出版社")
    NOTE = db.Column(db.String(255), comment="注意事项")

