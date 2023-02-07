# -*- coding: utf-8 -*-
# @Author     : yuyuyuj1e
# @GitHub     : https://github.com/yuyuyuj1e
# @CSDN       : https://blog.csdn.net/yuyuyuj1e
# @Time       : 2023/1/30 11:27
# @File       : app.py
# @Software   : PyCharm
# @Description:

from flask import Flask
import config
from exts import db
from blueprints.conference import bp as conference_bp

app = Flask(__name__)

# 配置
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(conference_bp)


if __name__ == '__main__':
    app.run()
