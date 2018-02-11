drop database PD2;
go
create database PD2;
go

drop table PVModule;
drop table BypassDiodes;
drop table PerformanceRating;
drop table Manufacturer;
drop table Laboratory;
drop table Test;
drop table DiodeToModule;

create table PVModule (
ModuleID int primary key not null,
Length int not null,
Width int not null,
CellArea int not null,
CellTechnology varchar(20),
TotalNumberOfCells int not null,
NumberOfCellsSeries int not null,
NumberOfCellsParallel int not null,
SeriesFuseRating varchar(10),
InterconnectMaterial varchar(30),
InterconnectSupplier varchar(20),
SuperstrateType varchar(20),
SuperstrateManufacturer varchar(20),
SubstrateType varchar(20),
SubstrateManufacturer varchar(20),
FrameMaterial varchar(20),
FrameAdhesive varchar(20),
EncapsulantType varchar(20),
EncapsulantManufacturer varchar(20),
JunctionBoxType varchar(20),
JunctionBoxManufacturer varchar(20),
JunctionBoxAdhesive varchar(20),
CableType varchar(20),
ConnectorType varchar(20),
MaximumSystemVoltage int not null,
);

create table BypassDiodes(
DiodeID int primary key not null,
Rating int not null,
MaxJunctionTemp int null
);

create table PerformanceRating (
PerformanceRating int primary key not null,
NOCT int not null,
ISC int not null,
VOC int not null,
IMP int not null,
VMP int not null,
FF int not null,
PMP int not null
);

create table Manufacturer (
ManufacturerID int primary key not null,
Date datetime not null,
PerformanceRating int not null,
constraint FK_PerformanceRating foreign key (PerformanceRating) references PerformanceRating(PerformanceRating),
Location varchar(20),
ManufacturerName varchar(20),
ContactFName varchar(20),
ContactLName varchar(20),
Address varchar(20),
City varchar(20),
State varchar(20),
Country varchar(30),
Phone varchar(9),
Email varchar(30)
);

create table Laboratory (
LabID int primary key not null,
LabName varchar(30),
Address varchar(20),
City varchar(20),
State varchar(20),
Country varchar(30),
ContactFName varchar(20),
ContactLName varchar(20),
Phone varchar(9),
Email varchar(30),
PVTestID int not null,
TestStandard varchar(20)
);

create table Test (
TestID int primary key not null,
TestEngineerFName varchar(20),
TestEngineerLName varchar(20),
Date datetime not null,
NOCT int not null,
ISC int not null,
VOC int not null,
IMP int not null,
VMP int not null,
FF int not null,
PMP int not null,
PassFail varchar(4)
);

create table DiodeToModule (
DiodeID int primary key references BypassDiodes(DiodeID),
ModuleID int not null,
constraint FK_ModuleID foreign key (ModuleID) references PV_Module(ModuleID)
);


select * from PV_Module;
select * from BypassDiodes;
select * from Manufacturer;
select * from PerformanceRating;
select * from Laboratory;
select * from Test;
select * from DiodeToModule;