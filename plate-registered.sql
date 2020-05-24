/*Trigger not working properly*/

/*CREATE TRIGGER capital
BEFORE INSERT
ON registered
FOR EACH ROW
BEGIN
   new.A := upper(:new.A);
   new.C := upper(:new.C);
END*/


CREATE TABLE registered(
    Person VARCHAR(50) PRIMARY KEY,
    A VARCHAR(2),
    B VARCHAR(2),
    C VARCHAR(2),
    D VARCHAR(4)
);

INSERT INTO registered (Person, A, B, C, D)VALUES('John','kl','58','g','100');
INSERT INTO registered (Person, A, B, C, D)VALUES('Smith','kl','27','g','2007');
INSERT INTO registered (Person, A, B, C, D)VALUES('Jacky','kl','19','c','3033');
INSERT INTO registered (Person, A, B, C, D)VALUES('Chan','kl','01','bq','5324');
INSERT INTO registered (Person, A, B, C, D)VALUES('Ramanan','kl','07','tc','168');
INSERT INTO registered (Person, A, B, C, D)VALUES('Raghavan','kl','49','e','7905');
INSERT INTO registered (Person, A, B, C, D)VALUES('Raghu','kl','38','f','5008');
INSERT INTO registered (Person, A, B, C, D)VALUES('Raghuvaran','kl','7','p','1065');
INSERT INTO registered (Person, A, B, C, D)VALUES('Lakshman','kl','31','e','0000');
INSERT INTO registered (Person, A, B, C, D)VALUES('Nicolas','kl','46','r','6125');
INSERT INTO registered (Person, A, B, C, D)VALUES('Brad','kl','05','aq','2255');
INSERT INTO registered (Person, A, B, C, D)VALUES('Rigu','kl','20','l','5147');
INSERT INTO registered (Person, A, B, C, D)VALUES('Bhaskaran','kl','22','n','5791');
INSERT INTO registered (Person, A, B, C, D)VALUES('Ravi','kl','54','a','2670');
INSERT INTO registered (Person, A, B, C, D)VALUES('Suku','kl','7','bm','9099');
INSERT INTO registered (Person, A, B, C, D)VALUES('Paul','kl','55','l','7373');
INSERT INTO registered (Person, A, B, C, D)VALUES('James','kl','01','b','055');
INSERT INTO registered (Person, A, B, C, D)VALUES('Gemarin','kl','05','ac','585');
INSERT INTO registered (Person, A, B, C, D)VALUES('Jeswin','kl','01','cb','5401');
INSERT INTO registered (Person, A, B, C, D)VALUES('Antony','kl','09','an','7779');
INSERT INTO registered (Person, A, B, C, D)VALUES('Joan','kl','58','l','7777');
INSERT INTO registered (Person, A, B, C, D)VALUES('Jain','kl','11','at','5500');
INSERT INTO registered (Person, A, B, C, D)VALUES('Rohan','kl','01','ay','69');
INSERT INTO registered (Person, A, B, C, D)VALUES('Rahul','kl','01','b','8686');
INSERT INTO registered (Person, A, B, C, D)VALUES('Akshay','kl','39','p','886');
INSERT INTO registered (Person, A, B, C, D)VALUES('Bibin','kl','01','bq','5320');
INSERT INTO registered (Person, A, B, C, D)VALUES('Jose','kl','06','n','8667');
INSERT INTO registered (Person, A, B, C, D)VALUES('Jerry','kl','26','d','999');
INSERT INTO registered (Person, A, B, C, D)VALUES('Tom','kl','46','d','1');
INSERT INTO registered (Person, A, B, C, D)VALUES('Ricky','kl','01','at','5555');
INSERT INTO registered (Person, A, B, C, D)VALUES('Johnny','kl','54','h','4444');