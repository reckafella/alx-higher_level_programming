# **0x0D. SQL - Introduction**
## **Topics**: SQL, MYSQL

## **Requirements**
### **General**
* Allowed editors: vi, vim, emacs
* All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT, WHERE…)
* A README.md file, at the root of the folder of the project, is mandatory
* The length of your files will be tested using wc

## **Tasks**:
0. List databases - a script that lists all databases of your MySQL server.

1. Create a database - a script that creates the database hbtn_0c_0 in your MySQL server.
	* If the database hbtn_0c_0 already exists, your script should not fail
	* You are not allowed to use the SELECT or SHOW statements

2. Delete a database - a script that deletes the database hbtn_0c_0 in your MySQL server.
	* If the database hbtn_0c_0 doesn’t exist, your script should not fail
	* You are not allowed to use the SELECT or SHOW statements

3. List tables - a script that lists all the tables of a database in your MySQL server.
	* The database name will be passed as argument of mysql command.

4. First table - a script that creates a table called first_table in the current database in your MySQL server.
  * first_table description:
    + id INT
    + name VARCHAR(256)
  * The database name will be passed as an argument of the mysql command
  * If the table first_table already exists, your script should not fail
  * You are not allowed to use the SELECT or SHOW statements

5. Full description - a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

  * The database name will be passed as an argument of the mysql command
  * You are not allowed to use the DESCRIBE or EXPLAIN statements
