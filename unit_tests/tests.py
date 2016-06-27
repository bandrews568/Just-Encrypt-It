import unittest
from codecs import encode, decode 

from main import EncryptText

class JustEncryptItTest(unittest.TestCase):

	def setUp(self):
		self.encrypt = EncryptText()
		#encrypted word: "test"
		#password:"test" 
		self.encrypted_128bit_str = "KVpSnAQB2bUp2OW4EXXmwQ==" 
		self.encrypted_rot13_str = "grfg"
		self.no_args_string = "(Select Encryption Type)"

	def test_encryptstring_rot13(self):
		"""
			ROT 13 encryption
			elif key == 'ROT 13'
		"""
		rot13_test = self.encrypt.encryptstring("test", "ROT 13")
		self.assertEqual(rot13_test, self.encrypted_rot13_str)

	def test_encryptstring_128bit(self):
		"""
			128 Bit Encryption
			elif key == '128 Bit' and len(pass_key) > 0:
		"""
		_128bit_test = self.encrypt.encryptstring("test", 
											"128 Bit", 
											pass_key = "test")
		self.assertEqual(_128bit_test, self.encrypted_128bit_str)

	def test_encryptstring_128bit_nopass(self):
		"""
			elif key == '128 Bit' and pass_key == "": 
		"""
		nopass_test = self.encrypt.encryptstring("test",
												"128 Bit",
												pass_key = "")
		self.assertEqual(nopass_test, None) 

	def test_encryptstring_no_args(self):
		"""
			*Else statement*
			No arguments passed
		"""
		no_args_test = self.encrypt.encryptstring(None, None, None)
		self.assertEqual(no_args_test, self.no_args_string)

	def test_decryptstring_rot13(self):
		"""
			ROT 13 decryption
			elif key == 'ROT 13'
		"""
		rot13_test = self.encrypt.decryptstring(self.encrypted_rot13_str, 
											"ROT 13")
		self.assertEqual(rot13_test, "test")

	def test_decryptstring_128bit(self):
		"""
			128 Bit decryption
			elif key == '128 Bit' and len(pass_key) > 0:
		"""
		_128bit_test = self.encrypt.decryptstring(self.encrypted_128bit_str, 
											"128 Bit", 
											pass_key = "test")
		self.assertEqual(_128bit_test, "test")

	def test_decryptstring_128bit_nopass(self):
		"""
			elif key == '128 Bit' and pass_key == "": 
		"""
		nopass_test = self.encrypt.decryptstring("test",
												"128 Bit",
												pass_key = "")
		self.assertEqual(nopass_test, None) 

	def test_encryptstring_no_args(self):
		"""
			*Else statement*
			No arguments passed
		"""
		no_args_test = self.encrypt.decryptstring(None, None, None)
		self.assertEqual(no_args_test, self.no_args_string)

	def test_paste_text(self):
		"""
			paste_text()
			else: return self.pasted_str
		"""
		from kivy.core.clipboard import Clipboard
		_clipboard = Clipboard.copy("test")
		test_paste = self.encrypt.paste_text()
		self.assertEqual(test_paste, "test")

	def test_paste_text_max(self):
		"""
			paste_text()
			if len(self.pasted_str) >= 1000:
		"""
		from kivy.core.clipboard import Clipboard
		_clipboard = Clipboard.copy("test" * 1000)
		test_paste = self.encrypt.paste_text()
		self.assertEqual(test_paste, "")

		
if __name__ == '__main__':
    unittest.main()
