from flask import Blueprint, render_template,request,redirect,url_for,flash, g
from pybo import db
from pybo.models import User,Reservation
from pybo.forms import ReservationForm
from datetime import datetime
from pybo.views.auth_views import login_required


from pybo.models import Restaurant, Tag, Type

bp = Blueprint('restaurant',__name__,url_prefix='/restaurant')

@bp.route('/')
def _home():
    return render_template('main.html')

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

@bp.route('/create/<int:restaurant_id>/', methods=('GET', 'POST'))
@login_required
def detail(restaurant_id):
    form = ReservationForm()
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    if request.method == 'POST' and form.validate_on_submit():
        user = g.user.username
        # user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash('존재하지 않는 사용자 입니다.')
        else:
            reserve = Reservation(restaurant_id=restaurant_id,
                                  user_name=user,
                                  user_num = form.usernum.data,
                                  create_date = datetime.now(),
                                  peoplenum = form.peoplenum.data)
            db.session.add(reserve)
            db.session.commit()
            return redirect(url_for('main.index'))
    return render_template('search/create_reserve.html',restaurant=restaurant,form=form)


