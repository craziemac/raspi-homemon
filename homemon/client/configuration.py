
# Created: 2013-11-01
# Version: 1.0.0.0
# Author: Marcus Jonsson
# Description: Contains class that parses XML file with site configuration

import sys
import xml.etree.ElementTree as ET

class Configuration(object):
    """ Parses a XML file containing site configuration.  
    """

    def __init__(self,file):
        """ Constructor """
        self.file = file

    def loadconfig(self):
        """ Loads XML file for parsing and stores configuration.  
        """
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
            if self.database is None \
            or "Name" not in self.database.attrib \
            or "Host" not in self.database.attrib \
            or "User" not in self.database.attrib \
            or "Password" not in self.database.attrib:
                raise Exception("Error: Database not configured correctly in Config.xml")
        
            # Get all installed sensors
            installbase = site.find("Installbase[@Name='Sensor']")
            self.sensors = installbase.findall("Sensor")
        
        except Exception as exc:
            print(exc)
            sys.exit()
        
