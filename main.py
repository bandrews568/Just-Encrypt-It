__version__ = '0.2'

import base64
from codecs import encode, decode

from Crypto.Cipher import AES

from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window 
from kivy.uix.spinner import Spinner 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.properties import ObjectProperty

if platform == 'android':
	from jnius import cast
	from jnius import autoclass	

class EncryptRoot(BoxLayout):
	pass


class EncryptText(BoxLayout):

	def encryptstring(self, string, key, pass_key=None):
		if key == 'ROT 13':
			encrypted_text = [encode(letter, 'rot13') for letter in string if \
							  ord(letter) in range(32, 127)]
			encrypted_text = "".join(str(letter) for letter in encrypted_text)
			return encrypted_text

		elif key == '128 Bit' and len(pass_key) > 0:
			if len(pass_key) > 16:
				Window.release_all_keyboards()
				MaxPassPopup().open()
			elif len(pass_key) < 16:
				#Add filler bits to password 
				pass_key = pass_key + ("x" * (16 - len(pass_key)))
			block_size = 16
			padding = '{'
			pad = lambda s: s + (block_size - len(s) % block_size) * padding
			EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))	
			cipher = AES.new(pass_key)
			encoded = EncodeAES(cipher, encode(string, 'utf-8'))
			return encoded

		elif key == '128 Bit':
			NoPassPopup().open()

		else:
			return '(Select Encryption Type)'
		
	def decryptstring(self, string, key, pass_key=None):
		if key == 'ROT 13':
			decrypted_text = [decode(letter, 'rot13') for letter in string if \
							  ord(letter) in range(32, 127)]
			decrypted_text= "".join(str(value) for value in decrypted_text)
			return decrypted_text

		elif key == '128 Bit' and len(pass_key) > 0:
			if len(pass_key) > 16:
				Window.release_all_keyboards()
				MaxPassPopup().open()
			elif len(pass_key) < 16:
				#Add filler bits to password
				pass_key = pass_key + ("x" * (16 - len(pass_key)))
			padding = '{'
			DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(padding)
			cipher = AES.new(pass_key)
			decoded = DecodeAES(cipher, string)
			return decoded

		elif key == '128 Bit':
			#Remind user to enter a password
			NoPassPopup().open()

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
				intent.putExtra(Intent.EXTRA_TEXT, 
					            cast('java.lang.CharSequence', 
					            String(data)))
				intent.setType('text/plain') 
				currentActivity = cast('android.app.Activity', 
					                   PythonActivity.mActivity)
				currentActivity.startActivity(intent) 

class NoPassPopup(Popup):
	pass

class MaxPassPopup(Popup):
	pass

class EncryptApp(App):
	pass
		
if __name__ == '__main__':	
	EncryptApp().run()
