#!/usr/bin/python3

"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], charset='utf8', port=3306)

    cursor = db.cursor()
    query = "SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM\
        `cities` INNER JOIN `states` ON `states`.`id` = `cities`.`state_id`"

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
