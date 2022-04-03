# Task
# write a function to fetch data from sql table via api
from flask import Flask, request, jsonify
from API_SQL import getData,makeConn
from API_MONGO import MongoConn,make_collection,find_data

app = Flask(__name__)

@app.route('/postSql',methods=['GET','POST'])
def sqlData():
    """
    This function work with post as well get request method and authentite the user and password credentials,
    and then the data of the SQLITE database gets returned
    :return: json data of the students table
    """

    # POST reguest will work on sqlite database
    if (request.method == 'POST'):
        user = request.json['user']
        password = request.json['password']

        # Validating the user and password
        if user == "sunny" and password == "HappyCoding":

            # making connection with the database and getting data from the database
            makeConn()
            data = getData()

            return jsonify(str(data))
        else:
            return jsonify(str("user or password is not correct"))


@app.route('/getMongo',methods=['GET','POST'])
def mongoData():
    """
    This function takes public get requests and authenticate  it and provides with data to valid users and the data is
    returned from mongoDB database
    :return: json data
    """
    if (request.method == 'GET'):
        user = request.args.get('user')
        password = request.args.get('password')

    # Authenticating the user
    if user == "sunny" and password == "HappyCoding":

        ## make connection with database and fetch data
        MongoConn()
        make_collection()
        data = find_data()

        return jsonify(str(data))
    else:
        return jsonify(str("user or password is incorrect"))


if __name__ == '__main__':
    app.run(port=8000)
