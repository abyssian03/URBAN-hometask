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
        for participant in self.participants:
            participant.distance = 0
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

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner('name')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner('name')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner('name1')
        runner2 = Runner('name2')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        self.all_results = []

    def setUp(self):
        global runner1, runner2, runner3

        runner1 = Runner('Usein', 10)
        runner2 = Runner('Andrew', 9)
        runner3 = Runner('Nik', 3)

    @classmethod
    def tearDownClass(self):
            for i in range(len(self.all_results)):
                print(self.all_results[i])

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        tournament1 = Tournament(90, runner1, runner3)
        tournament2 = Tournament(90, runner2, runner3)
        tournament3 = Tournament(90, runner1, runner2, runner3)
        self.all_results.append(tournament1.start())
        self.all_results.append(tournament2.start())
        self.all_results.append(tournament3.start())
        for i in range(3):
            last_place = max(self.all_results[i].keys())
            someone = self.all_results[i].get(last_place)
            self.assertTrue(runner3.__eq__(someone))

if __name__ == '__main__':
    unittest.main()