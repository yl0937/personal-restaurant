from flask import Blueprint, render_template,request,redirect,url_for,flash, g
from pybo import db
from pybo.models import User,Reservation, Liked
from pybo.forms import ReservationForm
from datetime import datetime
from pybo.views.auth_views import login_required
from sqlalchemy import desc, asc


from pybo.models import Restaurant, Tag, Type, Reservation

bp = Blueprint('reservation',__name__,url_prefix='/reservation')

@bp.route('/list/')
@login_required
def _list():
    user = g.user.userid
    type = request.args.get('type', type=int, default='')
    page = request.args.get('page', type=int, default=1)  # 페이지
    restaurant_list = Reservation.query.filter(Reservation.user_name.ilike(user))
    if(type==1):
        restaurant_list = Reservation.query.filter(Reservation.user_name.ilike(user)).order_by(Reservation.id.desc())
    elif(type==2):
        restaurant_list = Reservation.query.filter(Reservation.user_name.ilike(user)).order_by(Reservation.peoplenum.desc())
    elif(type==3):
        restaurant_list = Reservation.query.filter(Reservation.user_name.ilike(user)).order_by(asc(Reservation.create_date))
    restaurant_list = restaurant_list.paginate(page, per_page=10)
    return render_template('reservation/reservation_list.html', restaurant_list=restaurant_list,page=page)

@bp.route('/liked/')
@login_required
def like():
    user = g.user.username
    page = request.args.get('page', type=int, default=1)  # 페이지
    liked_list = Liked.query.filter(Liked.user_name.ilike(user))
    liked_list = liked_list.paginate(page, per_page=10)
    return render_template('reservation/liked_list.html', liked_list=liked_list,page=page)


@bp.route('/delete/<int:reservation_id>')
@login_required
def delete(reservation_id):
    reservation = Reservation.query.get(reservation_id)
    db.session.delete(reservation)
    db.session.commit()
    return redirect(url_for('reservation._list'))
