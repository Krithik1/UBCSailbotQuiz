from AngleCalc import AngleCalc
import unittest

class TestAngleCalcMethods(unittest.TestCase):
    
    def testboundTo180(self):
        self.assertEqual(AngleCalc().boundTo180(-450),-90)
        self.assertEqual(AngleCalc().boundTo180(270),-90)
    
    def testisAngleBetween(self):
        self.assertTrue(AngleCalc().isAngleBetween(-90,-180,110))
        self.assertFalse(AngleCalc().isAngleBetween(-90,-180,80))

if __name__ == '__main__':
    unittest.main()