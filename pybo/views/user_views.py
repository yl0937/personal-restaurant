from flask import Blueprint
bp = Blueprint('user',__name__,url_prefix='/user')

@bp.route('/')
def user_info():
    return "All user Info"

@bp.route('/list')
def hello_pybo():
    return "hello 사용자"

