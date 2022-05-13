from pybo import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(30), unique=True, nullable=False)

class Foodtype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typename = db.Column(db.String(30), unique=True, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.String(15),unique=True,nullable=False)
    password = db.Column(db.String(200),nullable=False)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant = db.Column(db.String(30),nullable=False)
    address = db.Column(db.String(50),nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey(
        'tag.id', ondelete='CASCADE'), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey(
        'foodtype.id', ondelete='CASCADE'), nullable=False)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurant.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class UserLiked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurant.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)