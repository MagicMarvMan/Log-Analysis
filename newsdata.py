import psycopg2
import time
import os

def clear_shell():
	os.system("clear")

conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()


print("Querying authors...")
cur.execute("")
authors = cur.fetchall()
clear_shell()


print("Querying articles...")
cur.execute("")
articles = cur.fetchall()
clear_shell()


print("Querying log...")
cur.execute("")
log = cur.fetchall()
clear_shell()