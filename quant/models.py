#!/usr/bin/env python3

"""Database schema"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import sqlalchemy
from datetime import datetime
from enum import Enum

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


class ProductEnum(Enum):
    homeloan = 1
    eduloan = 2
    deposit_1 = 3


class Product(db.Model):
    """collection of all users"""
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.Integer, nullable=False)

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return "<Product id='%s', name='%s', category='%s'>" % (
            self.id, self.name, self.category)

    @property
    def product_details(self):
        if self.category == ProductEnum.homeloan.value:
            return "query from homeloan table"
        elif self.category == ProductEnum.eduloan.value:
            return "query from eduloan table"
        elif self.category == ProductEnum.deposit_1.value:
            return "query from deposits available"


class Review(db.Model):
    """collection of all users"""
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    productid = db.Column(db.Integer, db.ForeignKey('product.id'))
    rating = db.Column(db.String(2), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(500))

    user = relationship("User")
    product = relationship("Product")

    __table_args__ = (
        sqlalchemy.UniqueConstraint("userid", "productid", name="unique_review"),
    )

    def __init__(self, userid, productid, rating, title, comment):
        rating_float = float(rating)
        if not(rating_float >= 0 and rating_float <= 5):
            raise ValueError
        self.userid = userid
        self.productid = productid
        self.title = title
        self.rating = str(rating)
        self.comment = comment

    def __repr__(self):
        return "<Review id='%s', userid='%s', productid='%s', rating='%s', created_at='%s', user='%s', product='%s'>" % (
            self.id, self.userid, self.productid, self.rating, self.comment, self.user, self.product)


# class Feedback(db.Model):
#     """ This also serves as review, but it is for the right dashboard, recommendations"""


class Issue(db.Model):
    """issue to be resolved if any
    status: open / closed
    """
    __tablename__ = "issue"
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
    __tablename__ = "account"
    # sqlite doesn't allow floating points, so store as strings
    account_number = db.Column(db.String(20), primary_key=True)
    owner_cif = db.Column(db.String(20), db.ForeignKey("user.cif"))
    balance = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, account_number, owner_cif, balance):
        self.account_number = account_number
        self.owner_cif = owner_cif
        self.balance = balance

    def __repr__(self):
        return "<Account #='%s' balance='%f' type='%s'>" % (
            self.account_number, self.balance, self.AccountCategory)

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


class Homeloan(db.Model):
    __tablename__ = "homeloan"

    Id = db.Column(db.Integer, primary_key = True)
    LoanType = db.Column(db.String(80))
    LoanName = db.Column(db.String(100))
    InterestRate = db.Column(db.Float)
    TenureLowerLimit = db.Column(db.Integer)
    TenureUpperLimit = db.Column(db.Integer)
    PrincipalLowerLimit = db.Column(db.Integer)
    PrincipalUpperLimit = db.Column(db.Integer)
    PrePaymentPenalty = db.Column(db.Integer)
    FlexiPay = db.Column(db.Integer)
    ageLowerLimit = db.Column(db.Integer)
    ageUpperLimit = db.Column(db.Integer)
    CustomerType = db.Column(db.String(100))
    Comments = db.Column(db.String(100))


    def calc_emi(self,N,P) :
        r = self.InterestRate
        tot_emi = (r*((1 + r)**N)*P)/(((1 + r)**N) - 1)
        return tot_emi
    
    def __init__(self, Id, LoanType, LoanName, InterestRate, TenureLowerLimit, TenureUpperLimit, PrincipalLowerLimit, PrincipalUpperLimit, PrePaymentPenalty, FlexiPay, ageLowerLimit, ageUpperLimit, CustomerType, Comments):
        self.Id = Id
        self.LoanType = LoanType
        self.LoanName = LoanName
        self.InterestRate = InterestRate
        self.TenureLowerLimit = TenureLowerLimit
        self.TenureUpperLimit = TenureUpperLimit
        self.PrincipalLowerLimit = PrincipalLowerLimit
        self.PrincipalUpperLimit = PrincipalUpperLimit
        self.PrePaymentPenalty = PrePaymentPenalty
        self.FlexiPay = FlexiPay
        self.ageLowerLimit = ageLowerLimit
        self.ageUpperLimit = ageUpperLimit
        self.CustomerType = CustomerType
        self.Comments = Comments

    def __repr__(self):
        return '<Homeloan %r' % self.Id


class EduLoan(db.Model):
    __tablename__ = "eduloan"

    Id = db.Column(db.Integer, primary_key=True)
    LoanType = db.Column(db.String(80))
    Tenure = db.Column(db.Float)
    EffInterestRate = db.Column(db.Float)
    ResetPeriod = db.Column(db.Float)
    Nationality = db.Column(db.String(100))
    CourseType = db.Column(db.String(100))
    InstituteType = db.Column(db.String(100))
    InstituteCountry = db.Column(db.String(100))
    LoanLimit = db.Column(db.Integer)
    Security = db.Column(db.String(100))
    Gender = db.Column(db.String(10))
    Concession = db.Column(db.Float)
    Comments = db.Column(db.String(100))

    def calc_emi(self,N,P) :
        r = self.EffInterestRate - self.Concession
        tot_emi = (r*((1 + r)**N)*P)/(((1 + r)**N) - 1)
        return tot_emi

    def __init__(self, Id, LoanType, Tenure, EffInterestRate, ResetPeriod, Nationality, CourseType,
                 InstituteType, InstituteCountry, LoanLimit, Security, Gender, Concession, Comments):
        self.Id = Id
        self.LoanType = LoanType
        self.Tenure = Tenure
        self.EffInterestRate = EffInterestRate
        self.ResetPeriod = ResetPeriod
        self.Nationality = Nationality
        self.CourseType = CourseType
        self.InstituteType = InstituteType
        self.InstituteCountry = InstituteCountry
        self.LoanLimit = LoanLimit
        self.Security = Security
        self.Gender = Gender
        self.Concession = Concession
        self.Comments = Comments

    def __repr__(self):
        return '<Eduloan %r>' % self.Id


class Transaction(db.Model):
    """ All transactions, required for mini-statement """
    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    amount = db.Column(db.Integer, nullable=False)
    accountNumber = db.Column(db.Integer, db.ForeignKey("account.account_number"))


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
    db.session.add(Issue(reviewid=3))
    db.session.add(Issue(reviewid=4))
    db.session.add(Issue(reviewid=5))
    print('issue created', Issue.query.all())
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
