# Create a dictionary that:
# Has 3 key-value pairs and the values are numbers
dictionar1 = {
    "cheie1": 1,
    "cheie2": 2,
    "cheie3": 3,
    "cheie4": 19
}
# Print the sum of all three values
suma = 0
for key, val in dictionar1.items():
    suma = suma + val
print(suma)
# Delete one of the pairs
dictionar1.popitem()
print(dictionar1)
# Print the value of the key ‘history’ from the dictionary: my_dict = { "class": { "student": { "name": "Mike", "marks": { "physics": 70, "history": 80}}}}
my_dict = { 
    "class": { 
        "student": {
             "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80}
                    }
            }
         }
for val in my_dict.values():
    for std in val.values():
        for materii in std.values():
            if type(materii) is dict:
                print(materii["history"])
# sau  muuuuuuuuuuuult mai usor:
print(my_dict["class"]["student"]["marks"]["history"])         

# Create the following dictionary: my_dict = {"a": 1, "b": 2, "c": 3} and check if:
# “a” and “d” are keys
# 3 and “a” are values




# For the following dictionary change brad's salary to 8500:
my_dict = {
    'emp1': {
        'name': 'Jhon', 
        'salary': 7500
    }, 
    'emp2': {
        'name': 'Emma', 
        'salary': 8000
    }, 
    'emp3': {
        'name': 'Brad', 
        'salary': 6500
    }
}
my_dict["emp3"]["salary"] = 8500

# sau cu un cod

#for emp_nr, emp_info in my_dict:
#for key in my_dict:
    
# Have the following dictionary:
studenti = {
    "student_1": {
        "math": [4, 4, 5, 5],
        "physics": [4, 5, 5, 6],
        "english": [8, 9, 9, 10]
    },
    "student_2": {
        "math": [8, 10, 10, 7],
        "physics": [8, 10, 10, 10],
        "english": [7, 5, 1, 8]
    },
    "student_3": {
        "math": [9, 9, 9, 10],
        "physics": [8, 8, 7, 10],
        "english": [10, 10, 9, 10]
    }
}
def roundul_meu(nr):
    if nr - int(nr) >= 0.5:
        nr = int(nr) + 1
    else:
        nr = int(nr)
#sau functiile floor() si ceil() din libraria numpy
# for student, materii in studenti.items():
#     for materie, note in materii.items():
#         print(f"Studentul {student} are nota {sum(note) / len(note)} la materia {materie}")
#         print(f"Studentul {student} are nota {roundul_meu(sum(note) / len(note))} la materia {materie}")

# Print the average of every course, for every student
# Round up all the averages (e.g. 4.5 = 5, 7.4 = 7 etc.)
# Print each student’s average for all courses
# Round up all the averages

for student, materii in studenti.items():
    medii = {}
    for materie, note in materii.items():
        medii[materie] = roundul_meu(sum(note) / len(note))
    
    print(f"media anuala a studentului {student} este {roundul_meu(sum(medii.values()) / len(medii.values()))}")