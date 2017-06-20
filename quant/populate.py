import random, string, time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)

def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

for i in rang(1,25):
    curdate = randomDate("2005-01-01", "2017-06-20", random.random())
    temp = Log(userid = i,productid = random.randint(1,5), timestamp= curdate)
    db.session.add(temp)

for i in rnge(1,25):
    name = randomword(random.randint(4,9))
    category = random.randint(1,5)
    temp = Product(name,category)
    db.session.add(temp)

for i in range(1,25):
    name = randomword(random.randint(4,9))
    cif = random.randint(1,10000)
    temp = User(name,cif)
    db.session.add(temp)

for i in range(1,40):
    userid = random.randint(1,25)
    productid = random.randint(1,25)
    rating = random.randint(1,5)
    title = randomword(random.randint(5,10))
    comment = randomword(random.randint(5,15))
    temp = Review(userid, productid, rating, title, comment)
    db.session.add(temp)

for i in rang(1,7) : 
    reviewid = i
    temp = Issue(reviewid)
    db.session.add(temp)

for i in range(1,50):
    account_number =  str(random.randint(100000000000000000000,99999999999999999999))
    owner_cif = str(random.randint(10000000000,9999999999))
    balance = random.randint(10000,10000000)
    temp = Account(account_number, owner_cif, balance)
    db.session.add(temp)

for i in range(1,20):
    curtime = randomDate("2005-01-01", "2017-06-20", random.random())
    am = random.randint(10000,5000000)
    accNumber = str(random.randint(100000000000000000000,99999999999999999999))
    temp = transaction(id = i,timestamp = curtime, amount = am, accountNumber = accNumber)
    db.session.add(temp)

eduloans = [
	EduLoan(1, 'ScholarSBI1', 4, 9.0, 1, 'Indian', 'UnderGrad', 'IIT/IIM/NIT/IIIT', 'India', 1000000, 'Parent', 'M/F', 0.0, 'Mighty IITians'),
	EduLoan(2, 'ScholarSBI2', 5.5, 10.5, 1, 'Indian', 'UnderGrad/PostGrad', 'Any', 'India', 1000000, 'Parent', 'M/F', 0.0, 'None'),
	EduLoan(3, 'ScholarSBI3', 5, 9.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 5000000, 'Parent', 'F', 1.0, 'Ladies first'),
	EduLoan(4, 'ScholarSBI4', 6, 8.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 2000000, 'Parent/Collateral', 'M/F', 0.0, 'None')
	EduLoan(5, 'ScholarSBI5', 10, 7.5, 1, 'Indian', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 4000000, 'Parent/Collateral', 'M/F', 0.0, 'Indians only')
	EduLoan(6, 'ScholarSBI6', 15, 10, 1, 'NRI', 'UnderGrad/PostGrad', 'Any', 'India', 7000000, 'Collateral', 'M/F', 0.0, 'Especially for NRI')
	EduLoan(7, 'ScholarSBI7', 6, 8, 1, 'Indian/NRI', 'PostGrad', 'Any', 'India/Abroad', 1500000, 'Parent/Collateral', 'M/F', 0.0, 'PG only')
	EduLoan(8, 'ScholarSBI8', 5, 11, 1, 'Indian/NRI', 'UnderGrad', 'Any', 'India/Abroad', 2000000, 'Parent/Collateral', 'M/F', 0.0, 'UG only')
]
db.session.add_all(eduloans)

homeloan = [
    Homeloan(1, 'SBI_Home_Loan_1', 11.9, 20, 100000, 3000000, 0, 1, 18, 70, 'Senior Citizen', 'For personal use')
    Homeloan(2, 'SBI_Home_Loan_2', 8.5, 25, 100000, 5000000, 0, 1, 18, 70, 'Female', 'Ladies Quota')
    Homeloan(3, 'SBI_Home_Loan_3', 9.7, 35, 100000, 10000000, 0, 1, 18, 70, 'Any', 'Home Only')
    Homeloan(4, 'SBI_Home_Loan_4', 7.7, 30, 100000, 50000000, 0, 1, 18, 70, 'SC', 'Bahut faydaa hai')
	Homeloan(5, 'SBI_Home_Loan_5', 9.9, 20, 100000, 500000, 0, 1, 18, 70, 'Any', 'kam loge to yahi hoga')
	Homeloan(6, 'SBI_Home_Loan_6', 7.5, 30, 100000, 50000000, 0, 1, 18, 70, 'ST', 'Bahut faydaa hai')
	Homeloan(7, 'SBI_Home_Loan_7', 8.0, 25, 100000, 50000000, 0, 1, 18, 28, 'Any', 'Young Raho')
	Homeloan(8, 'SBI_Home_Loan_8', 9, 8, 100000, 50000000, 0, 1, 18, 70, 'Any', 'Fast repayment')
	
]
db.session.add_all(homeloan)

insurance = [
    Insurance(1, 'SBI_Insurance_1', 24000, 10, 30, 8, 30, 70, 40, 80, "Yearly", 24000, 'Infinite', 'Retirment',220)
    Insurance(2, 'SBI_Insurance_1', 24000, 10, 30, 8, 30, 70, 40, 80, "Half-Yearly", 15000, 'Infinite', 'Retirment',220)
    Insurance(3, 'SBI_Insurance_1', 24000, 10, 30, 8, 30, 70, 40, 80, "Quaterly", 7500, 'Infinite', 'Retirment',220)
    Insurance(4, 'SBI_Insurance_1', 24000, 10, 30, 8, 30, 70, 40, 80, "Monthly", 2500, 'Infinite', 'Retirment',220)

    Insurance(5, 'SBI_Insurance_2', 6000, 0, 70, 15, 0, 13, 21, 50, "Yearly", 6000, 'Infinite', 'Child',250)
    Insurance(6, 'SBI_Insurance_2', 6000, 0, 70, 15, 0, 13, 21, 50, "Half-Yearly", 3000, 'Infinite', 'Child',250)
    Insurance(7, 'SBI_Insurance_2', 6000, 0, 70, 15, 0, 13, 21, 50, "Quaterly", 1500, 'Infinite', 'Child',250)
    Insurance(8, 'SBI_Insurance_2', 6000, 0, 70, 15, 0, 13, 21, 50, "Monthly", 500, 'Infinite', 'Child',250)
	
    Insurance(9, 'SBI_Insurance_3', 30000, 0, 70, 15, 0, 70, 20, 80, "Yearly", 30000, 'Infinite', 'Any',200)
    Insurance(10, 'SBI_Insurance_3', 30000, 0, 70, 15, 0, 70, 20, 80, "Yearly", 17000, 'Infinite', 'Any',200)
    Insurance(11, 'SBI_Insurance_3', 30000, 0, 70, 15, 0, 70, 20, 80, "Yearly", 10000, 'Infinite', 'Any',200)
    Insurance(12, 'SBI_Insurance_3', 30000, 0, 70, 15, 0, 70, 20, 80, "Yearly", 4000, 'Infinite', 'Any',200)
]
db.session.add_all(insurance)
db.session.commit()
