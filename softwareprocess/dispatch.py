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
from softwareprocess.adjustHelper import adjustHelper as AH
from softwareprocess.predictHelper import predictHelper as PH
import softwareprocess.conversionHelper as CH

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
            del values['op']
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
        # Greenwich Hour Angle for Aries
        GHAA = {'date': '2001-01-01', 'time': '00:00:00',
                'deg': '100d42.6'}
        adjustedGHA = PH.getAdjustedGHA(values['date'], values['time'])


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







