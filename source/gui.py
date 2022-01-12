import PySimpleGUI as gui
from myDecorators import *
import threading
import time

""" Things I should probably do!
- Overhawl the searching algorithm to fit the new object style Listboxes.
- Think about how I can create objects. 
"""



# Class that defines how the main Graphical User Interface will be layed out and how it will interact with back-end and database.
class mainGUI():
    def __init__(self):
        # Initiate the oject with empty Listbox.
        self.objects = []
        
        # Define the layout of the main window
        self.mainLayout = [[gui.Text('Search for titles'), gui.Text('Search for dates', pad=(50, 2))],
                [gui.Input(size=(14, 1), enable_events=True, key='-TITLEINPUT-'), gui.Input(size=(14, 1), enable_events=True, key='-DATEINPUT-', pad=(40, 2))],
                [gui.Listbox(self.objects, size=(20, 4), enable_events=True, key='-LIST-', expand_x=True)],
                [gui.Button('AddINFO'), gui.Button('Exit')],
                [gui.Button("Remove")]
                ]

        self.window = gui.Window('QFinance - Main Page', self.mainLayout, size=(500, 400), resizable=True, finalize=True)
    
    # Append Object
    def appendObj(self, obj):
        self.objects.append(obj)
    
    # Overhawl this
    # Remove Object from Listbox and Dictionary of the GUI
    def removeObj(self, obj):
        self.objects.remove(obj)
        self.titles.remove(f"{obj.t_id} {obj.name}")

    # Opens up a window to collect information.
    def addINFOwindow(self, obj):
        obj.showWindow()
        obj.loopThrough()
        time.sleep(1)
        obj.hideWindow()
        
    # Event Loop
    @debug
    def loopThrough(self, addINFOobj):
        while True:
            event, values = self.window.read()
            if event in (gui.WIN_CLOSED, 'Exit'):
                break
            
            # Not working
            if values['-TITLEINPUT-'] != '':                         # if a keystroke entered in search field
                search = values['-TITLEINPUT-']
                new_values = [x for x in self.objects if search in x]  # do the filtering
                self.window['-LIST-'].update(new_values)     # display in the listbox

            # Not working
            elif values['-DATEINPUT-'] != '':
                search = values['-DATEINPUT-']
                new_values = [x for x in self.objects if search in x]
                self.window['-LIST-'].update(new_values)
            else:
                # display original unfiltered list
                self.window['-LIST-'].update(self.objects)

            # Not working
            # if a list item is chosen
            if event == '-LIST-' and len(values['-LIST-']):
                selected = values['-LIST-']
                print(f"Selected : {selected}")
                #print(f"Titles available : {self.titles}")
                print(f"Dictionary of objects: {self.objects}")

            # Not working
            # Removes object
            if event == 'Remove':
                self.titles.remove(" ".join(selected))
                self.objects.pop(selected[0][0])
                # display original unfiltered list
                self.window['-LIST-'].update(self.titles)

            # Opens a window to insert information
            if event == 'AddINFO':
                self.addINFOwindow(addINFOobj)
                
        self.window.close()

# Defying a blueprint window to gather information for main window.
class infoGatherer():
    def __init__(self):
        self.layout = [
            [gui.Text("Destination:"), gui.Input(size=(14, 1), key="-destinationINPUT-")],
            [gui.Text("Sender:"), gui.Input(size=(14, 1), key="-senderINPUT-")],
            [gui.Text("Amount:"), gui.Input(size=(14, 1), key="-amountINPUT-")],
            [gui.Text("Method:"), gui.Input(size=(14, 1), key="-methodINPUT-")],
            [gui.Text("Platform:"), gui.Input(size=(14, 1), key="-platformINPUT-")],
            [gui.Text("Date:"), gui.Input(size=(14, 1), key="-dateINPUT-")],
            [gui.Text("Reason:"), gui.Input(size=(14, 1), key="-reasonINPUT-")],
            [gui.Button("Exit"), gui.Button("Submit")]
            
        ]

        self.window = gui.Window("Insert Information", self.layout, finalize=True, disable_close=True)
        self.window.hide() # Initialize a window hidden.

    @debug
    def loopThrough(self):
        while True:
            event, values = self.window.read()
            if event in (gui.WIN_CLOSED, "Exit"): 
                break

            if event in "Submit":
                print(values) # returns a dictionary in form "Key" : "Value" ex: {"Destionation:" : "some input"}
                addInfo = self.getInput(values)
                #print(addInfo)

    @debug
    def hideWindow(self):
        self.window.hide() 

    @debug
    def showWindow(self):
        self.window.un_hide()

    def getInput(self, values): 
        for value in values:
            print(f"{value} : {values.get(value)}")
            
    
        
