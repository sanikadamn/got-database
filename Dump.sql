--
-- creating a data dump for dnaproject
-- group 17
-- database name: CITADEL
--

DROP DATABASE IF EXISTS CITADEL;
CREATE DATABASE CITADEL;

USE CITADEL;

--
-- creating tables
--
--

DROP TABLE IF EXISTS PEOPLE;
CREATE TABLE PEOPLE
(   PID INT NOT NULL,
    Fname VARCHAR(30) NOT NULL,
    Lname VARCHAR(30) NOT NULL,
    DOB DATE NOT NULL,
    Status_Dead_or_Alive VARCHAR(10),
    House_Name VARCHAR(30),
    Kingdom_they_are_in VARCHAR(50),
PRIMARY KEY (PID) );

DROP TABLE IF EXISTS KINGS_LANDING_RULERS;
CREATE TABLE KINGS_LANDING_RULERS
(   PID INT NOT NULL,
    House VARCHAR(30),
    Duration_Years INT,
FOREIGN KEY (PID) REFERENCES PEOPLE(PID));


DROP TABLE IF EXISTS KINGDOMS;
CREATE TABLE KINGDOMS
(   Name VARCHAR(50) NOT NULL,
    Continent VARCHAR(30),
PRIMARY KEY (Name) );

DROP TABLE IF EXISTS AREA;
CREATE TABLE AREA
(   Location VARCHAR(30) NOT NULL,
    Kingdom VARCHAR(50),
FOREIGN KEY (Kingdom) REFERENCES KINGDOMS(Name),
PRIMARY KEY (Location));

DROP TABLE IF EXISTS DRAGONS;
CREATE TABLE DRAGONS
(   Name VARCHAR(20) NOT NULL,
    Age INT,
    Color VARCHAR(30),
    Status_Dead_or_Alive VARCHAR(10),
PRIMARY KEY (Name) );

DROP TABLE IF EXISTS HOUSES;
CREATE TABLE HOUSES
(   Name VARCHAR(30) NOT NULL,
    Sigil VARCHAR(30) NOT NULL,
    Motto VARCHAR(40) NOT NULL,
PRIMARY KEY (Name) );

DROP TABLE IF EXISTS COOL_DEATHS;
CREATE TABLE COOL_DEATHS
(   Person_Dead_PID INT NOT NULL,
    When_ DATE,
    Weapon_Used VARCHAR(30),
    Manner_of_Killing VARCHAR(40),
    Place VARCHAR(30),
FOREIGN KEY (Person_Dead_PID) REFERENCES PEOPLE(PID));

DROP TABLE IF EXISTS RULED_BY;
CREATE TABLE RULED_BY
(   Kingdom VARCHAR(50) NOT NULL,
    House VARCHAR(30),
FOREIGN KEY (Kingdom) REFERENCES KINGDOMS(Name),
FOREIGN KEY (House) REFERENCES HOUSES(Name));

DROP TABLE IF EXISTS RIDE;
CREATE TABLE RIDE
(   Dragon VARCHAR(20) NOT NULL,
    Rider_PID INT NOT NULL,
FOREIGN KEY (Dragon) REFERENCES DRAGONS(Name),
FOREIGN KEY (Rider_PID) REFERENCES PEOPLE(PID));

DROP TABLE IF EXISTS DIE_BY;
CREATE TABLE DIE_BY
(   Person_Dead_PID INT NOT NULL,
    People_Responsible_PID INT NOT NULL,
FOREIGN KEY (People_Responsible_PID) REFERENCES PEOPLE(PID),
FOREIGN KEY (Person_Dead_PID) REFERENCES COOL_DEATHS(Person_Dead_PID));

-- DROP TABLE IF EXISTS PEOPLE_RESPONSIBLE;
-- CREATE TABLE PEOPLE_RESPONIBLE
-- (   Fname VARCHAR(20),
--     Killed VARCHAR(20),
-- FOREIGN KEY (Fname) REFERENCES DIE_BY(People_Responsible_Fname),
-- FOREIGN KEY (Killed) REFERENCES COOL_DEATHS(Name_of_Person_Dead) );

ALTER TABLE PEOPLE
 ADD CONSTRAINT Ppl_hs FOREIGN KEY (House_Name) REFERENCES HOUSES(Name);
ALTER TABLE PEOPLE
 ADD CONSTRAINT Ppl_kdom FOREIGN KEY (Kingdom_they_are_in) REFERENCES KINGDOMS(Name);
ALTER TABLE KINGS_LANDING_RULERS
    ADD CONSTRAINT Rul_hs FOREIGN KEY (House) REFERENCES HOUSES(Name);
    
-- tables created
--
--
--

-- dumping data for tables
--
--
--


INSERT INTO HOUSES VALUES
('Stark','Direwolf','Winter is Coming'),
('Targaryen','Dragon','Fire and Blood'),
('Baratheon','Stag','Ours is the Fury'),
('Greyjoy','Kraken','We do not sow'),
('Lannister','Lion','Hear me Roar'),
('Martell','Sun','Unbowed. Unbent. Unbroken'),
('Tyrell','Rose','Growing Strong'),
('Bolton', 'Flayed Man', 'Our blades are sharp'),
('Arryn','Falcon','As High as Honour');

INSERT INTO KINGDOMS VALUES
('Kingdom of the North','Westeros'),
('Kingdom of Mountain and Vale','Westeros'),
('Kingdom of the Isles and the Rivers','Westeros'),
('Kingdom of the Rock','Westeros'),
('Kingdom of the Reach','Westeros'),
('Kingdom of the Stormlands','Westeros'),
('Principality of Dorne','Westeros'),
('The Crownlands','Westeros'),
('The Wall','Westeros'),
('Braavos','Essos'),
('Lorath','Essos'),
('Dothraki Sea','Essos'),
('Slaver' 's Bay','Essos');

INSERT INTO PEOPLE VALUES
(1, 'Robb', 'Stark', '1999-09-03', 'Dead', 'Stark', 'Kingdom of Mountain and Vale'),
(2, 'Sansa', 'Stark', '2003-12-04', 'Alive', 'Stark', 'The Crownlands'),
(3, 'Bran', 'Stark', '2007-03-24', 'Alive', 'Stark', 'Kingdom of the North'),
(4, 'Arya', 'Stark', '2005-05-30', 'Alive', 'Stark', 'Braavos'),
(5, 'Jon', 'Snow', '1999-05-01', 'Alive', 'Stark', 'The Wall'),
(6, 'Ned', 'Stark', '1950-04-23', 'Dead', 'Stark', 'Kingdom of the North'),
(7, 'Robert', 'Baratheon', '1949-06-24','Dead','Baratheon','The Crownlands'),
(8, 'Joffrey','Baratheon','2002-12-05','Dead','Baratheon','The Crownlands'),
(9, 'Cersei','Lannister','1980-03-06','Alive','Lannister','The Crownlands'),
(10, 'Daenerys','Targaryen','1999-06-06','Alive','Targaryen','Dothraki Sea'),
(11, 'Missandei','Naath','2000-04-21','Alive','Targaryen','Slaver' 's Bay'),
(12, 'Olenna','Tyrell','1920-09-18','Dead','Tyrell','Kingdom of the Reach'),
(15, 'Shae', 'Shae', '1995=05-05', 'Dead', NULL, 'Lorath'),
(16, 'Ellaria', 'Sand', '1988-02-13', 'Alive', NULL, 'Principality of Dorne'),
(18, 'Tommen', 'Baratheon', '2006-03-18', 'Dead', 'Baratheon', 'The Crownlands'),
(19, 'Myrcella', 'Baratheon', '2004-01-04', 'Dead', 'Baratheon', 'Principality of Dorne'),
(20, 'Jaime', 'Lannister', '1980-03-06', 'Alive', 'Lannister', 'The Crownlands'),
(21, 'Lisa', 'Arryn', '1981-09-14', 'Alive', 'Arryn', 'Kingdom of Mountain and Vale'),
(13, 'Tyrion', 'Lannister', '1984-12-20', 'Alive', 'Lannister', 'The Crownlands'),
(23, 'Roose', 'Bolton', '1992-02-03', 'Alive', 'Bolton', 'Kingdom of the North'),
(22, 'Night', 'King', '0001-01-01', 'Alive', NULL, 'The Wall'),
(17,'Nushka','Stark','2003-03-05','Dead','Stark','The Crownlands'),
(24,'Nika','Snow','2003-07-15','Dead','Stark','Kingdom of the North'),
(14, 'Nanya','Targaryen','2003-08-03','Alive','Targaryen','The Crownlands');

INSERT INTO KINGS_LANDING_RULERS VALUES
(2,  'Stark', 8),
(3,  'Stark', 4),
(5, 'Stark',2),
(7, 'Baratheon',10),
(8, 'Lannister',2),
(9, 'Lannister',4),
(10, 'Targaryen',3),
(12, 'Tyrell',1),
(14,'Targaryen',5),
(18, 'Lannister', 2);

INSERT INTO AREA VALUES
('King' 's Landing', 'The Crownlands'),
('Winterfell','Kingdom of the North'),
('Vaes Dothrak','Dothraki Sea'),
('Highgarden','Kingdom of the Reach'),
('Castle Black','The Wall'),
('The Eyrie','Kingdom of Mountain and Vale'),
('Sunspear','Principality of Dorne'),
('Dragonstone','The Crownlands'),
('House of Black and White','Braavos'),
('Meereen','Slaver' 's Bay'),
('Storm' 's End','Kingdom of the Stormlands');

INSERT INTO DRAGONS VALUES
('Syrax',22,'Yellow','Alive'),
('Caraxes',31,'Red','Alive'),
('Balerion',12,'Black','Alive'),
('Seasmoke',43,'Grey','Dead'),
('Dreamfyre',12,'Blue','Alive'),
('Vhagar',90,'Black','Dead'),
('Maleyes',56,'Scarlet','Dead'),
('Drogon',10,'Black','Alive'),
('Rhaegal',10,'Green','Alive'),
('Viserion',10,'Red','Alive');

INSERT INTO COOL_DEATHS VALUES
(1, '2018-10-24', 'Knife', 'Throat slit', 'The Red Wedding'),
(6, '2017-11-16', 'Sword', 'Beheaded', 'Kings Landing'),
(7, '2017-11-13', 'Poison', 'Boar wounds/poisoned', 'Kings Landing'),
(8, '2019-05-09', 'Poison', 'Poisoned', 'Kings Landing'),
(12, '2022-01-29', 'Poison', 'Poisoned', 'Highgarden'),
(15, '2019-06-15', 'Rope', 'Suffocating', 'Kings Landing'),
(18, '2020-04-01', 'Poison', 'Kissed with poison', 'Dornish seas'),
(24,'2022-11-26','Ensems','Nanya got more marks','The Crownlands'),
(17,'2022-11-26','Ensems','Nanya got more marks','The Crownlands');

INSERT INTO RULED_BY VALUES
('Kingdom of the North','Stark'),
('Kingdom of Mountain and Vale','Arryn'),
('Kingdom of the Isles and the Rivers','Greyjoy'),
('Kingdom of the Rock','Lannister'),
('Kingdom of the Reach','Tyrell'),
('Kingdom of the Stormlands','Targaryen'),
('The Crownlands','Baratheon'),
('Principality of Dorne','Martell');


INSERT INTO RIDE VALUES
('Drogon', 10),
('Drogon', 5),
('Drogon', 9),
('Rhaegal', 10),
('Viserion', 10),
('Viserion', 2),
('Rhaegal', 22),
('Seasmoke', 15),
('Syrax', 16),
('Syrax', 3),
('Balerion', 3),
('Dreamfyre', 13);

INSERT INTO DIE_BY VALUES
(1, 23),
(6, 9),
(6, 8),
(7, 9),
(8, 12),
(12, 20),
(15, 13),
(18, 16),
(24,14),
(6,14),
(1,10),
(8,10),
(17,14);

--
-- data dump complete
--
--