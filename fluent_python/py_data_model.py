# Python class methods demonstrating _ _ getitem __ and _ _ len _ _ magic methods.

# Deck of cards

Card = ['spades', 'hearts', 'diamonds', 'king', 'queen', 'joker']

class FrenchDeck:
    _list = []

    def __init__(self, list_ds):
        self._list = list_ds
    
    def __getitem__(self, position):
        return self._list[position]
    
    def __len__(self):
        return len(self._list)
        
trial = FrenchDeck(Card)
print(len(trial))
print(trial[4])

