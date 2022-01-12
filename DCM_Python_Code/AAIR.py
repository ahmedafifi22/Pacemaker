from tkinter import *

def AAIR(user):
    aair = Tk()
    aair.title("AAIR")
    aair.geometry("900x400")

    parameters = Label(aair, text="Parameters")
    parameters.grid(row=1, column=1, columnspan=2)
    f = font.Font(parameters, parameters.cget("font"))
    f.configure(underline=True)
    parameters.configure(font=f)

    lower = Label(aair, text="AAIR Lower Rate Limit: ")
    lower.grid(row=2, column=1)
    upper = Label(aair, text="AAIR Upper Rate Limit: ")
    upper.grid(row=3, column=1)
    aamp = Label(aair, text="AAIR Amplitude:")
    aamp.grid(row=4, column=1)
    apulse = Label(aair, text="AAIR Pulse Width:")
    apulse.grid(row=5, column=1)
    asense = Label(aair, text="AAIR Sensitivity:")
    asense.grid(row=6, column=1)
    arp = Label(aair, text="AAIR ARP:")
    arp.grid(row=7, column=1)
    pvarp = Label(aair, text="AAIR PVARP:")
    pvarp.grid(row=8, column=1)
    ahys = Label(aair, text="AAIR Hysteresis:")
    ahys.grid(row=9, column=1)
    asmooth = Label(aair, text="AAIR Rate Smoothing:")
    asmooth.grid(row=10, column=1)
    amaxsensor = Label(aair, text="AAIR Maximum Sensor Rate:")
    amaxsensor.grid(row=11, column=1)
    athreshold = Label(aair, text="AAIR Activity Threshold:")
    athreshold.grid(row=12, column=1)
    areaction = Label(aair, text="AAIR Reaction Time:")
    areaction.grid(row=13, column=1)
    aresponse = Label(aair, text="AAIR Response Factor:")
    aresponse.grid(row=14, column=1)
    arecovery = Label(aair, text="AAIR Recovery Time:")
    arecovery.grid(row=15, column=1)
      
    def write1(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Lower Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store1 = partial(write1, user)

    def combine1(value):
        printlrl(value)
        store1(value)

    def write2(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Upper Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store2 = partial(write2, user)

    def combine2(value):
        printurl(value)
        store2(value)
        
    def write3(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Amplitude : " + str(value) + "\n")
        return

    from functools import partial
    store3 = partial(write3, user)

    def combine3(value):
        printvamp(value)
        store3(value)

    def write4(user, value):
        if value == "0.05 ms":
            with open(user, 'a+') as f:
                f.write("AAIR Pulse Width : " + str(value) + "\n")
            return

        with open(user, 'a+') as f:
            f.write("AAIR Pulse Width : " + str(value) + " ms \n")
        return

    from functools import partial
    store4 = partial(write4, user)

    def combine4(value):
        printvpulse(value)
        store4(value)

    # Setup for drow down menu

    def printlrl(value):
        final = Label(aair, text="Chosen Value : " + str(value) + " ppm").grid(row=2, column=4)
        return value

    def printurl(value):
        final = Label(aair, text="Chosen Value : " + str(value) + " ppm").grid(row=3, column=4)
        return value

    def printvamp(value):
        clean = Label(aair, text="                                ").grid(row=4, column=4)
        final = Label(aair, text="Chosen Value : " + str(value)).grid(row=4, column=4)
        return value

    def printvpulse(value):
        if value == "0.05 ms":
            final = Label(aair, text="Chosen Value : " + str(value)).grid(row=5, column=4)
        else:
            final = Label(aair, text="Chosen Value : " + str(value) + ' ms').grid(row=5, column=4)
            return value

    def func1(value):  # checks range of ppm
        if value == "30-50 ppm":
            inc()
        if value == "50-90 ppm":
            inc2()
        if value == "90-175 ppm":
            inc3()
            
    # Lower Limit
    para = StringVar(aair)
    choices = ['30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(aair, para, *choices, command=func1)
    popupMenu.grid(row=2, column=2)

    def inc():  # 30-50 ppm
        clean = Label(aair, text="                                ").grid(row=2, column=3)
        para = StringVar(aair)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc2():  # 50-90 ppm
        clean = Label(aair, text="                                ").grid(row=2, column=3)
        para = StringVar(aair)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc3():  # 90-175 ppm
        clean = Label(aair, text="                                ").grid(row=2, column=3)
        para = StringVar(aair)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    # Upper Limit
    def func3(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc()

    para = StringVar(aair)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(aair, para, *choices, command=func3)
    popupMenu.grid(row=3, column=2)

    def uinc():  # Upper Limit increments
        para = StringVar(aair)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine2)
        popupMenu.grid(row=3, column=3)

    # Vamp
    para = StringVar(aair)
    choices = ['OFF', '1.25 V', '2.5 V', '3.75 V', '5.0 V']
    para.set('Choose a Voltage...')
    popupMenu = OptionMenu(aair, para, *choices, command=combine3)
    popupMenu.grid(row=4, column=2)

    # Vpulse

    def pulsefunc(value):
        if value == "1-19 ms":
            pinc()
        if value == "0.05 ms":
            combine4(value)

    para = StringVar(aair)
    choices = ['0.05 ms', '1-19 ms']
    para.set('Choose Pulse Width Value...')
    popupMenu = OptionMenu(aair, para, *choices, command=pulsefunc)
    popupMenu.grid(row=5, column=2)

    def pinc():  # Pulse Increments
        para = StringVar(aair)
        choices = []
        i = 0.1
        for i in range(1, 20, 1):
            choices.append(i)
        para.set('Choose value...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine4)
        popupMenu.grid(row=5, column=3)


    #sense

    def printsense(value):
        clean = Label(aair, text="                                ").grid(row=6, column=4)
        final = Label(aair, text="Chosen Value : " + str(value)).grid(row=6, column=4)

    def write5(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Sensitivity : " + str(value) + "\n")
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
        para = StringVar(aair)
        choices = []
        for i in range(10, 105,5):
            choices.append(i/10)
        para.set('Choose a Sensitivity...')
        popupMenu = OptionMenu(aair, para, *choices,command=combine5)
        popupMenu.grid(row=6, column=3)

    para = StringVar(aair)
    choices = ['0.25 mV', '0.5 mV', '0.75 mV', '1.0-10 mV']
    para.set('Choose a Sensitivity...')
    popupMenu = OptionMenu(aair, para, *choices, command=sensefunc)
    popupMenu.grid(row=6, column=2)

    # ARP


    def printarp(value):
        clean = Label(aair, text="                                ").grid(row=7, column=4)
        final = Label(aair, text="Chosen Value : " + str(value) + " ms").grid(row=7, column=4)

    def write6(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR ARP : " + str(value) + "\n")
        return

    from functools import partial
    store6 = partial(write6, user)

    def combine6(value):
        printarp(value)
        store6(value)

    def arpfunc(value):
        if value == "150-500 ms":
            arpinc()
        else:
            combine6(value)

    def arpinc():
        para = StringVar(aair)
        choices = []
        for i in range(150, 510, 10):
            choices.append(i)
        para.set('Choose a value...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine6)
        popupMenu.grid(row=7, column=3)

    para = StringVar(aair)
    choices = ['150-500 ms']
    para.set('Choose a range...')
    popupMenu = OptionMenu(aair, para, *choices, command=arpfunc)
    popupMenu.grid(row=7, column=2)

    # PVARP


    def printpvarp(value):
        clean = Label(aair, text="                                ").grid(row=8, column=4)
        final = Label(aair, text="Chosen Value : " + str(value) + " ms").grid(row=8, column=4)

    def write7(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR PVARP : " + str(value) + "\n")
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
        para = StringVar(aair)
        choices = []
        for i in range(150, 510, 10):
            choices.append(i)
        para.set('Choose a value...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine7)
        popupMenu.grid(row=8, column=3)

    para = StringVar(aair)
    choices = ['150-500 ms']
    para.set('Choose a range...')
    popupMenu = OptionMenu(aair, para, *choices, command=pvarpfunc)
    popupMenu.grid(row=8, column=2)

  # Hysteresis

    def printhys(value):
        clean = Label(aair, text="                                ").grid(row=9, column=4)
        final = Label(aair, text="Chosen Value : " + str(value)).grid(row=9, column=4)

    def write8(user, value):
        with open(user, 'a+') as f:
            if value == "OFF":
                f.write("AAIR Hysteresis : " + str(value) + "\n")
                return
            f.write("AAIR Hysteresis : " + str(value) + " ppm"+"\n")
        return

    from functools import partial
    store8 = partial(write8, user)

    def combine8(value):
        printhys(value)
        store8(value)

    def hysfunc(value):
        clean = Label(aair,text="                                                     ").grid(row=8,column=3)
        if value == "30-50 ppm":
            hysinc()
        if value == "50-90 ppm":
            hysinc2()
        if value == "90-175 ppm":
            hysinc3()
        if value == "OFF":
            combine8(value)

    para = StringVar(aair)
    choices = ['OFF','30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(aair, para, *choices, command=hysfunc)
    popupMenu.grid(row=9, column=2)

    def hysinc():  # 30-50 ppm
        clean = Label(aair, text="                                ").grid(row=9, column=3)
        para = StringVar(aair)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine8)
        popupMenu.grid(row=9, column=3)

    def hysinc2():  # 50-90 ppm
        clean = Label(aair, text="                                ").grid(row=9, column=3)
        para = StringVar(aair)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine8)
        popupMenu.grid(row=9, column=3)

    def hysinc3():  # 90-175 ppm
        clean = Label(aair, text="                                ").grid(row=9, column=3)
        para = StringVar(aair)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine8)
        popupMenu.grid(row=9, column=3)


    #RATE SMOOTHING

    def printsmooth(value):
        clean = Label(aair, text="                                ").grid(row=10, column=4)
        final = Label(aair, text="Chosen Value : " + str(value)).grid(row=10, column=4)

    def write9(user, value):
        with open(user, 'a+') as f:
            if value == "OFF":
                f.write("AAIR Rate Smoothing : " + str(value) + "\n")
                return
            f.write("AAIR Rate Smoothing : " + str(value) +"\n")
        return

    from functools import partial
    store9 = partial(write9, user)

    def combine9(value):
        printsmooth(value)
        store9(value)

    para = StringVar(aair)
    choices = ['OFF','3%','6%','9%','12%','15%','18%','21%','25%']
    para.set('Choose a Percentage...')
    popupMenu = OptionMenu(aair, para, *choices, command=combine9)
    popupMenu.grid(row=10, column=2)

#################################
########## 
    def write10(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Maximum Sensor Rate : " + str(value) + " ppm \n")
        return
    from functools import partial
    store10 = partial(write10, user)
    def combine10(value):
        printmsr(value)
        store10(value)
    def printmsr(value):
        final = Label(aair, text="Chosen Value: " + str(value) + " ppm").grid(row=11, column=4)
        return value
    def func4(value):
        if value == "50-175 ppm":
            msrinc()
    para = StringVar(aair)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(aair, para, *choices, command=func4)
    popupMenu.grid(row=11, column=2)
    
    def msrinc():
        para = StringVar(aair)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aair, para, *choices, command=combine10)
        popupMenu.grid(row=11, column=3)
      
##########
    def write11(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Activity Threshold : " + str(value) + "\n")
        return

    from functools import partial
    store11 = partial(write11, user)

    def combine11(value):
        printthreshold(value)
        store11(value)

    def printthreshold(value):
        final = Label(aair, text="Chosen Value : " + str(value)).grid(row=12, column=4)
        return value
    para = StringVar(aair)
    choices = ['V-Low', 'Low', 'Med-Low', 'Med', 'Med-High', 'High', 'V-High']
    para.set('Choose threshold...')
    popupMenu = OptionMenu(aair, para, *choices, command=combine11)
    popupMenu.grid(row=12, column=2)

##########
    def write12(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Reaction Time : " + str(value) + " sec \n")
        return

    from functools import partial
    store12 = partial(write12, user)

    def combine12(value):
        printreaction(value)
        store12(value)
    def printreaction(value):
        final = Label(aair, text="Chosen Value : " + str(value) + "sec").grid(row=13, column=4)
        return value
    para = StringVar(aair)
    choices = ['10', '20', '30', '40', '50']
    para.set('Choose reaction time...')
    popupMenu = OptionMenu(aair, para, *choices, command=combine12)
    popupMenu.grid(row=13, column=2)

##########
    def write13(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Response Factor : " + str(value) + " \n")
        return

    from functools import partial
    store13 = partial(write13, user)

    def combine13(value):
        printfactor(value)
        store13(value)
    def printfactor(value):
        final = Label(aair, text="Chosen Value: " + str(value)).grid(row=14, column=4)
        return value
    para = StringVar(aair)
    choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    para.set('Choose factor...')
    popupMenu = OptionMenu(aair, para, *choices, command=combine13)
    popupMenu.grid(row=14, column=2)

##########
    def write14(user, value):
        with open(user, 'a+') as f:
            f.write("AAIR Recovery Time : " + str(value) + " min \n")
        return

    from functools import partial
    store14 = partial(write14, user)

    def combine14(value):
        printrecovery(value)
        store14(value)
    def printrecovery(value):
        final = Label(aair, text="Chosen Value: " + str(value)+ "min").grid(row=15, column=4)
        return value
    para = StringVar(aair)
    choices = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    para.set('Choose recovery time...')
    popupMenu = OptionMenu(aair, para, *choices, command=combine14)
    popupMenu.grid(row=15, column=2)
    
