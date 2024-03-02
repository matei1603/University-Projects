use PastryShops

--check an int 
create function checkInt(@n int)
returns int as
begin
	declare @no int 
	if @n>=0
		set @no = 1
	else
		set @no = 0
	return @no
end
go
--check a varchar
create function checkVarchar(@v varchar(50))
returns bit as
begin
	declare @b bit
	if @v LIKE '[a-z]%[a-z]'
		set @b=1
	else
		set @b=0
	return @b
end
go
 -- procedure for inserting in Laboratory
create procedure addLab @n int, @a int, @b int
as
begin
    -- validate the parameters @n, @a, @b
    if dbo.checkInt(@n) = 1 and dbo.checkInt(@a) = 1 and dbo.checkInt(@b) = 1
    begin
        insert into Laboratory(Lid, NoOfCakes,NoOfEmployees) values (@n, @a, @b);
        print 'value added';
        select * from Laboratory;
    end
    else
    begin
        print 'the parameters are not correct';
        select * from Laboratory;
    end
end
go
drop procedure addLab
SET IDENTITY_INSERT Laboratory OFF;
exec addLab 51, 251, 21
exec addLab 52, 252, 22


--procedure for inserting in CakeTypes
create procedure addCakeType @n int, @a varchar(50), @b int
as
begin
    -- validate the parameters @n, @a, @b
    if dbo.checkInt(@n) = 1 and dbo.checkVarChar(@a) = 1 and dbo.checkInt(@b) = 1
    begin
        insert into CakeTypes(Sid, Type,NoOfCakes) values (@n, @a, @b);
        print 'value added';
        select * from CakeTypes;
    end
    else
    begin
        print 'the parameters are not correct';
        select * from CakeTypes;
    end
end
go
select * from CakeTypes
SET IDENTITY_INSERT CakeTypes OFF;
exec addCakeType 106, SecretAroma, 16
exec addCakeType 107, Fistic, 20
