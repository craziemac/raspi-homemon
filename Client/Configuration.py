'''
Created on 1 nov 2013

@author: Marcus Jonsson
'''
import sys
import xml.etree.ElementTree as ET

class Configuration(object):
    '''
    classdocs
    '''

    ''' Constructor '''
    def __init__(self,file):
        self.file = file

    '''Methods'''
    def LoadConfig(self):
        # Read configuration file
        try:
            tree = ET.parse(self.file)
            root = tree.getroot()
            sites = list(root)
            
            # Check that there is one and only one site configured.
            if len(sites)!=1:
                raise Exception("Error: There must be (only) 1 site configured in Config.xml")
            else:
                site = sites[0]
        
            self.database = site.find("Database")
            # Check that the database configuration is correct.
            if self.database == None \
            or "Name" not in self.database.attrib \
            or "Host" not in self.database.attrib \
            or "User" not in self.database.attrib \
            or "Password" not in self.database.attrib:
                raise Exception("Error: Database not configured correctly in Config.xml")
        
            # Get all installed sensors
            installbase = site.find("Installbase[@Name='Sensor']")
            self.sensors = installbase.findall("Sensor")
        
        except Exception as ex:
            print(ex)
            sys.exit()
        