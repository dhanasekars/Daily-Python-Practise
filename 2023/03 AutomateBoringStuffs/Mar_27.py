"""
Created on : 27/03/23 2:53 pm
@author : ds  
"""

import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text("Some text in Row 1")],
          [sg.Text("Some text in Row 2")],
          [sg.InputText(key='-IN-')],
          [sg.InputText()],
          [sg.Button('OK'), sg.Button('Cancel')]]

window = sg.Window('Expense Tracker', layout)


event, values = window.read()
window.close()

sg.popup(f"You entered {values['-IN-']} first and then {values[0]}", title='Success')
