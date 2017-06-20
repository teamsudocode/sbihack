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
    id = i
    timestamp = randomDate("2005-01-01", "2017-06-20", random.random())
    amount = random.randint(10000,5000000)
    accountNumber = random.randint(10000,5000000)

eduloans = [
	EduLoan(1, 'ScholarSBI1', 4, 9.0, 1, 'Indian', 'UnderGrad', 'IIT/IIM/NIT/IIIT', 'India', 1000000, 'Parent', 'M/F', 0.0, 'Mighty IITians'),
	EduLoan(2, 'ScholarSBI2', 5.5, 10.5, 1, 'Indian', 'UnderGrad/PostGrad', 'Any', 'India', 1000000, 'Parent', 'M/F', 0.0, 'None'),
	EduLoan(3, 'ScholarSBI3', 5, 9.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 1000000, 'Parent', 'F', 1.0, 'Ladies first'),
	EduLoan(4, 'ScholarSBI4', 6, 8.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 1000000, 'Parent/Collateral', 'M/F', 0.0, 'None')
]
db.session.add_all(eduloans)
db.session.commit()
