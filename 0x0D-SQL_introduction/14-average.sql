-- a script that computes the average of all records in the table `second_table` of the database `hbtn_0c_0`
-- in the MYSQL server.

-- result column should be average
-- database name will be passed as an argument of the `mysql` command

SELECT AVG(`score`) as `average`
FROM `second_table`;
