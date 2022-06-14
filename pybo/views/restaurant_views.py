from flask import Blueprint, render_template,request,redirect,url_for,flash, g,session
from pybo import db
from pybo.models import User,Reservation, Liked, Poped
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
    user_id = session.get('user_id')
    if user_id is None:
        like_list=0
    else:
        user = User.query.get(user_id)
        liked_list = Liked.query.filter(Liked.user_name==user.username)
        like_list = []
        for like in liked_list:
            like_list.append(like.restaurant_name)
    return render_template('search/restaurant_list.html', restaurant_list=restaurant_list,page=page,kw=kw,like_list=like_list)

@bp.route('/popup/<int:restaurant_id>/')
def _popup(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    poped = Reservation(restaurant_id=restaurant_id)

    return render_template('search/popup.html',restaurant=restaurant,poped=poped)

@bp.route('/create/<int:restaurant_id>/', methods=('GET', 'POST'))
@login_required
def detail(restaurant_id):
    form = ReservationForm()
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    if request.method == 'POST' and form.validate_on_submit():
        create_date = request.form['search_end_input']
        date = create_date[0:10]
        time = create_date[11:16]
        create_date = (date + " " + time)
        create_date = str(create_date)
        create_date = datetime.strptime(create_date, '%Y-%m-%d %H:%M')
        user = g.user.userid
        if not user:
            flash('존재하지 않는 사용자 입니다.')
        else:
            reserve = Reservation(restaurant_id=restaurant_id,
                                  user_name=user,
                                  user_num = form.usernum.data,
                                  create_date = create_date,
                                  peoplenum = form.peoplenum.data)
            db.session.add(reserve)
            db.session.commit()
            return redirect(url_for('main.index'))
    return render_template('search/create_reserve.html',restaurant=restaurant,form=form)

@bp.route('/liked/<int:restaurant_id>/', methods=('GET', 'POST'))
@login_required
def like(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    user = g.user.username
    if not user:
        flash('존재하지 않는 사용자 입니다.')
    else:
        liked = Liked(restaurant_name=restaurant.restaurant,
                      address = restaurant.address,
                      tag_name = restaurant.tag.name,
                      type_name = restaurant.type.name,
                      user_name=user,
                      create_date = datetime.now())
        db.session.add(liked)
        db.session.commit()
    return redirect(url_for('restaurant._list',restaurant=restaurant))

@bp.route('/deleteLiked/<int:restaurant_id>/', methods=('GET', 'POST'))
@login_required
def delete_like(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    user = g.user.username
    if not user:
        flash('존재하지 않는 사용자 입니다.')
    else:
        liked = Liked.query.filter(Liked.restaurant_name==restaurant.restaurant,Liked.user_name==user)
        db.session.delete(liked[0])
        db.session.commit()
    return redirect(url_for('restaurant._list',restaurant=restaurant))

