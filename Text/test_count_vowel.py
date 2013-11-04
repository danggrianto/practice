import unittest
from count_vowel import count_vowel


class CountVowelTest(unittest.TestCase):
    def count_only_vowels_test(self):
        word = 'a'*5
        self.assertEqual(count_vowel(word), 5)

    def count_only_consonant_test(self):
        word = 'b'*5
        self.assertEqual(count_vowel(word), 0)

    def word_with_space_test(self):
        word = 'a b'
        self.assertEqual(count_vowel(word), 1)
