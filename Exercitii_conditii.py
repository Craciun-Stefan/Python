# #ex1
# nr = input("Da un nr")
# if int(nr) % 2 == 0:
#     print(f"{nr} este par")
# elif int(nr) % 2 == 1:
#     print(f"{nr} este impar")
# if int(nr) >=10:
#     print(f"{nr} este mai mare ca 10")
#ex2
# nr1 = input("Da-mi nr 1 ")
# nr2 = input("Da-mi nr 2 ")
# if nr1 > nr2:
#     print(nr1)
# else:
#     print(nr2)
#ex3
# nr = input("Da-mi un nr")
# if int(nr) % 5 == 0:
#     print(f"{nr} este multiplu de 5")
# else:
#     print(f"{nr} nu este multiplu de 5")
#ex4
# nr1 = input("Da-mi un nr de la 1 la 7")
# nr = int(nr1)
# while nr < 1 or nr >7:
#     nr1 = input("Da-mi un nr de la 1 la 7")
#     nr = int(nr1)
# if nr == 1:
#     print("Monday")
# elif nr == 2:
#     print("Tuesday")
# elif nr == 3:
#     print("Wednesday")
#ex5
# nr_cursuri = input("Cate cursuri ai?")
# nr_prez = input("La cate din aceste cursuri ai fost?")
# print(f"ai o prezenta de{(int(nr_prez)/int(nr_cursuri))}%")
# if (int(nr_prez)/int(nr_cursuri))*100 > 75:
#     print("Ai prezenta peste 75%")
#ex6
# bet1 = input("Fa un pariu")
# bet = int(bet1)
# import random
# nr1 = random.randint(1,6)
# nr2 = random.randint(1,6)
# print(f"Zar 1: {nr1}")
# print(f"Zar 2 = {nr2}")
# if (nr1 + nr2) == 4 or (nr1 + nr2) == 10:
#     if nr1 == nr2:
#         print(f"Ai castigat {bet*7}")
#     else:
#         print("Ai pierdut")
# elif (nr1 + nr2) == 6 or (nr1 + nr2) == 8:
#     if nr1 == nr2:
#         print(f"Ai castigat {bet*9}")
#     else:
#         print("Ai pierdut")
# elif (nr1 + nr2) == 7:
#     print("Ai pierdut")
# else:
#     print("Ia banii inapoi")

# note_mate = [6, 8, 3]
# note_info = [4, 6, 9]
# note_roma = [9, 5, 3]

# for nota_mate, nota_info, nota_roma in zip(note_roma, note_info, note_mate):
#     print(sum([nota_mate, nota_info, nota_roma]) / 3)

#set2 de exercitii
#ex1  
# nr = int(input("Da-mi un nr: "))
# suma = 0
# i = 0
# while i < nr:
#     i = i + 1``
#     suma = suma + i
# print(suma)
#ex2
# cuvant = input("Scrie-mi ceva")
# i = 0
# while i != 1:
#     cuvant = list(cuvant)
#     cuvant = list(reversed(cuvant))
#     cuvant = ''.join(cuvant)
#     print(cuvant)
#     cuvant = input("Scrie-mi ceva")
#ex3
# nr = int(input("Da-mi un nr: "))
# i = 1
# while i <=10:
#     print(nr**i)
#     i = i + 1
#ex4
# nr = list(input("Scrie un nr"))
# print(len(nr))
#ex5
i = 0
nr_salvate = []
while i != - 1:
    nr = input("Da-mi un nr")
    nr_int = int(nr)
    nr_lista = list(nr)
    if nr_int >=100 & nr_int <=500:
        for x in nr_lista:
            if  :
                i = i + 1
                if i == 3:
                    nr_salvate.append(nr_int)
                    print(nr_salvate)
                    i = 0
    else:
        print("Nr nu a fost salvat")            


    

