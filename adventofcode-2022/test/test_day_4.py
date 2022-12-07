import unittest
import day_4 as day

data = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

class TestDay_4(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_quest_1(self):
        result = day.quest_1(data)
        self.assertEqual(result, 2)

    def test_quest_2(self):
        result = day.quest_2(data)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()
