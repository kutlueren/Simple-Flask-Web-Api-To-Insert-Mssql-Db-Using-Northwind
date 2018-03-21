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

    def addCustomer(self, customerId):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Customers VALUES (?,?,?,?,?,?,?,?,?,?,?)")
        Values = [customerId, u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test']

        self.__execute(SQLCommand, Values)

        return id

    def addRegion(self):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Region(RegionID,RegionDescription) VALUES (?,?)")
        Values = [id, u'test']
        self.__execute(SQLCommand, Values)
        return id

    def addSupplier(self):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Suppliers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)")
        Values = [id, u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test', u'test']
        self.__execute(SQLCommand, Values)
        return id

    def addTerritory(self, regionId):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Territories VALUES (?,?,?)")
        Values = [str(id), u'test', regionId]
        self.__execute(SQLCommand, Values)
        return id

    def addEmployee(self):
        id = self.__getNextId()

        SQLCommand = ("INSERT INTO Employees VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
        Values = [id, u'test', u'test', u'test', u'test', u'1948-12-08 00:00:00.000', u'1948-12-08 00:00:00.000',
                  u'test', u'test', u'test', u'test', u'test'
            , u'test', u'test', u'test', 2, u'test']
        self.__execute(SQLCommand, Values)
        return id

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
