#reading the entire file
filename='text_files/learning_python.txt'
with open(filename) as file_object:
    contents=file_object.read()
print(contents) 
#looping over the file objects
filename='text_files/learning_python.txt'
with open(filename) as file_object:
    for file in file_object:
        print(file.strip())
#storing in a list and then working with them outside the with block
filename='text_files/learning_python.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())