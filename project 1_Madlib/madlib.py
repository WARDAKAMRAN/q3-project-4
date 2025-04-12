# Mad Libs Gam
# # Getting user input
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
food = input("Enter a food item: ")

# Story template
story = f"""
Once upon a time, {name} went to {place}. 
There, they saw a {adjective} {animal} that was {verb} happily. 
Surprised, {name} decided to feed it some {food}, and they became best friends forever!
"""

# Display the final story
print("\nYour Mad Libs story:\n")
print(story)