#!/usr/bin/python3
""" A script that lists all 'states' from the database 'hbtn_0e_0_usa' """

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cursor = db.cursor()

    cursor.execute('SELECT * FROM `states` ORDER BY `id` ASC')

    all_rows = cursor.fetchall()

    for row in all_rows:
        print(row)

    cursor.close()
    db.close()
