# Create a program that will:
# a. Ask the user for a string
# b. If the string contains numeric characters, print a message and get out of the loop
# c. If it doesnʼt, print that there are no numbers in the string
# d. At the end, print the word “Finish”
# while True:
#     user_input = input("Please enter a string: ")
#     if any(char.isdigit() for char in user_input): #list comprehension
#         print("The string contains numeric characters.")
#         break  # Exit the loop
#     else:
#         print("There are no numbers in the string.")
# print("Finish")

#sau varianta curs:
# cuvant = 'ana'
# contine_cifre = any(c.isdigit() for c in cuvant)
# contine_cifre = True
# for c in cuvant:
#     if c.isdigit():
#         contine_cifre = True
#         break
# else: # daca iese natural, fara break
#     print("No numbers in the string")
# print("FInish")
# Use the continue statement to resolve the following problem:
# a. Create a list that contains all the numbers from 0 to 9
# b. Divide the number 24 by each of the numbers
# c. Fix the issue in which the number is “0” (generates ZeroDivisionError)
# list_1 = range(10)
# for i in list_1:
#     if i == 0:
#         #ZeroDivisionError
#         continue
#     x = 24/i
#     print(f"24 impartit la {i} este egal cu: {x} ")
# Create a program with:
# a. A while True loop
# b. Inside, randomly generate integers from 0 to 25
# c. Get out of the loop when it finds a multiple of 7

# import random
# while True:
#     x = random.randint(0,25)
#     print(x)
#     if x == 0:
#         print("{x} este 0")
#         break
#     elif x % 7 == 0:
#         print(f"{x} is a multiple of 7")
#         break
#     else:
#         continue

#  Implement a program that:
# a. Randomly generates a string sequence for the letters a, b, c, d, e and f, with a length of 1000
# b. Iterate through the sequence
# c. Get out of the loop when the same character can be found one after the other 3 times (e.g. aaa, bbb etc.)
# d. Otherwise, print the fact that there is no such sequence 

# sequence_of_let = ["a", "b", "c", "d", "e", "f"]
# j = 1
# while len(sequence_of_let) < 1000:
#     x = random.choice(sequence_of_let)
#     sequence_of_let.append(x)
# # sau cuvant_generat = ''.join(random.choices('abcdef', k=1000)) mai usor
# for i in range(len(sequence_of_let)-3):
#     if(sequence_of_let[i] == sequence_of_let[i+1] == sequence_of_let[i+2]):
#         print(sequence_of_let[i], sequence_of_let[i+1], sequence_of_let[i+2])
#         ("Exista 3 litere la fel")
#         j = 0
#         break
#     else:
#         continue
# if j == 1:
#     print("Nu exista 3 litere la fel")
# # sau 
# for i, c in enumerate(cuvant_generat, 1):
#      c == cuvant_generat[i+1] and c = cuvant_generat[i-1]
#      break
# else:
#     print("Nu exsita 3 litere la fel")



#iegzericicile 5
# Create a program that will:
# a. Ask for a integer
# b. Reverse the number (i.e. 123 will be 321)
# c. Use two methods

# nr = input("Da-mi un numar")
# i = -1
# while nr.isnumeric() == False:
#     nr = input("Da-mi un numar")
# nr_invers = [] // METODA 1
# while len(nr_invers) != len(nr): 
#     nr_invers.append(nr[i])
#     i = i - 1
# print("".join(nr_invers))
# x = list(nr) // METODA 2
# x.reverse()
# print("".join(x))
# print(nr(::-1)) // METODA 3
# print(''.join(list(reversed(nr)))) // METODA 4
# For the following list: my_list = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique'], select the
# string that contains the biggest number of unique characters
# my_list = ['cat', 'catatatatctsa', '124259239185125', 'bcdefhijklmnop', 'foo', 'unique', 'df']
# y = []
# for a in my_list:
#     x = list(set(a))
#     print(x)
#     if len(x) > len(set(y)):
#         y = a
#     else:
#         continue
# print(y)
# # sau
# max_unique = my_list[0]
# for cuv in my_list:
#     if len(set(cuv)) > len(set(max_unique)):
#         max_unique = cuv

# Write a program that:
# a. Asks for an integer, n, between 1 and 9
# b. Return n + nn + nnn

# nr = input("Da-mi nr intre 1 si 9")
# while nr < '1' or nr > '9':
#     nr = input("Da-mi nr intre 1 si 9")
# print(int(nr) + int(''.join([nr, nr])) + int(''.join([nr, nr, nr])))
#sau
# suma = sum(map(int, [c, c * 2, c * 3]))
#sau
# Create a program that will:
# a. Ask for an integer
# b. Return all the prime numbers smaller than the given number

# nr = input("da-mi un nr: ")
# prime_Nrs = []
# while nr.isnumeric() == False:
#     nr = input("da-mi un nr: ")
# for a in range(int(nr)+1):
#     is_prime = True
#     for i in range(2, a // 2 + 1):
#         if a % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime_Nrs.append(a)
# print(prime_Nrs)


# Create a list with a couple of strings in it. The program should return the longest common prefix e.g. [“flower”,
# “flow”, “flight”] will return “fl”
# list_1 = ['bar', 'barman', 'bars', 'barr']
# longest_prefix = list_1[0]
# for stringuri in list_1[1:]:
#     while stringuri[:len(longest_prefix)] != longest_prefix:
#             longest_prefix = longest_prefix[:-1]
# print(longest_prefix)
# #sau
# len_prefix = 1
# whil




# def suma_a_3_numere(a, b, c, negativ=False):
#     print(a)
#     print(b)
#     print(c)
#     suma = a + b + c
#     if negativ: #daca ii dau cand apelez functia kwarg negativ = true, imi printeaza suma nr negativ
#         return suma * -1
#     else:
#         return suma
# suma = suma_a_3_numere(-1, 2, 3)
# print(suma)


# def suma_a_oricate_numere(*args, **kwargs):
#     lista = []
#     if args:
#         lista.extend(args)
#     if kwargs:
#         lista.extend(kwargs.values())
#     print(kwargs)
#     return sum(lista)


# suma = suma_a_oricate_numere(1, 2, 3, 4, 5, 6, a=2, b=3, c=4)
# print(suma)


# def print(*args, sep=" ", end="\n"):
#     for arg in args:
#         cout<<arg<<sep;
#     cout<<end;


# def suma_a_oricate_numere(a, b, *args, x=3, y=4, **kwargs):
#     lista = []
#     lista.append(a)
#     lista.append(b)
#     lista.extend(args)
#     if x:
#         lista.append(x)
#     if y:
#         lista.append(y)
#     if kwargs:
#         lista.extend(kwargs.values())
#     return sum(lista)


# suma = suma_a_oricate_numere(1, 2, 3, 4, 5, k=6, t=1, z=5, g=7, f=4)
# print(suma)

# tuplu = (1, 2, 3)
# print(tuplu, sep="|")
# print(*tuplu, sep="|")

# suma = lambda *args: sum(args)
# s = suma(1,2,3,4,5)
# print(s)

# # def suma(a, b):
# #     return a + b

# print(list(range(10)))

# def inverseaza_nr(x):
#     return x * -1

# lista = [1,2,3,4,5]
# lista_de_nr_inv = map(inverseaza_nr, lista)
# print(list(lista_de_nr_inv))
# def is_even(x):
#     return x % 2 == 0
# lista = [1,2,3,4,5,6,7,8,9]
# lista_de_nr_inv = filter(is_even, lista)
# print(list(lista_de_nr_inv))
# from functools import reduce
# def adunare_2_nr(a, b):
#     return a + b
# lista = [1,2,3,4,5,6]
# print(reduce(adunare_2_nr,lista))
# lista = [1, 2, 3, 4, 5]
# lista_de_nr_inv = map(lambda x: -1 * x, lista)
# print(list(lista_de_nr_inv))
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista_de_nr_inv = filter(lambda x: x % 2 == 0, lista)
# print(list(lista_de_nr_inv))




# Create a function that:
# a. Asks for a number
# b. Returns the string “Itʼs even” if the number is even, else
# “Itʼs odd”
# c. Returns “Wrong input” if itʼs a string and recall the
# function
# def fnct_nr_par():
#     even = "The number is even"
#     odd = "The number is odd"
#     nr = input("Da-mi un nr")
#     if nr.isnumeric() == False:
#         print("Wrong input") 
#         fnct_nr_par()
#     elif int(nr) % 2 == 0:
#         return even 
#     else:
#         return odd
#print(fnct_nr_par())

# Create a function that:
# a. Accepts any number of arguments (numbers)
# b. Returns their average
# c. Handle the scenario in which no arguments are passed
# def fnct_avg(*args): # () = falsy, (1) = truthy
#     if len(args) == 0: sau if args:
#         print("Error, no args provided")
#     else:
#         numbers_list = list(args)
#         print(sum(numbers_list)/len(args)) 
# fnct_avg(3, 12, 15, 18)

# Recreate the following function using lambda:
# def my_func(x):
# return (x + 1) ** (x - 2)
# x = 1
# lambda_fnc = lambda x: (x + 1) ** (x - 2)
# print(lambda_fnc(x))

# Create a function that:
# a. Accepts at least three numbers
# b. Returns their median
# def fnc_median(a, b, c, *args):
#     list_agruments = [a, b, c]
#     list_agruments.extend(list(args))
#     list_agruments.sort()
#     if len(list_agruments) % 2 == 0:
#         med = (list_agruments[len(list_agruments)//2] + list_agruments[len(list_agruments)//2 -1 ])/2
#         return med
#     else:
#         med = list_agruments[len(list_agruments)//2]
#         return med
# print(fnc_median(3, 4, 5, 10, 9, 9))

# Create a function that checks if the given string is a pangram or not
# def fnct_pangram(x):
#     letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '']
#     lista_x = list(set(x)) 
#     i = 'pangram'
#     j = 'no pangram'
#     if len(letters_list) == len(lista_x):
#         return i
#     else:
#         return j
# print(fnct_pangram('Jackdaws love my big sphinx of quartz'))

# Using the map function, write a program that triples
# all numbers from a given iterator of integers
# lista = [1, 3, 5, 10]
# list_times3 = map(lambda x: x*3, lista)
# print(list(list_times3))

# Using the map function, write a program that
# converts all the letters of a string to lowercase
# prop = 'Ana has mere and mere has aNa'
# prop_lower = map(lambda x: x.lower(),prop)
# print(''.join(list(prop_lower)))

# Using the filter function, filter all negative numbers from a given iterable
# nr_list = [-1, 1, -5, 6]
# nr_list_neg = filter(lambda x: x < 0, nr_list)
# print(list(nr_list_neg))

# Using reduce and lambda, create a function that multiplies all the numbers from an iterable
# from functools import reduce
# nr_list = [-1, 3, 10]
# nr_list_multip = reduce(lambda x, y: x*y, nr_list)
# print(nr_list_multip)

my_string = 'Practice Problems to Drill List Comprehension in Your Head.'
# Do the following using comprehensions:
# 1. Print all numbers from 1–1000 that are divisible by 8
# 2. Print all numbers from 1–1000 that have a 6 in them
# 3. Count the number of spaces in the above string
# 4. Remove all vowels in the above string
# 5. Print all of the words in the above string that have less than 5 letters
# 6. Use a dictionary comprehension to keep track of the length of each word in my_string
# new_list = [a for a in range(1, 1001) if a % 8 == 0] #ex1
# print(new_list)
# new_list = [a for a in range(1, 1001) if '6' in str(a)] #ex2
# print(new_list)
# spaces_counter = [a for a in my_string if a == ' '] #ex3
# print(len(spaces_counter))
# vowels_remover = [a for a in my_string if a not in ['a', 'e', 'i', 'o', 'u']] #ex4
# print(''.join(vowels_remover))
# words_lessthan5 = [a for a in my_string.split(' ') if len(a) <=4] #ex5
# print(words_lessthan5)
# word_length = {k: len(k) for k in my_string.split(' ')} #ex6
# print(word_length)
loto_lori = {
    'Stefan&Ralu' : [6, 7, 8, 9, 10, 11],
    'Andreea&Madalin' : [9, 34, 46, 8, 23, 32],
    'Alex&Ramona' : [34, 45, 47, 29, 39, 11]
}
numere_loto = [3, 5, 49, 8, 23, 32]
rezultate = {k: len(set.intersection(set(v), set(numere_loto))) for k, v in loto_lori.items()}
print(rezultate)







        

















    
    

