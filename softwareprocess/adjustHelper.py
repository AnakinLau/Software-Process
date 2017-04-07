import math
import conversionHelper as CH

def checkObservationFormat(observation):
    if(observation.count('d') != 1):
        return False
    posOfd = observation.find('d')
    degString = observation[0: posOfd]
    minString = observation[posOfd + 1: len(observation)]

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
    if(len(degString) > 2 or len(degString) == 0):
        return False
    if(not(degString.isdigit())):
        return False
    if(int(degString) < 0 or int(degString) >= 90):
        return False
    return True


def checkHeightFormat(height):
    try:
        if(float(height) >= 0):
            return True
        else:
            return False
    except ValueError:
        return False


def checkTemperatureFormat(temperature):
    try:
        if(float(temperature) >= -20 and float(temperature) <= 120
           and temperature.count('.') == 0):

            return True
        else:
            return False
    except ValueError:
        return False


def checkPressureFormat(pressure):
    try:
        if(float(pressure) >= 100 and float(pressure) <= 1100
           and pressure.count('.') == 0):

            return True
        else:
            return False
    except ValueError:
        return False


def checkHorizonFormat(horizon):
    try:
        if(horizon.lower() == 'natural' or horizon.lower() == 'artificial'):
            return True
        else:
            return False
    except ValueError:
        return False


def getDip(dictInput):
    if(dictInput['horizon'].lower() == 'natural'):
        return float((-0.97 * math.sqrt(float(dictInput['height']))) / 60)
    else :
        return 0


def getRefraction(dictInput):
    refractionP1 = (-0.00452 * int(dictInput['pressure']))
    refractionP2 = (273 + ((int(dictInput['temperature']) - 32) / 1.8))
    degToInt = CH.getObservationDegToInt(dictInput['observation'])
    minToFloat = CH.getObservationMinToFloat(dictInput['observation'])
    print("minToFloat= {0}".format(minToFloat))
    refractionP3 = (math.tan(math.radians(degToInt +
                                          (CH.convertMinToNumber(minToFloat)))))
    print("refractionP1= {0}, refractionP2= {1}, "
          "refractionP3= {2}".format(refractionP1, refractionP2, refractionP3))
    return refractionP1 / refractionP2 / refractionP3


def getAltitude(dictInput):
    dip = getDip(dictInput)
    refraction = getRefraction(dictInput)
    degInt = CH.getObservationDegToInt(dictInput['observation'])
    minFloat = CH.getObservationMinToFloat(dictInput['observation'])
    degMinNum = CH.convertDegMinToNumber(degInt, minFloat)
    degMinNum = degMinNum + dip + refraction
    print("degMinNum= {0}".format(degMinNum))
    return CH.convertNumToDegMinString(degMinNum)
