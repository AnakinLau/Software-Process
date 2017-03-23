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

    if(not(isinstance(degString, int))):
        return False
    if(not(isinstance(minString, float))):
        return False
    if (not(minString[::-1].find('.'))):
        return False
    return True
