use PastryShops
select *from Laboratory

-- Clustered index scan query on CakeTypes
SELECT *
FROM CakeTypes
WHERE Type = 'Chocolate';

-- Clustered index seek query on CakeTypes with ORDER BY clause
SELECT *
FROM CakeTypes
ORDER BY Sid;


-- Nonclustered index scan query on Laboratory
SELECT *
FROM Laboratory
WHERE NoOfCakes > 100;

-- Nonclustered index seek query on Laboratory
SELECT *
FROM Laboratory
WHERE Lid = 50;

-- Key lookup query on CakeTypes and Laboratory tables
SELECT Cakes.Name, CakeTypes.Type, Laboratory.NoOfCakes
FROM Cakes
INNER JOIN CakeTypes ON Cakes.Sid = CakeTypes.Sid
INNER JOIN Laboratory ON Cakes.Lid = Laboratory.Lid;

