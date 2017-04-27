import unittest
import datetime
import softwareprocess.dispatch as DSP
import softwareprocess.conversionHelper as CH
import softwareprocess.adjustHelper as AH
import softwareprocess.predictHelper as PH

import math

class predictTest(unittest.TestCase):

    def test100_010_ShouldReturnParameterIsMissing(self):
        expectedString = {'error' : 'parameter is missing'}
        #self.assertIsInstance(DSP.dispatch())
        # additional tests are for boundary value coverage
        #self.assertIsInstance(SM.Sample(2), SM.Sample)
        #self.assertIsInstance(SM.Sample(29), SM.Sample)
        self.assertEquals(expectedString, DSP.dispatch())

    #def test100_011_NotShouldReturnParameterIsMissing(self):
    #    expectedString = {'rror' : 'parameter is missing'}
    #    #self.assertIsInstance(DSP.dispatch())
    #    # additional tests are for boundary value coverage
    #    #self.assertIsInstance(SM.Sample(2), SM.Sample)
    #    #self.assertIsInstance(SM.Sample(29), SM.Sample)
    #    self.assertEquals(expectedString, DSP.dispatch())

    def test100_020_ShouldReturnParameterIsNotADictionary(self):
        expectedString = {'error':'parameter is not a dictionary'}
        self.assertEquals(expectedString, DSP.dispatch(42))

    def test100_021_ShouldReturnParameterIsNotALegalOperation(self):
        expectedString = {'error':'op is not a legal operation'}
        self.assertEquals(expectedString, DSP.dispatch({'op': 'unknown'}))

    def test200_010_ShouldReturnMandatoryInfoIsMissing(self):
        expectedString = {'error':'mandatory information is missing'}
        self.assertEquals(expectedString, DSP.dispatch({'op': 'predict'}))

    def test200_011_ShouldReturnStarNotInCatalog(self):
        expectedString = {'error': 'star not in catalog'}
        self.assertEquals(expectedString['error'],
                          DSP.dispatch({'op': 'predict', 'body': 'mars'})['error'])

    def test200_012_ShouldReturnInvalidDate(self):
        expectedString = {'error': 'invalid date'}
        self.assertEquals(expectedString['error'],
                          DSP.dispatch({'op': 'predict', 'body': 'Betelgeuse',
                                        'date': '2000-01-24'})['error'])

    def test200_013_ShouldReturnInvalidDate(self):
        expectedString = {'error': 'invalid date'}
        self.assertEquals(expectedString['error'],
                          DSP.dispatch({'op': 'predict', 'body': 'Betelgeuse',
                                        'date': '200A-01-24'})['error'])

    def test200_013_ShouldReturnInvalidTime(self):
        expectedString = {'error': 'invalid time'}
        self.assertEquals(expectedString['error'],
                          DSP.dispatch({'op': 'predict', 'body': 'Betelgeuse',
                                        'date': '2007-01-24', 'time': '01:24:60'})['error'])

# Should change the string to have added default params if not already there
    def test202_100_ShouldReturnWithDefaultParam(self):
        entryDict = {'body': 'Betelgeuse',  'op': 'predict'}
        correctReturnedDict = {'body': 'Betelgeuse',  'op': 'predict', 'time': '00:00:00',
            'date': '2001-01-01'}

        parsedDict = DSP.getDefaultOptionalValues(entryDict, 'predict')

        self.assertEquals(correctReturnedDict['body'], parsedDict['body']);
        self.assertEquals(correctReturnedDict['time'], parsedDict['time']);
        self.assertEquals(correctReturnedDict['date'], parsedDict['date']);

    #def test202_101_ShouldReturnWithDefaultParamFailHaveTime(self):
    #    entryDict = {'body': 'Betelgeuse',  'op': 'predict', 'time': '70:05:01'}
    #    correctReturnedDict = {'body': 'Betelgeuse',  'op': 'predict', 'time': '00:00:00',
    #        'date': '2001-01-01'}
#
    #    parsedDict = DSP.getDefaultOptionalValues(entryDict, 'predict')
#
    #    self.assertEquals(correctReturnedDict['body'], parsedDict['body']);
    #    self.assertEquals(correctReturnedDict['time'], parsedDict['time']);
    #    self.assertEquals(correctReturnedDict['date'], par#sedDict['date']);

    #def test202_102_ShouldReturnWithDefaultParamFailHaveDate(self):
    #    entryDict = {'body': 'Betelgeuse',  'op': 'predict', 'date': '2017-12-10'}
    #    correctReturnedDict = {'body': 'Betelgeuse',  'op': 'predict', 'time': '00:00:00',
    #        'date': '2001-01-01'}
#
    #    parsedDict = DSP.getDefaultOptionalValues(entryDict, 'predict')
#
    #    self.assertEquals(correctReturnedDict['body'], parsedDict['body']);
    #    self.assertEquals(correctReturnedDict['time'], parsedDict['time']);
    #    self.assertEquals(correctReturnedDict['date'], parsedDict['date']);

# Test checkBodyFormat
    def test202_201_ShouldReturnCheckBodyPass(self):
        bodyInput = 'Kochab'
        self.assertEquals(True, PH.checkBodyFormat(bodyInput));

    def test202_202_ShouldReturnCheckBodyFail(self):
        bodyInput = 'Kochabd'
        self.assertEquals(False, PH.checkBodyFormat(bodyInput));

    def test202_203_ShouldReturnCheckBodyPass(self):
        bodyInput = 'kochab'
        self.assertEquals(True, PH.checkBodyFormat(bodyInput));

    def test202_204_ShouldReturnCheckBodyPass(self):
        bodyInput = 'KOChab'
        self.assertEquals(True, PH.checkBodyFormat(bodyInput));

    def test202_205_ShouldReturnCheckBodyPass(self):
        bodyInput = 'Kaus Aust.'
        self.assertEquals(True, PH.checkBodyFormat(bodyInput));

    def test202_206_ShouldReturnCheckBodyPass(self):
        bodyInput = 'kAus aUSt.'
        self.assertEquals(True, PH.checkBodyFormat(bodyInput));

    def test202_211_ShouldReturnCheckDatePass(self):
        dateInput = '2002-03-04'
        self.assertEquals(True, PH.checkDateFormat(dateInput));

    def test202_212_ShouldReturnCheckDatePass(self):
        dateInput = '2002-01-01'
        self.assertEquals(True, PH.checkDateFormat(dateInput));

    def test202_213_ShouldReturnCheckDateTrue(self):
        dateInput = '2001-01-01'
        self.assertEquals(True, PH.checkDateFormat(dateInput));

    def test202_214_ShouldReturnCheckDateFail(self):
        dateInput = '2002-14-04'
        self.assertEquals(False, PH.checkDateFormat(dateInput));

    def test202_215_ShouldReturnCheckDateFail(self):
        dateInput = '2002-03-60'
        self.assertEquals(False, PH.checkDateFormat(dateInput));

    def test202_216_ShouldReturnCheckDateFail(self):
        dateInput = '2002-02-29'
        self.assertEquals(False, PH.checkDateFormat(dateInput));

    def test202_217_ShouldReturnCheckDateFail(self):
        dateInput = '2001-00-00'
        self.assertEquals(False, PH.checkDateFormat(dateInput));

    def test202_218_ShouldReturnCheckDatePass(self):
        dateInput = '2001-01-01'
        self.assertEquals(True, PH.checkDateFormat(dateInput));

    def test202_219_ShouldReturnCheckDateFail(self):
        dateInput = '2000-12-31'
        self.assertEquals(False, PH.checkDateFormat(dateInput));

    def test202_220_ShouldReturnCheckDateFail(self):
        dateInput = '200B-12-31'
        self.assertEquals(False, PH.checkDateFormat(dateInput));

    def test202_221_ShouldReturnCheckDateFail(self):
        dateInput = '200B-ds-31'
        self.assertEquals(False, PH.checkDateFormat(dateInput));

    def test202_231_ShouldReturnCheckTimePass(self):
        timeInput = '01:02:52'
        self.assertEquals(True, PH.checkTimeFormat(timeInput));

    def test202_232_ShouldReturnCheckTimePass(self):
        timeInput = '00:00:00'
        self.assertEquals(True, PH.checkTimeFormat(timeInput));

    def test202_233_ShouldReturnCheckTimePass(self):
        timeInput = '21:02:52'
        self.assertEquals(True, PH.checkTimeFormat(timeInput));

    def test202_234_ShouldReturnCheckTimeFail(self):
        timeInput = '01:02:63'
        self.assertEquals(False, PH.checkTimeFormat(timeInput));

    def test202_235_ShouldReturnCheckTimeFail(self):
        timeInput = '01:67:13'
        self.assertEquals(False, PH.checkTimeFormat(timeInput));

    def test202_236_ShouldReturnCheckTimeFail(self):
        timeInput = '25:02:63'
        self.assertEquals(False, PH.checkTimeFormat(timeInput));

# Testing Calculations
    def test202_301_GetAdjustedGHAPass(self):
        timeInput = '03:15:42'
        dateInput = '2016-01-17'
        expectedCumProg = '164d54.5'
        self.assertEquals(expectedCumProg, PH.getAdjustedGHA(dateInput, timeInput));

    def test202_302_GetCumProgPass(self):
        expectedCumProg = '-3d34.8'
        self.assertEquals(expectedCumProg, PH.getCumProg(15));

    def test202_303_GetNumOfLeapYearInbtwPass(self):
        expectedNum = 3
        self.assertEquals(expectedNum, PH.getNumOfLeapYearInbtw(2001,2016));

    def test202_304_GetTotalProgressionPass(self):
        expectedNum = '2d56.9'
        self.assertEquals(expectedNum, PH.getTotalProgression(3));

    def test202_305_GetPrimeMeriRotationPass(self):
        expectedNum = '100d4.8'
        self.assertEquals(expectedNum, PH.getPrimeMeriRotation('100d42.6', '-3d34.8',
                                                                '2d56.9'));
    def test202_306_GetEarthRotatSinceYearStartPass(self):
        expectedNum = '64d49.7'
        starDateTimeObj = datetime.datetime.strptime('2016-01-17 03:15:42',
                                                 '%Y-%m-%d %H:%M:%S')
        self.assertEquals(expectedNum, PH.getEarthRotatSinceYearStart(starDateTimeObj));

    def test202_307_GetTotalAdjustedGHAPass(self):
        expectedNum = '164d54.5'
        self.assertEquals(expectedNum, PH.getTotalAdjustedGHA('100d4.8', '64d49.7'));

    def test202_308_GetGHAStarLongPass(self):
        expectedNum = '75d53.6'
        #'270d59.1'
        self.assertEquals(expectedNum, PH.getGHAStarLong('164d54.5', 'betelgeuse'));

    def test202_309_GetGHAStarLongPass(self):
        expectedNum = '75d53.6'
        #'270d59.1'
        self.assertEquals(expectedNum, PH.getGHAStarLong('164d54.5', 'BetElgEuse'));

    def test202_310_GetGHAStarLatPass(self):
        expectedNum = '7d24.3'
        self.assertEquals(expectedNum, PH.getGHAStarLat('BetElgEuse'));

    # Testing whole of Predict Implementation
    def test203_001_ShouldReturnWithLongLatBetelgeuse(self):
        entryDict = {'body': 'Betelgeuse',  'op': 'predict'}
        correctReturnedDict = {'body': 'Betelgeuse',  'op': 'predict', 'time': '03:15:42',
            'date': '2016-01-17', 'long': '75d53.6', 'lat': '7d24.3'}

        parsedDict = DSP.dispatch({'body': 'Betelgeuse',  'op': 'predict', 'time': '03:15:42',
            'date': '2016-01-17'})
        print parsedDict
        self.assertEquals(correctReturnedDict['body'], parsedDict['body']);
        self.assertEquals(correctReturnedDict['time'], parsedDict['time']);
        self.assertEquals(correctReturnedDict['date'], parsedDict['date']);
        self.assertEquals(correctReturnedDict['long'], parsedDict['long']);
        self.assertEquals(correctReturnedDict['lat'], parsedDict['lat']);

    def test203_002_ShouldReturnWithLongLatError(self):
        entryDict = {'name': 'Betelgeuse',  'op': 'predict'}
        correctReturnedDict = {'name': 'Betelgeuse',  'op': 'predict', 'time': '03:15:42',
            'date': '2016-01-17', 'long': '75d53.6', 'lat': '7d24.3',
                               'error': 'long and/or lat already exist!'}

        parsedDict = DSP.dispatch({'name': 'Betelgeuse',  'op': 'predict', 'time': '03:15:42',
            'date': '2016-01-17', 'long': '75d53.6', 'lat': '7d24.3'})
        print parsedDict
        self.assertEquals(correctReturnedDict['name'], parsedDict['name']);
        self.assertEquals(correctReturnedDict['time'], parsedDict['time']);
        self.assertEquals(correctReturnedDict['date'], parsedDict['date']);
        self.assertEquals(correctReturnedDict['long'], parsedDict['long']);
        self.assertEquals(correctReturnedDict['lat'], parsedDict['lat']);
        self.assertEquals(correctReturnedDict['error'], parsedDict['error']);

