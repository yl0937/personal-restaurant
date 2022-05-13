from flask import Blueprint, render_template

from pybo.models import Restaurant

bp = Blueprint('restaurant',__name__,url_prefix='/restaurant')

@bp.route('/list/')
def _list():
    restaurant_list = Restaurant.query.order_by(Restaurant.id.desc())
    return render_template('search/restaurant_list.html',restaurant_list=restaurant_list)

@bp.route('/detail/<int:restaurant_id>/')
def detail(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    return render_template('search/restaurant_detail.html',restaurant=restaurant)