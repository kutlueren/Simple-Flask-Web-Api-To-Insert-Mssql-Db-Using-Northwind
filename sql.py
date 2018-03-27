from configparser import ConfigParser
from flask import Flask
from flask import request
from flask import jsonify
from flask_injector import FlaskInjector
from injector import singleton, inject
from DbBusiness import DbBusiness

app = Flask(__name__)


@app.route('/Index',  methods=['GET'])
def Index():
    cfg = ConfigParser()
    cfg.read("config.ini")
    str = cfg.get('Settings', 'AppName')

    return str

@app.route('/AddCategory',  methods=['POST'])
@inject
def AddCategory(dbBusiness:DbBusiness):

    id=dbBusiness.addCategory()


    result = {
         'Id': id,
    }

    return jsonify({'result': result})

@app.route('/UpdateCategory',  methods=['POST'])
@inject
def UpdateCategory(dbBusiness:DbBusiness):

    dbBusiness.updateCategory(request.json['CategoryId'])


    result = {
         'Message': 'Success',
    }

    return jsonify({'result': result}),

@app.route('/DeleteCategory',  methods=['POST'])
@inject
def DeleteCategory(dbBusiness:DbBusiness):

    id=dbBusiness.deleteCategory(request.json['CategoryId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/AddRegion',  methods=['POST'])
@inject
def AddRegion(dbBusiness:DbBusiness):

    id = dbBusiness.addRegion()

    result = {
         'Id': id,
    }

    return jsonify({'result': result})

@app.route('/UpdateRegion',  methods=['POST'])
@inject
def UpdateRegion(dbBusiness:DbBusiness):

    dbBusiness.updateRegion(request.json['RegionId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})


@app.route('/DeleteRegion',  methods=['POST'])
@inject
def DeleteRegion(dbBusiness:DbBusiness):

    dbBusiness.deleteRegion(request.json['RegionId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/AddCustomer',  methods=['POST'])
@inject
def AddCustomer(dbBusiness:DbBusiness):

    dbBusiness.addCustomer(str(request.json['CustomerId']))

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/UpdateCustomer',  methods=['POST'])
def UpdateCustomer(dbBusiness:DbBusiness):

    dbBusiness.updateCustomer(request.json['CustomerId'])


    result = {
         'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/DeleteCustomer',  methods=['POST'])
def DeleteCustomer(dbBusiness:DbBusiness):

    dbBusiness.deleteCustomer(request.json['CustomerId'])


    result = {
         'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/AddSupplier',  methods=['POST'])
@inject
def AddSupplier(dbBusiness:DbBusiness):

    id = dbBusiness.addSupplier()

    result = {
         'Id': id,
    }

    return jsonify({'result': result}),

@app.route('/UpdateSupplier',  methods=['POST'])
@inject
def UpdateSupplier(dbBusiness:DbBusiness):

    dbBusiness.updateSupplier(request.json['SupplierId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/DeleteSupplier',  methods=['POST'])
@inject
def DeleteSupplier(dbBusiness:DbBusiness):

    dbBusiness.deleteSupplier(request.json['SupplierId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/AddTerritory',  methods=['POST'])
@inject
def AddTerritory(dbBusiness:DbBusiness):

    id = dbBusiness.addTerritory(int(request.json['RegionId']))

    result = {
         'Id': id,
    }

    return jsonify({'result': result})

@app.route('/UpdateTerritory',  methods=['POST'])
@inject
def UpdateTerritory(dbBusiness:DbBusiness):

    dbBusiness.updateTerritory(request.json['TerritoryId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/DeleteTerritory',  methods=['POST'])
@inject
def DeleteTerritory(dbBusiness:DbBusiness):

    dbBusiness.deleteTerritory(request.json['TerritoryId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/AddEmployee',  methods=['POST'])
@inject
def AddEmployee(dbBusiness:DbBusiness):

    id = dbBusiness.addEmployee()

    result = {
         'Id': id,
    }

    return jsonify({'result': result})

@app.route('/UpdateEmployee',  methods=['POST'])
@inject
def UpdateEmployee(dbBusiness:DbBusiness):

    dbBusiness.updateEmployee(request.json['EmployeeId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/DeleteEmployee',  methods=['POST'])
@inject
def DeleteEmployee(dbBusiness:DbBusiness):

    dbBusiness.deleteEmployee(request.json['EmployeeId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/AddOrder',  methods=['POST'])
@inject
def AddOrder(dbBusiness:DbBusiness):

    id = dbBusiness.addOrder()


    result = {
         'Id': id,
    }

    return jsonify({'result': result})


@app.route('/UpdateOrder',  methods=['POST'])
@inject
def UpdateOrder(dbBusiness:DbBusiness):

    dbBusiness.updateOrder(request.json['OrderId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

@app.route('/DeleteOrder',  methods=['POST'])
@inject
def DeleteOrder(dbBusiness:DbBusiness):

    dbBusiness.deleteOrder(request.json['OrderId'])

    result = {
        'Message': 'Success',
    }

    return jsonify({'result': result})

def configure(binder):
    cfg=ConfigParser()
    cfg.read("config.ini")
    str = cfg.get('Settings','ConnectionString')

    binder.bind(DbBusiness, to= DbBusiness(str), scope=request)

FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
    app.run()