-- a script that lists all the tables of a database in your MySQL server.
-- The database name will be passed as argument of mysql command

SET @dbname = '%s'

SET @sql = CONCAT('SELECT table_name FROM information_schema.tables WHERE table_schema = "', @dbname, '";');

-- Execute Prepared Statements
PREPARE statement FROM @sql;
EXECUTE statement;
DEALLOCATE PREPARE statement;
