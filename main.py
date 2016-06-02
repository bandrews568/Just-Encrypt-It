
#qpy:2
#qpy:kivy

__version__ = '1.0'

import base64
from codecs import encode, decode

from Crypto.Cipher import AES

from kivy.app import App
from kivy.utils import platform
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel

if platform == 'android':
	from jnius import cast
	from jnius import autoclass		

class EncryptRoot(BoxLayout):
	pass

class EncryptText(BoxLayout):

	popup = Popup(title = 'Invalid Character',
				  title_align = 'center', 
				  content = Label(text = '''Not a valid character to encrypt.\n 
											Use only characters on the standard
								  			keyboard i.e no emojis'''),
				  auto_dimiss = False,
				  size_hint = (None, None),
				  size = (700, 700))

	password_popup = Popup(title = 'Password Max',
						   title_align = 'center',
						   content = Label(text = "Max length for a password\nis 16 characters."),
						   size_hint=(1.0, .4))

	def encryptstring(self, string, key, pass_key=None):
		if key != 'None' and key == 'ROT 13':
			encrypted_text = [encode(letter, 'rot13') for letter in string]
			encrypted_text = "".join(str(letter) for letter in encrypted_text)
			return encrypted_text

		elif key != 'None' and key == '128 Bit' and len(pass_key) > 0:
			if len(pass_key) > 16:
				self.password_popup.open()
			elif len(pass_key) < 16:
				difference = 16 - len(pass_key)
				pass_key = pass_key + ("x" * difference)
			BLOCK_SIZE = 16
			PADDING = '{'
			pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
			EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))	
			cipher = AES.new(pass_key)
			encoded = EncodeAES(cipher, string)
			return encoded

		else:
			return '(Select Encryption Type)'
		
	def decryptstring(self, string, key, pass_key=None):
		if key != 'None' and key == 'ROT 13':
			decrypted_text = [decode(letter, 'rot13') for letter in string]
			decrypted_text= "".join(str(value) for value in decrypted_text)
			return decrypted_text

		elif key != 'None' and key == '128 Bit' and len(pass_key) > 0:
			if len(pass_key):
				self.password_popup.open()
			elif len(pass_key) < 16:
				difference = 16 - len(pass_key)
				pass_key = pass_key + ("x" * difference)
			PADDING = '{'
			DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
			encryption = string
			cipher = AES.new(pass_key)
			decoded = DecodeAES(cipher, encryption)
			return decoded 

		else:
			return '(Select Encryption Type)'

	def share(self, data=None):
		if platform == 'android':
			if data: 
				PythonActivity = autoclass('org.renpy.android.PythonActivity') 
				Intent = autoclass('android.content.Intent')
				String = autoclass('java.lang.String')
				intent = Intent() 
				intent.setAction(Intent.ACTION_SEND)
				intent.putExtra(Intent.EXTRA_TEXT, \
					            cast('java.lang.CharSequence', \
					            String(data)))
				intent.setType('text/plain') 
				currentActivity = cast('android.app.Activity', \
					                   PythonActivity.mActivity)
				currentActivity.startActivity(intent) 
			else:
				return

class EncryptApp(App):
	pass

if __name__ == '__main__':
	EncryptApp().run()