from masterclass import MasterModel
import random
import time

from faker import Faker

POSSIBLE_STATES = ['ACTIVE', 'INACTIVE']
faker = Faker('en')

sqlTable = '''
        CREATE TABLE roles(
          id INT PRIMARY KEY AUTO_INCREMENT,
          code VARCHAR(50) NOT NULL UNIQUE,
          status VARCHAR(50) NOT NULL,
          createdAt TIMESTAMP,
          updatedAt TIMESTAMP
        );
        '''

sqlInsert = '''
            INSERT INTO roles (code,  status)
            VALUES (%(code)s,   %(status)s);
            '''
sqlRelation = [""]


class Role(MasterModel):
    def __init__(self, conn, cursor, numberElements):
        self.data = [{
            'code': "USER",
            'status': random.choice(POSSIBLE_STATES)
        },{
            'code': "ADMIN",
            'status': random.choice(POSSIBLE_STATES)
        }]
        MasterModel.__init__(self, conn, cursor, sqlTable,
                             sqlInsert, sqlRelation, "roles", self.data)
