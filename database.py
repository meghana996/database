import mysql.connector
import sys
import getopt
import datetime

global conn,cursor;

conn=mysql.connector.connect(host="localhost", user="root", password="root")

def connection():
	if conn.is_connected():
		return True
	else:
		return False

def create_database():
	if connection():
		mycursor=conn.cursor()
		mycursor.execute("CREATE DATABASE reg_181040005")
		print("Database is created sucessfully")
	else:
		print("Couldn't connect to mysql server")

def create_table():
	db_conn=mysql.connector.connect(host="localhost",db="reg_181040005",user="root", password="root")
	if db_conn.is_connected():
		mycursor=db_conn.cursor()
		try:
			mycursor.execute("CREATE TABLE reg_no(id INT(20) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), dob DATE)")
			print("Table reg_no is created sucessfully\n")
		except:
			print("table is already created")
	

def insert_values():
	db_conn=mysql.connector.connect(host="localhost",db="reg_181040005",user="root",password="root")
	if db_conn.is_connected():
		mycursor= db_conn.cursor()

		query = "INSERT INTO reg_no(id, firstname, lastname, dob) VALUES (%s,%s,%s,%s) "
		id = input("Enter id\n")
		firstname = input("Enter first name\n")
		lastname = input("Enter last name\n")
		dob=input("Enter date of birth (yyyy/mm/dd)\n")
		value=(id,firstname,lastname,dob)
		mycursor.execute(query,value)
		db_conn.commit()
		print("sucessfully inserted")

		if not ValidDate(dob):
			print("Incorrect format.Enter in yyyy/mm/dd format ")
			sys.exit()
	db_conn.close()


def ValidDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
        
    except ValueError:
        return False


def alter_table():
	db_conn=mysql.connector.connect(host="localhost",db="reg_181040005",user="root",password="root")
	if db_conn.is_connected():
		mycursor= db_conn.cursor()

		column=input("Enter column name")
		query = "ALTER TABLE reg_no add %s VARCHAR(255)" %(column)
		mycursor.execute(query)
		db_conn.commit
		print("sucessfully added the column")

	db_conn.close()

def display_values():
	db_conn=mysql.connector.connect(host="localhost",db="reg_181040005",user="root",password="root")
	if db_conn.is_connected():
		mycursor= db_conn.cursor()

		query="SELECT * FROM reg_no"

		mycursor.execute(query)
		result=mycursor.fetchall()
		for x in result:
			print(x)
		
	db_conn.close()


def truncate_table():
	db_conn=mysql.connector.connect(host="localhost",db="reg_181040005",user="root",password="root")
	if db_conn.is_connected():
		mycursor= db_conn.cursor()

		query = "DROP TABLE reg_no"
		mycursor.execute(query)
		db_conn.commit()
		print("Table is sucessfully dropped")
		
	db_conn.close()


def main():

	while True:
		print("Enter your choice:\n")
		choice = input("Enter the option :\t")
		if choice=='1':
			create_database()
		if choice=='2':
			create_table()
		if choice=='3':
			insert_values()
		if choice=='4':
			display_values()
		if choice == '5':
			alter_table()
		if choice == '6':
			truncate_table()
		if choice == 'q':
			sys.exit()

if __name__ == '__main__':
	main()