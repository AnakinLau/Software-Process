import datetime
import calendar
import conversionHelper as CH
import math

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

def getInterDist(values, LHA):
    latInNum = CH.convertDegMinStrToNumber(values['lat'])
    assLatInNum = CH.convertDegMinStrToNumber(values['assumedLat'])
    LHAInNum = CH.convertDegMinStrToNumber(LHA)
    interDist = (math.sin(math.radians(latInNum)) * math.sin(math.radians(assLatInNum))) + \
                (math.cos(math.radians(latInNum)) * math.cos(math.radians(assLatInNum)) *
                 math.cos(math.radians(LHAInNum)))
    return interDist

def getCorrectedAltitude(interDist):
    ansInRad = math.asin(interDist)
    ansInDeg = math.degrees(ansInRad)
    return CH.convertNumToDegMinString(ansInDeg)

def getCorrectedDistance(values, correctedAlt):
    altInNum = CH.convertDegMinStrToNumber(values['altitude'])
    corrtAltInNum = CH.convertDegMinStrToNumber(correctedAlt)
    corrDistString = CH.convertNumToDegMinString(altInNum - corrtAltInNum)
    return CH.convertDegMinToArcMinInt(corrDistString)

def getCorrectedAzimuth(values, interDist):
    latInNum = CH.convertDegMinStrToNumber(values['lat'])
    assLatInNum = CH.convertDegMinStrToNumber(values['assumedLat'])
    azimuthInRad = math.acos((math.sin(latInNum) - (math.sin(assLatInNum) * interDist))/
              (math.cos(assLatInNum) * math.cos(math.asin(interDist))))
    azimuthInDeg = math.degrees(azimuthInRad)
    return CH.convertNumToDegMinString(azimuthInDeg)
