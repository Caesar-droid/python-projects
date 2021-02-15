#working with a file's contents
filename="text_files/pi_digits.txt"
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))
#large files:one million digits
filename='text_files/pi_million_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string +=line.strip()
birthday=input("Enter your birthday,in  the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
print(f"{pi_string[:52]}...")
print(len(pi_string))