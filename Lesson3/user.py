class User:
    
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printName(self):
        print(self.first_name)

    def printLast(self):
        print(self.last_name)

    def printFullName(self):
        print(self.first_name, self.last_name)

    