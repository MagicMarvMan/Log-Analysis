import psycopg2
import time
import os
import db

def clear_shell():
	os.system("clear")

conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()


print("Querying authors...")
authors = db.query("",cursor)
clear_shell()


print("Querying articles...")
articles = db.query("",cursor)
clear_shell()


print("Querying log...")
log = db.query("",cursor)
clear_shell()