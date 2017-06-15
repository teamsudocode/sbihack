class EduLoan(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    LoanType = db.Column(db.String(80))
    MCLR1Year = db.Column(db.Float)
    Spread = db.Column(db.Float)
    EffInterestRate = db.Column(db.Float)
    ResetPeriod = db.Column(db.Float)
    Nationality = db.Column(db.String(100))
    InstituteName = db.Column(db.String(100))
    InstituteType = db.Column(db.String(100))
    InstituteCountry = db.Column(db.String(100))
    LoanLimit = db.Column(db.Integer)
    Security = db.Column(db.String(100))
    Gender = db.Column(db.String(10))
    Concession = db.Column(db.Float)
    Comments = db.Column(db.String(100))

    def __init__(self, Id, LoanType, MCLR1Year, Spread, EffInterestRate, ResetPeriod, Nationality, InstituteName,
                 InstituteType, InstituteCountry, LoanLimit, Security, Gender, Concession, Comments):
        self.Id = Id
        self.LoanLimit = LoanLimit
        self.MCLR1Year = MCLR1Year
        self.Spread = Spread
        self.EffInterestRate = EffInterestRate
        self.ResetPeriod = ResetPeriod
        self.Nationality = Nationality
        self.InstituteName = InstituteName
        self.InstituteType = InstituteType
        self.InstituteCountry = InstituteCountry
        self.LoanLimit = LoanLimit
        self.Security = Security
        self.Gender = Gender
        self.Concession = Concession
        self.Comments = Comments

    def __repr__(self):
        return '<Eduloan %r>' % self.Id