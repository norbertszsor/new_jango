import chucknorris.quips as q

class norris:
    def __init__(self,name):
        self.name = name
    def wypisz(self):
        {
            print(q.random(self.name))
        }