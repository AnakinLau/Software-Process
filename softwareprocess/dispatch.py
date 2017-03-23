
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

