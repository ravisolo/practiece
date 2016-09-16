#! /usr/bin/python 

import MySQLdb

db=MySQLdb.connect(host="localhost",user="root",passwd="rootroot",db="solo")



def create_database(cur):
	query="create database %s   ",%newdb;
	print query
	cur.execute(query)
	data=cur.fetchall();
	print data
	cur.close()

	
create_database(cur)
