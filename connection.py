import mysql.connector
from mysql.connector import InterfaceError
import time


class Connection():
    def __init__(self):
        config = {
            'user': 'root',
            'password': 'changeit',
            'host': 'host.docker.internal', 
            'port': '3306',
            'database': 'database'
        }
        while not hasattr(self, 'connection'):
            try:
                self.connection = mysql.connector.connect(**config)
                self.cursor = self.connection.cursor()
            except InterfaceError:
                print("MySQL Container has not started yet. Sleep and retry...")
                time.sleep(2)