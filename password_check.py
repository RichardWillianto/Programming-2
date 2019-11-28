password = input("Enter password : ")
password_length = len(password)

for characters in range(0, password_length):
    print("*", end='')
print()