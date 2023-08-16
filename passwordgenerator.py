import random 
import string 
import PySimpleGUI as sg

upper=random.sample(string.ascii_uppercase,2)
lower=random.sample(string.ascii_lowercase,2)
digits=random.sample(string.digits,2)
symobls=random.sample(string.punctuation,2)

total=upper+lower+digits+symobls
total=random.sample(total,len(total))
total=''.join(total)
print(total)


layout=[
    
    [sg.Text('uppercase:'),sg.Input()],
    [sg.Text('lowercase:'),sg.Input()],
    [sg.Text('Digits:'),sg.Input()],
    [sg.Text('Symbols:'),sg.Input()],
    [sg.Button('ok:'),sg.Button()],
    [sg.Text('password:'),sg.multiline()]
]
window=sg.window('Password Generator',layout)

window.read()


window.close()

