#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config
from src.question_a.question_a import use_global

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_use_global(self):
        self.assertEqual(use_global(10), 110)
        self.assertEqual(use_global(5), 105)


