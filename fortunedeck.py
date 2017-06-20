
# coding: utf-8

# In[18]:

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
    
    Checks if Usurper card, deck[0], is dealt and resets deck.
    
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
    
    print(hand)

def fortunedeck():
    '''() -> list of [str] 

    Prompt the player to enter a command and return an appropriate response.  See "help" command text for more.
    
    >>> nnb
    [['Winter, Reversed: Inexperience'],
     ['Sowing Stones, Reversed: Ceasing Fruitless Labor'],
     ['War, Balanced: Great Effort vs. Effort Misspent']]
 
    >>> bnnnnn
    [['The Smith, Balanced: Productivity vs. Evil Effort'],
     ['The Satyr, Reversed: Moderation'],
     ['The King, Reversed: Tyrrany'],
     ['Fertility, Upright: Growth'],
     ["Striking The Dragon's Tail, Upright: Underestimating the Challenge"],
     ['The Defender, Reversed: Peril']]
     
    >>> shuffle
    All cards have been shuffled into the deck.
    
    >>> usurper
    What is the Upright meaning?  Hardened
    What is the Reversed meaning?  Contraction
    The Usurper has taken its new form.
    '''
    
    global deck
    command = []

    while command != "exit":
        print('\n')
        command = input("Your wishes?  (Type 'help' for more): ")
    
        if command == "help":
            print('''The Fortune Deck is a storytelling tool from the game Everway.  More about the game below.
            Commands consist of: 
            help -- if you're reading this, you've just used this command
            usurper -- the program will prompt you for custom upright/reversed meanings for the Usurper to display
            shuffle -- resets the deck (this is done automatically each time the Usurper is dealt)
            
            To deal, simply enter \'n\' for a normal deal (randomly upright or reversed) or \'b\' for a balanced card.
            To deal all the cards of a reading, simply string together the types of deals you want.
            
            For example: to deal a Virtue, Fault, and Fate, enter nnb.  Or to do the typical pyramid-style reading,
            where the top card is horizontal, the next row of two cards are normal vertical ones, followed by a row of 
            three normal vertical cards, enter bnnnnn
            
            ABOUT EVERWAY
            Everway is a storytelling game written by Jonathan Tweet.  It was originally published by Wizards of the Coast.
            In gaming terms, it's a rules-light roleplaying game.  Rather than the more common style of resolving conflict or
            risk situations with dice, it uses the Fortune Deck, a Tarot-style deck where each card has unique meanings when
            dealt upright or an opposing meaning when dealt upside down, or reversed.  
            
            The deck also has a card called The Usurper, which works as a wild card.  In different adventures, the Usurper's
            meaning may be adjusted to fit the circumstances.  This program allows a renaming of those meanings.  Following
            the Everway rules, the appearance of The Usurper triggers a reshuffling of previously dealt cards back into the
            deck.
            
            As the Gamemaster of an Everway game determines the results of the other players' efforts, she consults the 
            Fortune Deck.  Or...a Python program that simulates one.
            ''')
        elif command == "usurper":
            card_info[0][1] = input("What is the Upright meaning? ")
            card_info[0][2] = input("What is the Reversed meaning? ")
            print("The Usurper has taken its new form.")
        elif command == "shuffle":
            deck = list(range(0,36))
            print("All cards have been shuffled into the deck.")
        else: 
            for c in command:
                if c == "n":
                    deal(1)
                elif c == "b":
                    index = random.randrange(0,len(deck))
                    dealt = deck.pop(index)
                    balanced = [card_info[dealt][0] + ", Balanced: " + card_info[dealt][1] + " vs. " + card_info[dealt][2]]
                    if index == 0:
                        deck = list(range(0,36))
                    print(balanced)
    

