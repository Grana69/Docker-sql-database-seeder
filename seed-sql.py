#!/usr/bin/env python3.6

#import connection
from connection import Connection

#import classes
from tb_user import User
from tb_role import Role
from tb_balance import Balance
""" 
from classes import classes """

# stablish connection
conn = Connection()
# number of users
total_users = 10

# Array Class creation and append
classes = []
classes.append(User)
classes.append(Role)
classes.append(Balance)

# Tables
tables = []

# Instance creation
for a in classes:
    tables.append(a(conn.connection, conn.cursor, total_users))

# Drop tables
for a in tables:
    a.drop_table()

# Create tables
for a in tables:
    a.create_table()

# Create relations
for a in tables:
    a.create_relation()

# Insert Data
for a in tables:
    a.insertData()

tables[0].pushAndClose()
