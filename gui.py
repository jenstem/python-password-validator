from tkinter import *
import bcrypt

# create validate function
def validate(password):
    # save hashed password
    hash = b'$2b$12$LtgtOpJ15vdK.HMw4hx3ZeujgU78gKJ.J5EIaA.YZ1R2QAJowNGOG'
    # compare entered password to hashed password
    # take code from validator.py
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        print("You're logged in!")
    else:
        print("Invalid login!  Please try again.")

root = Tk()
# set width and height
root.geometry("300x300")

# creates box for password entry
password_entry = Entry(root)
# adds to tkinter window
password_entry.pack()
# get password
# password_entry.get()

# button to hash password
# accept password after user has entered it - lambda function
button = Button(text="Validate Password", command=lambda: validate(password_entry.get()))
# adds to tkinter window
button.pack()

root.mainloop()
