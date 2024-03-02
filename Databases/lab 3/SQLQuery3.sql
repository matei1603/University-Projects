use PastryShops
go
create procedure addCountrytoShops as
    alter table Shops add Country varchar(30)
go
create procedure deleteCountrytoShops as
    alter table Shops drop column Country

go
create procedure addDefaultToEmployees as
    alter table Employees add constraint DEFAULT0 default(2000) for Salary
go
create procedure deleteDefaultToEmployees as
    alter table Employees drop constraint DEFAULT0
go
create procedure addSales as
    CREATE TABLE Sales (
    SaleID INT PRIMARY KEY IDENTITY,
    Cid INT,
    SaleDate DATE,
    Amount INT,
	PID INT,
    FOREIGN KEY (Cid) REFERENCES Cakes(Cid)
)
    
go
create procedure dropSales as
    drop table Sales
go
create procedure newForeignKeySales AS
    alter table Sales
        ADD CONSTRAINT SALES_FOREIGN_KEY_SHOPS FOREIGN KEY (PID) REFERENCES Shops(PID);
go
create procedure dropForeignKeySales as
    alter table Sales
		drop constraint SALES_FOREIGN_KEY_SHOPS

create table versionTable (
    version int
)

insert into versionTable values (1) -- initial version

create table proceduresTable (
    fromVersion int,
    toVersion int,
    primary key (fromVersion, toVersion),
    nameProc varchar(max)
)

insert into proceduresTable values (1, 2, 'addCountrytoShops')
insert into proceduresTable values (2, 1, 'deleteCountrytoShops')
insert into proceduresTable values (2, 3, 'addDefaultToEmployees')
insert into proceduresTable values (3, 2, 'deleteDefaultToEmployees')
insert into proceduresTable values (3, 4, 'addSales')
insert into proceduresTable values (4, 3, 'dropSales')
insert into proceduresTable values (4, 5, 'newForeignKeySales')
insert into proceduresTable values (5, 4, 'dropForeignKeySales')
select * from proceduresTable

go
create procedure goToVersion(@newVersion int) as
    declare @curr int
    declare @var varchar(max)
    select @curr=version from versionTable

    if @newVersion > (select max(toVersion) from proceduresTable)
        raiserror ('Bad version', 10, 1)

    while @curr > @newVersion begin
        select @var=nameProc from proceduresTable where fromVersion=@curr and toVersion=@curr-1
        exec (@var)
        set @curr=@curr-1
    end

    while @curr < @newVersion begin
        select @var=nameProc from proceduresTable where fromVersion=@curr and toVersion=@curr+1
        exec (@var)
        set @curr=@curr+1
    end

    update versionTable set version=@newVersion

execute goToVersion 1 
go
select * from Shops



select *from versionTable

