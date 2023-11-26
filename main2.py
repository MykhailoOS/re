import re

string = '9999-9999-9999-9566'
pattern = r'\d{4}-?\d{4}-?\d{4}-?\d{4}'
make = re.search(pattern, string)
if make:
    print("Successful")
    print(make.group())
else:
    print("Error")

# Task1
string = 'Rbrdfhf'
pattern = r'[R]\w+[br]+\w*'
make = re.search(pattern, string)
print(make.group())

# Task3
string = "abcd009@gmail.com"
pattern = r'^[^-_]\w+\d[0-9]+\S[-_]*\w[A-Za-z]*\S\w+'
make = re.search(pattern, string)
if make:
    print(f"{make.group()} Email is correct")
else:
    print("Error")

# Task4
login = 'adsad465'
pattern = r'^\S{2,10}$'
make = re.search(pattern, login)
if make:
    print(f"{make.group()} Valid login")
else:
    print("Incorrect login")