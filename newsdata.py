import psycopg2
import time
import os
import db
import json


def clear_shell():
    os.system("clear")

config = json.loads(open("config.json", "r").read())

conn = psycopg2.connect(
    "dbname="+config["database"]+" user="+config["username"]+" password="+config["password"])
cursor = conn.cursor()


queries = {
	"articles": {
    	"sql": "SELECT articles.title, count(*) AS views FROM articles INNER JOIN log ON log.path LIKE concat('%',articles.slug,'%') GROUP BY articles.title, log.path ORDER BY views DESC LIMIT 3", 
    	"title": "What are the most popular articles?"
    },

    "authors": {
    	"sql": "SELECT authors.name, count(*) AS views FROM articles INNER JOIN authors ON articles.author = authors.id INNER JOIN log ON log.path LIKE concat('%',articles.slug,'%') GROUP BY authors.name ORDER BY views DESC",
    	"title": "Who are the most popular articles authors of all time?"
    },

}

clear_shell()


def execute_visual_query(name):
    print("Loading "+str(name)+"...")
    que = db.query(queries[name]["sql"], cursor)
    print(" ")
    print(" ")
    print("==========================================")
    print(queries[name]["title"])
    print("==========================================")
    print(" ")
    for x in que:
        print(str(x[0])+" - "+str(x[1]))
    print(" ")


execute_visual_query("articles")
execute_visual_query("authors")
