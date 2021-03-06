#!/usr/bin/env python3

import psycopg2
import time
import os
import db
import json


def clear_shell():
    os.system("clear")

config = json.loads(open("config.json", "r").read())

conn = psycopg2.connect(
    "dbname="+config["database"] +
    " user="+config["username"] +
    " password="+config["password"])
cursor = conn.cursor()


queries = {
    "articles": {
        "sql": "SELECT articles.title, count(*) AS views FROM articles"
        " INNER JOIN log ON log.path LIKE concat('%',articles.slug,'%')"
        " WHERE log.status='200 OK'"
        " GROUP BY articles.title, log.path"
        " ORDER BY views DESC LIMIT 3",
        "title": "1. What are the most popular three articles of all time?"
    },

    "authors": {
        "sql": "SELECT authors.name, count(*) AS views FROM articles"
        " INNER JOIN authors ON articles.author = authors.id"
        " INNER JOIN log ON log.path LIKE concat('%',articles.slug,'%')"
        " WHERE log.status='200 OK' GROUP BY authors.name "
        "ORDER BY views DESC",
        "title": "2. Who are the most popular article authors of all time?"
    },

    "errors": {
        "sql": "SELECT day, perc FROM"
        " (SELECT day, round((sum(requests)/(SELECT count(*)"
        " FROM log WHERE substring(cast(log.time AS text),0,11)"
        " = day)*100),2) AS perc FROM (SELECT substring"
        "(cast(log.time AS text),0,11) AS day, count(*) AS requests"
        " FROM log WHERE status != '200 OK' GROUP BY day) AS lp"
        " GROUP BY day ORDER BY perc DESC) AS final WHERE perc >= 1",
        "title": "3. On which days did more than 1% of "
        "requests lead to errors?"
    }

}

clear_shell()


def get_value_with_suffix(name,val):
    if(name == "errors"):
        return(str(val)+"%")
    elif(name == "articles"):
        return(str(val)+" views")
    elif(name == "authors"):
        return(str(val)+" views")
    else:
        return(str(val))

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
        print(str(x[0])+" - "+str(get_value_with_suffix(name,x[1])))
    print(" ")


execute_visual_query("articles")
execute_visual_query("authors")
execute_visual_query("errors")
