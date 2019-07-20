import unittest

import piglatin


class PigLatinTest(unittest.TestCase):

    def test_pig_latin_moves_consonant_to_end_of_word_and_appends_ay(self):
        self.assertEqual('arbay', piglatin.convert_word('bar'))
        self.assertEqual('oodfay', piglatin.convert_word('food'))

    def test_pig_latin_appends_way_to_words_beginning_with_vowel(self):
        self.assertEqual('appleway', piglatin.convert_word('apple'))

    def test_pig_latin_copes_when_first_letter_capitalised(self):
        self.assertEqual('Arbay', piglatin.convert_word('Bar'))
        self.assertEqual('Appleway', piglatin.convert_word('Apple'))

    def test_pig_latin_copes_when_entire_word_capitalized(self):
        self.assertEqual('ARBAY', piglatin.convert_word('BAR'))
        self.assertEqual('APPLEWAY', piglatin.convert_word('APPLE'))


if __name__ == '__main__':
    unittest.main()
