"""

Database helper functions for newsdata

"""

import psycopg2

def query(sql,cur):
	cur.execute(sql)
	return(cur.fetchall)
