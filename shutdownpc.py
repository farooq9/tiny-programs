# program to shutdown pc
#This program asks the user to enter pin to shutdown pc
import pyautogui as po
import os

options = po.confirm('Do you want to shutdown pc?', buttons= ['Yes', 'No'])
pin = '1234' #This is the correct pin

if options == 'Yes':
    a = po.password('Enter pin to Shutdown PC')
    if a == pin:
        print('pc is shutting down in 5 seconds')
        os.system('shutdown /s /t 5')
    else:

        po.alert('Your pin is Incorrect\nPlease keep practicing Python')
else:
    po.alert('Your pc is not gonna shutdown.')
    exit()

print(f'Your pin:{a}\nSystem pin {pin} ')
