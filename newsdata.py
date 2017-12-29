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
articles = db.query("SELECT articles.title, count(*) AS views FROM articles INNER JOIN log ON log.path LIKE concat('%',articles.slug,'%') GROUP BY articles.title, log.path ORDER BY views DESC LIMIT 3",cursor)
clear_shell()


print("Querying log...")
log = db.query("",cursor)
clear_shell()

def print_query(query):
	for x in query:
		print(x[0])

clear_shell()

print_query(articles)