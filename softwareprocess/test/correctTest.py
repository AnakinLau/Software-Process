import unittest
import datetime
import softwareprocess.dispatch as DSP
import softwareprocess.conversionHelper as CH
import softwareprocess.adjustHelper as AH
import softwareprocess.predictHelper as PH
import softwareprocess.correctHelper as OH

import math

class correctTest(unittest.TestCase):

    def test100_000_ShouldReturnParameterIsMissing(self):
        expectedString = {'error' : 'parameter is missing'}
        #self.assertIsInstance(DSP.dispatch())
        # additional tests are for boundary value coverage
        #self.assertIsInstance(SM.Sample(2), SM.Sample)
        #self.assertIsInstance(SM.Sample(29), SM.Sample)
        self.assertEquals(expectedString, DSP.dispatch())

    def test100_010_ShouldReturnMandatoryInfoIsMissing(self):
        expectedString = {'error':'mandatory information is missing', 'op': 'correct'}
        self.assertEquals(expectedString['error'], DSP.dispatch({'op': 'correct'})['error'])

    def test100_011_ShouldReturnMandatoryInfoIsMissingLat(self):
        expectedString = {'error':'mandatory information is missing', 'op': 'correct'}
        inputString = {'op':'correct', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_012_ShouldReturnMandatoryInfoIsMissingLong(self):
        expectedString = {'error':'mandatory information is missing', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d32.3', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_013_ShouldReturnMandatoryInfoIsMissingAlt(self):
        expectedString = {'error':'mandatory information is missing', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95.41.6',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_014_ShouldReturnMandatoryInfoIsMissingAssLat(self):
        expectedString = {'error':'mandatory information is missing', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_015_ShouldReturnMandatoryInfoIsMissingAssLong(self):
        expectedString = {'error':'mandatory information is missing', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_016_ShouldNotReturnMandatoryInfoIsMissing(self):
        expectedString = {'error':'mandatory information is missing', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    # Test return of Invalid Lat Input Errors
    def test100_100_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'90d00.0', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_101_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'-90d00.0', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_102_ShouldReturnNoErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_103_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d322.3', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_104_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d32.35', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_105_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d60.0', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_106_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d-0.1', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_107_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d-1.1', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_108_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d59.9', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_109_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'-89d59.9', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_110_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'-1d59.9', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    # Test return of Invalid Long Input Errors
    def test100_200_ShouldNotReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_200_ShouldReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d416', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])


    def test100_201_ShouldReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'360d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])


    def test100_202_ShouldReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'-0d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])


    def test100_203_ShouldReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d60.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])


    def test100_204_ShouldReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d-2.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])


    def test100_205_ShouldReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d91.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])


    def test100_206_ShouldReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.62', 'altitude':'013d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    # Test return of Invalid Altitude Input Errors
    def test100_300_ShouldNotReturnErrorInvalidAltitude(self):
        expectedString = {'error':'invalid altitude', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong': '74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_301_ShouldReturnErrorInvalidAltitude(self):
        expectedString = {'error':'invalid altitude', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'90d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_302_ShouldReturnErrorInvalidAltitude(self):
        expectedString = {'error':'invalid altitude', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'0d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_303_ShouldReturnErrorInvalidAltitude(self):
        expectedString = {'error':'invalid altitude', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'1d60.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_304_ShouldReturnErrorInvalidAltitude(self):
        expectedString = {'error':'invalid altitude', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'1d-00.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_305_ShouldReturnErrorInvalidAltitude(self):
        expectedString = {'error':'invalid altitude', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'1d09.33',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_306_ShouldReturnErrorInvalidAltitude(self):
        expectedString = {'error':'invalid altitude', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'-1d09.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    # Test return of Invalid AssumedLat Input Errors
    def test100_400_ShouldNotReturnErrorInvalidAssumedLat(self):
        expectedString = {'error':'invalid assumedLat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong': '74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_401_ShouldReturnErrorInvalidAssumedLat(self):
        expectedString = {'error':'invalid assumedLat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-90d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_402_ShouldReturnErrorInvalidAssumedLat(self):
        expectedString = {'error':'invalid assumedLat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'90d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_403_ShouldNotReturnErrorInvalidAssumedLat(self):
        expectedString = {'error':'invalid assumedLat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-0d38.4', 'assumedLong':'74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    # Test return of Invalid AssumedLong Input Errors
    def test100_500_ShouldNotReturnErrorInvalidAssumedLong(self):
        expectedString = {'error':'invalid assumedLong', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_501_ShouldReturnErrorInvalidAssumedLong(self):
        expectedString = {'error':'invalid assumedLong', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'-0d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_502_ShouldReturnErrorInvalidAssumedLong(self):
        expectedString = {'error':'invalid assumedLong', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'-1d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_503_ShouldReturnErrorInvalidAssumedLong(self):
        expectedString = {'error':'invalid assumedLong', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'360d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])

    def test100_504_ShouldNotReturnErrorInvalidAssumedLong(self):
        expectedString = {'error':'invalid assumedLong', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':'0d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    # Calculation Portion
    # Test return of getLHA
    def test200_000_ShouldReturnTrueGetLHA(self):
        expectedString = '170d17.0'
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong': '74d35.3'}
        stringAnsw = OH.getLHA(inputString)

        self.assertAlmostEqual(CH.convertDegMinStrToNumber(expectedString),
                               CH.convertDegMinStrToNumber(stringAnsw),
                               delta=0.0035)
        #self.assertEquals(expectedString, OH.getLHA(inputString))

    def test200_001_ShouldReturnTrueGetLHA(self):
        expectedString = '228d40.7'
        inputString = {'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',
                       'assumedLat':'35d59.7', 'assumedLong': '74d35.3'}
        stringAnsw = OH.getLHA(inputString)

        self.assertAlmostEqual(CH.convertDegMinStrToNumber(expectedString),
                               CH.convertDegMinStrToNumber(stringAnsw),
                               delta=0.0035)

    # Test return of getLHA
    def test200_010_ShouldReturnTrueGetInterDist(self):
        expectedString = -0.789
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong': '74d35.3'}
        stringLHA = OH.getLHA(inputString)
        self.assertAlmostEqual(expectedString,
                               OH.getInterDist(inputString, stringLHA),
                               delta=0.0035)

    def test200_011_ShouldReturnTrueGetInterDist(self):
        expectedString = 0.581474856
        inputString = {'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',
                       'assumedLat':'35d59.7', 'assumedLong': '74d35.3'}
        stringLHA = OH.getLHA(inputString)
        self.assertAlmostEqual(expectedString,
                               OH.getInterDist(inputString, stringLHA),
                               delta=0.0015)

    # Test return of getCorrectedAltitude
    def test200_020_ShouldReturnTrueGetCorrectedAltitude(self):
        expectedString = '-52d07.8'
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong': '74d35.3'}
        stringLHA = OH.getLHA(inputString)
        interDist = OH.getInterDist(inputString, stringLHA)
        correctedAlt = OH.getCorrectedAltitude(interDist)
        self.assertAlmostEqual(CH.convertDegMinStrToNumber(expectedString),
                               CH.convertDegMinStrToNumber(correctedAlt),
                               delta=0.0025)

    def test200_021_ShouldReturnTrueGetCorrectedAltitude(self):
        expectedString = '35d33.3'
        inputString = {'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',
                       'assumedLat':'35d59.7', 'assumedLong': '74d35.3'}
        stringLHA = OH.getLHA(inputString)
        interDist = OH.getInterDist(inputString, stringLHA)
        correctedAlt = OH.getCorrectedAltitude(interDist)
        self.assertAlmostEqual(CH.convertDegMinStrToNumber(expectedString),
                               CH.convertDegMinStrToNumber(correctedAlt),
                               delta=0.0025)

    # Test return of getCorrectedDistance
    def test200_030_ShouldReturnTrueGetCorrectedDistance(self):
        expectedString = 104
        inputString = {'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',
                       'assumedLat':'35d59.7', 'assumedLong': '74d35.3'}
        stringLHA = OH.getLHA(inputString)
        interDist = OH.getInterDist(inputString, stringLHA)
        correctedAlt = OH.getCorrectedAltitude(interDist)
        correctedDist = OH.getCorrectedDistance(inputString, correctedAlt)

        self.assertAlmostEqual(expectedString,
                               int(correctedDist),
                               delta=0.0025)

    # Test return of getCorrectedAzimuth
    def test200_040_ShouldReturnTrueGetCorrectedAzimuth(self):
        expectedString = '0d36.8'
        inputString = {'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',
                       'assumedLat':'35d59.7', 'assumedLong': '74d35.3'}
        stringLHA = OH.getLHA(inputString)
        interDist = OH.getInterDist(inputString, stringLHA)
        correctedAlt = OH.getCorrectedAltitude(interDist)
        azimuth = OH.getCorrectedAzimuth(inputString, interDist)
        self.assertAlmostEqual(CH.convertDegMinStrToNumber(expectedString),
                               CH.convertDegMinStrToNumber(azimuth),
                               delta=0.0015)
