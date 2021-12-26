class something():
    def __init__(self):
        self.name = "nothing"

    def changeName(self):
        self.name = "this"

thisClass = something()
thisClass.changeName()

print(thisClass.name)