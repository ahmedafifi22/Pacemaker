from tkinter import *

def AOOR(user):
    aoor = Tk()
    aoor.title("AOOR")
    aoor.geometry("900x300")

    parameters = Label(aoor, text="Parameters")
    parameters.grid(row=1, column=1, columnspan=2)
    f = font.Font(parameters, parameters.cget("font"))
    f.configure(underline=True)
    parameters.configure(font=f)

    lower = Label(aoor, text="AOOR Lower Rate Limit: ")
    lower.grid(row=2, column=1)
    upper = Label(aoor, text="AOOR Upper Rate Limit: ")
    upper.grid(row=3, column=1)
    vamp = Label(aoor, text="AOOR Amplitude: ")
    vamp.grid(row=4, column=1)
    vpulse = Label(aoor, text="AOOR Pulse Width: ")
    vpulse.grid(row=5, column=1)
    amaxsensor = Label(aoor, text="AOOR Maximum Sensor Rate: ")
    amaxsensor.grid(row=6, column=1)
    athreshold = Label(aoor, text="AOOR Activity Threshold: ")
    athreshold.grid(row=7, column=1)
    areaction = Label(aoor, text="AOOR Reaction Time: ")
    areaction.grid(row=8, column=1)
    aresponse = Label(aoor, text="AOOR Response Factor: ")
    aresponse.grid(row=9, column=1)
    arecovery = Label(aoor, text="AOOR Recovery Time: ")
    arecovery.grid(row=10, column=1)

    # How to write chosen value into file
    def write1(user, value):
        with open(user, 'a+') as f:
            f.write("AOOR Lower Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store1 = partial(write1, user)

    def combine1(value):
        printlrl(value)
        store1(value)

    def write2(user, value):
        with open(user, 'a+') as f:
            f.write("AOOR Upper Rate Limit : " + str(value) + " ppm \n")
        return

    from functools import partial
    store2 = partial(write2, user)

    def combine2(value):
        printurl(value)
        store2(value)

    def write3(user, value):
        with open(user, 'a+') as f:
            f.write("AOOR Amplitude : " + str(value) + "\n")
        return

    from functools import partial
    store3 = partial(write3, user)

    def combine3(value):
        printvamp(value)
        store3(value)

    def write4(user, value):
        if value == "0.05 ms":
            with open(user, 'a+') as f:
                f.write("AOOR Pulse Width : " + str(value) + "\n")
            return

        with open(user, 'a+') as f:
            f.write("AOOR Pulse Width : " + str(value) + " ms \n")
        return

    from functools import partial
    store4 = partial(write4, user)

    def combine4(value):
        printvpulse(value)
        store4(value)

    # Setup for drow down menu

    def printlrl(value):
        final = Label(aoor, text="Chosen Value : " + str(value) + " ppm").grid(row=2, column=4)
        return value

    def printurl(value):
        final = Label(aoor, text="Chosen Value : " + str(value) + " ppm").grid(row=3, column=4)
        return value

    def printvamp(value):
        clean = Label(aoor, text="                                ").grid(row=4, column=4)
        final = Label(aoor, text="Chosen Value : " + str(value)).grid(row=4, column=4)
        return value

    def printvpulse(value):
        if value == "0.05 ms":
            final = Label(aoor, text="Chosen Value : " + str(value)).grid(row=5, column=4)
        else:
            final = Label(aoor, text="Chosen Value : " + str(value) + ' ms').grid(row=5, column=4)
            return value

    def func1(value):  # checks range of ppm
        if value == "30-50 ppm":
            inc()
        if value == "50-90 ppm":
            inc2()
        if value == "90-175 ppm":
            inc3()

    # Lower Limit
    para = StringVar(aoor)
    choices = ['30-50 ppm', '50-90 ppm', '90-175 ppm']
    para.set('Choose ppm range...')
    popupMenu = OptionMenu(aoor, para, *choices, command=func1)
    popupMenu.grid(row=2, column=2)

    def inc():  # 30-50 ppm
        clean = Label(aoor, text="                                ").grid(row=2, column=3)
        para = StringVar(aoor)
        choices = ['30', '35', '40', '45', '50']
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoor, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc2():  # 50-90 ppm
        clean = Label(aoor, text="                                ").grid(row=2, column=3)
        para = StringVar(aoor)
        choices = []
        for i in range(50, 91):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoor, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    def inc3():  # 90-175 ppm
        clean = Label(aoor, text="                                ").grid(row=2, column=3)
        para = StringVar(aoor)
        choices = []
        for i in range(90, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoor, para, *choices, command=combine1)
        popupMenu.grid(row=2, column=3)

    # Upper Limit
    def func3(value):  # checks range of ppm  need to be able to place dropdown menu
        if value == "50-175 ppm":
            uinc()

    para = StringVar(aoor)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(aoor, para, *choices, command=func3)
    popupMenu.grid(row=3, column=2)

    def uinc():  # Upper Limit increments
        para = StringVar(aoor)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoor, para, *choices, command=combine2)
        popupMenu.grid(row=3, column=3)

    # Vamp
    para = StringVar(aoor)
    choices = ['OFF', '1.25 V', '2.5 V', '3.75 V', '5.0 V']
    para.set('Choose a Voltage...')
    popupMenu = OptionMenu(aoor, para, *choices, command=combine3)
    popupMenu.grid(row=4, column=2)

    # Vpulse

    def pulsefunc(value):
        if value == "1-19 ms":
            pinc()
        if value == "0.05 ms":
            combine4(value)

    para = StringVar(aoor)
    choices = ['0.05 ms', '1-19 ms']
    para.set('Choose Pulse Width Value...')
    popupMenu = OptionMenu(aoor, para, *choices, command=pulsefunc)
    popupMenu.grid(row=5, column=2)

    def pinc():  # Pulse Increments
        para = StringVar(aoor)
        choices = []
        i = 0.1
        for i in range(1, 20, 1):
            choices.append(i)
        para.set('Choose value...')
        popupMenu = OptionMenu(aoor, para, *choices, command=combine4)
        popupMenu.grid(row=5, column=3)
###############################################################
########## 
    def write5(user, value):
        with open(user, 'a+') as f:
            f.write("AOOR Maximum Sensor Rate : " + str(value) + " ppm \n")
        return
    from functools import partial
    store5 = partial(write5, user)
    def combine5(value):
        printmsr(value)
        store5(value)
    def printmsr(value):
        final = Label(aoor, text="Chosen Value: " + str(value) + " ppm").grid(row=6, column=4)
        return value
    def func4(value):
        if value == "50-175 ppm":
            msrinc()
    para = StringVar(aoor)
    choices = ['50-175 ppm']
    para.set('Choose ppm Range...')
    popupMenu = OptionMenu(aoor, para, *choices, command=func4)
    popupMenu.grid(row=6, column=2)
    
    def msrinc():
        para = StringVar(aoor)
        choices = []
        for i in range(50, 180, 5):
            choices.append(i)
        para.set('Choose ppm...')
        popupMenu = OptionMenu(aoor, para, *choices, command=combine5)
        popupMenu.grid(row=6, column=3)
      
##########
    def write6(user, value):
        with open(user, 'a+') as f:
            f.write("AOOR Activity Threshold : " + str(value) + "\n")
        return

    from functools import partial
    store6 = partial(write6, user)

    def combine6(value):
        printthreshold(value)
        store6(value)

    def printthreshold(value):
        final = Label(aoor, text="Chosen Value : " + str(value)).grid(row=7, column=4)
        return value
    para = StringVar(aoor)
    choices = ['V-Low', 'Low', 'Med-Low', 'Med', 'Med-High', 'High', 'V-High']
    para.set('Choose threshold...')
    popupMenu = OptionMenu(aoor, para, *choices, command=combine6)
    popupMenu.grid(row=7, column=2)

##########
    def write7(user, value):
        with open(user, 'a+') as f:
            f.write("AOOR Reaction Time : " + str(value) + " sec \n")
        return

    from functools import partial
    store7 = partial(write7, user)

    def combine7(value):
        printreaction(value)
        store7(value)
    def printreaction(value):
        final = Label(aoor, text="Chosen Value : " + str(value) + "sec").grid(row=8, column=4)
        return value
    para = StringVar(aoor)
    choices = ['10', '20', '30', '40', '50']
    para.set('Choose reaction time...')
    popupMenu = OptionMenu(aoor, para, *choices, command=combine7)
    popupMenu.grid(row=8, column=2)

##########
    def write8(user, value):
        with open(user, 'a+') as f:
            f.write("AOOR Response Factor : " + str(value) + " \n")
        return

    from functools import partial
    store8 = partial(write8, user)

    def combine8(value):
        printfactor(value)
        store8(value)
    def printfactor(value):
        final = Label(aoor, text="Chosen Value: " + str(value)).grid(row=9, column=4)
        return value
    para = StringVar(aoor)
    choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    para.set('Choose factor...')
    popupMenu = OptionMenu(aoor, para, *choices, command=combine8)
    popupMenu.grid(row=9, column=2)

##########
    def write9(user, value):
        with open(user, 'a+') as f:
            f.write("AOOR Recovery Time : " + str(value) + " min \n")
        return

    from functools import partial
    store9 = partial(write9, user)

    def combine9(value):
        printrecovery(value)
        store9(value)
    def printrecovery(value):
        final = Label(aoor, text="Chosen Value :  " + str(value)+ "min").grid(row=10, column=4)
        return value
    para = StringVar(aoor)
    choices = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    para.set('Choose recovery time...')
    popupMenu = OptionMenu(aoor, para, *choices, command=combine9)
    popupMenu.grid(row=10, column=2)

        

