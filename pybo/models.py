from pybo import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

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
        'type.id', ondelete='CASCADE'), nullable=False)
    tag = db.relationship('Tag', backref=db.backref('tag_set'))
    type = db.relationship('Type', backref=db.backref('type_set'))

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurant.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    restaurant = db.relationship('Restaurant',backref=db.backref('restaurant_set'))
    user = db.relationship('User',backref=db.backref('user_set'))

# class Liked(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     restaurant_id = db.Column(db.Integer, db.ForeignKey(
#         'restaurant.id', ondelete='CASCADE'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey(
#         'user.id', ondelete='CASCADE'), nullable=False)
#     create_date = db.Column(db.DateTime(), nullable=False)
#     restaurant = db.relationship('Restaurant',backref=db.backref('restaurant_set'))
#     user = db.relationship('User',backref=db.backref('user_set'))