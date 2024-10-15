# Do the following:
# Create a tuple that contains 3 elements
# Unpack the tuple in several variables
# Create a program that adds an element to a tuple
# Create two sets: one that contains all numbers from 0 to 7, and a 2nd one that contains all numbers from 4 to 10. Do the following:
# Print all the elements from both sets
# Print only the common elements
# Print all the elements from the 1st set, that are not part of the 2nd
# Print all the elements from the 2nd set, that are not part of the 1st
# Print all the elements from both sets that are NOT common

# tuplu = (1, 2, 3)
# x, y, z = tuplu
# elem = input("Adauga elementul: ")
# tuplu_elem = tuplu + (int(elem), )
# print(tuplu_elem)
set1 = {0, 1, 2, 3, 4, 5, 6, 7}
set2 = {4, 5, 6, 7, 8, 9, 10}
print(set1, set2)
# for i in set1:
#     print(i)
# for j in set2:
#     print(j)
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1)) # sau cu - intre set-uri
print(set1.symmetric_difference(set2)) # Print all the elements from both sets that are NOT common

# Have the following tuples: my_tuple_1 = (1, 2, 3, “a”, “b”, 10, “5”) and my_tuple_2 = (7, 5, “b”, “5”, 3). Do the following:
# Print the elements that are part of the 1st tuple, but not the 2nd one
# Add the two tuples and print the total number of duplicates
my_tuple_1 = (1, 2, 3, "a", "b", 10, "5")
my_tuple_2 = (7, 5, "b", "5", 3)
set_tupl1 = set(my_tuple_1) # se taie automat daca faci lista si dupa se facea diferenta din length de lista - lenght de set
persoana = { #dictionar
    "nume": "cristiii",
    "varsta": 20,
    "inaltime": 1.8,
    "note": [1, 5, 9]

}
from pprint import pprint as pp
dictt = {} # dictionar gol
print(persoana["nume"])
print(list(persoana.items()))
#for key, val in persoana.items() #merge in tot dictionarul(key in cheie, val in valoare), ia la rand elementele

#by default for-ul itereaza in key cand e vorba de dictionar



