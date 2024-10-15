# # # # #exercitiul 1
# # # # nr_1 = int(input("Da-mi primul numar"))
# # # # nr_2 = int(input("Da-mi al doilea numar"))
# # # # suma = nr_1+nr_2
# # # # diferenta = nr_1-nr_2
# # # # inmultire =nr_1*nr_2
# # # # print(suma)
# # # # print(diferenta)
# # # # print(inmultire)
# # # #exercitiul 2
# # # varsta = int(input("Cati ani ai?"))
# # # luni = int(input("Cate luni au trecut de la ultima ta zi de nastere?"))
# # # print(varsta*12 + luni)
# #exercitiul 3
# nr1 = int(input("Da-mi nr1:"))
# nr2 = int(input("Da-mi nr2:"))
# suma = nr1 + nr2
# if (suma % 2) == 0:
#     print("True")
# else:
#     print("False")
# # #exercitiul 4
# # nr1 = float(input("Da-mi nr1:"))
# # nr2 = float(input("Da-mi nr2:"))
# # nr3 = float(input("Da-mi nr3:"))
# # suma = nr1 + nr2 + nr3
# # if suma / round(suma) == 1:
# sau cu if int(suma) == suma
# #     print("True")
# # else:
# #     print("False")
#exercitiul 5
an = int(input("Spune-mi un an:"))
if (an % 4 != 0) or (an % 100 == 0):
    print("False")
else:
    print("True")

