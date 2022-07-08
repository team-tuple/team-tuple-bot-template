import mysql.connector
from bot.config import database


class dbconnect:
    def __init__(self):
    
    #dbconnect
    self.MYSQLHost = database['host']
    self.MYSQLLogin = database['user']
    self.