# Mind_Meld_scorer
Script to help with score keeping in the Incomparible Game Show Mind Meld

# Game Rules
A topic is chosen by one of the players. All of the players then submit items, typically five, in that topic to the host. The various players' list are compared to each other and a player scores for each item on their list that matches another. If all items in a player's list are found in other's list, they've acheived a mind meld and are awarded additional points.

# Why this exists
One of the longest sections of the show is the hosts comparing the players list and scoring the results. While this can be quite entertaining to the listener, it's error prone.

# Limitations
This script is very much "on the rails", following a linear path of 
* create list of players
* enter players list
* compare said scripts
* score the results
* give the hosts the chnce to give/take points away
* proceed to the next round and repeat

This is a CLI (command line interface) script with no GUI (graphical user interface) or anything pretty about it. It's functional with a bit of sass, and that's it.

All submitions must be spelled the same in order for the script to compare them. So no armor and armour, or theater and theatre.
