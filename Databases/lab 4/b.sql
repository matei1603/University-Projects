--create a view that will show us the detalis about a cake when its price is >15 : its name,its type, its laboratory and its shopcake 
CREATE VIEW vCakeDetails
AS
SELECT ck.Name AS CakeName, lab.Lid AS LaboratoryID, sc.Pid AS ShopCakeID, ct.Type AS CakeType
FROM Cakes ck
JOIN ShopsCakes sc ON ck.Cid = sc.Cid
JOIN CakeTypes ct ON ck.Sid = ct.Sid
JOIN Laboratory lab ON ck.Lid = lab.Lid
WHERE ck.Price > 15;

go

select * from vCakeDetails

create table Logs( lid int primary key identity, TriggerDate date, TriggerType varchar(50), NameAffectedTable varchar(50), NoAMDRows int)
select* from Logs
--copy of the table
create table CakeTypesT(Sid int primary key, Type varchar(50),NoOfCakes int)
go

select * from CakeTypes