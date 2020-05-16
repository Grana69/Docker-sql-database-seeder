class MasterModel():
    def __init__(self, conn, cursor, sqlTable, sqlInsert, sqlRelations, tableName, data):
        self.connection = conn
        self.cursor = cursor
        self.sqlTable = sqlTable
        self.sqlInsert = sqlInsert
        self.sqlRelations = sqlRelations
        self.tableName = tableName
        self.data = data

    def seed(self):
        self.drop_table()
        self.create_table()
        self.create_relation()
        self.insertData()

    def pushAndClose(self):
        print('Pushing SQL data ' + self.tableName+'...')
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        print("Done")

    def insertData(self):
        print('Inserting data ' + self.tableName + '...')
        for single in self.data:
            self.cursor.execute(self.sqlInsert, single)

    def drop_table(self):
        print('Clearing old data ' + self.tableName + '...')
        self.cursor.execute('SET FOREIGN_KEY_CHECKS=OFF;')
        self.cursor.execute(' DROP TABLE IF EXISTS '+self.tableName+';')

    def create_table(self):
        print('Creating table ' + self.tableName + '...')
        self.cursor.execute(self.sqlTable)

    def create_relation(self):
        print('Inserting Relations ' + self.tableName + '...')
        for single in self.sqlRelations:
            self.cursor.execute(single)
