#Task
# write a function to fetch data from sql table via api
import sqlite3 as sql

# making connection with the database
def makeConn():
    try:
        global db, cur
        db = sql.connect('taskData.db')
        cur = db.cursor()
    except Exception as e:
        print('makeConn',e)

# Function will create table
def createTable():
    try:
        # columns name id,name,age,course
        cur.execute("CREATE TABLE students(id INT,name VARCHAR(30), age INT(5), course VARCHAR(30))")
    except Exception as e:
        print(e)

# Function will insert data inside the students table
def insertData(data):
    """
    This function takes argument of data = [(col1,col2...),(col1,....)]
    """
    try:
        # data is a list of tuple and tuple contains the values
        if type(data) == tuple or type(data) == list:
            for d in data:
                print(d)
                command = f"INSERT INTO students(id,name,age,course) values('{d[0]}','{d[1]}','{d[2]}','{d[3]}')"
                cur.execute(command)
                print(command)
    except Exception as e:
        print(e)
        db.rollback()
    else:
        db.commit()
        db.close()

def getData():
    """
    This Function extract information from the database and show it to console and also returns the data
    """
    try:
        # selecting all student from students table
        cur.execute("SELECT * FROM students")
    except Exception as e:
        print('getData',e)
    else:
        print("Students Information are as follow")
        data = cur.fetchall()
        for c in data:
            print(c)
        return data

data = [
    (1,'David Gilmore',23,'full stack developement'),
    (2,'Tommy Maguire',25,'machine learning'),
    (3,'Irfan Khan',27,'AI Ops'),
    (4, 'Vin Diesel', 33, 'Blockchain'),
    (5,'Tom Hanks',37,'Data Science')
]

## To create table uncomment the below line
#createTable()

# To insert data into database table uncomment the below line
#insertData(data)

# makes connection and fetch data
#makeConn()
#getData()