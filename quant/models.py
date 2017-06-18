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
    timestamp = db.Column(db.DateTime, default=datetime.now())
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
    created_at = db.Column(db.DateTime, default=datetime.now())

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
    created_at = db.Column(db.DateTime, default=datetime.now())
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


class Issue(db.Model):
    """issue to be resolved if any
    status: open / closed
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    reviewid = db.Column(db.Integer, db.ForeignKey("review.id"), nullable=False)
    status = db.Column(db.String(10), default="open")

    review = relationship("Review")

    def __init__(self, reviewid):
        self.reviewid = reviewid

    def __repr__(self):
        return "<Issue id='%s', created_at='%s', userid='%s', productid='%s'" % (
            self.id, self.created_at, self.review.user.name, self.review.product.name)


class Account(db.Model):
    """collection of all bank accounts"""
    # sqlite doesn't allow floating points, so store as strings
    AccountNumber = db.Column(db.String(20), primary_key=True)
    AccountCategory = db.Column(db.String(1))
    AccountOpeningDate = db.Column(db.String(4))
    AccountStatus = db.Column(db.String(10))
    AccountType = db.Column(db.String(30))
    AccountTypeCode = db.Column(db.String(5))
    ApprovedSanctionedAmount = db.Column(db.String(10))
    AvailableBalance = db.Column(db.String(10))
    Currency = db.Column(db.String(5))
    DPAvailable = db.Column(db.String(5))
    HomeBranch = db.Column(db.String(5))
    IntCategory = db.Column(db.String(5))
    InterestRate = db.Column(db.String(5))
    Link = db.Column(db.String(5))
    MaturityAmount = db.Column(db.String(10))
    MaturityDate = db.Column(db.String(8))
    PrincipleAmount = db.Column(db.String(10))
    TermPeriod = db.Column(db.String(10))
    TotalBalance = db.Column(db.String(10))

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return "<Account balance='%f' type='%s'>" % (
            self.balance, self.AccountCategory)

    @property
    def balance(self):
        return float(self.TotalBalance)

    @property
    def principle_amount(self):
        return float(self.PrincipleAmount)

    @property
    def created_at(self):
        try:
            return datetime.strptime(self.AccountOpeningDate, "%Y%m%d")
        except ValueError:
            return self.AccountOpeningDate

    @property
    def maturity_date(self):
        return datetime.strptime(self.MaturityDate, "%Y%m%d")


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
        User(name="sudhanshu", cif="012"),
        User(name="sharma", cif="232"),
        User(name="priyanshu", cif="423")
    ]
    products = [
        Product(name="produ1", category="home"),
        Product(name="produ2", category="new")
    ]
    db.session.add_all(users)
    db.session.add_all(products)
    reviews = [
        Review(userid=1, productid=2, rating="1.2", comment="haha lol"),
        Review(userid=1, productid=1, rating="2.3", comment="nice"),
        Review(userid=2, productid=1, rating="3.3", comment="nice"),
        Review(userid=3, productid=1, rating="3.3", comment="nice"),
        Review(userid=4, productid=1, rating="4.3", comment="nice")
    ]
    db.session.add_all(reviews)
    db.session.commit()
    issue = Issue(reviewid=2)
    db.session.add(issue)
    print('issue created', Issue.query.filter_by(id=1).first())
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
        Log(userid=1, productid=2, timestamp=datetime.strptime("2017-05-04", "%Y-%m-%d")),
        Log(userid=1, productid=1, timestamp=datetime.strptime("2017-05-29", "%Y-%m-%d")),
        Log(userid=2, productid=1, timestamp=datetime.strptime("2017-04-03", "%Y-%m-%d")),
        Log(userid=2, productid=2, timestamp=datetime.strptime("2017-06-13", '%Y-%m-%d'))
    ]
    db.session.add_all(logs)
    db.session.commit()
    for log in (Log.query.all()):
        print(log)
        print(log.id, log.product.name)

    print(Log.query.filter_by(productid=1).all())
    print()
    print("filtered logs")
    start_date = datetime.strptime("2017-04-01", "%Y-%m-%d")
    end_date = datetime.strptime("2017-05-01", "%Y-%m-%d")
    print(Log.query.filter(Log.timestamp > start_date, Log.timestamp < end_date).all())

    acc = Account(**{
        "AccountCategory": "L",
        "AccountNumber": "00000030001514444",
        "AccountOpeningDate": "00000000",
        "AccountStatus": "OPEN",
        "AccountType": "BR-STUDENTLN ISB STUDENTS",
        "AccountTypeCode": "6251",
        "ApprovedSanctionedAmount": "100000.00",
        "AvailableBalance": "0",
        "Currency": "INR",
        "DPAvailable": "0.00",
        "HomeBranch": "00437",
        "IntCategory": "4303",
        "InterestRate": "9.75",
        "Link": "OWN",
        "MaturityAmount": "0.00",
        "MaturityDate": "",
        "PrincipleAmount": "0.00",
        "TermPeriod": "",
        "TotalBalance": "0.00"
    })
    print(acc)
    acc = Account(**{
        "AccountCategory": "L",
        "AccountNumber": "00000030001514012",
        "AccountOpeningDate": "00000000",
        "AccountStatus": "OPEN",
        "AccountType": "BR-STUDENTLN ISB STUDENTS",
        "AccountTypeCode": "6251",
        "ApprovedSanctionedAmount": "",
        "AvailableBalance": "600000.00",
        "Currency": "INR",
        "DPAvailable": "0.05",
        "HomeBranch": "00438",
        "IntCategory": "1101",
        "InterestRate": "4.00",
        "Link": "OWN",
        "MaturityAmount": "0.01",
        "MaturityDate": "",
        "PrincipleAmount": "600000.00",
        "TermPeriod": "",
        "TotalBalance": "600000.00"
    })
    print(acc)
    acc = Account(**{
            "AccountCategory": "L",
            "AccountNumber": "00000030001514012",
            "AccountOpeningDate": "00000000",
            "AccountStatus": "OPEN",
            "AccountType": "BR-STUDENTLN ISB STUDENTS",
            "AccountTypeCode": "6251",
            "ApprovedSanctionedAmount": "",
            "AvailableBalance": "600000.00",
            "Currency": "INR",
            "DPAvailable": "0.05",
            "HomeBranch": "00438",
            "IntCategory": "1101",
            "InterestRate": "4.00",
            "Link": "OWN",
            "MaturityAmount": "0.01",
            "MaturityDate": "",
            "PrincipleAmount": "600000.00",
            "TermPeriod": "",
            "TotalBalance": "600000.00"
        })
    print(acc.balance, type(acc.balance))
    print(acc.created_at)
