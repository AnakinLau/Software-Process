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

    def test202_101_ShouldReturnWithDefaultParamHaveHeightFail(self):
        entryDict = {'observation': '42d0.0',  'op': 'adjust', 'height': '13'}
        correctReturnedDict = {'observation': '42d0.0',  'op': 'adjust', 'height': '0', 'temperature': '72'
            , 'pressure': '1010', 'horizon' : 'natural'}

        parsedDict = DSP.getDefaultOptionalValues(entryDict)

        self.assertEquals(correctReturnedDict['observation'], parsedDict['observation']);
        self.assertEquals(correctReturnedDict['op'], parsedDict['op']);
        self.assertEquals(correctReturnedDict['height'], parsedDict['height']);
        self.assertEquals(correctReturnedDict['temperature'], parsedDict['temperature']);
        self.assertEquals(correctReturnedDict['pressure'], parsedDict['pressure']);
        self.assertEquals(correctReturnedDict['horizon'], parsedDict['horizon']);

    def test202_101_ShouldReturnWithDefaultParamHaveTemperatureFail(self):
        entryDict = {'observation': '42d0.0',  'op': 'adjust', 'temperature': '13'}
        correctReturnedDict = {'observation': '42d0.0',  'op': 'adjust', 'height': '0', 'temperature': '72'
            , 'pressure': '1010', 'horizon' : 'natural'}

        parsedDict = DSP.getDefaultOptionalValues(entryDict)

        self.assertEquals(correctReturnedDict['observation'], parsedDict['observation']);
        self.assertEquals(correctReturnedDict['op'], parsedDict['op']);
        self.assertEquals(correctReturnedDict['height'], parsedDict['height']);
        self.assertEquals(correctReturnedDict['temperature'], parsedDict['temperature']);
        self.assertEquals(correctReturnedDict['pressure'], parsedDict['pressure']);
        self.assertEquals(correctReturnedDict['horizon'], parsedDict['horizon']);

    def test202_101_ShouldReturnWithDefaultParamHavePressureFail(self):
        entryDict = {'observation': '42d0.0',  'op': 'adjust', 'pressure': '13'}
        correctReturnedDict = {'observation': '42d0.0',  'op': 'adjust', 'height': '0', 'temperature': '72'
            , 'pressure': '1010', 'horizon' : 'natural'}

        parsedDict = DSP.getDefaultOptionalValues(entryDict)

        self.assertEquals(correctReturnedDict['observation'], parsedDict['observation']);
        self.assertEquals(correctReturnedDict['op'], parsedDict['op']);
        self.assertEquals(correctReturnedDict['height'], parsedDict['height']);
        self.assertEquals(correctReturnedDict['temperature'], parsedDict['temperature']);
        self.assertEquals(correctReturnedDict['pressure'], parsedDict['pressure']);
        self.assertEquals(correctReturnedDict['horizon'], parsedDict['horizon']);

    def test202_101_ShouldReturnWithDefaultParamHaveHorizonFail(self):
        entryDict = {'observation': '42d0.0',  'op': 'adjust', 'horizon': '13'}
        correctReturnedDict = {'observation': '42d0.0',  'op': 'adjust', 'height': '0', 'temperature': '72'
            , 'pressure': '1010', 'horizon' : 'natural'}

        parsedDict = DSP.getDefaultOptionalValues(entryDict)

        self.assertEquals(correctReturnedDict['observation'], parsedDict['observation']);
        self.assertEquals(correctReturnedDict['op'], parsedDict['op']);
        self.assertEquals(correctReturnedDict['height'], parsedDict['height']);
        self.assertEquals(correctReturnedDict['temperature'], parsedDict['temperature']);
        self.assertEquals(correctReturnedDict['pressure'], parsedDict['pressure']);
        self.assertEquals(correctReturnedDict['horizon'], parsedDict['horizon']);

    # Test checkObservationFormat
    def test202_201_ShouldReturnCheckObservationPass(self):
        observationInput = '30d1.5'
        self.assertEquals(True, DSP.checkObservationFormat(observationInput));

    def test202_202_ShouldReturnCheckObservationFail(self):
        observationInput = '301.5'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_203_ShouldReturnCheckObservationFail(self):
        observationInput = '30dd1.5'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_204_ShouldReturnCheckObservationFail(self):
        observationInput = '30d15'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_205_ShouldReturnCheckObservationFail(self):
        observationInput = '30d1..5'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_206_ShouldReturnCheckObservationFail(self):
        observationInput = '30d100.5'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_207_ShouldReturnCheckObservationFail(self):
        observationInput = '30d60.5'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_208_ShouldReturnCheckObservationPass(self):
        observationInput = '30d59.9'
        self.assertEquals(True, DSP.checkObservationFormat(observationInput));

    def test202_209_ShouldReturnCheckObservationFail(self):
        observationInput = '30d-0.5'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_210_ShouldReturnCheckObservationFail(self):
        observationInput = '30d0.-5'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_211_ShouldReturnCheckObservationFail(self):
        observationInput = '30d0.45'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_212_ShouldReturnCheckObservationFail(self):
        observationInput = '30d0.00'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_213_ShouldReturnCheckObservationFail(self):
        observationInput = '90d0.0'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_214_ShouldReturnCheckObservationFail(self):
        observationInput = '91d0.0'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_215_ShouldReturnCheckObservationPass(self):
        observationInput = '89d0.0'
        self.assertEquals(True, DSP.checkObservationFormat(observationInput));

    def test202_216_ShouldReturnCheckObservationFail(self):
        observationInput = '-01d0.0'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_217_ShouldReturnCheckObservationFail(self):
        observationInput = 'sd0.0'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_218_ShouldReturnCheckObservationFail(self):
        observationInput = '-d00.0g'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    def test202_219_ShouldReturnCheckObservationFail(self):
        observationInput = '001d0.0'
        self.assertEquals(False, DSP.checkObservationFormat(observationInput));

    # Test checkHeightFormat
    def test202_300_ShouldReturnCheckHeightPass(self):
        heightInput = '0'
        self.assertEquals(True, DSP.checkHeightFormat(heightInput));

    def test202_301_ShouldReturnCheckHeightPass(self):
        heightInput = '1'
        self.assertEquals(True, DSP.checkHeightFormat(heightInput));

    def test202_302_ShouldReturnCheckHeightPass(self):
        heightInput = '11111.111111'
        self.assertEquals(True, DSP.checkHeightFormat(heightInput));

    def test202_303_ShouldReturnCheckHeightFail(self):
        heightInput = '11111.1111.11'
        self.assertEquals(False, DSP.checkHeightFormat(heightInput));

    def test202_304_ShouldReturnCheckHeightFail(self):
        heightInput = 'b'
        self.assertEquals(False, DSP.checkHeightFormat(heightInput));

    def test202_305_ShouldReturnCheckHeightFail(self):
        heightInput = '-0.12'
        self.assertEquals(False, DSP.checkHeightFormat(heightInput));

    # Test checkTemperatureFormat
    def test202_400_ShouldReturnCheckTemperaturePass(self):
        temperatureInput = '-20'
        self.assertEquals(True, DSP.checkTemperatureFormat(temperatureInput));

    def test202_401_ShouldReturnCheckTemperaturePass(self):
        temperatureInput = '120'
        self.assertEquals(True, DSP.checkTemperatureFormat(temperatureInput));

    def test202_402_ShouldReturnCheckTemperaturePass(self):
        temperatureInput = '80'
        self.assertEquals(True, DSP.checkTemperatureFormat(temperatureInput));

    def test202_403_ShouldReturnCheckTemperatureFail(self):
        temperatureInput = '-80'
        self.assertEquals(False, DSP.checkTemperatureFormat(temperatureInput));

    def test202_404_ShouldReturnCheckTemperatureFail(self):
        temperatureInput = '80.0'
        self.assertEquals(False, DSP.checkTemperatureFormat(temperatureInput));

    def test202_405_ShouldReturnCheckTemperatureFail(self):
        temperatureInput = '121'
        self.assertEquals(False, DSP.checkTemperatureFormat(temperatureInput));

    def test202_406_ShouldReturnCheckTemperatureFail(self):
        temperatureInput = '-21'
        self.assertEquals(False, DSP.checkTemperatureFormat(temperatureInput));

    def test202_407_ShouldReturnCheckTemperatureFail(self):
        temperatureInput = 'b'
        self.assertEquals(False, DSP.checkTemperatureFormat(temperatureInput));

# Test checkPressureFormat
    def test202_500_ShouldReturnCheckPressurePass(self):
        pressureInput = '1100'
        self.assertEquals(True, DSP.checkPressureFormat(pressureInput));

    def test202_501_ShouldReturnCheckPressurePass(self):
        pressureInput = '100'
        self.assertEquals(True, DSP.checkPressureFormat(pressureInput));

    def test202_502_ShouldReturnCheckPressurePass(self):
        pressureInput = '500'
        self.assertEquals(True, DSP.checkPressureFormat(pressureInput));

    def test202_503_ShouldReturnCheckPressureFail(self):
        pressureInput = '-80'
        self.assertEquals(False, DSP.checkPressureFormat(pressureInput));

    def test202_504_ShouldReturnCheckPressureFail(self):
        pressureInput = '500.0'
        self.assertEquals(False, DSP.checkPressureFormat(pressureInput));

    def test202_505_ShouldReturnCheckPressureFail(self):
        pressureInput = '121'
        self.assertEquals(False, DSP.checkPressureFormat(pressureInput));

    def test202_506_ShouldReturnCheckPressureFail(self):
        pressureInput = '-21'
        self.assertEquals(False, DSP.checkPressureFormat(pressureInput));

    def test202_507_ShouldReturnCheckPressureFail(self):
        pressureInput = 'b'
        self.assertEquals(False, DSP.checkPressureFormat(pressureInput));


    def test202_001_DipShouldReturnZero(self):
        expectedNumber = 0
        self.assertEquals(expectedNumber, DSP.getDip({'observation': '42d0.0',  'op': 'adjust', 'height': '0', 'horizon': 'natural'}))
