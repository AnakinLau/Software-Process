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

    def test100_011_ShouldReturnMandatoryInfoIsMissing(self):
        expectedString = {'error':'mandatory information is missing', 'op': 'correct'}
        inputString = {'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',
                       'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertEquals(expectedString['error'], DSP.dispatch(inputString)['error'])
