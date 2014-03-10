'''
Created on 5 nov 2013

@author: Marcus Jonsson
'''

class DOSensor(object):
    '''
    classdocs
    '''

    ''' Constructor '''
    def __init__(self):
        #Property
        self.SENS_Ruid = None
        self.SENS_Item = None
        self.SENS_Desc = None
        self.SENS_Rcre = None
        self.SENS_Rcha = None
        self.SENS_Unit = None
        self.SENS_Prec = None
        self.SENS_Eid1 = None

    ''' Method '''
    def RowToDO(self, cursor, row):
        for i in range(len(cursor.description)):
            if cursor.description[i][0] == "SENS_Ruid":
                self.SENS_Ruid = row[i]
            elif cursor.description[i][0] == "SENS_Item":
                self.SENS_Item = row[i]
            elif cursor.description[i][0] == "SENS_Desc":
                self.SENS_Desc = row[i]
            elif cursor.description[i][0] == "SENS_Rcre":
                self.SENS_Rcre = row[i]
            elif cursor.description[i][0] == "SENS_Rcha":
                self.SENS_Rcha = row[i]
            elif cursor.description[i][0] == "SENS_Unit":
                self.SENS_Unit = row[i]
            elif cursor.description[i][0] == "SENS_Prec":
                self.SENS_Prec = row[i]
            elif cursor.description[i][0] == "SENS_Eid1":
                self.SENS_Eid1 = row[i]
