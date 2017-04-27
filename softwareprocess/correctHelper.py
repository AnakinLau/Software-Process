import datetime
import calendar
import conversionHelper as CH

# Helper Classes Specifically for Correct()
def checkLatFormat(lat):
    if(not(isinstance(lat, basestring))):
        return False
    else:
        if(lat.count('d') != 1):
            return False
        posOfd =     lat.find('d')
        degString = lat[0: posOfd]
        minString = lat[posOfd + 1: len(lat)]

        if(minString.count('.') != 1):
            return False
        posOfPeriod = minString.find('.')
        yInt = minString[0: posOfPeriod]
        yDecimal = minString[posOfPeriod + 1 : len(minString)]
        if(len(yDecimal) != 1):
            return False
        if(len(yInt) > 2 or len(yInt) == 0):
            return False
        if(not(yDecimal.isdigit())):
            return False
        if(not(yInt.isdigit())):
            return False
        if(int(yInt) > 59 or int(yInt) < 0):
            return  False

        # check if deg is a digit first
        if(len(degString) == 0):
            return False
        # Need to also consider and accept negative 0s
        try:
            int(degString)
        except ValueError:
            print('degString is not a digit ={0}', format(degString))
            return False
        #if(not(degString.isdigit())):
        #    print('degString is not a digit ={0}', format(degString))
        #    return False
        if(int(degString) <= -90 or int(degString) >= 90):
            return False
        return True

def checkLongFormat(long):
    if(not(isinstance(long, basestring))):
        return False
    else:
        if(long.count('d') != 1):
            return False
        posOfd = long.find('d')
        degString = long[0: posOfd]
        minString = long[posOfd + 1: len(long)]

        if(minString.count('.') != 1):
            return False
        posOfPeriod = minString.find('.')
        yInt = minString[0: posOfPeriod]
        yDecimal = minString[posOfPeriod + 1 : len(minString)]
        if(len(yDecimal) != 1):
            return False
        if(len(yInt) > 2 or len(yInt) == 0):
            return False
        if(not(yDecimal.isdigit())):
            return False
        if(not(yInt.isdigit())):
            return False
        if(int(yInt) > 59 or int(yInt) < 0):
            return  False

        # check if deg is a digit first
        if(len(degString) == 0):
            return False
        #try:
        #    int(degString)
        #except ValueError:
        #    print('degString is not a digit ={0}', format(degString))
        #    return False
        if(not(degString.isdigit())): # Can be use to eliminate -0
            print('degString is not a digit ={0}', format(degString))
            return False
        if(int(degString) < 0 or int(degString) >= 360):
            return False
        return True

def checkAltitudeFormat(altitude):
    if(not(isinstance(altitude, basestring))):
        return False
    else:
        if(altitude.count('d') != 1):
            return False
        posOfd = altitude.find('d')
        degString = altitude[0: posOfd]
        minString = altitude[posOfd + 1: len(altitude)]

        if(minString.count('.') != 1):
            return False
        posOfPeriod = minString.find('.')
        yInt = minString[0: posOfPeriod]
        yDecimal = minString[posOfPeriod + 1 : len(minString)]
        if(len(yDecimal) != 1):
            return False
        if(len(yInt) > 2 or len(yInt) == 0):
            return False
        if(not(yDecimal.isdigit())):
            return False
        if(not(yInt.isdigit())):
            return False
        if(int(yInt) > 59 or int(yInt) < 0):
            return  False

        # check if deg is a digit first
        if(len(degString) == 0):
            return False
        #try:
        #    int(degString)
        #except ValueError:
        #    print('degString is not a digit ={0}', format(degString))
        #    return False
        if(not(degString.isdigit())): # Can be use to eliminate -0
            print('degString is not a digit ={0}', format(degString))
            return False
        if(int(degString) <= 0 or int(degString) >= 90):
            return False
        return True


def checkAssumedLatFormat(assumedLat):
    if(not(isinstance(assumedLat, basestring))):
        return False
    else:
        if(assumedLat.count('d') != 1):
            return False
        posOfd = assumedLat.find('d')
        degString = assumedLat[0: posOfd]
        minString = assumedLat[posOfd + 1: len(assumedLat)]

        if(minString.count('.') != 1):
            return False
        posOfPeriod = minString.find('.')
        yInt = minString[0: posOfPeriod]
        yDecimal = minString[posOfPeriod + 1 : len(minString)]
        if(len(yDecimal) != 1):
            return False
        if(len(yInt) > 2 or len(yInt) == 0):
            return False
        if(not(yDecimal.isdigit())):
            return False
        if(not(yInt.isdigit())):
            return False
        if(int(yInt) > 59 or int(yInt) < 0):
            return  False

        # check if deg is a digit first
        if(len(degString) == 0):
            return False
        try:
            int(degString)
        except ValueError:
            print('degString is not a digit ={0}', format(degString))
            return False
        #if(not(degString.isdigit())): # Can be use to eliminate -0
        #    print('degString is not a digit ={0}', format(degString))
        #    return False
        if(int(degString) <= -90 or int(degString) >= 90):
            return False
        return True
