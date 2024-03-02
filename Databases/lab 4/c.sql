create trigger add_CakeTypes on CakeTypes for 
insert as
begin
insert into CakeTypesT(Sid, Type, NoOfCakes)
select Sid, Type, NoOfCakes
from inserted
insert into Logs(TriggerDate,TriggerType,NameAffectedTable,NoAMDRows)
values(GETDATE(),'INSERT','CakeTypes',@@ROWCOUNT)
end
go
SET IDENTITY_INSERT CakeTypes OFF;

drop trigger add_CakeTypes
select * from CakeTypes
select * from CakeTypesT
INSERT INTO CakeTypes(Sid, Type, NoOfCakes) VALUES (108, 'Lemon', 20);
select * from CakeTypes
select * from CakeTypesT


insert into CakeTypes(Type,NoOfCakes) values ('Lemon', 30)
