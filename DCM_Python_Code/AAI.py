from tkinter import *

def AAI(user):
    aai = Tk()
    aai.title("AAI")
    aai.geometry("900x300")

    parameters = Label(aai, text="Parameters")
    parameters.grid(row=1, column=1, columnspan=2)
    f = font.Font(parameters, parameters.cget("font"))
    f.configure(underline=True)
    parameters.configure(font=f)

    lower = Label(aai, text="AAI Lower Rate Limit: ")
    lower.grid(row=2, column=1)
    upper = Label(aai, text="AAI Upper Rate Limit: ")
    upper.grid(row=3, column=1)
    aamp = Label(aai, text="AAI Amplitude:")
    aamp.grid(row=4, column=1)
    apulse = Label(aai, text="AAI Pulse Width:")
    apulse.grid(row=5, column=1)
    asense = Label(aai, text="AAI Sensitivity:")
    asense.grid(row=6, column=1)
    arp = Label(aai, text="AAI ARP:")
    arp.grid(row=7, column=1)
    pvarp = Label(aai, text="AAI PVARP:")
    pvarp.grid(row=8, column=1)
    ahys = Label(aai, text="AAI Hysteresis:")
    ahys.grid(row=9, column=1)
    asmooth = Label(aai, text="AAI Rate Smoothing:")
    asmooth.grid(row=10, column=1)


    # How to write chosen value into file
    def write1(user, value):
        with open(user, 'a+') as f:
            f.write("AAI Lower Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store1 = partial(write1, user)

    def combine1(value):
        printlrl(value)
        store1(value)

    def write2(user, value):
        with open(user, 'a+') as f:
            f.write("AAI Upper Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store2 = partial(write2, user)

    def combine2(value):
        printurl(value)
        store2(value)

    def write3(user, value):
        with open(user, 'a+') as f:
            f.write("AAI Amplitude : " + str(value) + "\n")
        return

    from functools import partial
    store3 = partial(write3, user)

    def combine3(value):
        printvamp(value)
        store3(value)

    def write4(user, value):
        if value == "0.05 ms":
            with open(user, 'a+') as f:
                f.write("AAI Pulse Width : " + str(value) + "\n")
            return

        with open(user, 'a+') as f:
            f.write("AAI Pulse Width : " + str(value) + " ms \n")
        return

    from functools import partial
    store4 = partial(write4, user)

    def combine4(value):
        printvpulse(value)
        store4(value)

    # Setup for drow down menu

    def printlrl(value):
        final = Label(aai, text="Chosen Value : " + str(value) + " ppm").grid(row=2, column=4)
        return value

    def printurl(value):
        final = Label(aai, text="Chosen Value : " + str(value) + " ppm").grid(row=3, column=4)
        return value

    def printvamp(value):
        clean = Label(aai, text="                                ").grid(row=4, column=4)
        final = Label(aai, text="Chosen Value : " + str(value)).grid(row=4, column=4)
        return value

    def printvpulse(value):
        if value == "0.05 ms":
            final = Label(aai, text="Chosen Value : " + str(value)).grid(row=5, column=4)
        else:
            final = Label(aai, text="Chosen Value : " + str(value) + ' ms').grid(row=5, column=4)
            return value

    def func1(value):  # checks range of ppm
        if value == "30-50 ppm":
            inc()
        if value == "50-90 ppm":
            inc2()
        if value == "90-175 ppm":
            inc3()

    # Lower Limit
    para = StringVar(aai)
    choices = ['30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(aai, para, *choices, command=func1)
    popupMenu.grid(row=2, column=2)

    def inc():  # 30-50 ppm
        clean = Label(aai, text="                                ").grid(row=2, column=3)
        para = StringVar(aai)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc2():  # 50-90 ppm
        clean = Label(aai, text="                                ").grid(row=2, column=3)
        para = StringVar(aai)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc3():  # 90-175 ppm
        clean = Label(aai, text="                                ").grid(row=2, column=3)
        para = StringVar(aai)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    # Upper Limit
    def func3(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc()

    para = StringVar(aai)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(aai, para, *choices, command=func3)
    popupMenu.grid(row=3, column=2)

    def uinc():  # Upper Limit increments
        para = StringVar(aai)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine2)
        popupMenu.grid(row=3, column=3)

    # Vamp
    para = StringVar(aai)
    choices = ['OFF', '1.25 V', '2.5 V', '3.75 V', '5.0 V']
    para.set('Choose a Voltage...')
    popupMenu = OptionMenu(aai, para, *choices, command=combine3)
    popupMenu.grid(row=4, column=2)

    # Vpulse

    def pulsefunc(value):
        if value == "1-19 ms":
            pinc()
        if value == "0.05 ms":
            combine4(value)

    para = StringVar(aai)
    choices = ['0.05 ms', '1-19 ms']
    para.set('Choose Pulse Width Value...')
    popupMenu = OptionMenu(aai, para, *choices, command=pulsefunc)
    popupMenu.grid(row=5, column=2)

    def pinc():  # Pulse Increments
        para = StringVar(aai)
        choices = []
        i = 0.1
        for i in range(1, 20, 1):
            choices.append(i)
        para.set('Choose value...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine4)
        popupMenu.grid(row=5, column=3)


    #sense

    def printsense(value):
        clean = Label(aai, text="                                ").grid(row=6, column=4)
        final = Label(aai, text="Chosen Value : " + str(value)).grid(row=6, column=4)

    def write5(user, value):
        with open(user, 'a+') as f:
            f.write("AAI Sensitivity : " + str(value) + "\n")
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
        para = StringVar(aai)
        choices = []
        for i in range(10, 105,5):
            choices.append(i/10)
        para.set('Choose a Sensitivity...')
        popupMenu = OptionMenu(aai, para, *choices,command=combine5)
        popupMenu.grid(row=6, column=3)

    para = StringVar(aai)
    choices = ['0.25 mV', '0.5 mV', '0.75 mV', '1.0-10 mV']
    para.set('Choose a Sensitivity...')
    popupMenu = OptionMenu(aai, para, *choices, command=sensefunc)
    popupMenu.grid(row=6, column=2)

    # ARP


    def printarp(value):
        clean = Label(aai, text="                                ").grid(row=7, column=4)
        final = Label(aai, text="Chosen Value : " + str(value) + " ms").grid(row=7, column=4)

    def write6(user, value):
        with open(user, 'a+') as f:
            f.write("AAI ARP : " + str(value) + "\n")
        return

    from functools import partial
    store6 = partial(write6, user)

    def combine6(value):
        printarp(value)
        store6(value)

    def arpfunc(value):
        if value == "50-500 ms":
            arpinc()
        else:
            combine6(value)

    def arpinc():
        para = StringVar(aai)
        choices = []
        for i in range(50, 510, 10):
            choices.append(i)
        para.set('Choose a value...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine6)
        popupMenu.grid(row=7, column=3)

    para = StringVar(aai)
    choices = ['50-500 ms']
    para.set('Choose a range...')
    popupMenu = OptionMenu(aai, para, *choices, command=arpfunc)
    popupMenu.grid(row=7, column=2)


    # PVARP


    def printpvarp(value):
        clean = Label(aai, text="                                ").grid(row=8, column=4)
        final = Label(aai, text="Chosen Value : " + str(value) + " ms").grid(row=8, column=4)

    def write7(user, value):
        with open(user, 'a+') as f:
            f.write("AAI PVARP : " + str(value) + "\n")
        return

    from functools import partial
    store7 = partial(write7, user)

    def combine7(value):
        printpvarp(value)
        store7(value)

    def pvarpfunc(value):
        if value == "150-500 ms":
            pvarpinc()
        else:
            combine7(value)

    def pvarpinc():
        para = StringVar(aai)
        choices = []
        for i in range(150, 510, 10):
            choices.append(i)
        para.set('Choose a value...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine7)
        popupMenu.grid(row=8, column=3)

    para = StringVar(aai)
    choices = ['150-500 ms']
    para.set('Choose a range...')
    popupMenu = OptionMenu(aai, para, *choices, command=pvarpfunc)
    popupMenu.grid(row=8, column=2)

  # Hysteresis

    def printhys(value):
        clean = Label(aai, text="                                ").grid(row=9, column=4)
        final = Label(aai, text="Chosen Value : " + str(value)).grid(row=9, column=4)

    def write8(user, value):
        with open(user, 'a+') as f:
            if value == "OFF":
                f.write("AAI Hysteresis : " + str(value) + "\n")
                return
            f.write("AAI Hysteresis : " + str(value) + " ppm"+"\n")
        return

    from functools import partial
    store8 = partial(write8, user)

    def combine8(value):
        printhys(value)
        store8(value)

    def hysfunc(value):
        clean = Label(aai,text="                                                     ").grid(row=8,column=3)
        if value == "30-50 ppm":
            hysinc()
        if value == "50-90 ppm":
            hysinc2()
        if value == "90-175 ppm":
            hysinc3()
        if value == "OFF":
            combine8(value)

    para = StringVar(aai)
    choices = ['OFF','30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(aai, para, *choices, command=hysfunc)
    popupMenu.grid(row=9, column=2)

    def hysinc():  # 30-50 ppm
        clean = Label(aai, text="                                ").grid(row=9, column=3)
        para = StringVar(aai)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine8)
        popupMenu.grid(row=9, column=3)

    def hysinc2():  # 50-90 ppm
        clean = Label(aai, text="                                ").grid(row=9, column=3)
        para = StringVar(aai)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine8)
        popupMenu.grid(row=9, column=3)

    def hysinc3():  # 90-175 ppm
        clean = Label(aai, text="                                ").grid(row=9, column=3)
        para = StringVar(aai)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aai, para, *choices, command=combine8)
        popupMenu.grid(row=9, column=3)

    #RATE SMOOTHING

    def printsmooth(value):
        clean = Label(aai, text="                                ").grid(row=10, column=4)
        final = Label(aai, text="Chosen Value : " + str(value)).grid(row=10, column=4)

    def write9(user, value):
        with open(user, 'a+') as f:
            if value == "OFF":
                f.write("AAI Rate Smoothing : " + str(value) + "\n")
                return
            f.write("AAI Rate Smoothing : " + str(value) +"\n")
        return

    from functools import partial
    store9 = partial(write9, user)

    def combine9(value):
        printsmooth(value)
        store9(value)

    para = StringVar(aai)
    choices = ['OFF','3 %','6 %','9 %','12 %','15 %','18 %','21 %','25 %']
    para.set('Choose a Percentage...')
    popupMenu = OptionMenu(aai, para, *choices, command=combine9)
    popupMenu.grid(row=10, column=2)


