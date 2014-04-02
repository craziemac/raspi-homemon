
# Created: 2014-03-12
# Version: 1.0.0.0
# Author: Marcus Jonsson
# Description: Contains functions to validate data

from datetime import datetime
import sys

def valid_date(date):
    """ Validate that date is in correct format yyyy-mm-dd
        # Parameter <date> string: date to validate
        # Return boolean (True): if validation ok
        # Return boolean (False): if validation fails
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Incorrect date format, excpected yyyy-mm-dd")
        return False
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

def is_numeric(value):
    """ Validate that value is all numeric
        # Parameter <value> string: value to validate
        # Return boolean (True): if validation ok
        # Return boolean (False): if validation fails
    """
    try:
        float(value)
        return True
    except ValueError:
        return False
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    
