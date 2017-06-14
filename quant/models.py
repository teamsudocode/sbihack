#!/usr/bin/env python3

"""Database schema"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app


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

    def __init__(self, userid, productid, rating, comment):
        rating_float = float(rating)
        if not(rating_float >= 0 and rating_float <= 5):
            raise ValueError
        self.userid = userid
        self.productid = productid
        self.rating = str(rating)
        self.comment = comment

    def __repr__(self):
        return "<Review id='%s', userid='%s', productid='%s', rating='%s', created_at='%s'>" % (
            self.id, self.userid, self.productid, self.rating, self.comment)


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
        Review(userid=1, productid=2, rating="1.2", comment="haha lol")
    ]
    db.session.add_all(reviews)
    db.session.commit()
    print(User.query.all())
    print(Product.query.all())
    print(Review.query.all())
