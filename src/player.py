class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, card):
        if type(card) == type([]):
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)
    
    def __str__(self):
        return f"Player, {self.name} has {len(self.all_cards)} card."