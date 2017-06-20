eduloans = [
	EduLoan(1, 'ScholarSBI1', 4, 9.0, 1, 'Indian', 'UnderGrad', 'IIT/IIM/NIT/IIIT', 'India', 1000000, 'Parent', 'M/F', 0.0, 'Mighty IITians'),
	EduLoan(2, 'ScholarSBI2', 5.5, 10.5, 1, 'Indian', 'UnderGrad/PostGrad', 'Any', 'India', 1000000, 'Parent', 'M/F', 0.0, 'None'),
	EduLoan(3, 'ScholarSBI3', 5, 9.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 1000000, 'Parent', 'F', 1.0, 'Ladies first'),
	EduLoan(4, 'ScholarSBI4', 6, 8.5, 1, 'Indian/NRI', 'UnderGrad/PostGrad', 'Any', 'India/Abroad', 1000000, 'Parent/Collateral', 'M/F', 0.0, 'None')
]
db.session.add_all(eduloans)
db.session.commit()