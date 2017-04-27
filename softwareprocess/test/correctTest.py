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
