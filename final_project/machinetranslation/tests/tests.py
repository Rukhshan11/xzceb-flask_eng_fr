from ..translator import english_to_french, french_to_english
import unittest


class testTranslationEqual(unittest.TestCase):

    def test_null(self):
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(french_to_english(' '), ' ')

    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_question(self):
        self.assertEqual(english_to_french('How are You?'), 'Comment vous êtes?')
        self.assertEqual(french_to_english('Comment Vous estes?'), 'How are you?')


class testTranslationNotEqual(unittest.TestCase):
    def test_hello(self):
        self.assertNotEqual(english_to_french('Hello'), 'toi')
        self.assertNotEqual(french_to_english('Bonjour'), 'yo')

    def test_question(self):
        self.assertNotEqual(english_to_french('How are You?'), 'Comment êtes?')
        self.assertNotEqual(french_to_english('Comment oy?'), 'How are you?')
