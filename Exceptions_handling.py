# Create a program that:
# a. Ask the user for a series of grades, separated by commas
# b. Print the average
# c. Handle the scenario in which the one or more values are not valid (i.e. not numbers) using a try-except block
def avg_grades():
    grades_list = input("Enter the grades")
    lista = grades_list.split(",")
    try:
        avg = sum(map(lambda x: int(x), lista))/len(lista) #sau [int(n) for n in grades_list.split(",")]
        print(avg)
    except ValueError:
        print("Wrong input")
        return avg_grades() #fara return returneaza inputul anterior 
#avg_grades()


# Create a program that:
# a. Ask the user for a number
# b. Divide the number 10 by that number
# c. Handle both scenarios in which an invalid value has been provided

def invalid_div_value():
    try:
        nr = int(input("Enter a number:"))
        div_10 = 10/nr
        print(div_10)
    except (ValueError, ZeroDivisionError): #sau doua except separate
        print("Wrong input")
#invalid_div_value()
#walrus OPERATOR: :=
# Create a program that:
# a. Ask the user for a number
# b. Handle the scenario in which the input value is not a number and print “invalid character”
# c. Only if there are no errors, print “no errors”
# d. Regardless if thereʼs an error or not, print “exit”
def input_value():
    nr = input("Enter a number:")
    try:
        float(nr)
    except ValueError:
        print("Invalid character")
    else:
        print("No error")
    finally:
        print("Exit")
#input_value()
