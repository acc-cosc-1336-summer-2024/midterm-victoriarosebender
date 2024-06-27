#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_a.question_a import use_global
from src.question_b.question_b import get_random_number

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_use_global(self):
        self.assertEqual(use_global(10), 110)
        self.assertEqual(use_global(5), 105)

    def test_get_random_number(self):
        result_num = get_random_number()
        self.assertTrue(1 <= result_num <= 5, f"Generated number {result_num} is not within range [1, 5]")


