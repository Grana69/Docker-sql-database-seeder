from masterclass import MasterModel
import random

from faker import Faker

faker = Faker('en')

sqlTable = '''
        CREATE TABLE balances(
          id INT PRIMARY KEY AUTO_INCREMENT,
          amount DOUBLE(50,9) NOT NULL DEFAULT 0,
          id_user INT NOT NULL,
          createdAt TIMESTAMP,
          updatedAt TIMESTAMP
        );
        '''
sqlInsert = '''
            INSERT INTO balances (amount,  id_user)
            VALUES (%(amount)s,  %(id_user)s);
            '''
sqlRelation = ['''            
            ALTER TABLE balances
            ADD CONSTRAINT FK_user_balance_id FOREIGN KEY (id_user)
                REFERENCES users (id)
                ON DELETE CASCADE
            ; 
            ''']


class Balance(MasterModel):
    def __init__(self, conn, cursor, numberElements):
        self.data = []
        self.counter = 1
        for _ in range(numberElements):
            user_data = {
                'amount': 0,
                'id_user': self.counter
            }
            self.counter = self.counter+1
            self.data.append(user_data)
        MasterModel.__init__(self, conn, cursor, sqlTable,
                             sqlInsert, sqlRelation, "balances", self.data)
