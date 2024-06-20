
# # can you change the values inside a list which contained in set S?

# # s = {5,9,6,"Souvik",[1,2]}

s = {8, 7, 12, "Souvik", [1,2]}

s[4][0] = 9

# # It is not possible

# Creating the Set s:

# s is initialized as a set containing integers (8, 7, 12), a string ("Souvik"), and a list ([1,2]).
# Attempting to Modify the List Element:

# s[4][0] = 9 tries to access the fifth element (s[4]) of the set s and then modify its first element ([0]) to 9.
# Now, let's address why this code doesn't work:

# Sets Allow Only Immutable Elements: Sets in Python can only contain elements that are hashable, which typically means they must be immutable (such as integers, floats, strings, tuples, frozensets, etc.).

# Lists are Mutable: Lists in Python are mutable, meaning their elements can be changed after they are created. This makes lists unsuitable for inclusion in sets because their contents can change, which would disrupt the internal structure of the set.

# TypeError: When you try to include a mutable object like a list ([1,2]) in a set, Python raises a TypeError because mutable objects cannot be hashed or used as set elements.

# Therefore, attempting to modify the list [1, 2] within the set s directly violates the rule that sets can only contain immutable elements. To avoid this issue, you should use immutable types like tuples ((1, 2)) instead of lists when working with sets, as tuples are hashable and can be safely included as elements in sets.









