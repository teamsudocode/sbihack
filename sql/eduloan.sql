CREATE TABLE IF NOT EXISTS homeloan(
       Id int,
       LoanType varchar(40),
       MCLR1Year float,
       Spread float,
       EffInterestRate float,
       ResetPeriod float,
       Nationality int,
       InstituteName int,
       InstituteType int,
       InstituteCountry int,
       LoanLimit int,
       Security varchar(100),
       Gender varchar(100),
       AgeLowerLimit int,
       AgeUpperLimit int,
       Concession float,
       Comments varchar(100),
       PRIMARY KEY (Id)
);