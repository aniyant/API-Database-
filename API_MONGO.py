#Task2
# write a function to fetch data from mongodb table via api

import pymongo

# Making connection with mongodb server and creating database "api_tast_db"
def MongoConn():
    """
    This function will connect with mongodb server and create database and declare global varaibles
    :return:
    """
    try:
        global mongo,db
        mongo = pymongo.MongoClient("mongodb+srv://sunny:Heartbeat@cluster0.d6rrq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = mongo['api_task_db']
    except Exception as e:
        print("makeConn Error - ",e)

def make_collection():
    """
    This function creates or connects with collection and declare a global students variable
    :return:
    """
    try:
        global students
        students = db['students']
    except Exception as e:
        print("Database - ",e)

def insert_data(data):
    """
    This function takes args of data = [(data1,data2,...),(data1,...)] and insert data one by one into the database
    :param data:
    :return:
    """
    try:
        # takes data and loop with each tuple
        if type(data) == tuple or type(data) == list:
            for d in data:
                d = {
                    "_id" : d[0],
                    "name" : str(d[1]),
                    "age" : d[2],
                    "course" : d[3]
                }

                # calling students collection method insert one to insert data one by one into collection
                students.insert_one(d)
    except Exception as e:
        print("insert_data - ",e)

def find_data():
    """
    This function retreive all the data from the student collection and returns it
    :return:
    """
    dataobj = students.find()
    data = []
    for d in dataobj:
        print(d)
        data.append(d)
    return data


data = [
        (1, 'David Gilmore', 23, 'full stack developement'),
        (2, 'Tommy Maguire', 25, 'machine learning'),
        (3, 'Irfan Khan', 27, 'AI Ops'),
        (4, 'Vin Diesel', 33, 'Blockchain'),
        (5, 'Tom Hanks', 37, 'Data Science')
]

# making connection
#makeConn()
# selection or creating collection
#make_collection()
# to insert data uncomment the below code
#insert_data(data)

#find data
#find_data()