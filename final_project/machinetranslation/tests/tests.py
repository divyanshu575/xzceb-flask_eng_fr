import unittest

from translator import english_to_french, french_to_english

class testE2F(unittest.TestCase):

	def test1(self):
		
		self.assertNotEqual(english_to_french("None"), '')
		self.assertEqual(english_to_french('Hello'), 'Bonjour')
		self.assertNotEqual(english_to_french(0), 0)

class testF2E(unittest.TestCase):

	def test1(self):
		
		self.assertNotEqual(french_to_english("None"), '')
		self.assertEqual(french_to_english('Bonjour'), 'Hello')
		self.assertNotEqual(french_to_english(0), 0)
    
unittest.main()
