from flask import Flask, redirect, render_template
import json
import sqlite3
import requests
import os 
app = Flask(__name__)
@app.route("/home")
def home():
   render_template("index.html")
   return check()



def check():
    rip = requests.get("http://ip-api.com/json/").text
    IP_data = json.loads(rip)
    IP = (IP_data['query'])
    IP_con = (IP_data['country'])
    
    return ins_info(IP, "TEST", IP_con) # Passing info (IP, HEADER, COUNTRY)

def ins_info(IP, HEADER, country):
    con = sqlite3.connect('user_info.sqlite') # connecting the database duh
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Users_Info(IP varchar, country TEXT, HEADER varchar)') # Creating the table if not exists (IP, country, HEADER)
    cur.execute('INSERT INTO Users_Info(IP,country,HEADER) VALUES(?, ?, ?)', (IP, country, HEADER)) # Inserting all of the Info gottan
    con.commit()
    cur.close
app.run()