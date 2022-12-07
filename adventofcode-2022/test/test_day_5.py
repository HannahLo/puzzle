import unittest
import day_5 as day

data = '''\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

class TestDay_1(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_quest_1(self):
        result = day.quest_1(data)
        self.assertEqual(result, 'CMZ')

    def test_quest_2(self):
        result = day.quest_2(data)
        self.assertEqual(result, 'MCD')

if __name__ == "__main__":
    unittest.main()
