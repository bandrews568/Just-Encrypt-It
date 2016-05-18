#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

#TODO!
#Code in Kivy Popup if ascii character value not in range
#Popup and clock time an event, have it auto dismiss

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner 
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class EncryptRoot(BoxLayout):
	pass

class EncryptText(BoxLayout):
	decrypted_text = ObjectProperty()
	encrypted_text = ObjectProperty()
	encrypt_values = None
	key_value = None

	def encryptstring(self, string, key):
		if key != 'None':
			key_value = int(key)
			for letter in string:
				if ord(letter) not in range(32, 127):#change back to 32 after testing
					popup = Popup(title = 'Invalid Character',
								  content = Label(text = 'Not a valid character \
								  to encrypt.\n Use only characters on the standard  \
								  keyboard i.e no emojis'),
								  size_hint = (None, None),
								  size = (700, 700)) 
					popup.open()
					del string[-1] #HACK! Throws error but still deletes invaild character
					#Fix this tommorow!!!
					
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
		else:
			return '(Select encryption key)'
		

	def decryptstring(self, string, key):
		decrypt_values = [value - key for value in encrypt_values]
		#Finish this up! Kv file is already updated and ready to go

class EncryptApp(App):
	pass

if __name__ == '__main__':
	EncryptApp().run()