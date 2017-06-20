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


"""
Will add data tonight
"""
