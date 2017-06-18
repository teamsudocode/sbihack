class EduLoan(db.Model):
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

data1 = EduLoan(1, 'ScholarSBI1', 4, 9.0, 1, 'Indian', 'UnderGrad', 'IIT/IIM/NIT/IIIT', 'India', 1000000, 'Parent', 'M/F', 0.0, 'Mighty IITians')
data2 = EduLoan(2, 'ScholarSBI2', 5.5, 10.5, 1, 'Indian', 'UnderGrad/PostGrad', 'Any', 'India', 1000000, 'Parent', 'M/F', 0.0, 'None')
data3 = EduLoan(3, 'ScholarSBI3', 5, 9.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 1000000, 'Parent', 'F', 1.0, 'Ladies first')
data4 = EduLoan(4, 'ScholarSBI4', 6, 8.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 1000000, 'Parent/Collateral', 'M/F', 0.0, 'None')
db.session.add(data1)
db.session.add(data2)
db.session.add(data3)
db.session.add(data4)
db.session.commit()