class Address:

    def __init__(self, index, city, street, number_home, number_appartment):
        self.index = index
        self.city = city
        self.street = street
        self.home = number_home
        self.appartment = number_appartment
    
    def __str__(self):
        return f'{self.index}, {self.city}, {self.street}, {self.home}, {self.appartment}'
