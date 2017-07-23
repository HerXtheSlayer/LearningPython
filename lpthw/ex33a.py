from sys import argv
i = 0
numbers = []

script, a = argv
anum = int(a)

def looprun(lim):
    """Loop to make a list from 0 to argv"""
    for i in range(0, lim + 1):
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


        print "The numbers: "
        for num in numbers:
            print num

print "At the top i is %d" % i

print '%r' % a
looprun(anum)
