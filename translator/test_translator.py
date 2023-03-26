import unittest

class TestTranslations(unittest.TestCase):
    
    def test_french_to_english(self):
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')
        
        result = french_to_english('Comment ça va?')
        self.assertNotEqual(result, 'How are you?')
        
    def test_english_to_french(self):
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')
        
        result = english_to_french('How are you?')
        self.assertNotEqual(result, 'Comment ça va?')
