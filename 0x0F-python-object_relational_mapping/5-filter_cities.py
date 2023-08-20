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

    cursor.execute("SELECT `cities`.`name` FROM `cities` WHERE `state_id` =\
                   (SELECT `states`.`id` FROM `states` WHERE `states`.`name`\
                   = %s) ORDER BY `cities`.`id` ASC", (argv[4],))

    results = cursor.fetchall()

    for i in range(len(results)):
        if i < len(results) - 1:
            print(results[i][0], end=", ")
        else:
            print(results[i][0])

    cursor.close()
    db.close()
