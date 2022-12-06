import unittest
import day_3

data = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

class TestDay_3(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_quest_1(self):
        result = day_3.quest_1(data)
        self.assertEqual(result, 157)

    def test_quest_2(self):
        result = day_3.quest_2(data)
        self.assertEqual(result, 70)

if __name__ == "__main__":
    unittest.main()
