SET iDENTITY_INSERT Employees ON
use PastryShops
INSERT INTO Employees(PIN,NAME,Salary,Pid)
VALUES
(5030924863,'Vlad Ichim',3300,1),
(5020416552,'Sabin Barboi',3300,2),
(5020104312,'Brumari Darian', 2900,3),
(4030116332,'Maria Pop', 3000,4),
(4010630442,'Eliza Marinescu', 3300,5),
(4020512335,'Elena Popescu', 2900,6)



SET IDENTITY_INSERT CakeTypes OFF;
INSERT INTO CakeTypes(Sid,Type,NoOfCakes)
VALUES
(100,'Chocolate',5),
(101,'Mint', 8),
(102,'Vanilla',10),
(103,'Rom',2),
(104,'Strawberry',5),
(105,'Cherry',12)


SET IDENTITY_INSERT Laboratory OFF;
INSERT INTO Laboratory(Lid,NoOfCakes,NoOfEmployees)
VALUES
(50,250,20)

SET IDENTITY_INSERT Shops ON;
INSERT INTO Shops(PID,NAME,City,NoOfClients)
VALUES
(1,'Panemar','Cluj-Napoca',50),
(2,'Donuterie','Suceava',100),
(3,'CandyMandy','Botosani',20),
(4,'LazyCandy','Zalau',30),
(5,'Candies','Galati',45),
(6,'Belpan','Bacau',55)

SET IDENTITY_INSERT Shops OFF;

SET IDENTITY_INSERT Cakes Off;
INSERT INTO Cakes(Cid,Name,Quantity,Price,Sid,Lid)
VALUES
(150,'Diplomat',12,60,100,50),
(151,'Bavaria',20,80,101,50),
(152,'Negresa',30,20,102,50),
(153,'Chec',8,30,103,50),
(154,'Amandina',16,15,104,50),
(155,'LavaCake',30,30,105,50)
SET IDENTITY_INSERT Cakes OFF;

SET IDENTITY_INSERT ShopsCakes ON;
INSERT INTO ShopsCakes(Cid,Pid)
VALUES
(150,1),
(151,2),
(152,3),
(153,4),
(154,5),
(155,6);
select * from ShopsCakes

SET IDENTITY_INSERT Employees ON;
INSERT INTO Employees(PIN,NAME,Salary,Pid)
VALUES
(5030924863,'Vlad Ichim',3300,1),
(5020416552,'Sabin Barboi',3300,2),
(5020104312,'Brumari Darian', 2900,3),
(4030116332,'Maria Pop', 3000,4),
(4010630442,'Eliza Marinescu', 3300,5),
(4020512335,'Elena Popescu', 2900,6)

SET IDENTITY_INSERT Managers ON;
INSERT INTO Managers
VALUES
(1,'Vlad Morosanu', 5),
(2,'Horea Turc', 8)


UPDATE Employees
SET Salary = 3500
WHERE PIN = 5030924863;

Update CakeTypes
SET NoOfCakes = 10
WHERE NoOfCakes = 5 OR Type= 'Chocolate';

UPDATE Employees
SET Salary = NULL
WHERE Salary = 3000;

UPDATE Employees
SET Salary = 3500
WHERE Salary IS NULL;

UPDATE Cakes
SET Price = 50
WHERE Price BETWEEN 40 AND 60;

UPDATE Cakes
SET Price = 70
WHERE Sid IN (100, 101);

UPDATE Shops
SET NoOfClients = 60
WHERE NAME LIKE '%Candy%';

-- UNION: Combines Employees and Managers names
SELECT Name FROM Employees
UNION
SELECT Name FROM Managers;

-- INTERSECT:we display names of cakes where the price is >60
SELECT Name FROM Cakes
WHERE Price > 60 and Quantity> 10
INTERSECT
SELECT Name FROM Cakes;

SELECT * FROM Cakes;

-- EXCEPT: we display Name and Quantity from the table Cakes where the price is >=40
SELECT Name, Quantity FROM Cakes
EXCEPT
SELECT Name, Quantity from Cakes
WHERE Price <40 or Quantity >30

use PastryShops
--INNER JOIN: names from the Shops table that have corresponding entries in the "ShopsCakes" table through an INNER JOIN on their shared ID columns.
SELECT Shops.NAME
FROM Shops
INNER JOIN ShopsCakes ON Shops.PID = ShopsCakes.Pid

--LEFT JOIN: Retrieves all shops and their corresponding cake types, if any
SELECT Shops.Name, CakeTypes.Type
FROM Shops
LEFT JOIN ShopsCakes ON Shops.PID = ShopsCakes.Pid
LEFT JOIN Cakes ON ShopsCakes.Cid = Cakes.Cid
LEFT JOIN CakeTypes ON Cakes.Sid = CakeTypes.Sid;

-- RIGHT JOIN: Retrieves all cake types and the shops selling them, if any
SELECT CakeTypes.Type, Shops.Name
FROM CakeTypes
RIGHT JOIN Cakes ON CakeTypes.Sid = Cakes.Sid
RIGHT JOIN ShopsCakes ON Cakes.Cid = ShopsCakes.Cid
RIGHT JOIN Shops ON ShopsCakes.Pid = Shops.PID;

--FULL JOIN: Retrieves all shop names and cake types, merging their relationships
SELECT COALESCE(Shops.Name, 'No Shop') AS ShopName, COALESCE(CakeTypes.Type, 'No Type') AS CakeType
FROM Shops
FULL JOIN ShopsCakes ON Shops.PID = ShopsCakes.Pid
FULL JOIN Cakes ON ShopsCakes.Cid = Cakes.Cid
FULL JOIN CakeTypes ON Cakes.Sid = CakeTypes.Sid;

-- Query using IN operator with a subquery + DISTINCT 
SELECT Name, City
FROM Shops
WHERE PID IN (
    SELECT DISTINCT Pid
    FROM ShopsCakes
);

-- Query using EXISTS operator with a subquery + ORDER BY
SELECT Name, City
FROM Shops s
WHERE EXISTS (
    SELECT 1
    FROM ShopsCakes sc
    WHERE sc.Pid = s.PID
)
ORDER BY PID DESC
;


--FROM: Average sales
SELECT AverageSales
FROM (
    SELECT AVG(NoOfClients) AS AverageSales
    FROM Shops
) AS AvgSalesPerShop;

--GROUP BY: we group the no of clients by the city + top 
SELECT TOP 5 City, SUM(NoOfClients) AS TotalClients
FROM Shops
GROUP BY City;

--GROUP BY + HAVING: we display all the cities which have more than 2 shops
SELECT City, COUNT(*) AS ShopCount
FROM Shops
GROUP BY City
HAVING COUNT(*) > 2;

select * from Shops

--GROUP BY + HAVING + AVG: we display all the cities where the no of clients if greater than the overall average + ORDER BY
SELECT City, AVG(NoOfClients) AS AvgClients
FROM Shops
GROUP BY City
HAVING AVG(NoOfClients) > (
    SELECT AVG(NoOfClients)
    FROM Shops
)
ORDER BY AvgClients ASC;
