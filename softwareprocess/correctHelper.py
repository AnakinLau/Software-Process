import datetime
import calendar
import conversionHelper as CH

# Helper Classes Specifically for Correct()
def checkCorrectInputFormat(checkVal, valType):
    if(not(isinstance(checkVal, basestring))):
        return False
    else:
        if(checkVal.count('d') != 1):
            return False
        posOfd = checkVal.find('d')
        degString = checkVal[0: posOfd]
        minString = checkVal[posOfd + 1: len(checkVal)]

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
        if(valType == 'AssumedLong' or valType == 'Altitude' or valType == 'Long'):
            if(not(degString.isdigit())): # Can be use to eliminate -0
                print('degString is not a digit ={0}', format(degString))
                return False
            if(valType == 'AssumedLong' or valType == 'Long'):
                if(int(degString) < 0 or int(degString) >= 360):
                    return False
            if(valType == 'Altitude'):
                if(int(degString) <= 0 or int(degString) >= 90):
                    return False

        if(valType == 'Lat' or valType == 'AssumedLat'):
            # Need to also consider and accept negative 0s
            try:
                int(degString)
            except ValueError:
                print('degString is not a digit ={0}', format(degString))
                return False

            if(int(degString) <= -90 or int(degString) >= 90):
                return False
        return True

def getLHA(values):
    LHANumber = CH.convertDegMinStrToNumber(values['long']) \
                 + CH.convertDegMinStrToNumber(values['assumedLong'])
    return CH.convertNumToDegMinString(LHANumber)

def getInterDist(value, LHA):
    math.sin()