
# Created: 2013-10-31
# Version: 1.0.0.0
# Author: Marcus Jonsson
# Description: Main entry point for raspi-homemon

import sys,os
sys.path.append(os.path.realpath('..'))

from client import configuration
from database import database, dosensor
from hardware import sht1x_py
from time import sleep

def main():
    try:
        # Read configuration file
        config = configuration.Configuration("config.xml")
        config.loadconfig()
        
        # Configure database connection
        db = database.DatabaseConn()
        db.cnxdetails.user = config.database.attrib["User"]
        db.cnxdetails.password = config.database.attrib["Password"]
        db.cnxdetails.host = config.database.attrib["Host"]
        db.cnxdetails.name = config.database.attrib["Name"]
        
        # Connect to database
        if db.connection == None:
            db.connect()

        # Fetch data for configured sensors
        sensors = []
        for cnfsensor in config.sensors:
            query = "SELECT * FROM SENSOR WHERE SENS_Item={0} LIMIT 1".format(cnfsensor.attrib["Item"])
            cur = db.execute(query)
            row = cur.fetchone()
            newsensor = dosensor.DOSensor()
            newsensor.add_row(cur, row)
            sensors.append(newsensor)
    
        # Collect data from sensors and store in database
        sht15read = False
        for sensor in sensors:
            if sensor.sens_type == 1 or sensor.sens_type == 2 or sensor.sens_type == 3:
                if sht15read == False:
                    senssht15 = sht1x_py.SHT15()
                    senssht15.read()
                    sht15read = True
                if senssht15.temperature is not None and sensor.sens_type == 1:
                    query = "INSERT INTO SENSORDATA (SEDA_Eid1, SEDA_Valu) VALUES({0}, {1})".format(sensor.sens_ruid, senssht15.temperature)
                    cur = db.execute(query)
                if senssht15.humidity is not None and sensor.sens_type == 2:
                    query = "INSERT INTO SENSORDATA (SEDA_Eid1, SEDA_Valu) VALUES({0}, {1})".format(sensor.sens_ruid, senssht15.humidity)
                    cur = db.execute(query)
                if senssht15.dewpoint is not None and sensor.sens_type == 3:
                    query = "INSERT INTO SENSORDATA (SEDA_Eid1, SEDA_Valu) VALUES({0}, {1})".format(sensor.sens_ruid, senssht15.dewpoint)
                    cur = db.execute(query)
        
        db.commit()

    except Exception as exc:
        print(exc)
        db.disconnect()

    db.disconnect()

if __name__=="__main__":
    main()

