'''
Created on 1 nov 2013

@author: Marcus Jonsson
'''
import mysql.connector
from mysql.connector import errorcode

class Database(object):
    '''
    classdocs
    '''

    ''' Constructor '''
    def __init__(self):
        self.cnxdetails = Database.ConnectionDetails()
        self.connection = None
        self.cursor = None

    ''' Method '''
    def Connect(self):
        try:
            if self.cnxdetails._user != None and self.cnxdetails._password != None and self.cnxdetails._host != None and self.cnxdetails._name != None:
                self.connection = mysql.connector.connect(user=self.cnxdetails._user, password=self.cnxdetails._password, host=self.cnxdetails._host, database=self.cnxdetails._name)
                self.cursor = self.connection.cursor() 
            else:
                raise Exception("Error: Connection details are incorrect")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: Access denied with supplied username and password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Error: Database does not exists")
            else:
                print(err)
        except Exception as ex:
            print(ex)

    def Execute(self, query, data = None):
        try:
            if self.connection != None:
                self.cursor.execute(query, data)
                return self.cursor
            else:
                raise Exception("Error: No connection open")
        except Exception as ex:
            print(ex)

    def Commit(self):
        try:
            if self.connection != None and self.cursor != None:
                self.connection.commit()
            else:
                raise Exception("Error: No connection or cursor open")
        except Exception as ex:
            print(ex)

    def Disconnect(self):
        try:
            if self.connection != None:
                self.connection.close()
            else:
                raise Exception("Error: No active connection available")
        except Exception as ex:
            print(ex)
        
    ''' Property '''
    class ConnectionDetails(object):
        ''' Constructor '''
        def __init__(self):
            # Property
            self._user = None
            self._password = None
            self._host = None
            self._name = None

        @property
        def user(self):
            ''' The username for the database connection '''
            return self._user
        @user.setter
        def user(self, value):
            self._user = value
        @user.deleter
        def user(self):
            del self._user

        @property
        def password(self):
            ''' The password for the database connection '''
            return self._password
        @password.setter
        def password(self, value):
            self._password = value
        @password.deleter
        def password(self):
            del self._password

        @property
        def host(self):
            ''' The host for the database connection '''
            return self._host
        @host.setter
        def host(self, value):
            self._host = value
        @host.deleter
        def host(self):
            del self._host

        @property
        def name(self):
            ''' The name for the database connection '''
            return self._name
        @name.setter
        def name(self, value):
            self._name = value
        @name.deleter
        def name(self):
            del self._name