import source
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='UTF-8', format='%(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rn = source.Runner('George', speed=-5)
            for i in range(10):
                rn.walk()
            self.assertEqual(rn.distance, 50)
            logging.info(msg='"test_walk" выполнен успешно', exc_info=True)
        except ValueError as err:
            logging.warning(msg='Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            rn = source.Runner(65)
            for i in range(10):
                rn.run()
            self.assertEqual(rn.distance, 100)
            logging.info(msg='"test_run" выполнен успешно', exc_info=True)
        except:
            logging.warning(msg='Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rn1 = source.Runner('Semen')
        rn2 = source.Runner('Denis')
        for i in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)


if __name__ == '__main__':

    unittest.main()
