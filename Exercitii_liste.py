# ex1
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nr = int(input("Introdu un numar: "))
# lista.append(nr) #adauga nr la finalul listei
# lista.pop(3) #sterge nr cu indexul 3
# lista.append(lista.index(9)) #imi adauga la finalul listei indexul elementului cu valoarea 9 din lista
# lista.remove(max(lista)) #sterge cel mai mare nr din lista
# lista.reverse
# primele_5 = sum(lista[:5])
# ultimele_5 = sum(lista[4:9])
# avg_ultimele = ultimele_5/5
# print(lista[0] - lista[-1])
# ex2 algoritm palindrom
text = input("Scrie un cuvant ")
text_prim = list(text)
if text_prim == text_prim[::-1]:
# print(text_prim[::-1])
# if text_prim == text_inv:
     print("True")
else:
     print("False")
#rezolvare
#cuvant = input("cuvant =")
#print(cuvant[::-1])
#if-ul...

#ex 3

# my_list = [1, 2, [1, 2, 3], 3, 4, [4, 5, 6, 7, 8], 4, 5, 6]
# new_list = []
# for element in my_list:
#     if isinstance(element, int):
#         new_list.append(element)
#     elif isinstance(element, list):
#          for el_mic in element:
#             new_list.append(el_mic)
#             #sau in loc de for new_list.extend(element) mai bun


