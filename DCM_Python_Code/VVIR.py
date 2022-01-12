from tkinter import *

def VVIR(user):


    vvir = Tk()
    vvir.title("VVIR")
    vvir.geometry("800x400")

    parameters = Label(vvir, text="Parameters")
    parameters.grid(row=1, column=1, columnspan=2)
    f = font.Font(parameters, parameters.cget("font"))
    f.configure(underline=True)
    parameters.configure(font=f)

    lower = Label(vvir, text="VVIR Lower Rate Limit: ")
    lower.grid(row=2, column=1)
    upper = Label(vvir, text="VVIR Upper Rate Limit: ")
    upper.grid(row=3, column=1)
    vamp = Label(vvir, text="VVIR Ventricular Amplitude:")
    vamp.grid(row=4, column=1)
    vpulse = Label(vvir, text="VVIR Ventricular Pulse Width:")
    vpulse.grid(row=5, column=1)
    maxsensor = Label(vvir, text="VVIR Maximum Sensor Rate:")
    maxsensor.grid(row=6, column=1)
    acthresh = Label(vvir, text="VVIR Activity Threshold:")
    acthresh.grid(row=7, column=1)
    reaction = Label(vvir, text="VVIR Reaction Time:")
    reaction.grid(row=8, column=1)
    resfactor = Label(vvir, text="VVIR Response Factor:")
    resfactor.grid(row=9, column=1)
    rectime = Label(vvir, text="VVIR Recovery Time:")
    rectime.grid(row=10, column=1)
    sense = Label(vvir,text="VVIR Sensitivity: ")
    sense.grid(row=11,column=1)
    vrp = Label(vvir,text="VVIR VRP: ")
    vrp.grid(row=12,column=1)
    hys = Label(vvir, text= "VVIR Hysteresis: ")
    hys.grid(row=13,column=1)
    rsmooz = Label(vvir,text = "VVIR Rate Smoothing: ")
    rsmooz.grid(row=14,column=1)
    
#### Lower Rate limit
    def write1(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Lower Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store1 = partial(write1, user)

    def combine1(value):
        printlrl(value)
        store1(value)
#### Upper Rate Limit
    def write2(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Upper Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store2 = partial(write2, user)

    def combine2(value):
        printurl(value)
        store2(value)
    
#### Pulse Amplitude
    def write3(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Amplitude : " + str(value) + "\n")
        return

    from functools import partial
    store3 = partial(write3, user)

    def combine3(value):
        printvamp(value)
        store3(value)

#### Pulse width
    def write4(user, value):
        if value == "0.05 ms":
            with open(user, 'a+') as f:
                f.write("VVIR Pulse Width : " + str(value) + "\n")
            return

        with open(user, 'a+') as f:
            f.write("VVIR Pulse Width : " + str(value) + " ms \n")
        return

    from functools import partial
    store4 = partial(write4, user)

    def combine4(value):
        printvpulse(value)
        store4(value)

#### Max sensor rate
    def write5(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Maximum Sensor Rate : " + str(value) + " ppm \n")
        return

    from functools import partial
    store5 = partial(write5, user)

    def combine5(value):
        printMaxSenRate(value)
        store5(value)

#### Activity Threshold
    def write6(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Activity Threshold : " + str(value) + "\n")
        return

    from functools import partial
    store6 = partial(write6, user)

    def combine6(value):
        printActThresh(value)
        store6(value)

#### Reaction Time
    def write7(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Reaction Time : " + str(value) + " sec \n")
        return

    from functools import partial
    store7 = partial(write7, user)

    def combine7(value):
        printRT(value)
        store7(value)

#### Response Factor
    def write8(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Response Factor : " + str(value) + "\n")
        return

    from functools import partial
    store8 = partial(write8, user)

    def combine8(value):
        printRF(value)
        store8(value)

#### Recovery Time
    def write9(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Recovery Time : " + str(value) + " min \n")
        return

    from functools import partial
    store9 = partial(write9, user)

    def combine9(value):
        printRecTime(value)
        store9(value)

#### Sense
    def write10(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR Sensitivity : " + str(value) + "\n")
        return

    from functools import partial
    store10 = partial(write10, user)

    def combine10(value):
        printsense(value)
        store10(value)

#### VRP
    def write11(user, value):
        with open(user, 'a+') as f:
            f.write("VVIR VRP : " + str(value) + "\n")
        return

    from functools import partial
    store11 = partial(write11, user)

    def combine11(value):
        printvrp(value)
        store11(value)

#### Hysteresis
    def write12(user, value):
        with open(user, 'a+') as f:
            if value == "OFF":
                f.write("VVIR Hysteresis : " + str(value) + "\n")
                return
            f.write("VVIR Hysteresis : " + str(value) + " ppm"+"\n")
        return

    from functools import partial
    store12 = partial(write12, user)

    def combine12(value):
        printhys(value)
        store12(value)

#### Rate Smoothing
    def write13(user, value):
        with open(user, 'a+') as f:
            if value == "OFF":
                f.write("VVIR Rate Smoothing : " + str(value) + "\n")
                return
            f.write("VVIR Rate Smoothing : " + str(value) +"\n")
        return

    from functools import partial
    store13 = partial(write13, user)

    def combine13(value):
        printsmooth(value)
        store13(value)

#### Setup for drop down menus

    def printlrl(value):
        final = Label(vvir, text="Chosen Value : " + str(value) + " ppm").grid(row=2, column=4)
        return value

    def printurl(value):
        final = Label(vvir, text="Chosen Value : " + str(value) + " ppm").grid(row=3, column=4)
        return value

    def printvamp(value):
        clean = Label(vvir, text="                                ").grid(row=4, column=4)
        final = Label(vvir, text="Chosen Value : " + str(value)).grid(row=4, column=4)
        return value

    def printvpulse(value):
        if value == "0.05 ms":
            final = Label(vvir, text="Chosen Value : " + str(value)).grid(row=5, column=4)
        else:
            final = Label(vvir, text="Chosen Value : " + str(value) + ' ms').grid(row=5, column=4)
            return value
    def printMaxSenRate(value):
        final = Label(vvir, text="Chosen Value : " + str(value) + " ppm").grid(row=6, column=4)
        return value

    def printActThresh(value):
        final = Label(vvir, text="Chosen Value : " + str(value)).grid(row=7, column=4)
        return value
    
    def printRT(value):
        final = Label(vvir, text="Chosen Value : " + str(value) + " sec").grid(row=8, column=4)
        return value
    
    def printRF(value):
        final = Label(vvir, text="Chosen Value : " + str(value)).grid(row=9, column=4)
        return value
    
    def printRecTime(value):
        final = Label(vvir, text="Chosen Value : " + str(value) + " min").grid(row=10, column=4)
        return value
    
    def printsense(value):
        clean = Label(vvir, text="                                ").grid(row=11, column=4)
        final = Label(vvir, text="Chosen Value : " + str(value)).grid(row=11, column=4)

    def printvrp(value):
        clean = Label(vvir, text="                                ").grid(row=12, column=4)
        final = Label(vvir, text="Chosen Value : " + str(value)).grid(row=12, column=4)

    def printhys(value):
        clean = Label(vvir, text="                                ").grid(row=13, column=4)
        final = Label(vvir, text="Chosen Value : " + str(value)).grid(row=13, column=4)

    def printsmooth(value):
        clean = Label(vvir, text="                                ").grid(row=14, column=4)
        final = Label(vvir, text="Chosen Value : " + str(value)).grid(row=14, column=4)

##########################################
    def func1(value):  # checks range of ppm
        if value == "30-50 ppm":
            inc()
        if value == "50-90 ppm":
            inc2()
        if value == "90-175 ppm":
            inc3()

    # Lower Limit
    para = StringVar(vvir)
    choices = ['30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(vvir, para, *choices, command=func1)
    popupMenu.grid(row=2, column=2)

    def inc():  # 30-50 ppm
        clean = Label(vvir, text="                                ").grid(row=2, column=3)
        para = StringVar(vvir)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc2():  # 50-90 ppm
        clean = Label(vvir, text="                                ").grid(row=2, column=3)
        para = StringVar(vvir)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc3():  # 90-175 ppm
        clean = Label(vvir, text="                                ").grid(row=2, column=3)
        para = StringVar(vvir)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

##### Upper Limit
    def func3(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc()

    para = StringVar(vvir)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(vvir, para, *choices, command=func3)
    popupMenu.grid(row=3, column=2)

    def uinc():  # Upper Limit increments
        para = StringVar(vvir)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine2)
        popupMenu.grid(row=3, column=3)

##### Vamp
    para = StringVar(vvir)
    choices = ['OFF', '1.25 V', '2.5 V', '3.75 V', '5.0 V']
    para.set('Choose a Voltage...')
    popupMenu = OptionMenu(vvir, para, *choices, command=combine3)
    popupMenu.grid(row=4, column=2)

##### Vpulse

    def pulsefunc(value):
        if value == "0.1-1.9 ms":
            pinc()
        if value == "0.05 ms":
            combine4(value)

    para = StringVar(vvir)
    choices = ['0.05 ms', '0.1-1.9 ms']
    para.set('Choose Pulse Width Value...')
    popupMenu = OptionMenu(vvir, para, *choices, command=pulsefunc)
    popupMenu.grid(row=5, column=2)

    def pinc():  # Pulse Increments
        para = StringVar(vvir)
        choices = []
        i = 0.1
        for i in range(10, 200, 10):
            choices.append(i / 100)
        para.set('Choose value...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine4)
        popupMenu.grid(row=5, column=3)
        
##### Max Sensor Rate
    def func5(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc2()

    para = StringVar(vvir)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(vvir, para, *choices, command=func5)
    popupMenu.grid(row=6, column=2)

    def uinc2():  # Upper Limit increments
        para = StringVar(vvir)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine5)
        popupMenu.grid(row=6, column=3)
        
##### Activity Threshold
    para = StringVar(vvir)
    choices = ['V-Low', 'Low', 'Med-Low', 'Med', 'Med-High', 'High', 'V-High']
    para.set('Choose a Threshold...')
    popupMenu = OptionMenu(vvir, para, *choices, command=combine6)
    popupMenu.grid(row=7, column=2)

##### Reaction Time
    para = StringVar(vvir)
    choices = ['10', '20', '30', '40', '50']
    para.set('Choose a Time...')
    popupMenu = OptionMenu(vvir, para, *choices, command=combine7)
    popupMenu.grid(row=8, column=2)

##### Response Factor
    para = StringVar(vvir)
    choices = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    para.set('Choose a Factor...')
    popupMenu = OptionMenu(vvir, para, *choices, command=combine8)
    popupMenu.grid(row=9, column=2)


##### Recovery Time
    para = StringVar(vvir)
    choices = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    para.set('Choose a Time...')
    popupMenu = OptionMenu(vvir, para, *choices, command=combine9)
    popupMenu.grid(row=10, column=2)
    
##### Sesne
    def sensefunc(value):
        if value == "1.0-10 mV":
            senseinc()
        else:
            combine10(value)

    def senseinc():
        para = StringVar(vvir)
        choices = []
        for i in range(10, 105,5):
            choices.append(i/10)
        para.set('Choose a Sensitivity...')
        popupMenu = OptionMenu(vvir, para, *choices,command=combine10)
        popupMenu.grid(row=11, column=3)

    para = StringVar(vvir)
    choices = ['0.25 mV', '0.5 mV', '0.75 mV', '1.0-10 mV']
    para.set('Choose a Sensitivity...')
    popupMenu = OptionMenu(vvir, para, *choices, command=sensefunc)
    popupMenu.grid(row=11, column=2)

##### VRP
    def vrpfunc(value):
        if value == "150-500 ms":
            vrpinc()
        else:
            combine11(value)

    def vrpinc():
        para = StringVar(vvir)
        choices = []
        for i in range(150, 510, 10):
            choices.append(i)
        para.set('Choose a value...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine11)
        popupMenu.grid(row=12, column=3)

    para = StringVar(vvir)
    choices = ['150-500 ms']
    para.set('Choose a range...')
    popupMenu = OptionMenu(vvir, para, *choices, command=vrpfunc)
    popupMenu.grid(row=12, column=2)

##### Hysteresis

    def hysfunc(value):
        clean = Label(vvir,text="                                                     ").grid(row=8,column=3)
        if value == "30-50 ppm":
            hysinc()
        if value == "50-90 ppm":
            hysinc2()
        if value == "90-175 ppm":
            hysinc3()
        if value == "OFF":
            combine12(value)

    para = StringVar(vvir)
    choices = ['OFF','30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(vvir, para, *choices, command=hysfunc)
    popupMenu.grid(row=13, column=2)

    def hysinc():  # 30-50 ppm
        clean = Label(vvir, text="                                ").grid(row=13, column=3)
        para = StringVar(vvir)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine12)
        popupMenu.grid(row=13, column=3)

    def hysinc2():  # 50-90 ppm
        clean = Label(vvir, text="                                ").grid(row=13, column=3)
        para = StringVar(vvir)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine12)
        popupMenu.grid(row=13, column=3)

    def hysinc3():  # 90-175 ppm
        clean = Label(vvir, text="                                ").grid(row=13, column=3)
        para = StringVar(vvir)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(vvir, para, *choices, command=combine12)
        popupMenu.grid(row=13, column=3)

##### Rate SMOOTHING
    para = StringVar(vvir)
    choices = ['OFF','3%','6%','9%','12%','15%','18%','21%','25%']
    para.set('Choose a Percentage...')
    popupMenu = OptionMenu(vvir, para, *choices, command=combine13)
    popupMenu.grid(row=14, column=2)

    
    vvir.mainloop()
