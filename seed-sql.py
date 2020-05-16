#!/usr/bin/env python3.6

#import connection
from connection import Connection

#import classes
from tb_user import User
from tb_role import Role
from tb_balance import Balance

# stablish connection
conn = Connection()
# number of users
total_users = 10

# Instancias
userClass = User(conn.connection, conn.cursor, total_users)
roleClass = Role(conn.connection, conn.cursor, total_users)
balanceClass = Balance(conn.connection, conn.cursor, total_users)


# Drop tables
userClass.drop_table()
roleClass.drop_table()
balanceClass.drop_table()


# Create tables
userClass.create_table()
roleClass.create_table()
balanceClass.create_table()

# Create Relations
userClass.create_relation()
balanceClass.create_relation()

# Insert Data
userClass.insertData()
roleClass.insertData()
balanceClass.insertData()


# Commit Changes
balanceClass.pushAndClose()
