
# Created: 2013-10-31
# Version: 1.0.0.0
# Author: Marcus Jonsson
# Description: Read data from sensirion SHT15

from sht1x.Sht1x import Sht1x as SHT1x

class SHT15(object):
    """ Class used to read and store data from a sensirion SHT15.  
    """

    def __init__(self, dataPin = 18, sckPin = 16, gpioMode = GPIO_BOARD):
        """ Constructor """
        #Property
        self.dataPin = dataPin
        self.sckPin = sckPin
        self.gpioMode = gpioMode
        self.temperature = None
        self.humidity = None
        self.dewpoint = None
        
    def read(self):
        """ Read temperature and humidity from sensor """
        try:
            sht1x = SHT1x(self.dataPin, self.sckPin, self.gpioMode)
            self.temperature = sht1x.read_temperature_C()
            self.humidity = sht1x.read_humidity()
            self.dewpoint = sht1x.calculate_dew_point(self.temperature, self.humidity)
        except Exception as exc:
            print(exc)
