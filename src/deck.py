import random
from src.card import suits, ranks, values, Card

class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_cards = Card(suit, rank)
                self.all_cards.append(created_cards)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()