from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, IntegerField, DateTimeField, DateTimeLocalField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름',validators=[
        DataRequired(), Length(min=3,max=25)])
    userbirth = StringField('생년월일', validators=[
        DataRequired(), Length(min=6, max=25)])
    userid = StringField('사용자이름',validators=[
        DataRequired(), Length(min=3,max=25)])
    password1 = PasswordField('비밀번호',validators=[
        DataRequired(), EqualTo('password2','비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인',validators=[DataRequired()])
    email = EmailField('이메일',[DataRequired(),Email()])

class UserLoginForm(FlaskForm):
    userid = StringField('사용자이름',validators=[DataRequired(),Length(min=3,max=25)])
    password = PasswordField('비밀번호',validators=[DataRequired()])

class ReservationForm(FlaskForm):
    usernum = StringField('전화번호',validators=[
        DataRequired(), Length(min=3,max=25)])
    peoplenum = IntegerField('예약인원',validators=[
        DataRequired()])
    create_date = DateTimeField('예약시간',validators=[
        DataRequired()])
