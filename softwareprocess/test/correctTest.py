import unittest
import datetime
import softwareprocess.dispatch as DSP
import softwareprocess.conversionHelper as CH
import softwareprocess.adjustHelper as AH
import softwareprocess.predictHelper as PH

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
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
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
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
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
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_109_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'-89d59.9', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_110_ShouldReturnErrorInvalidLat(self):
        expectedString = {'error':'invalid lat', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'-1d59.9', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    # Test return of Invalid Long Input Errors
    def test100_200_ShouldNotReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(True, not('error' in DSP.dispatch(inputString)))

    def test100_200_ShouldReturnErrorInvalidLong(self):
        expectedString = {'error':'invalid long', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.6', 'altitude':'13d42.3',
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
        inputString = {'op':'correct', 'lat':'89d00.0', 'long':'95d41.62', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])
