#!/usr/bin/env python3

"""

Database helper functions for newsdata

"""

import psycopg2


def query(sql, cur):
    if(sql == ""):
        return []
    else:
        cur.execute(sql)
        return(cur.fetchall())
