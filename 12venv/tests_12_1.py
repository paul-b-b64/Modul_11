import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn = Runner('George')
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn = Runner('George')
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)
    def test_challenge(self):
        rn1 = Runner('Semen')
        rn2 = Runner('Denis')
        for i in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)

if __name__ == '__main__':
    unittest.main()

