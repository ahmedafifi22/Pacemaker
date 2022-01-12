from tkinter import *

def VVI(user):


    vvi = Tk()
    vvi.title("VVI")
    vvi.geometry("900x300")

    parameters = Label(vvi, text="Parameters")
    parameters.grid(row=1, column=1, columnspan=2)
    f = font.Font(parameters, parameters.cget("font"))
    f.configure(underline=True)
    parameters.configure(font=f)

    lower = Label(vvi, text="VVI Lower Rate Limit: ")
    lower.grid(row=2, column=1)
    upper = Label(vvi, text="VVI Upper Rate Limit: ")
    upper.grid(row=3, column=1)
    vamp = Label(vvi, text="VVI Amplitude: ")
    vamp.grid(row=4, column=1)
    vpulse = Label(vvi, text="VVI Pulse Width: ")
    vpulse.grid(row=5, column=1)
    sense = Label(vvi,text="VVI Sensitivity: ")
    sense.grid(row=6,column=1)
    vrp = Label(vvi,text="VVI VRP: ")
    vrp.grid(row=7,column=1)
    hys = Label(vvi, text= "VVI Hysteresis: ")
    hys.grid(row=8,column=1)
    rsmooz = Label(vvi,text = "VVI Rate Smoothing: ")
    rsmooz.grid(row=9,column=1)

    def write1(user, value):
        with open(user, 'a+') as f:
            f.write("VVI Lower Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store1 = partial(write1, user)

    def combine1(value):
        printlrl(value)
        store1(value)

    def write2(user, value):
        with open(user, 'a+') as f:
            f.write("VVI Upper Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store2 = partial(write2, user)

    def combine2(value):
        printurl(value)
        store2(value)

    def write3(user, value):
        with open(user, 'a+') as f:
            f.write("VVI Amplitude : " + str(value) + "\n")
        return

    from functools import partial
    store3 = partial(write3, user)

    def combine3(value):
        printvamp(value)
        store3(value)

    def write4(user, value):
        if value == "0.05 ms":
            with open(user, 'a+') as f:
                f.write("VVI Pulse Width : " + str(value) + "\n")
            return

        with open(user, 'a+') as f:
            f.write("VVI Pulse Width : " + str(value) + " ms \n")
        return

    from functools import partial
    store4 = partial(write4, user)

    def combine4(value):
        printvpulse(value)
        store4(value)

    # Setup for drow down menu

    def printlrl(value):
        final = Label(vvi, text="Chosen Value : " + str(value) + " ppm").grid(row=2, column=4)
        return value

    def printurl(value):
        final = Label(vvi, text="Chosen Value : " + str(value) + " ppm").grid(row=3, column=4)
        return value

    def printvamp(value):
        clean = Label(vvi, text="                                ").grid(row=4, column=4)
        final = Label(vvi, text="Chosen Value : " + str(value)).grid(row=4, column=4)
        return value

    def printvpulse(value):
        if value == "0.05 ms":
            final = Label(vvi, text="Chosen Value : " + str(value)).grid(row=5, column=4)
        else:
            final = Label(vvi, text="Chosen Value : " + str(value) + ' ms').grid(row=5, column=4)
            return value

    def printsense(value):
        clean = Label(vvi, text="                                ").grid(row=6, column=4)
        final = Label(vvi, text="Chosen Value : " + str(value)).grid(row=6, column=4)

    def printvrp(value):
        clean = Label(vvi, text="                                ").grid(row=7, column=4)
        final = Label(vvi, text="Chosen Value : " + str(value)).grid(row=7, column=4)


    # Lower Limit

    def func1(value):  # checks range of ppm
        if value == "30-50 ppm":
            inc()
        if value == "50-90 ppm":
            inc2()
        if value == "90-175 ppm":
            inc3()

    para = StringVar(vvi)
    choices = ['30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(vvi, para, *choices, command=func1)
    popupMenu.grid(row=2, column=2)

    def inc():  # 30-50 ppm
        clean = Label(vvi, text="                                ").grid(row=2, column=3)
        para = StringVar(vvi)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc2():  # 50-90 ppm
        clean = Label(vvi, text="                                ").grid(row=2, column=3)
        para = StringVar(vvi)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc3():  # 90-175 ppm
        clean = Label(vvi, text="                                ").grid(row=2, column=3)
        para = StringVar(vvi)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    # Upper Limit
    def func3(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc()

    para = StringVar(vvi)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(vvi, para, *choices, command=func3)
    popupMenu.grid(row=3, column=2)

    def uinc():  # Upper Limit increments
        para = StringVar(vvi)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine2)
        popupMenu.grid(row=3, column=3)

    # Vamp
    para = StringVar(vvi)
    choices = ['OFF', '1.25 V', '2.5 V', '3.75 V', '5.0 V']
    para.set('Choose a Voltage...')
    popupMenu = OptionMenu(vvi, para, *choices, command=combine3)
    popupMenu.grid(row=4, column=2)

    # Vpulse

    def pulsefunc(value):
        if value == "1-19 ms":
            pinc()
        if value == "0.05 ms":
            combine4(value)

    para = StringVar(vvi)
    choices = ['0.05 ms', '1-19 ms']
    para.set('Choose Pulse Width Value...')
    popupMenu = OptionMenu(vvi, para, *choices, command=pulsefunc)
    popupMenu.grid(row=5, column=2)

    def pinc():  # Pulse Increments
        para = StringVar(vvi)
        choices = []
        for i in range(1, 20, 1):
            choices.append(i)
        para.set('Choose value...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine4)
        popupMenu.grid(row=5, column=3)


    #sense

    def write5(user, value):
        with open(user, 'a+') as f:
            f.write("VVI Sensitivity : " + str(value) + "\n")
        return

    from functools import partial
    store5 = partial(write5, user)

    def combine5(value):
        printsense(value)
        store5(value)

    def sensefunc(value):
        if value == "1.0-10 mV":
            senseinc()
        else:
            combine5(value)

    def senseinc():
        para = StringVar(vvi)
        choices = []
        for i in range(10, 105,5):
            choices.append(i/10)
        para.set('Choose a Sensitivity...')
        popupMenu = OptionMenu(vvi, para, *choices,command=combine5)
        popupMenu.grid(row=6, column=3)

    para = StringVar(vvi)
    choices = ['0.25 mV', '0.5 mV', '0.75 mV', '1.0-10 mV']
    para.set('Choose a Sensitivity...')
    popupMenu = OptionMenu(vvi, para, *choices, command=sensefunc)
    popupMenu.grid(row=6, column=2)

    # VRP

    def write6(user, value):
        with open(user, 'a+') as f:
            f.write("VVI VRP : " + str(value) + "\n")
        return

    from functools import partial
    store6 = partial(write6, user)

    def combine6(value):
        printvrp(value)
        store6(value)

    def vrpfunc(value):
        if value == "50-500 ms":
            vrpinc()
        else:
            combine6(value)

    def vrpinc():
        para = StringVar(vvi)
        choices = []
        for i in range(50, 510, 10):
            choices.append(i)
        para.set('Choose a value...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine6)
        popupMenu.grid(row=7, column=3)

    para = StringVar(vvi)
    choices = ['50-500 ms']
    para.set('Choose a range...')
    popupMenu = OptionMenu(vvi, para, *choices, command=vrpfunc)
    popupMenu.grid(row=7, column=2)

    # Hysteresis

    def printhys(value):
        clean = Label(vvi, text="                                ").grid(row=8, column=4)
        final = Label(vvi, text="Chosen Value : " + str(value)).grid(row=8, column=4)

    def write7(user, value):
        with open(user, 'a+') as f:
            if value == "OFF":
                f.write("VVI Hysteresis : " + str(value) + "\n")
                return
            f.write("VVI Hysteresis : " + str(value) + " ppm"+"\n")
        return

    from functools import partial
    store7 = partial(write7, user)

    def combine7(value):
        printhys(value)
        store7(value)

    def hysfunc(value):
        clean = Label(vvi,text="                                                     ").grid(row=8,column=3)
        if value == "30-50 ppm":
            hysinc()
        if value == "50-90 ppm":
            hysinc2()
        if value == "90-175 ppm":
            hysinc3()
        if value == "OFF":
            combine7(value)

    para = StringVar(vvi)
    choices = ['OFF','30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(vvi, para, *choices, command=hysfunc)
    popupMenu.grid(row=8, column=2)

    def hysinc():  # 30-50 ppm
        clean = Label(vvi, text="                                ").grid(row=8, column=3)
        para = StringVar(vvi)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine7)
        popupMenu.grid(row=8, column=3)

    def hysinc2():  # 50-90 ppm
        clean = Label(vvi, text="                                ").grid(row=8, column=3)
        para = StringVar(vvi)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine7)
        popupMenu.grid(row=8, column=3)

    def hysinc3():  # 90-175 ppm
        clean = Label(vvi, text="                                ").grid(row=8, column=3)
        para = StringVar(vvi)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvi, para, *choices, command=combine7)
        popupMenu.grid(row=8, column=3)


    #RATE SMOOTHING

    def printsmooth(value):
        clean = Label(vvi, text="                                ").grid(row=9, column=4)
        final = Label(vvi, text="Chosen Value : " + str(value)).grid(row=9, column=4)

    def write8(user, value):
        with open(user, 'a+') as f:
            if value == "OFF":
                f.write("VVI Rate Smoothing : " + str(value) + "\n")
                return
            f.write("VVI Rate Smoothing : " + str(value) +"\n")
        return

    from functools import partial
    store8 = partial(write8, user)

    def combine8(value):
        printsmooth(value)
        store8(value)

    para = StringVar(vvi)
    choices = ['OFF','3 %','6 %','9 %','12 %','15 %','18 %','21 %','25 %']
    para.set('Choose a Percentage...')
    popupMenu = OptionMenu(vvi, para, *choices, command=combine8)
    popupMenu.grid(row=9, column=2)



    vvi.mainloop()