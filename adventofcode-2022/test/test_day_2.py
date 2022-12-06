import unittest
import day_2

data = '''\
A Y
B X
C Z
'''

class TestDay_2(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_quest_1(self):
        result = day_2.quest_1(data)
        self.assertEqual(result, 15)

    def test_quest_2(self):
        result = day_2.quest_2(data)
        self.assertEqual(result, 12)
        pass

if __name__ == "__main__":
    unittest.main()
