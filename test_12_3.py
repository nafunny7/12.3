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
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.man1 = Runner("Уссейн", 10)
        self.man2 = Runner("Андрей", 9)
        self.man3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for a, b in cls.all_result.items():
            print(f"{a} : {b}")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_round1(self):
        self.round1 = Tournament(90, self.man1, self.man3)
        rn1 = self.round1.start()
        self.all_result = rn1
        check_NIK = self.all_result[2].name
        self.assertTrue(check_NIK, self.man3.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_round2(self):
        self.round2 = Tournament(90, self.man2, self.man3)
        rn2 = self.round2.start()
        self.all_result = rn2
        check_NIK = self.all_result[2].name
        self.assertTrue(check_NIK, self.man3.name)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_round3(self):
        self.round3 = Tournament(90, self.man1, self.man2, self.man3)
        rn3 = self.round3.start()
        self.all_result = rn3
        check_NIK = self.all_result[3].name
        self.assertTrue(check_NIK, self.man3.name)


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        man = Runner("IVAN_GAV")
        for i in range(0, 10):
            man.walk()
        self.assertEqual(man.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        man = Runner("Nicola_Tesla")
        for i in range(0, 10):
            man.run()
        self.assertEqual(man.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenger(self):
        man1 = Runner("ISAK")
        man2 = Runner("POLYAK")
        for i in range(0, 10):
            man1.run()
            man2.walk()
        self.assertNotEqual(man1.distance, man2.distance)

if __name__ == "__main__":
    unittest.main()
