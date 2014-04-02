
# Created: 2013-11-01
# Version: 1.0.0.0
# Author: Marcus Jonsson
# Description: Contains class to handle mysql database connection

import mysql.connector
from mysql.connector import errorcode

class DatabaseConn(object):
    """ Contains connection details to a mysql database
    and handles the connection to the database.  
    """

    def __init__(self):
        """ Constructor """
        self.cnxdetails = DatabaseConn.ConnectionDetails()
        self.connection = None
        self.cursor = None

    def connect(self):
        """ Opens a connection to a mysql database
        with the connection details specified in subclass ConnectionDetails.  
        """
        try:
            if self.cnxdetails._user is not None and self.cnxdetails._password is not None and self.cnxdetails._host is not None and self.cnxdetails._name is not None:
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
        except Exception as exc:
            print(exc)

    def execute(self, query, data = None):
        """ Executes query on existing mysql connection
        and returns the cursor.  
        """
        try:
            if self.connection is not None:
                self.cursor.execute(query, data)
                return self.cursor
            else:
                raise Exception("Error: No connection open")
        except Exception as exc:
            print(exc)

    def commit(self):
        """ Commits existing connection.  
        """
        try:
            if self.connection is not None and self.cursor is not None:
                self.connection.commit()
            else:
                raise Exception("Error: No connection or cursor open")
        except Exception as exc:
            print(exc)

    def disconnect(self):
        """ Disconnects existing connection.  
        """
        try:
            if self.connection is not None:
                self.connection.close()
            else:
                raise Exception("Error: No active connection available")
        except Exception as exc:
            print(exc)
        
    class ConnectionDetails(object):
        """ Contains properties with connection details
        for connecting to mysql database.  
        """

        def __init__(self):
            """ Constructor """
            # Property
            self._user = None
            self._password = None
            self._host = None
            self._name = None

        @property
        def user(self):
            """ The username for the database connection.  """
            return self._user
        @user.setter
        def user(self, value):
            self._user = value
        @user.deleter
        def user(self):
            del self._user

        @property
        def password(self):
            """ The password for the database connection.  """
            return self._password
        @password.setter
        def password(self, value):
            self._password = value
        @password.deleter
        def password(self):
            del self._password

        @property
        def host(self):
            """ The host for the database connection.  """
            return self._host
        @host.setter
        def host(self, value):
            self._host = value
        @host.deleter
        def host(self):
            del self._host

        @property
        def name(self):
            """ The name for the database connection.  """
            return self._name
        @name.setter
        def name(self, value):
            self._name = value
        @name.deleter
        def name(self):
            del self._name
