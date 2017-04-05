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

# Should change the string to have added default params if not already there
    def test202_100_ShouldReturnWithDefaultParam(self):
        entryDict = {'body': 'Betelgeuse',  'op': 'predict'}
        correctReturnedDict = {'body': 'Betelgeuse',  'op': 'predict', 'time': '00:00:00',
            'date': '2001-01-01'}

        parsedDict = DSP.getDefaultOptionalValues(entryDict, 'adjust')

        self.assertEquals(correctReturnedDict['body'], parsedDict['body']);
        self.assertEquals(correctReturnedDict['time'], parsedDict['time']);
        self.assertEquals(correctReturnedDict['date'], parsedDict['date']);
