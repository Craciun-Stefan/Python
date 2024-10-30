# 1. Create a program that:
# a. Exclusively creates file_2.txt in your project directory
# b. Run the script two times and explain the behavior
# 2. Create a program that prints the whole content of file.txt
# 3. Create a program that prints a list with all the lines from file.txt
# 4. Create a program that prints the number of lines in file.txt
# 5. Create a program that opens file.txt and prints the longest word
# 6. Create a program that opens file.txt and writes its content to file_2.txt
# 7. Create a program that overwrites the file_2.txt content with Python
# 8. Create a program that opens file.txt and appends at the end the word “Python”
# 9. Create a program that:
# a. Generates 26 .txt files from a.txt, up to z.txt
# b. Each file should have the word “Python” written in it, as many times as the file name indicates (i.e. once for a.txt, twice for b.txt,
# and so on)
file_path2 = r'C:\Users\Ralu\Desktop\Python_Exe\file_2.txt'
file_path = r'C:\Users\Ralu\Desktop\Python_Exe\file.txt'
# Ex1
# with open(file_path2, 'a') as file: //sau cu x
#     pass
#Ex2
# with open(file_path, 'r') as file:
#     content = file.read()
#     print(content)
#Ex3
# with open(file_path, 'r') as file:
#     content = ''.join(file.readlines()).split('\n')
#     content = [a for a in content if a != '']
#sau content = file.readlines()
#     print(content)
#Ex4
#print(len(content))
#Ex5
# with open(file_path, 'r') as file:
#     content = ''.join(file.readlines()).split('\n')
#     content = str(content).split(' ')
#     #content = str(content).split('--')
#     content = [a for a in set(content) if a != '']
#     #content_punctuation = [a for a in content if a.isdigit]
#     #print(content_punctuation)
#     word = ''
#     for a in content:
#         if len(a) > len(word):
#             word = a
    
#     print(word)
# sau cu fctia max(cuvinte, key=len) max_word = max(cuvinte, key=len)
#Ex6
# with open(file_path, 'r') as file:
#     content = file.readlines()
#     file.close
# with open(file_path2, 'w') as file:
#     file.write(''.join(content))
#     file.close
# sau: with open(file1, 'r') as f1, open(file2, 'w') as f2:
#   f2.write(f1.read())

