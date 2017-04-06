"""
    Created on Mar 21, 2017

    @author: Wan Anakin Lau

    Purpose of this program is to return a corrected altitude given a set
    of information based on temperature, altitude, pressure, height, and horizon.
    Gives back error when unexpected input is put through.

"""
import math
import datetime
def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    # Perform designated function
    # adjust operation--------->
    if(values['op'] == 'adjust'):
        if(not('observation' in values)):
            values['error'] = 'mandatory information is missing'
            del values['op']
            return values
        values = getDefaultOptionalValues(values, 'adjust')
        if(checkObservationFormat(values['observation']) == False):
            values['error'] =  'observation is invalid'
            return values
        if(checkHeightFormat(values['height']) == False):
            values['error'] =  'height is invalid'
            return values
        if(checkPressureFormat(values['pressure']) == False):
            values['error'] =  'pressure is invalid'
            return values
        if(checkTemperatureFormat(values['temperature']) == False):
            values['error'] =  'temperature is invalid'
            return values
        if(checkHorizonFormat(values['horizon']) == False):
            values['error'] =  'horizon is invalid'
            return values
        values['altitude'] = getAltitude(values)
        return values

    # Predict operations------>
    elif(values['op'] == 'predict'):
        if(not('body' in values)):
            values['error'] = 'mandatory information is missing'
            del values['op']
            return values
        values = getDefaultOptionalValues(values, 'predict')
        if(checkBodyFormat(values['body']) == False):
            values['error'] = 'star not in catalog'
            return values
        if(checkDateFormat(values['date']) == False):
            values['error'] = 'invalid date'
            return values

        return values
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        del values['op']
        return values

def getDefaultOptionalValues(values, operation):
    if(operation == 'adjust'):
        # All default optional values
        if(not('height' in values)):
            values['height'] = '0'
        if(not('temperature' in values)):
            values['temperature'] = '72'
        if(not('pressure' in values)):
            values['pressure'] = '1010'
        if(not('horizon' in values)):
            values['horizon'] = 'natural'
    elif(operation == 'predict'):
        if(not('date' in values)):
            values['date'] = '2001-01-01'
        if(not('time' in values)):
            values['time'] = '00:00:00'
    else:
        values['getDefaultOptionalValuesError'] = \
            'operation given is not one included in the function'
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
    print("degMinNum= {0}".format(degMinNum))
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
    print ("numInput= {0}".format(numInput))
    if numInput >= 0:
        decimalNum = float(numInput % 1)
    else:
        decimalNum = float((numInput * -1) % 1)
    deg = 0
    mins = round((decimalNum * 60),1)
    leftOver = mins / 60
    if(leftOver >= 1):
        print ("leftOver {0} is >= 1")
        deg = int(leftOver)
        mins = mins - (60 * leftOver)
    if(numInput < 0):
        deg = -1 * deg
    deg = deg + int(numInput)

    return str(deg) + 'd' + str(mins)


# Helper Classes Specifically for Predict()
def createStarDict():

    starDict = {
        'Alpheratz': {'SHA': '357d41.7', 'declination': '29d10.9'},
        'Ankaa': {'SHA': '353d14.1', 'declination': '-42d13.4'},
        'Schedar': {'SHA': '349d38.4', 'declination': '56d37.7'},
        'Diphda': {'SHA': '348d54.1', 'declination': '-17d54.1'},
        'Achernar': {'SHA': '335d25.5', 'declination': '-57d09.7'},
        'Hamal': {'SHA': '327d58.7', 'declination': '23d32.3'},
        'Polaris': {'SHA': '316d41.3', 'declination': '89d20.1'},
        'Akamar': {'SHA': '315d16.8', 'declination': '-40d14.8'},
        'Menkar': {'SHA': '314d13.0', 'declination': '4d09.0'},
        'Mirfak': {'SHA': '308d37.4', 'declination': '49d55.1'},
        'Aldebaran': {'SHA': '290d47.1', 'declination': '16d32.3'},
        'Rigel': {'SHA': '281d10.1', 'declination': '-8d11.3'},
        'Capella': {'SHA': '280d31.4', 'declination': '46d00.7'},
        'Bellatrix': {'SHA': '278d29.8', 'declination': '6d21.6'},
        'Elnath': {'SHA': '278d10.1', 'declination': '28d37.1'},
        'Alnilam': {'SHA': '275d44.3', 'declination': '-1d11.8'},
        'Betelgeuse': {'SHA': '270d59.1', 'declination': '7d24.3'},
        'Canopus': {'SHA': '263d54.8', 'declination': '-52d42.5'},
        'Sirius': {'SHA': '258d31.7', 'declination': '-16d44.3'},
        'Adara': {'SHA': '255d10.8', 'declination': '-28d59.9'},
        'Procyon': {'SHA': '244d57.5', 'declination': '5d10.9'},
        'Pollux': {'SHA': '243d25.2', 'declination': '27d59.0'},
        'Avior': {'SHA': '234d16.6', 'declination': '-59d33.7'},
        'Suhail': {'SHA': '222d50.7', 'declination': '-43d29.8'},
        'Miaplacidus': {'SHA': '221d38.4', 'declination': '-69d46.9'},
        'Alphard': {'SHA': '217d54.1', 'declination': '-8d43.8'},
        'Regulus': {'SHA': '207d41.4', 'declination': '11d53.2'},
        'Dubhe': {'SHA': '193d49.4', 'declination': '61d39.5'},
        'Denebola': {'SHA': '182d31.8', 'declination': '14d28.9'},
        'Gienah': {'SHA': '175d50.4', 'declination': '-17d37.7'},
        'Acrux': {'SHA': '173d07.2', 'declination': '-63d10.9'},
        'Gacrux': {'SHA': '171d58.8', 'declination': '-57d11.9'},
        'Alioth': {'SHA': '166d19.4', 'declination': '55d52.1'},
        'Spica': {'SHA': '158d29.5', 'declination': '-11d14.5'},
        'Alcaid': {'SHA': '152d57.8', 'declination': '49d13.8'},
        'Hadar': {'SHA': '148d45.5', 'declination': '-60d26.6'},
        'Menkent': {'SHA': '148d05.6', 'declination': '-36d26.6'},
        'Arcturus': {'SHA': '145d54.2', 'declination': '19d06.2'},
        'Rigil Kent.': {'SHA': '139d49.6', 'declination': '-60d53.6'},
        'Zubenelg.': {'SHA': '137d03.7', 'declination': '-16d06.3'},
        'Kochab': {'SHA': '137d21.0', 'declination': '74d05.2'},
        'Alphecca': {'SHA': '126d09.9', 'declination': '26d39.7'},
        'Antares': {'SHA': '112d24.4', 'declination': '-26d27.8'},
        'Atria': {'SHA': '107d25.2', 'declination': '-69d03.0'},
        'Sabik': {'SHA': '102d10.9', 'declination': '-15d44.4'},
        'Shaula': {'SHA': '96d20.0', 'declination': '-37d06.6'},
        'Rasalhague': {'SHA': '96d05.2', 'declination': '12d33.1'},
        'Etamin': {'SHA': '90d45.9', 'declination': '51d29.3'},
        'Kaus Aust.': {'SHA': '83d41.9', 'declination': '-34d22.4'},
        'Vega': {'SHA': '80d38.2', 'declination': '38d48.1'},
        'Nunki': {'SHA': '75d56.6', 'declination': '-26d16.4'},
        'Altair': {'SHA': '62d06.9', 'declination': '8d54.8'},
        'Peacock': {'SHA': '53d17.2', 'declination': '-56d41.0'},
        'Deneb': {'SHA': '49d30.7', 'declination': '45d20.5'},
        'Enif': {'SHA': '33d45.7', 'declination': '9d57.0'},
        'Alnair': {'SHA': '27d42.0', 'declination': '-46d53.1'},
        'Fomalhaut': {'SHA': '15d22.4', 'declination': '-29d32.3'},
        'Scheat': {'SHA': '13d51.8', 'declination': '28d10.3'},
        'Markab': {'SHA': '13d36.7', 'declination': '15d17.6'}
    }
    return starDict


def checkBodyFormat(body):
    starDict = createStarDict()
    if(not(body.title() in starDict)):
        return False
    else:
        return True


def checkDateFormat(dateInput):
    try:
        dateObj = datetime.datetime.strptime(dateInput, '%Y-%m-%d')
        if(dateObj.year > 2000):
            return True
        else:
            return False
    except ValueError:
        return False
