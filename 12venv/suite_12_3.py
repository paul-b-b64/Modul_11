import tests_12_1
import tests_12_2
import unittest

nabor_testov = unittest.TestSuite()
nabor_testov.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
nabor_testov.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(nabor_testov)
