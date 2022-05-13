from flask import Blueprint, render_template,request
from pybo import db

from pybo.models import Restaurant

bp = Blueprint('restaurant',__name__,url_prefix='/restaurant')

@bp.route('/list/')
def _list():
    kw = request.args.get('kw', type=str, default='')
    restaurant_list = Restaurant.query.order_by(Restaurant.id.desc())
    if kw:
        # search = '%'+kw+'%'
        restaurant_list = Restaurant.query.filter(Restaurant.restaurant.like(kw)).all()
    return render_template('search/restaurant_list.html', restaurant_list=restaurant_list, kw=kw)



@bp.route('/detail/<int:restaurant_id>/')
def detail(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    return render_template('search/restaurant_detail.html',restaurant=restaurant)
