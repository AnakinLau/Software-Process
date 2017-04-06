import unittest
import softwareprocess.dispatch as DSP
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
        self.assertEquals(True, DSP.checkBodyFormat(bodyInput));

    def test202_202_ShouldReturnCheckBodyFail(self):
        bodyInput = 'Kochabd'
        self.assertEquals(False, DSP.checkBodyFormat(bodyInput));

    def test202_203_ShouldReturnCheckBodyPass(self):
        bodyInput = 'kochab'
        self.assertEquals(True, DSP.checkBodyFormat(bodyInput));

    def test202_204_ShouldReturnCheckBodyPass(self):
        bodyInput = 'KOChab'
        self.assertEquals(True, DSP.checkBodyFormat(bodyInput));

    def test202_205_ShouldReturnCheckBodyPass(self):
        bodyInput = 'Kaus Aust.'
        self.assertEquals(True, DSP.checkBodyFormat(bodyInput));

    def test202_206_ShouldReturnCheckBodyPass(self):
        bodyInput = 'kAus aUSt.'
        self.assertEquals(True, DSP.checkBodyFormat(bodyInput));

    def test202_211_ShouldReturnCheckDatePass(self):
        dateInput = '2002-03-04'
        self.assertEquals(True, DSP.checkDateFormat(dateInput));

    def test202_212_ShouldReturnCheckDatePass(self):
        dateInput = '2002-01-01'
        self.assertEquals(True, DSP.checkDateFormat(dateInput));

    def test202_213_ShouldReturnCheckDateTrue(self):
        dateInput = '2001-01-01'
        self.assertEquals(True, DSP.checkDateFormat(dateInput));

    def test202_214_ShouldReturnCheckDateFail(self):
        dateInput = '2002-14-04'
        self.assertEquals(False, DSP.checkDateFormat(dateInput));

    def test202_215_ShouldReturnCheckDateFail(self):
        dateInput = '2002-03-60'
        self.assertEquals(False, DSP.checkDateFormat(dateInput));

    def test202_216_ShouldReturnCheckDateFail(self):
        dateInput = '2002-02-29'
        self.assertEquals(False, DSP.checkDateFormat(dateInput));

    def test202_217_ShouldReturnCheckDateFail(self):
        dateInput = '2001-00-00'
        self.assertEquals(False, DSP.checkDateFormat(dateInput));

    def test202_218_ShouldReturnCheckDatePass(self):
        dateInput = '2001-01-01'
        self.assertEquals(True, DSP.checkDateFormat(dateInput));

    def test202_219_ShouldReturnCheckDateFail(self):
        dateInput = '2000-12-31'
        self.assertEquals(False, DSP.checkDateFormat(dateInput));

    def test202_220_ShouldReturnCheckDateFail(self):
        dateInput = '200B-12-31'
        self.assertEquals(False, DSP.checkDateFormat(dateInput));

    def test202_221_ShouldReturnCheckDateFail(self):
        dateInput = '200B-ds-31'
        self.assertEquals(False, DSP.checkDateFormat(dateInput));

    def test202_231_ShouldReturnCheckTimePass(self):
        timeInput = '01:02:52'
        self.assertEquals(True, DSP.checkTimeFormat(timeInput));

    def test202_232_ShouldReturnCheckTimePass(self):
        timeInput = '00:00:00'
        self.assertEquals(True, DSP.checkTimeFormat(timeInput));

    def test202_233_ShouldReturnCheckTimePass(self):
        timeInput = '21:02:52'
        self.assertEquals(True, DSP.checkTimeFormat(timeInput));

    def test202_234_ShouldReturnCheckTimeFail(self):
        timeInput = '01:02:63'
        self.assertEquals(False, DSP.checkTimeFormat(timeInput));

    def test202_235_ShouldReturnCheckTimeFail(self):
        timeInput = '01:67:13'
        self.assertEquals(False, DSP.checkTimeFormat(timeInput));

    def test202_236_ShouldReturnCheckTimeFail(self):
        timeInput = '25:02:63'
        self.assertEquals(False, DSP.checkTimeFormat(timeInput));

# Testing Calculations
    def test202_301_GetAdjustedGHAPass(self):
        timeInput = '22:02:23'
        dateInput = '2002-02-02'
        expectedCumProg = '-3d34.8'
        self.assertEquals(False, DSP.getAdjustedGHA(dateInput, timeInput));
