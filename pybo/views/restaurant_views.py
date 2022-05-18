from flask import Blueprint, render_template,request
from pybo import db

from pybo.models import Restaurant, Tag, Type

bp = Blueprint('restaurant',__name__,url_prefix='/restaurant')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    kw = request.args.get('kw', type=str, default='')
    restaurant_list = Restaurant.query.order_by(Restaurant.id.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        search_list1 = Restaurant.query.filter(Restaurant.restaurant.ilike(search)).distinct()
        search_list2 = Restaurant.query.join(Tag).filter(Tag.name.ilike(search)).distinct()
        search_list3 = Restaurant.query.join(Type).filter(Type.name.ilike(search)).distinct()
        search_list4 = Restaurant.query.filter(Restaurant.address.ilike(search)).distinct()
        restaurant_list = search_list1.union_all(search_list2).union_all(search_list3).union_all(search_list4).order_by(Restaurant.id.desc())
    restaurant_list = restaurant_list.paginate(page, per_page=10)
    return render_template('search/restaurant_list.html', restaurant_list=restaurant_list,page=page,kw=kw)



@bp.route('/detail/<int:restaurant_id>/')
def detail(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    return render_template('search/restaurant_detail.html',restaurant=restaurant)
