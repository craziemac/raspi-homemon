
# Created: 2013-11-05
# Version: 1.0.0.0
# Author: Marcus Jonsson
# Description: Database object SENSOR

class DOSensor(object):
    """ Class representing database object SENSOR.  
    """

    def __init__(self):
        """ Constructor """
        #Property
        self.sens_ruid = None
        self.sens_item = None
        self.sens_desc = None
        self.sens_rcre = None
        self.sens_rcha = None
        self.sens_unit = None
        self.sens_prec = None
        self.sens_eid1 = None
        self.sens_type = None

    def add_row(self, cursor, row):
        """ Add row data from database to properties """
        for i in range(len(cursor.description)):
            if cursor.description[i][0] == "SENS_Ruid":
                self.sens_ruid = row[i]
            elif cursor.description[i][0] == "SENS_Item":
                self.sens_item = row[i]
            elif cursor.description[i][0] == "SENS_Desc":
                self.sens_desc = row[i]
            elif cursor.description[i][0] == "SENS_Rcre":
                self.sens_rcre = row[i]
            elif cursor.description[i][0] == "SENS_Rcha":
                self.sens_rcha = row[i]
            elif cursor.description[i][0] == "SENS_Unit":
                self.sens_unit = row[i]
            elif cursor.description[i][0] == "SENS_Prec":
                self.sens_prec = row[i]
            elif cursor.description[i][0] == "SENS_Eid1":
                self.sens_eid1 = row[i]
            elif cursor.description[i][0] == "SENS_Type":
                self.sens_type = row[i]
