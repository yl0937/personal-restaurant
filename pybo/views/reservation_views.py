from flask import Blueprint, render_template,request,redirect,url_for,flash, g
from pybo import db
from pybo.models import User,Reservation, Liked
from pybo.forms import ReservationForm
from datetime import datetime
from pybo.views.auth_views import login_required


from pybo.models import Restaurant, Tag, Type

bp = Blueprint('reservation',__name__,url_prefix='/reservation')

@bp.route('/list/')
@login_required
def _list():
    user = g.user.userid
    page = request.args.get('page', type=int, default=1)  # 페이지
    restaurant_list = Reservation.query.filter(Reservation.user_name.ilike(user))
    restaurant_list = restaurant_list.paginate(page, per_page=10)
    return render_template('reservation/reservation_list.html', restaurant_list=restaurant_list,page=page)
