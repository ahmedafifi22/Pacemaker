from tkinter import *

def AOO(user):
    aoo = Tk()
    aoo.title("AOO")
    aoo.geometry("700x300")

    parameters = Label(aoo, text="Parameters")
    parameters.grid(row=1, column=1, columnspan=2)
    f = font.Font(parameters, parameters.cget("font"))
    f.configure(underline=True)
    parameters.configure(font=f)

    lower = Label(aoo, text="AOO Lower Rate Limit: ")
    lower.grid(row=2, column=1)
    upper = Label(aoo, text="AOO Upper Rate Limit: ")
    upper.grid(row=3, column=1)
    vamp = Label(aoo, text="AOO Amplitude:")
    vamp.grid(row=4, column=1)
    vpulse = Label(aoo, text="AOO Pulse Width:")
    vpulse.grid(row=5, column=1)

    # How to write chosen value into file
    def write1(user, value):
        with open(user, 'a+') as f:
            f.write("AOO Lower Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store1 = partial(write1, user)

    def combine1(value):
        printlrl(value)
        store1(value)

    def write2(user, value):
        with open(user, 'a+') as f:
            f.write("AOO Upper Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store2 = partial(write2, user)

    def combine2(value):
        printurl(value)
        store2(value)

    def write3(user, value):
        with open(user, 'a+') as f:
            f.write("AOO Amplitude : " + str(value) + "\n")
        return

    from functools import partial
    store3 = partial(write3, user)

    def combine3(value):
        printvamp(value)
        store3(value)

    def write4(user, value):
        if value == "0.05 ms":
            with open(user, 'a+') as f:
                f.write("AOO Pulse Width : " + str(value) + "\n")
            return

        with open(user, 'a+') as f:
            f.write("AOO Pulse Width : " + str(value) + " ms \n")
        return

    from functools import partial
    store4 = partial(write4, user)

    def combine4(value):
        printvpulse(value)
        store4(value)

    # Setup for drow down menu

    def printlrl(value):
        final = Label(aoo, text="Chosen Value : " + str(value) + " ppm").grid(row=2, column=4)
        return value

    def printurl(value):
        final = Label(aoo, text="Chosen Value : " + str(value) + " ppm").grid(row=3, column=4)
        return value

    def printvamp(value):
        clean = Label(aoo, text="                                ").grid(row=4, column=4)
        final = Label(aoo, text="Chosen Value : " + str(value)).grid(row=4, column=4)
        return value

    def printvpulse(value):
        if value == "0.05 ms":
            final = Label(aoo, text="Chosen Value : " + str(value)).grid(row=5, column=4)
        else:
            final = Label(aoo, text="Chosen Value : " + str(value) + ' ms').grid(row=5, column=4)
            return value

    def func1(value):  # checks range of ppm
        if value == "30-50 ppm":
            inc()
        if value == "50-90 ppm":
            inc2()
        if value == "90-175 ppm":
            inc3()

    # Lower Limit
    para = StringVar(aoo)
    choices = ['30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(aoo, para, *choices, command=func1)
    popupMenu.grid(row=2, column=2)

    def inc():  # 30-50 ppm
        clean = Label(aoo, text="                                ").grid(row=2, column=3)
        para = StringVar(aoo)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoo, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc2():  # 50-90 ppm
        clean = Label(aoo, text="                                ").grid(row=2, column=3)
        para = StringVar(aoo)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoo, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc3():  # 90-175 ppm
        clean = Label(aoo, text="                                ").grid(row=2, column=3)
        para = StringVar(aoo)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoo, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    # Upper Limit
    def func3(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc()

    para = StringVar(aoo)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(aoo, para, *choices, command=func3)
    popupMenu.grid(row=3, column=2)

    def uinc():  # Upper Limit increments
        para = StringVar(aoo)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoo, para, *choices, command=combine2)
        popupMenu.grid(row=3, column=3)

    # Vamp
    para = StringVar(aoo)
    choices = ['OFF', '1.25 V', '2.5 V', '3.75 V', '5.0 V']
    para.set('Choose a Voltage...')
    popupMenu = OptionMenu(aoo, para, *choices, command=combine3)
    popupMenu.grid(row=4, column=2)

    # Vpulse

    def pulsefunc(value):
        if value == "1-19 ms":
            pinc()
        if value == "0.05 ms":
            combine4(value)

    para = StringVar(aoo)
    choices = ['0.05 ms', '1-19 ms']
    para.set('Choose Pulse Width Value...')
    popupMenu = OptionMenu(aoo, para, *choices, command=pulsefunc)
    popupMenu.grid(row=5, column=2)

    def pinc():  # Pulse Increments
        para = StringVar(aoo)
        choices = []
        for i in range(1, 200, 1):
            choices.append(i)
        para.set('Choose value...')
        popupMenu = OptionMenu(aoo, para, *choices, command=combine4)
        popupMenu.grid(row=5, column=3)


