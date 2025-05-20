numbers = list(range(1, 6))
print(numbers)

# We can also use the range() function to create a list of even numbers. 
# If you pass a third argument to range(), Python will use that value as a step size when generating numbers. 

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 12 , 2))
print(odd_numbers)

# Simple statistics with a list of numbers. 
# You can easily find the minimum, maximum, and sum of a list of numbers.. 

digits = [1, 2, 3, 4, 5]
min(digits)
max(digits)
sum(digits)
print(min(digits))

# List comprehension Example. 
squares = [value**2 for value in range(1, 11)]
print(squares)

# Slicing a list.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# This code prints a slice of the list, which includes the first three players.


# Looping through a slice. 
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

    # Copying a list. 
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)


print("\nMy friend's favorite foods are:")
print(friend_foods)

# Above, first we create a list called my_foods.
# Then we create a second list called friend_foods that is a copy of my_foods.
# The slice operator [:] makes a copy of the entire list.
# This means that changes made to one list will not affect the other.
# The original list was inputted into the friend_foods list/variable. 
# The .append() method adds a new item to the end of a list.
# The .insert() method inserts an item at a given position in a list.
# The .remove() method removes the first occurrence of a value from a list.

