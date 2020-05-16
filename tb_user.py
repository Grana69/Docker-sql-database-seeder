from masterclass import MasterModel
import random

from faker import Faker

POSSIBLE_STATES = ['ACTIVE', 'INACTIVE']
faker = Faker('en')

sqlTable = '''
        CREATE TABLE users(
          id INT PRIMARY KEY AUTO_INCREMENT,
          nickname VARCHAR(50) NOT NULL UNIQUE,
          password VARCHAR(50) NOT NULL,
          active VARCHAR(50) NOT NULL,
          id_role INT,
          createdAt TIMESTAMP,
          updatedAt TIMESTAMP
        );
        '''
sqlInsert = '''
            INSERT INTO users (nickname, password, active,  id_role)
            VALUES (%(nickname)s,  %(password)s, %(active)s, %(id_role)s);
            '''
sqlRelation = ['''            
            ALTER TABLE users
            ADD CONSTRAINT FK_role_user_id FOREIGN KEY (id_role)
                REFERENCES roles (id)
                ON DELETE CASCADE
            ; 
            ''']


class User(MasterModel):
    def __init__(self, conn, cursor, numberElements):
        self.data = []
        for _ in range(numberElements):
            user_data = {
                'nickname': faker.name(),
                'password': faker.date_time(),
                'active': random.choice(POSSIBLE_STATES),
                'id_role' : 1
            }
            self.data.append(user_data)
        MasterModel.__init__(self, conn, cursor, sqlTable,
                             sqlInsert, sqlRelation, "users", self.data)
