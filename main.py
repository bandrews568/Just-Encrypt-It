from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner 

class EncryptRoot(BoxLayout):
	pass

class EncryptText(BoxLayout):
	decrypted_text = ObjectProperty()
	encrypted_text = ObjectProperty()
	encrypt_radio = ObjectProperty()
	decrypt_radio = ObjectProperty()
	encrypt_values = None
	key_value = None

	def encryptstring(self, string, key):
		if key != 'None':
			key_value = int(key)
			ascii_values = [ord(letter) for letter in string]
			encrypt_values = [int(item + key_value) for item in ascii_values]
			encrypt_values = [chr(item) for item in encrypt_values]
			encrypt_values = "".join(str(value).strip("[],") for value in encrypt_values)
			return encrypt_values
			#BUG: key: 6 and character == 'y'
		else:
			return '(Select encryption key)'
		

	def decryptstring(self, string, key):
		decrypt_values = [value - key for value in encrypt_values]

class EncryptApp(App):
	pass

if __name__ == '__main__':
	EncryptApp().run()