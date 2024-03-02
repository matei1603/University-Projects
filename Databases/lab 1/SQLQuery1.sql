Create database PastryShops
go
usePastryShops
go

CREATE TABLE Shops
(PID INT PRIMARY KEY IDENTITY,
NAME VARCHAR(50),
City varchar(50) NOT NULL,
NoOfShops int,
NoOfClients int
CONSTRAINT FK_Laboratory FOREIGN KEY (Lid) REFERENCES Laboratory(Lid))

CREATE TABLE Laboratory
(Lid INT PRIMARY KEY IDENTITY,
NoOfCakes int,
NoOfEmployees int)

CREATE TABLE CakeTypes
(Sid INT PRIMARY  KEY IDENTITY,
Type varchar(50) Default 'Chocolate',
NoOfTeas int)

CREATE TABLE Cakes
(Cid INT PRIMARY KEY IDENTITY,
Name varchar(50),
Quantity int,
Price int,
Sid INT FOREIGN KEY REFERENCES CakeTypes(Sid))

CREATE TABLE ShopsCakes
(Cid INT FOREIGN KEY REFERENCES Cakes(Cid),
Pid INT FOREIGN KEY REFERENCES Shops(Pid),
CONSTRAINT pk_Teas PRIMARY KEY(Cid,Pid)
)

CREATE TABLE EMPLOYEES
( PIN INT PRIMARY KEY IDENTITY,
NAME varchar(50),
Salary int,
Pid INT FOREIGN KEY REFERENCES Shops(Pid))



CREATE TABLE Managers
(Mid INT FOREIGN KEY REFERENCES Shops(Pid),
Name varchar(50) NOT NULL,
Experience INT,
CONSTRAINT pk_ShopsManagers PRIMARY KEY(Mid))









