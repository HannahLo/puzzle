import unittest
import day_6 as day

class TestDay_6(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()

    def tearDown(self) -> None:
        super().tearDown()

    def test_quest_1(self):
        test_case = [
            ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
            ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
            ('nppdvjthqldpwncqszvftbrmjlhg', 6),
            ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
            ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11)
        ]

        for index, case in enumerate(test_case):
            with self.subTest(i=index):
                result = day.quest_1(case[0])
                self.assertEqual(result, case[1])

    def test_quest_2(self):
        test_case = [
            ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
            ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
            ('nppdvjthqldpwncqszvftbrmjlhg', 23),
            ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
            ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26)
        ]

        for index, case in enumerate(test_case):
            with self.subTest(i=index):
                result = day.quest_2(case[0])
                self.assertEqual(result, case[1])

if __name__ == "__main__":
    unittest.main()
