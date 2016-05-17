#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

#TODO!
#Code in Kivy Popup if ascii character value not in range
#Popup and clock time an event, have it auto dismiss



import re

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner 
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup

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
			for letter in string:
				if ord(letter) not in range(33, 127):
					pass
			ascii_values = [ord(letter) for letter in string]
			encrypt_values =[]
			for item in ascii_values:
				if int(item + key_value) > 125:
					#Fixes 'start byte' error thrown by kivy
					encrypt_values.append(item)
				else:
					encrypt_values.append(int(item) + key_value)

			encrypt_values = [chr(item) for item in encrypt_values]
			encrypt_values = "".join(str(value) for value in encrypt_values)
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