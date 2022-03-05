CREATE TABLE Trans (
    id int,
    TransDate text,
    PlaceName varchar(255),
    Amount decimal(65,2)
);

insert into Trans values (1, '2022-01-05', "Esso", 30.00);
insert into Trans values (2, '2022-01-06', "Elixor", 60.50);
insert into Trans values (3, '2022-02-10', "McDonald's", 32.64);
insert into Trans values (4, '2022-03-02', "PetroCanada", 30.00);