def variables():
    a = 1
    print a

    print_string = "This is a value of "
    b = 1 + a
    print print_string + "b: " + str(b)

    this_boolean = False
    print this_boolean
    print print_string + "this boolean: " + str(this_boolean)

    this_boolean = 5
    print this_boolean

    print_string = True
    print print_string

def conditional_flow():
    print "start conditional_flow"

    this_boolean = True
    this_boolean_two = 3

    if this_boolean_two >= 6:
        print "we're in the intial conditional"
    elif this_boolean_two == 3:
        print "we're a 3"
    else:
        print "we're in the else"

    STORE = "Fishing Goods"
    if "Auto" in STORE:
        print "This is a car store"
    elif "Food" in STORE:
        print "This is a food store"
    elif STORE == "Fishing Goods":
        print "This is a Fishing Goods store"
    else:
        print "This store is ACME"

def list_and_disctionaries():
    inventory_items = ["apples", "bananas"]
    print inventory_items
    print len(inventory_items)
    print inventory_items[0]
    print inventory_items.append("grapes")
    print inventory_items
    print len(inventory_items)

    inventory_items[0] = "red apples"
    print inventory_items

    inventory_items.remove("grapes")
    print inventory_items

    # dictionaries
    apples_int = 11
    bananas_int = 25
    grapes_int = 20

    inventory = {"apples":apples_int, "bananas":bananas_int, "grapes":grapes_int}
    print inventory
    print "Items in inventory: " + str(len(inventory))
    print inventory["apples"]
    print inventory.keys()
    print inventory.values()
    captured_value = inventory.pop("apples")
    print "captupred_value: " + str(captured_value)
    print inventory
    inventory["cherries"] = 26
    print inventory
    print inventory["cherries"]


def while_loops():
    print "starting while loops"
    apples = 51
    banannas = 55
    grapes = 14

    inventory = [apples, banannas, grapes]
    index = 0
    while index < len(inventory):
        print "index = " + str(index) + ", item = " + str(inventory[index])
        print inventory[index]
        index = index + 1
    else:
        print "no more inventory to print. index=" + str(index)

def for_loops():
    print "for_loops()"
    inventory_list = ["apples", "banannas", "grapes"]
    inventory_dictionary = {"apples":51, "banannas":10, "grapes":9}

    for i in inventory_list:
        print i

    # dictionary
    for k,v in inventory_dictionary.items():
        print k + " count=" + str(v)

    for k in inventory_dictionary.keys():
        print k

    for v in inventory_dictionary.values():
        print v

def strings():
    long_string= "apples-10|banannas-15 | grapes-19 | cherries-14"
    items={}
    new_str = long_string.split("|", 4)
    print new_str

    for s in new_str:
        (a,b) = s.replace(" ", "").split("-", 1)
        print a + "==" + b
        items[a]=int(b)

    print items
    print items.keys()
    print items.values()

def tuples():
    apples = "apples"
    apples_qty = 10
    an_item = apples + ":" + str(apples_qty)

    print an_item
    a,b = an_item.split(":",1)
    print a 
    print b
    tuples = an_item.split(":",1)
    print tuples[0]
    a_two = tuples[0]
    print a_two

    inventory = {"apples":10, "bananas":15, "grapes":19}
    for k,v in inventory.items():
        print k + " qty=" + str(v)

    items = (1,)
    print items[0]
    items = ("1st item", "2nd item", "3rd item", "4th item")
    print items[1:4]

    numbers = (1,2,3,4,5)
    print numbers[1:4]
    print numbers[0]
    #can't overwrite
    #numbers[0] = 22
    numbers = (22,33,44,55)
    print numbers
    print numbers[0]

def file_io():
    file_path = "/download/python/fast_track_for_newbs/file_io.txt"
    file_output = open(file_path, 'wt')
    file_output.write("1st item,\n2nd item,\n3rd item\n")
    file_output.close()

    file_input = open(file_path, 'rt')
    file_contents = file_input.read()
    file_input.close

    print file_contents
    array_of_contents = file_contents.replace("\n", "").split(",")
    print array_of_contents
    for i in array_of_contents:
        print i
    print array_of_contents[1]




#variables()
#conditional_flow()
#list_and_disctionaries()
#while_loops()
#for_loops()
#strings()
#tuples()
file_io()