import unittest
import test_12_3


testik = unittest.TestSuite()
testik.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
testik.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))

cool = unittest.TextTestRunner(verbosity=2)
cool.run(testik)

