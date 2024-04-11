from tkinter import *
import bcrypt


def validate(password):
    hash = b'$2b$12$LtgtOpJ15vdK.HMw4hx3ZeujgU78gKJ.J5EIaA.YZ1R2QAJowNGOG'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        print("You're logged in!")
    else:
        print("Invalid login!  Please try again.")


root = Tk()
root.geometry("300x300")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="Validate Password", command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()
