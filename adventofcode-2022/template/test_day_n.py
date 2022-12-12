import unittest
import day_${number} as day

class TestDay_${number}(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

        self.DATA = '''\
'''

    def tearDown(self) -> None:
        super().tearDown()

    def test_quest_1(self):
        result = day.quest_1(self.DATA)
        self.assertEqual(result, None)

    def test_quest_2(self):
        result = day.quest_2(self.DATA)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()
