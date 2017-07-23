import random

print "Let's play the game!"
print "For every number in the wrong place, you get a cow. For every number in the right place, you get a bull."
print "The game ends when you get 4 bulls!"
print "press O for the original number."
print "Type exit at any prompt to exit."

numbers = [int(random.uniform(0, 9)), int(random.uniform(0, 9)), int(random.uniform(0, 9)), int(random.uniform(0, 9))]
print numbers

playing = True

while playing:
    user_guess = []
    user_guess.append(raw_input("Give me your best guess!: (Hint: %s, *, %s, *) ")) % (numbers[0], numbers[2])
    print "(" + "Hint:" + numbers[0] + "*" + numbers[2] + "*)"
    if str(user_guess[0:3]) <> "exit":
        print user_guess
        guess_list = user_guess
        continue
        break

    else:
        print "Game over!"