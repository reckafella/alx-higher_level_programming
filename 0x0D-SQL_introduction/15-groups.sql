-- a script that lists the number of records with the same score in the table `second_table` of the database
-- `hbtn_0c_0` in the MYSQL server.

-- The result should display:
    -- the `score`
    -- the number of records for this `score` with the label `number`
-- the list should be sorted by the number of records (desc)
-- database name passed as an argument of the `mysql` command.

SELECT `score`, COUNT(`score`) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
