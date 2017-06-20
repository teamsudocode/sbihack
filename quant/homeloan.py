class Homeloan(db.Model):
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


 data1 = Homeloan(1, 'Homeloan', 'SBI Reverse Mortgage Loan', 11.9, 0, 30, 100000, 3000000, 0, 1, 18, 70, 'Senior Citizen', 'For personal use')

 db.session.add(data1)
 db.session.commit()
