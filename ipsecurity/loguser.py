import sqlite3
import json
from unicodedata import name
import requests
def ins_info(IP, HEADER, country):
    con = sqlite3.connect('user_info.sqlite')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Users_Info(IP varchar, country TEXT, HEADER varchar)')
    cur.execute('INSERT INTO Users_Info(IP,country,HEADER) VALUES(?, ?, ?)', (IP, country, HEADER))
    con.commit()
    cur.close
    print("Done")


def check():
    #GET IP INFO


check()