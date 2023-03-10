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
from config import per_page, max_pages

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
            .paginate(page=page, per_page=per_page)
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

    if request.method == 'GET':
        page = int(request.args.get("page", 1))
        content = request.args.get('search', '')
        conferences_pagination = get_conference(content, flags, page)
        page_begin = page_end = 0
        if flags[0] or flags[1] or flags[2] or flags[3]:
            if conferences_pagination.pages - page < max_pages:
                page_end = conferences_pagination.pages
            elif conferences_pagination.pages < max_pages:
                page_end = conferences_pagination.pages
            else:
                page_end = page + max_pages - 1

            if conferences_pagination.pages - page >= max_pages:
                page_begin = page
            elif conferences_pagination.pages < max_pages:
                page_begin = 1
            else:
                page_begin = conferences_pagination.pages - max_pages + 1

        print(f"page_begin:{page_begin}, page_end:{page_end}")
        print(request.form, request.args)
        print("GET", content, flags)
        return render_template('home.html', conferences_pagination=conferences_pagination, flags=flags, content=content, page_begin=page_begin, page_end=page_end)
    elif request.method == 'POST':
        content = request.form.get('search', '')
        conferences_pagination = get_conference(content, flags, 1)
        page_end = 0
        if flags[0] or flags[1] or flags[2] or flags[3]:
            if conferences_pagination.pages < max_pages:
                page_end = conferences_pagination.pages
            else:
                page_end = max_pages

        print(f"page_begin:1, page_end:{page_end}")
        print(request.form, request.args)
        print("POST", content, flags)
        return render_template('home.html', conferences_pagination=conferences_pagination, flags=flags, content=content, page_begin=1, page_end=page_end)
