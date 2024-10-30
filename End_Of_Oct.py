# Download the employees.csv file from here
# 1. Create a program that reads each row from the given employees.csv file and prints the content as it is
# 2. Create a program that reads the content of the employees.csv file as a list of lists
# 3. Create a program that gives us the first and last names of the person with the biggest salary
# 4. Create a program that gives us the first and last names of the person with the smaller salary
# 5. Create a program that prints the average salary, based on the info provided in employees.csv
# 6. Create a program that shows the number of members in each department
# 7. Rewrite employees.csv file as to have *** instead of the columnʼs value on the Telephone Number column
# 8. Create a new.csv file from scratch, that contains:
# a. First name, last name, Job Title and age columns
# b. 5 rows
import csv
file_path = r'C:\Users\Ralu\Desktop\Python_Exe\employees.csv'
with open(file_path, 'r') as f:
    read = list(csv.reader(f))
    #print(list(read))
    #ex3
    # salar_max = 1
    # for empl in read[1:]:
    #     if int(empl[8]) > salar_max:
    #         salar_max = int(empl[8])
    #         first_name = empl[0]
    #         last_name = empl[1]
    # print(first_name, last_name)
    #ex4
    # salar_min = 20000
    # for empl in list(read)[1:]:
    #     if int(empl[8]) < salar_min:
    #         salar_min = int(empl[8])
    #         first_name = empl[0]
    #         last_name = empl[1]
    # print(first_name, last_name)
    #ex5
    # salar_list = [a[8] for a in list(read)]
    # salar_list.remove("Salary")
    # sum = 0
    # for a in salar_list:
    #     sum = int(a) + sum
    # print(sum/len(salar_list))
   
    # maxlist = [int(a[8]) for a in read if a[8].isdigit()]
    # max_salar = [a[0] for a in read[1:] if int(a[8]) == max(maxlist)]
    # max_salar2 = [a[1] for a in read[1:] if int(a[8]) == max(maxlist)]
    # min_salar = [a[0] for a in read[1:] if int(a[8]) == min(maxlist)]
    # min_salar2 = [a[1] for a in read[1:] if int(a[8]) == min(maxlist)]
    # print(''.join(max_salar), ''.join(max_salar2))
    # for a, b in zip(min_salar, min_salar2):  
    #     print("Ppl with the lowest salary: ",a, b)
     #ex6
nr = 0
departments = set([a[9] for a in read[1:]])
#print(read)
#print(departments)
for depart_name in departments:
    for employee in read[1:]:
        if depart_name == employee[9]:
            nr = nr +1
    print(f"Department {a} has {nr} empl")
    nr = 0

    
    
            


