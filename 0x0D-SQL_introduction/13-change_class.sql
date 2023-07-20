-- A script that removes all records with a 'score <= 5' in the table 'second_table'
-- of the database 'hbtn_0c_0' in the MYSQL server.
-- The database name is passed as an argument to the `mysql` command

DELETE FROM `second_table`
WHERE `score` <= 5;
