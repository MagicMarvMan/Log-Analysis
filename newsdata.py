import psycopg2
import time
import os
import db

def clear_shell():
	os.system("clear")

conn = psycopg2.connect("dbname=news user=postgres password=postgres")
cursor = conn.cursor()


queries = {"articles":{"sql":"SELECT articles.title, count(*) AS views FROM articles INNER JOIN log ON log.path LIKE concat('%',articles.slug,'%') GROUP BY articles.title, log.path ORDER BY views DESC LIMIT 3","title":"What are the most popular articles?"}}


def execute_visual_query(name):
	print(" ")
	print(" ")
	print("==========================================")
	print(queries[name]["title"])
	print("==========================================")
	print(" ")
	for x in db.query(queries[name]["sql"],cursor):
		print(str(x[0]+" - "+x[1]))


clear_shell()

execute_visual_query("articles")