"""
    Created on Mar 21, 2017

    @author: Wan Anakin Lau

    Purpose of this program is to return a corrected altitude given a set
    of information based on temperature, altitude, pressure, height, and horizon.
    Gives back error when unexpected input is put through.

    Now this program will also give back latitude and longitude to a given star
    given a specific time and date
"""
import math
import datetime
import calendar
import adjustHelper as AH
import predictHelper as PH
import correctHelper as OH

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
        if(AH.checkObservationFormat(values['observation']) == False):
            values['error'] =  'observation is invalid'
            return values
        if(AH.checkHeightFormat(values['height']) == False):
            values['error'] =  'height is invalid'
            return values
        if(AH.checkPressureFormat(values['pressure']) == False):
            values['error'] =  'pressure is invalid'
            return values
        if(AH.checkTemperatureFormat(values['temperature']) == False):
            values['error'] =  'temperature is invalid'
            return values
        if(AH.checkHorizonFormat(values['horizon']) == False):
            values['error'] =  'horizon is invalid'
            return values
        values['altitude'] = AH.getAltitude(values)
        return values

    # Predict operations------>
    elif(values['op'] == 'predict'):
        if(not('body' in values)):
            values['error'] = 'mandatory information is missing'
            return values
        values = getDefaultOptionalValues(values, 'predict')
        if(PH.checkBodyFormat(values['body']) == False):
            values['error'] = 'star not in catalog'
            return values
        if(PH.checkDateFormat(values['date']) == False):
            values['error'] = 'invalid date'
            return values
        if(PH.checkTimeFormat(values['time']) == False):
            values['error'] = 'invalid time'
            return values
        if('long' in values or 'lat' in values):
            values['error'] = 'long and/or lat already exist!'
            return values

        adjustedGHA = PH.getAdjustedGHA(values['date'], values['time'])
        values['long'] = PH.getGHAStarLong(adjustedGHA, values['body'])
        values['lat'] = PH.getGHAStarLat(values['body'])

        return values

    # Correct operations------>
    elif(values['op'] == 'correct'):
        if(not(('lat' in values) and ('long' in values) and ('altitude' in values)
               and ('assumedLat' in values) and ('assumedLong' in values))):
            values['error'] = 'mandatory information is missing'
            return values
        if(OH.checkCorrectInputFormat(values['lat'], 'Lat') == False):
            values['error'] = 'invalid lat'
            return values
        if(OH.checkCorrectInputFormat(values['long'], 'Long') == False):
            values['error'] = 'invalid long'
            return values
        if(OH.checkCorrectInputFormat(values['altitude'], 'Altitude') == False):
            values['error'] = 'invalid altitude'
            return values
        if(OH.checkCorrectInputFormat(values['assumedLat'], 'AssumedLat') == False):
            values['error'] = 'invalid assumedLat'
            return values
        if(OH.checkCorrectInputFormat(values['assumedLong'], 'AssumedLong') == False):
            values['error'] = 'invalid assumedLong'
            return values
        LHA = OH.getLHA(values)
        interDist = OH.getInterDist(values, LHA)
        correctAlt = OH.getCorrectedAltitude(interDist)
        correctDist = OH.getCorrectedDistance(values, correctAlt)
        correctAzimuth = OH.getCorrectedAzimuth(values, interDist)
        values['correctedDistance'] = correctDist
        values['correctedAzimuth'] = correctAzimuth

        return values
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







