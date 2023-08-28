
class Card:
    # при таком раскладе мы можем только читать св-ва класса
    # карты: валет, дама, король, туз
    list_a = [6, 7, 8, 9, 10, 'jack', 'queen', 'king' ,'ace']
    # Масть карты: черви, пики, бубны, трефы
    list_b = ['hearts', 'spades', 'diamonds', 'clubs']
 
    def __init__(self):
        self.deck = [([i,y]) for i in self.list_a for y in self.list_b] #[]

    #def create_deck(self):
    #    self.deck = [str([i,y]) for i in self.list_a for y in self.list_b]

    def show_deck(self):
        print(f'Create_deck: {self.deck}')

a = Card()   
