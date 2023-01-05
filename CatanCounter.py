import matplotlib.pyplot as plt
from collections import Counter as cnt

print("""
Catan roll tracker -- Designed by Shane Simon

Enter the last roll to track. If you make a mistake, enter y
""")

# need to create an empty list
rolls = []

#main program loop
while True:
    print("Enter your last roll: ")
    dice = input("> ") # Get user input
    if dice.isdigit(): # is user input a digit?
        if int(dice) >= 2 and int(dice) <= 12: # if between these integers
            print("Last roll: ", dice)
            rolls.append(dice)
            #turn rolls list into a dictionary
            count = cnt(rolls)
            my_keys = list(count.keys()) # extract keys from dict
            my_keys.sort(key=int) # sort keys that are ints
            sorted_count = {i: count[i] for i in my_keys}
        if int(dice) < 2:
            print(f"{dice} is not a valid roll outcome!")
        if int(dice) > 12:
            print(f"{dice} is not a valid roll outcome!")
    if dice.lower() == 'y':
        rolls.pop()
    else: 
        pass
    print("dice list: ", rolls)

# create graph
    xaxis = list(sorted_count.keys())
    yaxis = list(sorted_count.values())
    plt.bar(xaxis, yaxis)
    plt.show(block=False)
    plt.pause(1) #pause for 1 seconds before closing the plot window
    plt.close('all')
    #end loop
    pass


