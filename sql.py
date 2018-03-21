from flask import Flask
from flask import request
from flask import jsonify

from DbBusiness import DbBusiness

app = Flask(__name__)

dbBusiness = DbBusiness("Driver={SQL Server Native Client 11.0};"
                        "Server=yourip;"
                        "Database=yourdbname;"
                        "uid=yourusername;pwd=yourpassword")

@app.route('/')

@app.route('/AddCategory',  methods=['POST'])
def AddCategory():

    id=dbBusiness.addCategory()

    result = {
         'Id': id,
    }

    return jsonify({'result': result}),

@app.route('/AddRegion',  methods=['POST'])
def AddRegion():

    id = dbBusiness.addRegion()

    result = {
         'Id': id,
    }

    return jsonify({'result': result}),

@app.route('/AddSupplier',  methods=['POST'])
def AddSupplier():

    id = dbBusiness.addSupplier()

    result = {
         'Id': id,
    }

    return jsonify({'result': result}),

@app.route('/AddTerritory',  methods=['POST'])
def AddTerritory():

    id = dbBusiness.addTerritory(int(request.json['RegionId']))

    result = {
         'Id': id,
    }

    return jsonify({'result': result}),

@app.route('/AddEmployee',  methods=['POST'])
def AddEmployee():

    id = dbBusiness.addEmployee()

    result = {
         'Id': id,
    }

    return jsonify({'result': result}),

@app.route('/AddOrder',  methods=['POST'])
def AddOrder():

    id = dbBusiness.addOrder()

    result = {
         'Id': id,
    }

    return jsonify({'result': result}),

@app.route('/AddCustomer',  methods=['POST'])
def AddCustomer():

    id = dbBusiness.addCustomer(str(request.json['CustomerId']))

    result = {
         'Id': id,
    }

    return jsonify({'result': result}),

if __name__ == "__main__":
    app.run()