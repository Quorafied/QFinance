import PySimpleGUI as gui

# Class that defines how the main Graphical User Interface will be layed out and how it will interact with back-end and database.
class GUI():
    def __init__(self):
        # Initiate the oject with empty Listbox.
        self.titles = []

        self.layout = [[gui.Text('Search for titles')],
                [gui.Input(size=(20, 1), enable_events=True, key='-INPUT-')],
                [gui.Listbox(self.titles, size=(20, 4), enable_events=True, key='-LIST-', expand_x=True)],
                [gui.Button('Chrome'), gui.Button('Exit')]]

        self.window = gui.Window('QFinance - Main Page', self.layout, size=(200, 800), resizable=True, )
        
    # Event Loop
    def loopThrough(self):
        while True:
            event, values = self.window.read()
            if event in (gui.WIN_CLOSED, 'Exit'):                # always check for closed window
                break
            if values['-INPUT-'] != '':                         # if a keystroke entered in search field
                search = values['-INPUT-']
                new_values = [x for x in self.titles if search in x]  # do the filtering
                self.window['-LIST-'].update(new_values)     # display in the listbox
            else:
                # display original unfiltered list
                self.window['-LIST-'].update(self.titles)
            # if a list item is chosen
            if event == '-LIST-' and len(values['-LIST-']):
                gui.popup('Selected ', values['-LIST-'])

        self.window.close()