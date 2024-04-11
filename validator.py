import bcrypt

password = b"thisismypassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

entered_password = input("Enter your password: ")
entered_password = bytes(entered_password, encoding='utf-8')
if bcrypt.checkpw(entered_password, hashed):
    print("You're logged in!")
else:
    print("Invalid login!  Please try again.")