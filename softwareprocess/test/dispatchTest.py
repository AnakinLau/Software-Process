import unittest
import softwareprocess.dispatch as DSP
import math

class dispatchTest(unittest.TestCase):
    # -----------------------------------------------------------------------
    # ---- Acceptance Tests
    # 100 constructor
    #    Desired level of confidence:    boundary value analysis
    #    Input-output Analysis
    #        inputs:      n ->    integer .GE. 2 and .LT. 30  mandatory, unvalidated
    #        outputs:    instance of TCurve
    #    Happy path analysis:
    #        n:      nominal value    n=4
    #                low bound        n=2
    #                high bound       n=29
    #    Sad path analysis:
    #        n:      non-int n          n="abc"
    #                out-of-bounds n    n=1; n=30
    #                missing n
    #
    # Sad path

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
        self.assertEquals(expectedString, DSP.dispatch({'op': 'adjust'}))

    #Happy Path
    def test201_010_ShouldReturnAltitude(self):
        expectedString = {'altitude':'41d59.0', 'observation': '42d0.0',  'op': 'adjust'}
        self.assertEquals(expectedString, DSP.dispatch({'observation': '42d0.0',  'op': 'adjust'}))

    #

    # Should change the string to have added default params if not already there
    def test202_100_ShouldReturnWithDefaultParam(self):
        entryDict = {'observation': '42d0.0',  'op': 'adjust'}
        correctReturnedDict = {'observation': '42d0.0',  'op': 'adjust', 'height': '0', 'temperature': '72'
            , 'pressure': '1010', 'horizon' : 'natural'}

        parsedDict = DSP.getDefaultOptionalValues(entryDict)

        self.assertEquals(correctReturnedDict['observation'], parsedDict['observation']);
        self.assertEquals(correctReturnedDict['op'], parsedDict['op']);
        self.assertEquals(correctReturnedDict['height'], parsedDict['height']);
        self.assertEquals(correctReturnedDict['temperature'], parsedDict['temperature']);
        self.assertEquals(correctReturnedDict['pressure'], parsedDict['pressure']);
        self.assertEquals(correctReturnedDict['horizon'], parsedDict['horizon']);






    def test202_001_DipShouldReturnZero(self):
        expectedNumber = 0
        self.assertEquals(expectedNumber, DSP.getDip({'observation': '42d0.0',  'op': 'adjust', 'height': '0', 'horizon': 'natural'}))
