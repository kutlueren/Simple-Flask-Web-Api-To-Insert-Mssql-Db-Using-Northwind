import pyodbc

class DbBusiness(object):

    def __init__(self, connectionString):
        self.connectionString = connectionString

    def __getNextId(self):
        cnxn = pyodbc.connect(self.connectionString)
        cursor = cnxn.cursor()
        id = 0
        cursor.execute("SELECT (NEXT VALUE FOR DBO.CT_SQ_PkAll) AS SequenceValue")
        for row in cursor.fetchone():
            id = row

        cnxn.commit()

        cnxn.close()
        return id

    def __execute(self, SQLCommand, Values):
        cnxn = pyodbc.connect(self.connectionString)
        cursor = cnxn.cursor()

        cursor.execute(SQLCommand, Values)

        cnxn.commit()

        cnxn.close()


    def addCategory(self):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Categories(CategoryID,CategoryName,Description) VALUES (?,?,?)")
        Values = [id, u'test', u'test']

        self.__execute(SQLCommand, Values)

        return id

    def updateCategory(self, categoryId):
        SQLCommand = "UPDATE Categories SET CategoryName = ?, Description = ? Where CategoryID = ?"
        Values = [u'testUpdate', u'testUpdate', categoryId]
        self.__execute(SQLCommand, Values )

    def deleteCategory(self, categoryId):
        SQLCommand = ("DELETE FROM Categories Where CategoryID = ? ")
        Values = [categoryId]
        self.__execute(SQLCommand, Values)

    def addCustomer(self, customerId):
        SQLCommand = ("INSERT INTO Customers VALUES (?,?,?,?,?,?,?,?,?,?,?)")
        Values = [customerId, u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test']

        self.__execute(SQLCommand, Values)

    def updateCustomer(self, customerId):

        SQLCommand = ("UPDATE Customers SET CompanyName = ?, ContactName = ? WHERE CustomerID = ?")
        Values = [ u'testUpdate', u'testUpdate', customerId]

        self.__execute(SQLCommand, Values)

    def deleteCustomer(self, customerId):

        SQLCommand = ("DELETE FROM Customers Where CustomerID = ? ")
        Values = [customerId]

        self.__execute(SQLCommand, Values)

    def addRegion(self):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Region (RegionID,RegionDescription) VALUES (?,?)")
        Values = [id, u'test']
        self.__execute(SQLCommand, Values)
        return id

    def updateRegion(self,regionId):

        SQLCommand = ("UPDATE Region SET RegionDescription = ? WHERE RegionID = ?")
        Values = [u'testUpdate', regionId]

        self.__execute(SQLCommand, Values)

    def deleteRegion(self,regionId):

        SQLCommand = ("DELETE FROM Region Where RegionID = ? ")
        Values = [regionId]
        self.__execute(SQLCommand, Values)

    def addSupplier(self):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Suppliers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)")
        Values = [id, u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test']
        self.__execute(SQLCommand, Values)
        return id

    def updateSupplier(self,supplierId):
        SQLCommand = ("UPDATE Suppliers SET CompanyName = ?, ContactName= ?  WHERE SupplierID = ?")
        Values = [u'testUpdate',u'testUpdate', supplierId]

        self.__execute(SQLCommand, Values)

    def deleteSupplier(self,supplierId):

        SQLCommand = ("DELETE FROM Suppliers Where SupplierID = ? ")
        Values = [supplierId]
        self.__execute(SQLCommand, Values)

    def addTerritory(self, regionId):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Territories VALUES (?,?,?)")
        Values = [str(id), u'test', regionId]
        self.__execute(SQLCommand, Values)
        return id

    def updateTerritory(self, territoryId):

        SQLCommand = ("UPDATE Territories SET TerritoryDescription = ? WHERE TerritoryID = ?")
        Values = [u'testUpdate',  str(territoryId)]
        self.__execute(SQLCommand, Values)

    def deleteTerritory(self, territoryId):

        SQLCommand = ("DELETE FROM Territories WHERE TerritoryID = ?")
        Values = [str(territoryId)]
        self.__execute(SQLCommand, Values)

    def addEmployee(self):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Employees VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
        Values = [id, u'test', u'test', u'test', u'test', u'1948-12-08 00:00:00.000', u'1948-12-08 00:00:00.000',
                  u'test', u'test', u'test', u'test', u'test'
            , u'test', u'test', u'test', 2, u'test']
        self.__execute(SQLCommand, Values)
        return id

    def updateEmployee(self, employeeId):

        SQLCommand = ("UPDATE Employees SET LastName = ?, FirstName = ? WHERE EmployeeID = ?")
        Values = [u'testUpdate', u'testUpdate',  employeeId]
        self.__execute(SQLCommand, Values)

    def deleteEmployee(self, employeeId):

        SQLCommand = ("DELETE FROM Employees WHERE EmployeeID = ?")
        Values = [employeeId]
        self.__execute(SQLCommand, Values)

    def addOrder(self):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Orders ([OrderID] ,[EmployeeID]      ,[OrderDate]      ,[RequiredDate]      ,[ShippedDate]      ,[ShipVia]     ,[Freight]      ,[ShipName]      ,[ShipAddress]      ,[ShipCity]      ,[ShipRegion]      ,[ShipPostalCode]     ,[ShipCountry])  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)")
        Values = [id,  1, u'2018-12-08 00:00:00.000', u'2018-12-08 00:00:00.000', u'2018-12-08 00:00:00.000',
                  3, 0, u'test', u'test', u'test', u'test', u'test', u'test']
        self.__execute(SQLCommand, Values)

        SQLCommand = ("INSERT INTO [Order Details] VALUES (?,?,?,?,?)")
        Values = [id, 1,1,1,0]
        self.__execute(SQLCommand, Values)

        return id

    def updateOrder(self, orderId):

        SQLCommand = ("UPDATE Orders SET ShipName = ?, ShipAddress = ? WHERE OrderID = ?")
        Values = [u'testUpdate', u'testUpdate',  orderId]
        self.__execute(SQLCommand, Values)

    def deleteOrder(self, orderId):

        SQLCommand = ("DELETE FROM [Order Details] WHERE OrderID = ?")
        Values = [orderId]
        self.__execute(SQLCommand, Values)

        SQLCommand = ("DELETE FROM Orders WHERE OrderID = ?")
        Values = [orderId]
        self.__execute(SQLCommand, Values)