-- a script that creates the database hbtn_0c_0 in your MySQL server.
-- If the database hbtn_0c_0 already exists, your script should not fail
-- You are not allowed to use the SELECT or SHOW statements

IF DB_ID('hbtn_0c_0') IS NULL
BEGIN
	CREATE DATABASE hbtn_0c_0;
END
