import unittest
import day_1

data = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

'''

class TestDay_1(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_quest_1(self):
        result = day_1.quest_1(data)
        self.assertEqual(result, 24000)

    def test_quest_2(self):
        result = day_1.quest_2(data)
        self.assertEqual(result, 45000)

if __name__ == "__main__":
    unittest.main()
