import math
def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    #Perform designated function
    if(values['op'] == 'adjust'):
        if(not('observation' in values)):
            values['error'] = 'mandatory information is missing'
            del values['op']
            return values
        # All default optional values
        if(not('height' in values)):
            values['height'] = '0'
        if(not('temperature' in values)):
            values['temperature'] = '72'
        if(not('pressure' in values)):
            values['pressure'] = '1010'
        if(not('horizon' in values)):
            values['horizon'] = 'natural'



        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        del values['op']
        return values

def getDefaultOptionalValues(values):
    # All default optional values
    if(not('height' in values)):
        values['height'] = '0'
    if(not('temperature' in values)):
        values['temperature'] = '72'
    if(not('pressure' in values)):
        values['pressure'] = '1010'
    if(not('horizon' in values)):
        values['horizon'] = 'natural'
    return values

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
    #if(not(is_(minString))):
    #    return False
    #if(not(isinstance(degString, int))):
    #    return False
    #if(not(isinstance(minString, float))):
    #    return False
    #if (not(minString[::-1].find('.'))):
    #    return False
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
        return float((-0.97 * math.sqrt(int(dictInput['height']))) / 60)
    else :
        return 0

def getRefraction(dictInput):
    refractionP1 = (-0.00452 * int(dictInput['pressure']))
    refractionP2 = (273 + ((int(dictInput['temperature']) - 32) / 1.8))
    #posOfd = dictInput['observation'].find('d')
    #degString = dictInput['observation'][0: posOfd]
    #minString = dictInput['observation'][posOfd + 1: len(dictInput['observation'])]
    #degToInt = int(degString)
    #print("degString= {0}".format(degString))
    #minToFloat = float(minString)
    degToInt = getObservationDegToInt(dictInput['observation'])
    minToFloat = getObservationMinToFloat(dictInput['observation'])
    print("minToFloat= {0}".format(minToFloat))
    refractionP3 = (math.tan(math.radians(degToInt +
                                          (convertMinToNumber(minToFloat)))))
    print("refractionP1= {0}, refractionP2= {1}, "
          "refractionP3= {2}".format(refractionP1, refractionP2, refractionP3))
    return refractionP1 / refractionP2 / refractionP3

def getAltitude(dictInput):
    dip = getDip(dictInput)
    refraction = getRefraction(dictInput)
    degInt = getObservationDegToInt(dictInput['observation'])
    minFloat = getObservationMinToFloat(dictInput['observation'])
    degMinNum = convertDegMinToNumber(degInt, minFloat)
    degMinNum = degMinNum + dip + refraction
    return convertNumToDegMinString(degMinNum)

# Helper methods getting degrees and minutes
def getObservationDegToInt(observationInput):
    posOfd = observationInput.find('d')
    degString = observationInput[0: posOfd]
    return int(degString)

def getObservationMinToFloat(observationInput):
    posOfd = observationInput.find('d')
    minString = observationInput[posOfd + 1: len(observationInput)]
    return float(minString)

def convertMinToNumber(minNum):
    return float(minNum/60)

def convertDegMinToNumber(degInput, minInput):
    return degInput + convertMinToNumber(minInput)

def convertNumToDegMinString(numInput):
    if numInput >= 0:
        decimalNum = float(numInput % 1)
    else:
        decimalNum = float((numInput * -1) % 1)
    deg = 0
    mins = round((decimalNum * 60),1)
    leftOver = float(min / 60)
    if(leftOver >= 1):
        deg = int(leftOver)
        mins = mins - (60 * leftOver)
    if(numInput < 0):
        deg = -1 * deg
    deg = deg + round(numInput, 0)

    return str(deg) + 'd' + str(mins)
