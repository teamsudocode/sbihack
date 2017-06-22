import random, string, time
from __init__ import *
from models import *

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

wordslist = []
with open("/usr/share/dict/words") as f:
    wordslist.extend(f.readlines())

def randomword(length):
    return ''.join(random.choice(wordslist) for i in range(length))

def randombignum(length):
    return ''.join(random.choice(string.digits) for i in range(length))

"""for i in range(1,40):
    curdate = randomDate("2005-01-01", "2017-06-20", random.random())
    temp = Log(userid = i,productid = random.randint(1,5), timestamp= curdate)
    db.session.add(temp)
    db.session.commit()"""

prodlist = []
for i in range(1,40):
    name = "Product-" + str(i)
    category = random.randint(1,5)
    temp = Product(name,category)
    prodlist.append(temp)
# db.session.add_all(prodlist)


userlist = []
for i in range(1,40):
    name = "User-"+str(i)
    cif = str(1234*i)
    temp = User(name,cif)
    userlist.append(temp)
# db.session.add_all(userlist)


ratingslist = []
for i in range(1,40):
    userid = i
    productid = i
    rating = str(random.randint(1,5))
    title = "Review-"+str(i)+randomword(random.randint(2,5))
    comment = randomword(random.randint(5,15))
    temp = Review(userid, productid, rating, title, comment)
    ratingslist.append(temp)
# db.session.add_all(ratingslist)


issuelist = []
for i in range(1,10) :
    reviewid = i
    temp = Issue(reviewid)
    issuelist.append(temp)
# db.session.add_all(issuelist)


accountlist = []
for i in range(1,40):
    account_number =  randombignum(20)
    owner_cif = 1234*i
    balance = random.randint(10000,10000000)
    temp = Account(account_number, owner_cif, balance)
    accountlist.append(temp)
# db.session.add_all(accountlist)


transactionlist = []
for i in range(1,20):
    curtime = datetime.strptime("2017-06-"+str(random.randint(1, 30)), "%Y-%m-%d")
    am = random.randint(10000,5000000)
    accNumber = randombignum(20)
    temp = Transaction(id = i,timestamp = curtime, amount = am, accountNumber = accNumber)
    transactionlist.append(temp)
# db.session.add_all(transactionlist)

i = 1
eduloans = [
	EduLoan(1, 'ScholarSBI1', 4, 9.0, 1, 'Indian', 'UnderGrad', 'IIT/IIM/NIT/IIIT', 'India', 1000000, 'Parent', 'M/F', 0.0, 'Mighty IITians', i),
	EduLoan(2, 'ScholarSBI2', 5.5, 10.5, 1, 'Indian', 'UnderGrad/PostGrad', 'Any', 'India', 1000000, 'Parent', 'M/F', 0.0, 'None', i+1),
	EduLoan(3, 'ScholarSBI3', 5, 9.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 5000000, 'Parent', 'F', 1.0, 'Ladies first', i+2),
	EduLoan(4, 'ScholarSBI4', 6, 8.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 2000000, 'Parent/Collateral', 'M/F', 0.0, 'None', i+3),
	EduLoan(5, 'ScholarSBI5', 10, 7.5, 1, 'Indian', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 4000000, 'Parent/Collateral', 'M/F', 0.0, 'Indians only', i+4),
	EduLoan(6, 'ScholarSBI6', 15, 10, 1, 'NRI', 'UnderGrad/PostGrad', 'Any', 'India', 7000000, 'Collateral', 'M/F', 0.0, 'Especially for NRI', i+5),
	EduLoan(7, 'ScholarSBI7', 6, 8, 1, 'Indian/NRI', 'PostGrad', 'Any', 'India/Abroad', 1500000, 'Parent/Collateral', 'M/F', 0.0, 'PG only', i+6),
	EduLoan(8, 'ScholarSBI8', 5, 11, 1, 'Indian/NRI', 'UnderGrad', 'Any', 'India/Abroad', 2000000, 'Parent/Collateral', 'M/F', 0.0, 'UG only', i+7)
]
i += 7
# db.session.add_all(eduloans)
# db.session.commit()

homeloan = [
    Homeloan(1, 'SBI_Home_Loan_1', 11.9, 20, 100000, 3000000, 0, 1, 18, 70, 'Senior Citizen', 'For personal use', i),
    Homeloan(2, 'SBI_Home_Loan_2', 8.5, 25, 100000, 5000000, 0, 1, 18, 70, 'Female', 'Ladies Quota', i+1),
    Homeloan(3, 'SBI_Home_Loan_3', 9.7, 35, 100000, 10000000, 0, 1, 18, 70, 'Any', 'Home Only', i+2),
    Homeloan(4, 'SBI_Home_Loan_4', 7.7, 30, 100000, 50000000, 0, 1, 18, 70, 'SC', 'Bahut faydaa hai', i+3),
	Homeloan(5, 'SBI_Home_Loan_5', 9.9, 20, 100000, 500000, 0, 1, 18, 70, 'Any', 'kam loge to yahi hoga', i+4),
	Homeloan(6, 'SBI_Home_Loan_6', 7.5, 30, 100000, 50000000, 0, 1, 18, 70, 'ST', 'Bahut faydaa hai', i+5),
	Homeloan(7, 'SBI_Home_Loan_7', 8.0, 25, 100000, 50000000, 0, 1, 18, 28, 'Any', 'Young Raho', i+6),
	Homeloan(8, 'SBI_Home_Loan_8', 9, 8, 100000, 50000000, 0, 1, 18, 70, 'Any', 'Fast repayment',i+7)
]
# db.session.add_all(homeloan)
# db.session.commit()

insurance = [
    Insurance(1, 'SBI_Insurance_1', 24000, 10, 30, 8, 30, 70, 40, 80, "Yearly", 24000, 'Infinite', 'Retirment',220),
    Insurance(2, 'SBI_Insurance_1', 24000, 10, 30, 8, 30, 70, 40, 80, "Half-Yearly", 15000, 'Infinite', 'Retirment',220),
    Insurance(3, 'SBI_Insurance_1', 24000, 10, 30, 8, 30, 70, 40, 80, "Quaterly", 7500, 'Infinite', 'Retirment',220),
    Insurance(4, 'SBI_Insurance_1', 24000, 10, 30, 8, 30, 70, 40, 80, "Monthly", 2500, 'Infinite', 'Retirment',220),
    Insurance(5, 'SBI_Insurance_2', 6000, 0, 70, 15, 0, 13, 21, 50, "Yearly", 6000, 'Infinite', 'Child',250),
    Insurance(6, 'SBI_Insurance_2', 6000, 0, 70, 15, 0, 13, 21, 50, "Half-Yearly", 3000, 'Infinite', 'Child',250),
    Insurance(7, 'SBI_Insurance_2', 6000, 0, 70, 15, 0, 13, 21, 50, "Quaterly", 1500, 'Infinite', 'Child',250),
    Insurance(8, 'SBI_Insurance_2', 6000, 0, 70, 15, 0, 13, 21, 50, "Monthly", 500, 'Infinite', 'Child',250),
    Insurance(9, 'SBI_Insurance_3', 30000, 0, 70, 15, 0, 70, 20, 80, "Yearly", 30000, 'Infinite', 'Any',200),
    Insurance(10, 'SBI_Insurance_3', 30000, 0, 70, 15, 0, 70, 20, 80, "Yearly", 17000, 'Infinite', 'Any',200),
    Insurance(11, 'SBI_Insurance_3', 30000, 0, 70, 15, 0, 70, 20, 80, "Yearly", 10000, 'Infinite', 'Any',200),
    Insurance(12, 'SBI_Insurance_3', 30000, 0, 70, 15, 0, 70, 20, 80, "Yearly", 4000, 'Infinite', 'Any',200)
]

# db.session.add_all(insurance)
# db.session.commit()

logs = [
    Log(userid=1, productid=2, timestamp=datetime.strptime("2017-05-04", "%Y-%m-%d")),
    Log(userid=1, productid=1, timestamp=datetime.strptime("2017-05-29", "%Y-%m-%d")),
    Log(userid=2, productid=1, timestamp=datetime.strptime("2017-04-03", "%Y-%m-%d")),
    Log(userid=2, productid=1, timestamp=datetime.strptime("2017-04-13", "%Y-%m-%d")),
    Log(userid=2, productid=1, timestamp=datetime.strptime("2017-04-23", "%Y-%m-%d")),
    Log(userid=2, productid=1, timestamp=datetime.strptime("2017-04-17", "%Y-%m-%d")),
    Log(userid=2, productid=1, timestamp=datetime.strptime("2017-04-18", "%Y-%m-%d")),
    Log(userid=2, productid=1, timestamp=datetime.strptime("2017-04-15", "%Y-%m-%d")),
    Log(userid=2, productid=1, timestamp=datetime.strptime("2017-04-10", "%Y-%m-%d")),
    Log(userid=2, productid=2, timestamp=datetime.strptime("2017-06-13", '%Y-%m-%d'))
]

finallist = []
finallist.extend(prodlist)
finallist.extend(userlist)
finallist.extend(ratingslist)
finallist.extend(issuelist)
finallist.extend(accountlist)
finallist.extend(transactionlist)

finallist.extend(eduloans)
finallist.extend(homeloan)
finallist.extend(insurance)
finallist.extend(logs)

db.session.add_all(finallist)
db.session.commit()
