import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global all_results
        all_results = []

    def setUp(self):
        self.rn1 = Runner('Усэйн', 10)
        self.rn2 = Runner('Андрей', 9)
        self.rn3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(*all_results, sep='\n')

    def test_1(self):
        global all_results
        loc_result = {}
        tour = Tournament(90, self.rn1, self.rn3)
        loc_result = tour.start()
        all_results.append(loc_result)
        self.assertTrue(loc_result[max(loc_result.keys())] == 'Ник')

    def test_2(self):
        global all_results
        loc_result = {}
        tour = Tournament(90, self.rn2, self.rn3)
        loc_result = tour.start()
        all_results.append(loc_result)
        self.assertTrue(loc_result[max(loc_result.keys())] == 'Ник')

    def test_3(self):
        global all_results
        loc_result = {}
        tour = Tournament(90, self.rn1, self.rn2, self.rn3)
        loc_result = tour.start()
        all_results.append(loc_result)
        self.assertTrue(loc_result[max(loc_result.keys())] == 'Ник')

    def test_4(self):  # дополнительные два теста, проверяют Усэйна и Андрея
        global all_results
        loc_result = {}
        tour = Tournament(90, self.rn1, self.rn2)
        loc_result = tour.start()
        all_results.append(loc_result)
        self.assertTrue(loc_result[max(loc_result.keys())] == 'Андрей')

    def test_5(self):  # в этом тесте Андрей приходит первый, хотя бежит медленнее
        global all_results
        loc_result = {}
        tour = Tournament(90, self.rn2, self.rn1)
        loc_result = tour.start()
        all_results.append(loc_result)
        self.assertTrue(loc_result[max(loc_result.keys())] == 'Андрей')

    if __name__ == '__main__':
        unittest.main()
