'''
Created on 5 nov 2013

@author: Marcus Jonsson
'''

import subprocess
import os

class SHT15(object):
    '''
    classdocs
    '''

    ''' Constructor '''
    def __init__(self):
        #Property
        self.Temperature = None
        self.Humidity = None
        self.DewPoint = None
    
    ''' Method '''
    def Read(self):
        try:
            directory = os.path.join(os.path.dirname(__file__), '../ExternalCpp/ReadSHT15')
            #print(directory)
            subprocess.check_output([directory], universal_newlines=True)
            #subprocess.check_output(["./ReadSHT15"], universal_newlines=True)
        except subprocess.CalledProcessError as e:
            #print(e.output)
            self.raw_reading = e.output.split("/")
            self.Temperature = str(self.raw_reading[0])[5:].replace(".","")
            self.Humidity = str(self.raw_reading[1])[5:].replace(".","")
            self.DewPoint = str(self.raw_reading[2])[5:].replace(".","")
