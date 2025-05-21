# create an empty list
my_list = []
print(my_list) # prints []



# using append method
my_list.append(10)
print("After Append:", my_list) #  append() adds [10]

my_list.append(20)
print("After Append:", my_list) # append() adds 20 [10, 20]


my_list.append(30)
print("After Append:", my_list) # append() adds 30 [10, 20, 30]


my_list.append(40)
print("After Append:", my_list) # append() adds 40 [10, 20, 30, 40]

# Using insert method
my_list = [10, 20, 30, 40]
my_list.insert(2, 15) # inserts 15 at index 2 (second position)
print(my_list) # list after my_list.insert [10, 20, 15, 30, 40]

# Using Extend method
my_list.extend([50, 60, 70])
print(my_list)  # List after extend [10, 20, 15, 30, 40, 50, 60, 70]

# Removing last element on my_list
my_list = [10, 20, 15, 30, 40, 50, 60, 70]
my_list.pop() # pop() Removes last element from my_list
print(my_list) # output: [10, 20, 15, 30, 40, 50, 60]

# Sort my_list in ascending order
my_list.sort() # Sorts the list in-place
my_list = [10, 20, 15, 30, 40, 50, 60, 70]
print(my_list) # sorted list in ascending order [10, 20, 15, 30, 40, 50, 60, 70]

# Finding Index
my_list = [10, 20, 15, 30, 40, 50, 60, 70]
#index      0   1   2   3   4   5   6   7
index_of_30 = my_list.index(30)
print("index of 30:", index_of_30) # outputs: index of 30: 3