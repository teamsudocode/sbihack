#!/usr/bin/env python3

"""Database schema"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import sqlalchemy
from datetime import datetime

ForeignKey = sqlalchemy.ForeignKey
relationship = sqlalchemy.orm.relationship

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


class Log(db.Model):
    """tracking all users"""
    __tablename__ = "log"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    userid = db.Column(db.Integer, ForeignKey('user.id'))
    productid = db.Column(db.Integer, ForeignKey('product.id'))

    user = relationship("User")
    product = relationship("Product")

    def __repr__(self):
        return "<Log id='%s' timestamp='%s', userid='%s', productid='%s', user='%s', product='%s'>" % (
            self.id, self.timestamp, self.userid, self.productid, self.user, self.product)


class User(db.Model):
    """collection of all users"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    cif = db.Column(db.String(20), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, name, cif):
        self.name = name
        self.cif = cif

    def __repr__(self):
        return "<User id='%s', name='%s', cif='%s', created_at='%s'>" % (
            self.id, self.name, self.cif, self.created_at)


class Product(db.Model):
    """collection of all users"""
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(20), nullable=False)

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return "<Product id='%s', name='%s', category='%s'>" % (
            self.id, self.name, self.category)


class Review(db.Model):
    """collection of all users"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    productid = db.Column(db.Integer, db.ForeignKey('product.id'))
    rating = db.Column(db.String(2), nullable=False)
    comment = db.Column(db.String(500))

    user = relationship("User")
    product = relationship("Product")

    __table_args__ = (
        sqlalchemy.UniqueConstraint("userid", "productid", name="unique_review"),
    )

    def __init__(self, userid, productid, rating, comment):
        rating_float = float(rating)
        if not(rating_float >= 0 and rating_float <= 5):
            raise ValueError
        self.userid = userid
        self.productid = productid
        self.rating = str(rating)
        self.comment = comment

    def __repr__(self):
        return "<Review id='%s', userid='%s', productid='%s', rating='%s', created_at='%s', user='%s', product='%s'>" % (
            self.id, self.userid, self.productid, self.rating, self.comment, self.user, self.product)


if __name__ == "__main__":
    """For testing purposes
    Use the same code for the main app
    """
    print("starting")
    app = create_app()
    app.app_context().push()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    print(db)
    db.create_all(app=app)
    users = [
        User(name="himanshu", cif="123"),
        User(name="sudhanshu", cif="012")
    ]
    products = [
        Product(name="produ1", category="home"),
        Product(name="produ2", category="new")
    ]
    db.session.add_all(users)
    db.session.add_all(products)
    reviews = [
        Review(userid=1, productid=2, rating="1.2", comment="haha lol"),
        Review(userid=1, productid=1, rating="2.3", comment="nice")
    ]
    db.session.add_all(reviews)
    db.session.commit()
    # re = Review(userid=1, productid=2, rating="0.6", comment="haha not good")
    # if above review exists
    # otherwise you'd get sqlalchemy.exc.IntegrityError, so try---catch
    target = Review.query.filter_by(productid=2, userid=1).first()
    if target:
        print("review already exists")
        target.rating = "0.6"
        target.comment = "not good"
        # that's all to be done to update information
        # you can also perform db.session.commit() for safety
    else:
        db.session.add(Review(userid=1, productid=2, rating="0.6", comment="not good"))
    print(User.query.all())
    print(Product.query.all())
    print(Review.query.all())
    print(Review.query.filter_by(productid=1).first())
    print(Review.query.filter_by(productid=2).first())

    logs = [
        Log(userid=1, productid=2),
        Log(userid=1, productid=1),
        Log(userid=2, productid=1),
        Log(userid=2, productid=2)
    ]
    db.session.add_all(logs)
    db.session.commit()
    for log in (Log.query.all()):
        print(log)