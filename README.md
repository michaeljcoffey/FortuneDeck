## Synopsis

This is an electronic version of the Fortune Deck from the storytelling game, Everway.  See: https://en.wikipedia.org/wiki/Everway

The Fortune deck is similar to a Tarot deck, which the gamemaster uses to do "readings" for the characters instead of dice.  This is an electronic version of the deck.

As with the physical deck, each of the 36 cards has two meanings: one when dealt "upright" and another roughly opposite meaning when dealt upside down, or "reversed."  A special card, The Usurper, has an undefined meaning, depending on the needs of each particular game.  According to the Everway rules, when the Usurper is drawn, the deck is reshuffled.  This code does the same thing--once a hand has been returned, if the Ursuper is in it, the deck is reset.


## Code Example

>>> deal(3)
[['Death, Upright: Change'], ['War, Upright: Great Effort'], ['The Dragon, Reversed: Blind Fury']]
>>> deal(1)
[['The Soldier, Reversed: Blind Obedience']]

## Motivation

I'd recently finished a Python class and wanted a project that was fairly simple, but with a few wrinkles to make it interesting.  The essentially random shuffle based on the appearance of a particular card and the two meanings for a single card both made it less straightforward than dealing from a standard deck of playing cards.  Plus, Everway's a fun game.

## Installation

Just run fortunedealer.py, assuming you've already installed Python.

Once the module has been run, it's deal(num) where num is the number of cards you'd like to deal.  (See Code Example, above)


## Contributors

Everway was created by Jonathan Tweet.  I wrote this program.  I'm at google.com/+MichaelJCoffey or @michaeljcoffey


## License

Not sure yet--working things out with Gaslight Press.  Contact me if you want to use it for anything.