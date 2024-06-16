class User:

    #fist_name = "имя"
    #last_name = "фамилия"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirstName(self):
            print("Моё имя", self.first_name)

    def sayLastName(self):
            print("Моя фамилия", self.last_name)

    def sayFirstAndLastName(self):
          print("Моё имя:", self.first_name, "Моя фамилия:", self.last_name)