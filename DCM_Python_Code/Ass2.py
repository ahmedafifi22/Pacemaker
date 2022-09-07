from tkinter import *
from tkinter import font
from win2 import win2

win = Tk() # creates blank window
win.title("Welcome to the Pika Pacemaker")
#win.geometry("700x300")

#New user Section

new = Label(win,text="New User")
new.grid(row=0,columnspan=2)

name = Label(win,text=" User Name:")
name.grid(row=1,sticky=E)
pw=Label(win,text="Password:")
pw.grid(row=2,sticky=E)
repass = Label(win,text="Re-enter Password:")
repass.grid(row=3,sticky=E)

name1=Entry(win)
pw1=Entry(win,show="*")
repass1=Entry(win,show="*")

name1.grid(row=1,column=1)
pw1.grid(row=2,column=1)
repass1.grid(row=3,column=1)

def storing():

    def clear():
        label.destroy()

    user1 = name1.get()
    password1 = pw1.get()
    repassg = repass1.get()


    array = list(user1)
    array2 = list(password1)

    check = '1' or '2' '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' not in array
    check2 = '1' or '2' '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' not in array2

    def error():
        error =Tk()
        error.title("Registration Rules")
        Label(error,text="*Username and Password must be minimum 5 characters long with minimum 1 number in both", fg="red").pack()

    if len(array) < 5 or len(array2) < 5 or check == TRUE or check2 == TRUE:
        error()
        return

    if user1 in open('users.txt').read():
        label = Label(win, text="Username taken!", fg="red")
        label.grid(row=4, columnspan=2)
        win.after(2000, clear)
        return

    numlines = sum(1 for line in open('users.txt'))
    if numlines == 10:
        label = Label(win, text="Max amount of users registered!", fg="red")
        label.grid(row=4,columnspan=2)  # only allows 10 users to be saved
        win.after(2000, clear)
        return

    if password1 != repassg:
        label = Label(win, text="Passwords don't match!", fg="red")
        label.grid(row=4, columnspan=2)
        win.after(2000, clear)
        return

    with open('users.txt', 'a+') as f:
        f.write(user1 + "\n")

    with open('passwords.txt', 'a+') as f:
        f.write(password1 + "\n")
        label = Label(win, text="Regisetration Successful!", fg="red")
        label.grid(row=4, columnspan=2)
        win.after(2000, clear)


    name1.delete(0, 100)
    pw1.delete(0, 100)
    repass1.delete(0, 100)


submit= Button(win,text="Sign Up", command=storing)
submit.grid(row=5,columnspan=2)


#### After Registration

existing = Label(win,text="Existing User")
existing.grid(row=0,column = 4,columnspan=2,sticky=N)

user=Label(win,text="Username:").grid(row=1,column=3)
password=Label(win,text="Passwords:").grid(row=2,column=3)

name2=Entry(win)
name2.grid(row=1,column=4)
pw2=Entry(win,show="*")
pw2.grid(row=2,column=4)


def logging():

    def clear():
        label.destroy()

    user1 = name2.get()
    password1 = pw2.get()

    array = list(user1)
    array2 = list(password1)

    check = '1' or '2' '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' not in array
    check2 = '1' or '2' '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' not in array2

    def error():
        error =Tk()
        error.title("Registration Rules")
        Label(error,text="*Username and Password must be minimum 5 characters long with minimum 1 number in both", fg="red").pack()

    if len(array) < 5 or len(array2) < 5 or check == TRUE or check2 == TRUE:
        error()
        return

    if user1  not in open('Users.txt').read():
        label = Label(win, text="Incorrect Username or Password!", fg="red")
        label.grid(row=3, column=4, columnspan=2)
        win.after(2000, clear)

    with open('Users.txt', 'r') as f: #displays a list of each line
        users = [line.strip() for line in f]

    with open('passwords.txt', 'r') as f:
        passw = [line.strip() for line in f]

    for i in range(len(users)):
        if user1 == users[i]:
            if password1 == passw[i]:
                win2(user1)
                break
    else:
        label = Label(win, text="Incorrect Username or Password!", fg="red")
        label.grid(row=3,column=4,columnspan=2)
        win.after(2000, clear)


submit= Button(win,text="Login", command=logging)
submit.grid(row=4,column=4,columnspan=2)



win.mainloop()
