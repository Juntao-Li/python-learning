print("Create an account:")

username = str(input("Input your username:"))
password = str(input("Input your password:")) # Password must be str, can't be numbers, because it will change 0012 to 12

print("Log in:")
for i in range(4):
    if i < 3:
        input_username = str(input("Input your username to log in:"))
        input_password = str(input("Input your password to log in:"))
        if username == input_username and password == input_password:
            print("Successfully log in!")
            break
        else:
            print("The username or password you input is wrong!")
    else:
        print("You have already tried too many times!")