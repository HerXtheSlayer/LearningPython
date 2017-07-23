from sys import exit

dagger = False

def entrance():
    """First zone, determines the loot"""
    print """
While visiting a frontier town near the edge of the
Timberway, you learn that merchants here pay
handsomely for the pelts of the elusive Timberway
lions-up to 50 gp apiece. By asking around town, you quickly
learn that a group of likeminded hunters recently left for
Bluerock Lodge, a shelter located near the traditional hunting
grounds of the lions in question. The townsfolk assure you
that if you wish to try your hand at lion hunting,
Bluerock is the place to go.
"""
    print """The stark black-and-white of the wintry forest is
broken by a splash of color in the landscape
toward the left. A man's body sits upright but
slumped against a tree. Around him, the snow is
stained a brilliant red.
"""

    print "\nWhat do you do?"
    dec = raw_input("> ")

    if  "body" in dec:
        print "\nThe body is that of Kyle Tanner, one of the hunters from Bluerock Lodge."
        print """
He died of blood loss from a terrible
bite wound on his shoulder. The bite was bandaged,
but it looks like the man tore the bandage loose and reopened
the wound with his own frostbitten hand."""
        print "\nYou find Kyle's Masterwork Dagger."

        icanhasdagger = True
        return icanhasdagger

    elif "area" in dec:
        print "\nYou explore the area and make a huge ruckus."

        icanhasdagger = False
        return icanhasdagger

    else:
        print "\nYou freeze to death."
        exit(0)


def lion(icanhasdagger):
    """Timberway Lion"""
    print """
A lone Timberway lion lurks in the area.
The poor creature is starving. When it hears you
approaching, the lion quickly hides nearby and gets
ready to pounce.
"""
    print "What do you do?"
    what = raw_input("> ")

    if "fight" in what and icanhasdagger == True:
        print """You take the Kyle's Masterwork Dagger and fiercly defend yourself.
After a few attacks, you manage to hit the exhausted beast in the heart.
When the beast is dead you skin it and, upon returning to the town,
you sell the pelt for 50 gp."""
        exit(0)
    elif "fight" in what and icanhasdagger == False:
        print """You try to fight the lion attacks with you bear hands, 
but the cat's claws prove to be a better weapon.
You die and the beast feasts on your body."""
        exit(0)
    else:
        print """You try to run away from the hungercrazed beast, 
but it catches you and devours your body."""
        exit(0)

def main():
    icanhasdagger = entrance()
    lion(icanhasdagger)

main()