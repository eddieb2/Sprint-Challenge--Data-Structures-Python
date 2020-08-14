import time
from bst import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
duplicates1 = []

# Replace the nested for loops below with your improvements
# Print out all duplicate entries

# MY CODE
#############################################

# creates the bst
bst = BSTNode(names_1[0])

# adds all remaining names to the BST
for name in names_1[1:]:
    bst.insert(name)

# compares the values from names_2 against the BST values. if the BST contains the names from names_2 add the name to the dups list
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

##############################################

# ORIGINAL CODE is O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates1.append(name_1)

# proves that my work is correct
# for dup in duplicates:
#     for dup1 in duplicates1:
#         if dup == dup1:
#             print(True)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# print (f"{len(duplicates1)} duplicates1:\n\n{', '.join(duplicates1)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

'''
Logic
-----
- Search through 2 files, find dups and return them.
- Make process faster than O(n^2) 

Current Logic
-------------
iterate through both files at the same time, find dups, append to a list
10,000^2

'''



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
