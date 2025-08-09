# LIST SLICING :-

# list_name[ starting_idx : ending_idx ]        # ending idx is not included

marks = [87, 64, 33, 95, 76]

print(marks[1:4])
print(marks[ : 4])
print(marks[1: ])
print(marks[-3:-1])


# List Methods :-
list = [2, 1, 3, 1]

list.append(4)          # adds one element at the end  
print(list)

#  Here, list is updated, so further updated list will be considered on which upcoming function will be applicable.
 
list.sort()             # sorts in ascending order
print(list)

list.sort(reverse=True)  # sorts in descending order
print(list )

list.reverse()         # reverse list
print(list)

list.insert(2,7)       # insert element at index
print(list)

list.remove(2)          # removes first occurrence of element
print(list)

list.pop(2)           # removes element at idx
print(list)