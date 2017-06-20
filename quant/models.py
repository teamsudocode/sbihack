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
    def product_category(self):
        if self.category == ProductEnum.homeloan.value:
            return "Home Loan"
        elif self.category == ProductEnum.eduloan.value:
            return "Education Loan"
        elif self.category == ProductEnum.deposit_1.value:
            return "Deposit Scheme"

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
    rating = db.Column(db.Integer, nullable=False)
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
    
    # def __init__(self, Id, LoanType, LoanName, InterestRate, TenureLowerLimit, TenureUpperLimit, PrincipalLowerLimit, PrincipalUpperLimit, PrePaymentPenalty, FlexiPay, ageLowerLimit, ageUpperLimit, CustomerType, Comments):
    #     self.Id = Id
    #     self.LoanType = LoanType
    #     self.LoanName = LoanName
    #     self.InterestRate = InterestRate
    #     self.TenureLowerLimit = TenureLowerLimit
    #     self.TenureUpperLimit = TenureUpperLimit
    #     self.PrincipalLowerLimit = PrincipalLowerLimit
    #     self.PrincipalUpperLimit = PrincipalUpperLimit
    #     self.PrePaymentPenalty = PrePaymentPenalty
    #     self.FlexiPay = FlexiPay
    #     self.ageLowerLimit = ageLowerLimit
    #     self.ageUpperLimit = ageUpperLimit
    #     self.CustomerType = CustomerType
    #     self.Comments = Comments

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

    # def __init__(self, Id, LoanType, Tenure, EffInterestRate, ResetPeriod, Nationality, CourseType,
    #              InstituteType, InstituteCountry, LoanLimit, Security, Gender, Concession, Comments):
    #     self.Id = Id
    #     self.LoanType = LoanType
    #     self.Tenure = Tenure
    #     self.EffInterestRate = EffInterestRate
    #     self.ResetPeriod = ResetPeriod
    #     self.Nationality = Nationality
    #     self.CourseType = CourseType
    #     self.InstituteType = InstituteType
    #     self.InstituteCountry = InstituteCountry
    #     self.LoanLimit = LoanLimit
    #     self.Security = Security
    #     self.Gender = Gender
    #     self.Concession = Concession
    #     self.Comments = Comments

    def __repr__(self):
        return '<Eduloan %r>' % self.Id

class Insurance(db.Model):
    __tablename__ = "insurance"

    Id = db.Column(db.Integer, primary_key=True)
    InsuranceType = db.Column(db.String(80))
    InsuranceAmount = db.Column(db.Integer)
    MinPolicyTerm = db.Column(db.Float)
    MaxPolicyTerm = db.Column(db.Float)
    PayingTerm = db.Column(db.Float)
    MinAgeEntry = db.Column(db.Integer)
    MaxAgeEntry = db.Column(db.Integer)
    MinAgeMaturity = db.Column(db.Integer)
    MaxAgeMaturity = db.Column(db.Integer)
    PremiumFreq = db.Column(db.String(20))
    MinPremiumAmount = db.Column(db.Integer)
    MaxPremiumAmount = db.Column(db.String(20))
    Category = db.Column(db.String(80))
    MaturityRate = db.Column(db.Integer)

    def profit(self, t):
        r = self.MaturityRate
        final_amount = (r*(self.InsuranceAmount)*(t))/100
        if self.PremiumFreq == 'Yearly' :
            initial_amount = t*self.MinPremiumAmount
        elif self.PremiumFreq == 'Half-Yearly' :
            initial_amount = 2*t*self.MinPremiumAmount
        elif self.PremiumFreq == 'Quaterly' :
            initial_amount = 4*t*self.MinPremiumAmount
        elif self.PremiumFreq == 'Monthly' :
            initial_amount = 12*t*self.MinPremiumAmount
        return (final_amount - initial_amount)

    def __init__(self, Id, InsuranceType, InsuranceAmount, MinPolicyTerm, MaxPolicyTerm,PayingTerm, MinAgeEntry, MaxAgeEntry, MinAgeMaturity,
                    MaxAgeMaturity, PremiumFreq, MinPremiumAmount, MaxPremiumAmount, Category, MaturityRate):
        self.Id = Id
        self.InsuranceType = InsuranceType
        self.InsuranceAmount = InsuranceAmount
        self.MinPolicyTerm = MinPolicyTerm
        self.MaxPolicyTerm = MaxPolicyTerm
        self.PayingTerm = PayingTerm
        self.MinAgeEntry = MinAgeEntry
        self.MaxAgeEntry = MaxAgeEntry
        self.MinAgeMaturity = MinAgeMaturity
        self.MaxAgeMaturity = MaxAgeMaturity
        self.PremiumFreq = PremiumFreq
        self.MinPremiumAmount = MinPremiumAmount
        self.MaxPremiumAmount = MaxPremiumAmount
        self.Category = Category
        self.MaturityRate = MaturityRate

    def __repr__(self):
        return '<Insurance %r>' % self.Id


class Transaction(db.Model):
    """ All transactions, required for mini-statement """
    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    amount = db.Column(db.Integer, nullable=False)
    accountNumber = db.Column(db.String(20), db.ForeignKey("account.account_number"))

    def __repr__(self):
        return "<Transaction timestamp='%s' amount='%s' accountNumber='%s' >" % (
            self.timestamp, self.amount, self.accountNumber)