import copy
import re

class Card:
    color = 0
    symbol = ''
    shading = ''
    number = 0

    def __init__(self, color, shade):
        self.color = color
        self.shading = shade
        self.symbol = shade[0]
        self.number = len(shade)

#All the checks that take 3 parameters as input
def Color(card1, card2, card3):
    if len(set([card1.color, card2.color, card3.color])) == 2:
        return False
    return True 

def Symbol(card1, card2, card3):
    if len(set([card1.symbol, card2.symbol, card3.symbol])) == 2:
        return False
    return True

def Number(card1, card2, card3):
    if len(set([card1.number, card2.number, card3.number])) == 2:
        return False
    return True

def Case(card1, card2, card3):
    case = {'a' : 1, 's' : 1, 'h' : 1, 'A' : 2, 'S' : 2, 'H' : 2, '@' : 3, '$' : 3, '#' : 3}
    if len(set([case[card1.symbol], case[card2.symbol], case[card3.symbol]])) == 2:
        return False
    return True

def Type(card1, card2, card3):
    type = {'a' : 1, 'A' : 1, '@' : 1, 's' : 2, 'S' : 2, '$' : 2, 'h' : 3, 'H' : 3, '#' : 3}
    if len(set([type[card1.symbol], type[card2.symbol], type[card3.symbol]])) == 2:
        return False
    return True

def getCards():
    cards = []
    data = []

    f = open('input.txt', 'r')
    lines = f.readlines()[1:]
    for line in lines:
        data.append(line.rstrip())
    f.close()

    for val in data:
        curr = val.split()
        cards.append(Card(curr[0], curr[1]))
    
    return cards

def isSet(cards, i,j,k):
    flag = True
    if not Color(cards[i], cards[j], cards[k]):
        flag = False
    if not Symbol(cards[i], cards[j], cards[k]):
        flag = False
    if not Number(cards[i], cards[j], cards[k]):
        flag = False
    if not Case(cards[i], cards[j], cards[k]):
        flag = False
    if not Type(cards[i], cards[j], cards[k]):
        flag = False
    return flag

sets = {}

#disjoint set counter
max_count = 0

#stores IDs of sets which are maximally independent
maxIndSet = []


cards = getCards()

idx = 0
for i in range(len(cards)):
    for j in range(i+1):
        for k in range(j+1):
            if isSet(cards,i,j,k) and i != j and i != k and j != k: #The sets dictionary now contains key(whichever set such as first set) and value(idxs of cards in the set)
                sets[idx] = sets.get(idx, []) + [i]
                sets[idx] = sets.get(idx, []) + [j]
                sets[idx] = sets.get(idx, []) + [k]
                idx += 1

print(sets)
print(idx)

