# -*- coding: utf-8 -*-
# @Author     : yuyuyuj1e
# @GitHub     : https://github.com/yuyuyuj1e
# @CSDN       : https://blog.csdn.net/yuyuyuj1e
# @Time       : 2023/1/30 11:54
# @File       : conference.py
# @Software   : PyCharm
# @Description: 会议蓝图

from flask import Blueprint, request
from flask import render_template
from models import ConferenceModel
from sqlalchemy import or_, text

bp = Blueprint("conference", __name__, url_prefix="/")


def get_conference(content, flags, page):
    conferences_pagination = []
    if flags[0] or flags[1] or flags[2] or flags[3]:
        conferences_pagination = ConferenceModel.query \
            .filter(
                or_(
                    ConferenceModel.CCF == 'A' if flags[0] else text(''),
                    ConferenceModel.CCF == 'B' if flags[1] else text(''),
                    ConferenceModel.CCF == 'C' if flags[2] else text(''),
                    ConferenceModel.CCF == 'N' if flags[3] else text('')
                )
            ) \
            .filter(
                ConferenceModel.sname.like("%" + content + "%") if content is not None else text('')
            ) \
            .order_by(ConferenceModel.year.desc()) \
            .paginate(page=page, per_page=5)
    print(page)
    # conferences_pagination = ConferenceModel.query.paginate(page=1, per_page=5)
    # print(conferences_pagination.items)
    # print(conferences_pagination.page, conferences_pagination.pages)
    # print(conferences_pagination.prev_num, conferences_pagination.has_prev)
    # print(conferences_pagination.next_num, conferences_pagination.has_next)
    return conferences_pagination


@bp.route("/", methods=['GET', 'POST'])
def index():
    flags = [
        True if request.args.get('check1', 'true') == 'true' or request.args.get('check1', 'true') == 'True' else False,
        True if request.args.get('check2', 'true') == 'true' or request.args.get('check2', 'true') == 'True' else False,
        True if request.args.get('check3', 'true') == 'true' or request.args.get('check3', 'true') == 'True' else False,
        True if request.args.get('check4', 'true') == 'true' or request.args.get('check4', 'true') == 'True' else False
    ]
    page = int(request.args.get("page", 1))

    if request.method == 'GET':
        content = request.args.get('search', '')
        conferences_pagination = get_conference(content, flags, page)
        print(request.form, request.args)
        print(1, content, flags)
        return render_template('home.html', conferences_pagination=conferences_pagination, flags=flags, content=content)
    elif request.method == 'POST':
        content = request.form.get('search', '')
        conferences_pagination = get_conference(content, flags, 1)
        print(request.form, request.args)
        print(2, content, flags)
        return render_template('home.html', conferences_pagination=conferences_pagination, flags=flags, content=content)
