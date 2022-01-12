from tkinter import *

def VOOR(user):


    voor = Tk()
    voor.title("VOOR")
    voor.geometry("800x300")

    parameters = Label(voor, text="Parameters")
    parameters.grid(row=1, column=1, columnspan=2)
    f = font.Font(parameters, parameters.cget("font"))
    f.configure(underline=True)
    parameters.configure(font=f)

    lower = Label(voor, text="VOOR Lower Rate Limit: ")
    lower.grid(row=2, column=1)
    upper = Label(voor, text="VOOR Upper Rate Limit: ")
    upper.grid(row=3, column=1)
    vamp = Label(voor, text="VOOR Ventricular Amplitude:")
    vamp.grid(row=4, column=1)
    vpulse = Label(voor, text="VOOR Ventricular Pulse Width:")
    vpulse.grid(row=5, column=1)
    maxsensor = Label(voor, text="VOOR Maximum Sensor Rate:")
    maxsensor.grid(row=6, column=1)
    acthresh = Label(voor, text="VOOR Activity Threshold:")
    acthresh.grid(row=7, column=1)
    reaction = Label(voor, text="VOOR Reaction Time:")
    reaction.grid(row=8, column=1)
    resfactor = Label(voor, text="VOOR Response Factor:")
    resfactor.grid(row=9, column=1)
    rectime = Label(voor, text="VOOR Recovery Time:")
    rectime.grid(row=10, column=1)

#Lower Rate limit
    def write1(user, value):
        with open(user, 'a+') as f:
            f.write("VOOR Lower Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store1 = partial(write1, user)

    def combine1(value):
        printlrl(value)
        store1(value)
#Upper Rate Limit
    def write2(user, value):
        with open(user, 'a+') as f:
            f.write("VOOR Upper Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store2 = partial(write2, user)

    def combine2(value):
        printurl(value)
        store2(value)
#Pulse Amplitude
    def write3(user, value):
        with open(user, 'a+') as f:
            f.write("VOOR Amplitude : " + str(value) + "\n")
        return

    from functools import partial
    store3 = partial(write3, user)

    def combine3(value):
        printvamp(value)
        store3(value)
#Pulse width
    def write4(user, value):
        if value == "0.05 ms":
            with open(user, 'a+') as f:
                f.write("VOOR Pulse Width : " + str(value) + "\n")
            return

        with open(user, 'a+') as f:
            f.write("VOOR Pulse Width : " + str(value) + " ms \n")
        return

    from functools import partial
    store4 = partial(write4, user)

    def combine4(value):
        printvpulse(value)
        store4(value)

#Max sensor rate
    def write5(user, value):
        with open(user, 'a+') as f:
            f.write("VOOR Maximum Sensor Rate : " + str(value) + " ppm \n")
        return

    from functools import partial
    store5 = partial(write5, user)

    def combine5(value):
        printMaxSenRate(value)
        store5(value)

#Activity Threshold
    def write6(user, value):
        with open(user, 'a+') as f:
            f.write("VOOR Activity Threshold : " + str(value) + "\n")
        return

    from functools import partial
    store6 = partial(write6, user)

    def combine6(value):
        printActThresh(value)
        store6(value)

#Reaction Time
    def write7(user, value):
        with open(user, 'a+') as f:
            f.write("VOOR Reaction Time : " + str(value) + " sec \n")
        return

    from functools import partial
    store7 = partial(write7, user)

    def combine7(value):
        printRT(value)
        store7(value)

#Response Factor
    def write8(user, value):
        with open(user, 'a+') as f:
            f.write("VOOR Response Factor : " + str(value) + "\n")
        return

    from functools import partial
    store8 = partial(write8, user)

    def combine8(value):
        printRF(value)
        store8(value)

#Recovery Time
    def write9(user, value):
        with open(user, 'a+') as f:
            f.write("VOOR Recovery Time : " + str(value) + " min \n")
        return

    from functools import partial
    store9 = partial(write9, user)

    def combine9(value):
        printRecTime(value)
        store9(value)

#### Setup for drop down menus

    def printlrl(value):
        final = Label(voor, text="Chosen Value : " + str(value) + " ppm").grid(row=2, column=4)
        return value

    def printurl(value):
        final = Label(voor, text="Chosen Value : " + str(value) + " ppm").grid(row=3, column=4)
        return value

    def printvamp(value):
        clean = Label(voor, text="                                ").grid(row=4, column=4)
        final = Label(voor, text="Chosen Value : " + str(value)).grid(row=4, column=4)
        return value

    def printvpulse(value):
        if value == "0.05 ms":
            final = Label(voor, text="Chosen Value : " + str(value)).grid(row=5, column=4)
        else:
            final = Label(voor, text="Chosen Value : " + str(value) + ' ms').grid(row=5, column=4)
            return value
    def printMaxSenRate(value):
        final = Label(voor, text="Chosen Value : " + str(value) + " ppm").grid(row=6, column=4)
        return value

    def printActThresh(value):
        final = Label(voor, text="Chosen Value : " + str(value)).grid(row=7, column=4)
        return value
    
    def printRT(value):
        final = Label(voor, text="Chosen Value : " + str(value) + " sec").grid(row=8, column=4)
        return value
    
    def printRF(value):
        final = Label(voor, text="Chosen Value : " + str(value)).grid(row=9, column=4)
        return value
    
    def printRecTime(value):
        final = Label(voor, text="Chosen Value : " + str(value) + " min").grid(row=10, column=4)
        return value
    
##########################################
    def func1(value):  # checks range of ppm
        if value == "30-50 ppm":
            inc()
        if value == "50-90 ppm":
            inc2()
        if value == "90-175 ppm":
            inc3()

    # Lower Limit
    para = StringVar(voor)
    choices = ['30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(voor, para, *choices, command=func1)
    popupMenu.grid(row=2, column=2)

    def inc():  # 30-50 ppm
        clean = Label(voor, text="                                ").grid(row=2, column=3)
        para = StringVar(voor)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(voor, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc2():  # 50-90 ppm
        clean = Label(voor, text="                                ").grid(row=2, column=3)
        para = StringVar(voor)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(voor, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc3():  # 90-175 ppm
        clean = Label(voor, text="                                ").grid(row=2, column=3)
        para = StringVar(voor)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(voor, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    # Upper Limit
    def func3(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc()

    para = StringVar(voor)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(voor, para, *choices, command=func3)
    popupMenu.grid(row=3, column=2)

    def uinc():  # Upper Limit increments
        para = StringVar(voor)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(voor, para, *choices, command=combine2)
        popupMenu.grid(row=3, column=3)

##### Vamp
    para = StringVar(voor)
    choices = ['OFF', '1.25 V', '2.5 V', '3.75 V', '5.0 V']
    para.set('Choose a Voltage...')
    popupMenu = OptionMenu(voor, para, *choices, command=combine3)
    popupMenu.grid(row=4, column=2)

##### Vpulse

    def pulsefunc(value):
        if value == "1-19 ms":
            pinc()
        if value == "0.05 ms":
            combine4(value)

    para = StringVar(voor)
    choices = ['0.05 ms', '1-19 ms']
    para.set('Choose Pulse Width Value...')
    popupMenu = OptionMenu(voor, para, *choices, command=pulsefunc)
    popupMenu.grid(row=5, column=2)

    def pinc():  # Pulse Increments
        para = StringVar(voor)
        choices = []
        for i in range(1, 20, 1):
            choices.append(i)
        para.set('Choose value...')
        popupMenu = OptionMenu(voor, para, *choices, command=combine4)
        popupMenu.grid(row=5, column=3)
        
#### Max Sensor Rate
    def func5(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc2()

    para = StringVar(voor)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(voor, para, *choices, command=func5)
    popupMenu.grid(row=6, column=2)

    def uinc2():  # Upper Limit increments
        para = StringVar(voor)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(voor, para, *choices, command=combine5)
        popupMenu.grid(row=6, column=3)
        
#### Activity Threshold
    para = StringVar(voor)
    choices = ['V-Low', 'Low', 'Med-Low', 'Med', 'Med-High', 'High', 'V-High']
    para.set('Choose a Threshold...')
    popupMenu = OptionMenu(voor, para, *choices, command=combine6)
    popupMenu.grid(row=7, column=2)

#### Reaction Time
    para = StringVar(voor)
    choices = ['0', '2', '3', '4', '5']
    para.set('Choose a Time...')
    popupMenu = OptionMenu(voor, para, *choices, command=combine7)
    popupMenu.grid(row=8, column=2)

#### Response Factor
    para = StringVar(voor)
    choices = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    para.set('Choose a Factor...')
    popupMenu = OptionMenu(voor, para, *choices, command=combine8)
    popupMenu.grid(row=9, column=2)


#### Recovery Time
    para = StringVar(voor)
    choices = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    para.set('Choose a Time...')
    popupMenu = OptionMenu(voor, para, *choices, command=combine9)
    popupMenu.grid(row=10, column=2)
    

    voor.mainloop()
