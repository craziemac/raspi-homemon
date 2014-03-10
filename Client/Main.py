'''
Created on 31 okt 2013

@author: Marcus
'''
import sys,os
sys.path.append(os.path.realpath('..'))

from Configuration import Configuration
from Database import Database
from Database import DOSensor
from Hardware import SHT1x
from time import sleep

try:
    #------------------------------------------------------------------------------ 
    # Read configuration file
    config = Configuration("Config.xml")
    config.LoadConfig()
    
    #------------------------------------------------------------------------------ 
    # Configure database connection
    db = Database.Database()
    db.cnxdetails.user = config.database.attrib["User"]
    db.cnxdetails.password = config.database.attrib["Password"]
    db.cnxdetails.host = config.database.attrib["Host"]
    db.cnxdetails.name = config.database.attrib["Name"]
    
    # Fetch data for configured sensors
    if db.connection == None:
        db.Connect()

    sensors = []
    for cnfsensor in config.sensors:
        query = "SELECT * FROM SENSOR WHERE SENS_Item={0} LIMIT 1".format(cnfsensor.attrib["Item"])
        cur = db.Execute(query)
        row = cur.fetchone()
        newSensor = DOSensor.DOSensor()
        newSensor.RowToDO(cur, row)
        sensors.append(newSensor)
    
    while True:
        SHT15Read = False
        for sensor in sensors:
            if sensor.SENS_Eid1 == 1 or sensor.SENS_Eid1 == 2 or sensor.SENS_Eid1 == 3:
                if SHT15Read == False:
                    sensSHT15 = SHT1x.SHT15()
                    sensSHT15.Read()
                    SHT15Read = True
                if sensSHT15.Temperature != None and sensor.SENS_Eid1 == 1:
                    query = "INSERT INTO SENSORDATA (SEDA_Eid1, SEDA_Valu) VALUES({0}, {1})".format(sensor.SENS_Ruid, sensSHT15.Temperature)
                    cur = db.Execute(query)
                if sensSHT15.Humidity != None and sensor.SENS_Eid1 == 2:
                    query = "INSERT INTO SENSORDATA (SEDA_Eid1, SEDA_Valu) VALUES({0}, {1})".format(sensor.SENS_Ruid, sensSHT15.Humidity)
                    cur = db.Execute(query)
                if sensSHT15.DewPoint != None and sensor.SENS_Eid1 == 3:
                    query = "INSERT INTO SENSORDATA (SEDA_Eid1, SEDA_Valu) VALUES({0}, {1})".format(sensor.SENS_Ruid, sensSHT15.DewPoint)
                    cur = db.Execute(query)
        
        db.Commit()
        sleep(3600)

except Exception as ex:
    print(ex)
    db.Disconnect()

db.Disconnect()

