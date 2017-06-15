CREATE TABLE IF NOT EXISTS eduloan(
       Id int,
       LoanType varchar(80),
       MCLR1Year float,
       Spread float,
       EffInterestRate float,
       ResetPeriod float,
       Nationality varchar(100),
       InstituteName varchar(100),
       InstituteType varchar(100),
       InstituteCountry varchar(100),
       LoanLimit int,
       Security varchar(100),
       Gender varchar(10),
       Concession float,
       Comments varchar(100),
       PRIMARY KEY (Id)
);
