# Initialize

import random

# future plans: add image file names for each card--upright, reversed, balanced.  Add 
card_info = [["The Usurper", "Upright Meaning", "Reversed Meaning"], 
             ["The Creator", "Nurture", "Abandonment"],
             ["The Defender", "Safety", "Peril"],
             ["The Lion", "The Body Prevails", "Weakness"],
             ["The Eagle", "The Mind Prevails", "Thoughtlessness"],
             ["The Fish", "The Soul Prevails", "Shallowness"],
             ["Spring", "New Growth", "Stagnation"],
             ["Summer", "Energy", "Exhaustion"],
             ["Autumn", "Plenty", "Want"],
             ["Winter", "Maturity", "Inexperience"],
             ["Overlooking The Diamond", "Failing to See Opportunity", "Recognizing Opportunity"],
             ["Sowing Stones", "Fruitless Labor", "Ceasing Fruitless Labor"],
             ["Fearing Shadows", "Unnecessary Fear", "Recognizing Safety"],
             ["Striking The Dragon's Tail", "Underestimating the Challenge", "Recognizing the Larger Problem"],
             ["Drowning In Armor", "Protective Measures Turn Dangerous", "True Prudence"],
             ["The Unicorn", "Purity", "Temptation"],
             ["The Griffin", "Valor", "Cowardice"],
             ["The Dragon", "Cunning", "Blind Fury"],
             ["The Satyr", "Indulgence", "Moderation"],
             ["The Cockatrice", "Corruption", "Recovery"],
             ["The Phoenix", "Rebirth", "Destruction"],
             ["The Fool", "Freedom", "Lack of Connection"],
             ["The Hermit", "Wisdom", "Isolation"],
             ["The Peasant", "Simple Strength", "Lack of Vision"],
             ["The Priestess", "Understanding Mysteries", "Impracticality"],
             ["The Smith", "Productivity", "Evil Effort"],
             ["The King", "Authority", "Tyrrany"],
             ["The Soldier", "Duty", "Blind Obedience"],
             ["Nature", "Life Energy", "Energy Sapped"],
             ["Fertility", "Growth", "Decline"],
             ["Knowledge", "Truth", "Falsehood"],
             ["Law", "Order", "Treachery"],
             ["Inspiration", "Creativity", "Lack of Imagination"],
             ["Trickery", "Deceit", "Subterfuge Revealed"],
             ["War", "Great Effort", "Effort Misspent"],
             ["Death", "Change", "Stasis"]]

deck = list(range(0,36))




def deal(num):
    '''(int) -> list
    
    Input is number of cards to deal.  Output is a list of cards taken from 'deck', including card name at index 0,
    orientation at index 1, and meaning(s) at index 2.  
    
    Checks if Usurper card, deck[1], is dealt and resets deck.
    
    Prerequisite: 0 < num < 37
    
    >>>deal(1)
    ['Fertility', 'Reversed', 'Decline']
    >>>deal(3)
    [['The Unicorn', 'Upright', 'Purity'], ['Summer', 'Upright', 'Energy'], ['The Creator', 'Reversed', 'Abandonment']]
    
    '''
    global deck
    hand = []
    reshuffle = False
    
    if len(deck) < num:
        print("There aren't that many cards left in the deck.  Here's what's left:")
        num = len(deck)
    
    for i in range(0,num):
    # 'index' as index for picking which remaining card in the deck; 'meaning' as index for upright/reversed
    # 'orientation' for the lanuage associated with 'meaning'

        index = random.randrange(0,len(deck))
        meaning = random.randrange(1,3)
        if meaning == 1:
            orientation = "Upright"
        else:
            orientation = "Reversed"
    
        dealt = deck.pop(index)
    
        # shuffle when Usurper is dealt
    
        if index == 0:
            reshuffle = True
            
        result = [card_info[dealt][0] + ", " + orientation + ": " + card_info[dealt][meaning]]
        
        hand.append(result)
        
    if reshuffle:
        deck = list(range(0,36))
    
    return hand
