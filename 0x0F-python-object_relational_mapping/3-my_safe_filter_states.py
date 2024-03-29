#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the `states`
table of `hbtn_0e_0_usa` where `name` matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    match = argv[4]
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute('SELECT * FROM `states`\
                   WHERE `states`.`name` = %s', (match,))

    query_results = cursor.fetchall()

    for row in query_results:
        print(row)

    cursor.close()
    db.close()
