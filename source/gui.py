import PySimpleGUI as gui
from myDecorators import *

# Class that defines how the main Graphical User Interface will be layed out and how it will interact with back-end and database.
class GUI():
    def __init__(self):
        # Initiate the oject with empty Listbox.
        self.titles = []
        self.objects = {}

        self.layout = [[gui.Text('Search for titles'), gui.Text('Search for dates', pad=(50, 2))],
                [gui.Input(size=(14, 1), enable_events=True, key='-TITLEINPUT-'), gui.Input(size=(14, 1), enable_events=True, key='-DATEINPUT-', pad=(40, 2))],
                [gui.Listbox(self.titles, size=(20, 4), enable_events=True, key='-LIST-', expand_x=True)],
                [gui.Button('Chrome'), gui.Button('Exit')],
                [gui.Button("Remove")]
                ]

        self.window = gui.Window('QFinance - Main Page', self.layout, size=(500, 400), resizable=True)
    
    # Append Object
    def appendObj(self, obj):
        self.objects[str(obj.t_id)] = obj
        self.titles.append(f"{obj.t_id} {obj.name}")
    
    # Remove Object from Listbox and Dictionary of the GUI
    def removeObj(self, obj):
        self.objects.remove(obj)
        self.titles.remove(f"{obj.t_id} {obj.name}")

        
    # Event Loop
    @debug
    def loopThrough(self):
        while True:
            event, values = self.window.read()
            if event in (gui.WIN_CLOSED, 'Exit'):
                break
            if values['-TITLEINPUT-'] != '':                         # if a keystroke entered in search field
                search = values['-TITLEINPUT-']
                new_values = [x for x in self.titles if search in x]  # do the filtering
                self.window['-LIST-'].update(new_values)     # display in the listbox
            elif values['-DATEINPUT-'] != '':
                search = values['-DATEINPUT-']
                new_values = [x for x in self.titles if search in x]
                self.window['-LIST-'].update(new_values)
            else:
                # display original unfiltered list
                self.window['-LIST-'].update(self.titles)

            # if a list item is chosen
            if event == '-LIST-' and len(values['-LIST-']):
                selected = values['-LIST-']
                print(f"Selected : {selected}")
                print(f"Titles available : {self.titles}")
                print(f"Dictionary of objects: {self.objects}")

            # Removes object
            if event == 'Remove':
                self.titles.remove(" ".join(selected))
                self.objects.pop(selected[0][0])
                # display original unfiltered list
                self.window['-LIST-'].update(self.titles)


        self.window.close()