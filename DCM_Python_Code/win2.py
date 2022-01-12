from tkinter import *
import numpy as np
import time,threading
import serial
import struct
import keyboard
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from getkey import getkey, keys
import sys

def win2(user):

    win2 = Tk()
    win2.title("Welcome " + user)
    win2.geometry("600x450")


    def display(user,mode):
        with open(user, 'a+') as f:
            para = [line.strip() for line in f]

        with open(user, 'r+') as f:  # displays a list of each line
            para = [line.strip() for line in f]

        Label(win2,text="                                                          ").grid(row=2,column=2)
        Label(win2,text="                                                          ").grid(row=3,column=2)
        Label(win2,text="                                                          ").grid(row=4,column=2)
        Label(win2,text="                                                         ").grid(row=5,column=2)
        Label(win2,text="                                                                                  ").grid(row=6,column=2)
        Label(win2,text="                                                                               ").grid(row=7,column=2)
        Label(win2,text="                                                                             ").grid(row=8,column=2)
        Label(win2,text="                                                               ").grid(row=9,column=2)
        Label(win2,text="                                                               ").grid(row=10,column=2)
        Label(win2,text="                                                               ").grid(row=11,column=2)
        Label(win2,text="                                                               ").grid(row=12,column=2)
        Label(win2,text="                                                               ").grid(row=13,column=2)
        Label(win2,text="                                                               ").grid(row=14,column=2)
        Label(win2,text="                                                               ").grid(row=15,column=2)



        if mode == "VOO":

            look1 = 'VOO Lower Rate Limit : '  # displayed parameter value on win2
            look2 = 'VOO Upper Rate Limit : '  # displayed parameter value on win2
            look3 = 'VOO Amplitude : '  # displayed parameter value on win2
            look4 = 'VOO Pulse Width : '  # displayed parameter value on win2
            for i in reversed(para):
                if look1 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=2, column=2)
                    x = list(i)
                    m1=[]
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str1 = ''
                        for digit in m1:
                            str1 += str(digit)
                    break
            for i in reversed(para):
                if look2 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=3, column=2)
                    x = list(i)
                    m2 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m2.append(n)
                            str2 = ''
                            for digit in m2:
                                str2 += str(digit)
                    break
            for i in reversed(para):
                if look3 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=4, column=2)
                    x = i.split()
                    l1 = "OFF"
                    l2 = "1.25"
                    l3 = '2.5'
                    l4 = '3.75'
                    l5 = '5.0'
                    if l1 in x:
                        str3 = "0"
                    if l2 in x:
                        str3 = '70'
                    if l3 in x:
                        str3 = '2'
                    if l4 in x:
                        str3 = '3'
                    if l5 in x:
                        str3 = '4'
                    break
            for i in reversed(para):
                if look4 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=5, column=2)
                    x = i.split()
                    l1 = "0.05"
                    if l1 in x:
                        str4 = '1000'
                        break

                    x = list(i)
                    m4 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m4.append(n)
                    str4 = ''
                    for digit in m4:
                        str4 += str(digit)
                    break

            with open(user + " state", 'w') as f:
                try:
                    f.write("10\n")
                    f.write("1\n") # 0 for VOO
                    f.write(str1+"\n")
                    f.write(str2+"\n")
                    f.write(str3+"\n")
                    f.write(str4+"\n")
                    for i in range(12):
                        f.write("0\n")
                    f.close()
                except:
                    return
            return

        if mode == "AOO":
            look1 = 'AOO Lower Rate Limit : '  # displayed parameter value on win2
            look2 = 'AOO Upper Rate Limit : '  # displayed parameter value on win2
            look3 = 'AOO Amplitude : '  # displayed parameter value on win2
            look4 = 'AOO Pulse Width : '  # displayed parameter value on win2
            for i in reversed(para):
                if look1 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=2, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        st1 = ''
                        for digit in m1:
                            st1 += str(digit)
                    break
            for i in reversed(para):
                if look2 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=3, column=2)
                    x = list(i)
                    m2 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m2.append(n)
                        st2 = ''
                        for digit in m2:
                            st2 += str(digit)
                    break
            for i in reversed(para):
                if look3 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=4, column=2)
                    x = i.split()
                    l1 = "OFF"
                    l2 = "1.25"
                    l3 = '2.5'
                    l4 = '3.75'
                    l5 = '5.0'
                    if l1 in x:
                        st3 = "0"
                    if l2 in x:
                        st3 = '70'
                    if l3 in x:
                        st3 = '2'
                    if l4 in x:
                        st3 = '3'
                    if l5 in x:
                        st3 = '4'
                    break
            for i in reversed(para):
                if look4 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=5, column=2)
                    x = list(i)
                    m4 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m4.append(n)
                            st4 = ''
                            for digit in m4:
                                st4 += str(digit)
                    break

            with open(user + " state", 'w') as f:
                f.write("10\n")
                f.write("2\n") # 1 for AOO
                f.write(st1+"\n")
                f.write(st2+"\n")
                f.write("0\n")
                f.write("0\n")
                f.write(st3+"\n")
                f.write(st4+"\n")
                for i in range(10):
                    f.write("0\n")
                f.close()


            return

        if mode == "VVI":
            look1 = 'VVI Lower Rate Limit : '  # displayed parameter value on win2
            look2 = 'VVI Upper Rate Limit : '  # displayed parameter value on win2
            look3 = 'VVI Amplitude : '  # displayed parameter value on win2
            look4 = 'VVI Pulse Width : '  # displayed parameter value on win2
            look5 = 'VVI Sensitivity : '  # displayed parameter value on win2
            look6 = 'VVI VRP : '  # displayed parameter value on win2
            look7 = 'VVI Hysteresis : '  # displayed parameter value on win2
            look8 = 'VVI Rate Smoothing : '  # displayed parameter value on win2

            for i in reversed(para):
                if look1 in i:
                    l1 = Label(win2, text=i)
                    l1.grid(row=2, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str1 = ''
                        for digit in m1:
                            str1 += str(digit)
                    break
            for i in reversed(para):
                if look2 in i:
                    l2 = Label(win2, text=i)
                    l2.grid(row=3, column=2)
                    x = list(i)
                    m2 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m2.append(n)
                            str2 = ''
                            for digit in m2:
                                str2 += str(digit)
                    break
            for i in reversed(para):
                if look3 in i:
                    l3 = Label(win2, text=i)
                    l3.grid(row=4, column=2)
                    x = i.split()
                    l1 = "OFF"
                    l2 = "1.25"
                    l3 = '2.5'
                    l4 = '3.75'
                    l5 = '5.0'
                    if l1 in x:
                        str3 = "0"
                    if l2 in x:
                        str3 = '70'
                    if l3 in x:
                        str3 = '2'
                    if l4 in x:
                        str3 = '3'
                    if l5 in x:
                        str3 = '4'
                    break
            for i in reversed(para):
                if look4 in i:
                    l4 = Label(win2, text=i)
                    l4.grid(row=5, column=2)
                    x = list(i)
                    m4 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m4.append(n)
                            str4 = ''
                            for digit in m4:
                                str4 += str(digit)
                    break
            for i in reversed(para):
                if look5 in i:
                    l5 = Label(win2,text=i)
                    l5.grid(row=6,column=2)
                    x = list(i)
                    m5 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m5.append(n)
                            str5 = ''
                            for digit in m5:
                                str5 += str(digit)
                    break
            for i in reversed(para):
                if look6 in i:
                    l6 = Label(win2,text=i + " ms")
                    l6.grid(row=7,column=2)
                    x = list(i)
                    m6 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m6.append(n)
                            str6 = ''
                            for digit in m6:
                                str6 += str(digit)
                    break
            for i in reversed(para):
                if look7 in i:
                    l7 = Label(win2,text=i)
                    l7.grid(row=8,column=2)
                    x = i.split()
                    l1 = "OFF"
                    if l1 in x:
                        str7='0'
                        break

                    x = list(i)
                    m7 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m7.append(n)
                            str7 = ''
                            for digit in m7:
                                str7 += str(digit)
                    break
            for i in reversed(para):
                if look8 in i:
                    l8 = Label(win2,text=i)
                    l8.grid(row=9,column=2)
                    x = i.split()
                    l1 = "OFF"
                    if l1 in x:
                        str8 = "0"
                    x = list(i)
                    m8 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m8.append(n)
                            str8 = ''
                            for digit in m8:
                                str8 += str(digit)
                    break

            with open(user + " state", 'w') as f:
                f.write("10\n")
                f.write("5\n") # 3 for VVI
                f.write(str1+"\n")
                f.write(str2+"\n")
                f.write(str3+"\n")
                f.write(str4+"\n")
                f.write("0\n")
                f.write("0\n")
                f.write(str6 + "\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.close()
            return

        if mode == "AAI":
            look1 = 'AAI Lower Rate Limit : '  # displayed parameter value on win2
            look2 = 'AAI Upper Rate Limit : '  # displayed parameter value on win2
            look3 = 'AAI Amplitude : '  # displayed parameter value on win2
            look4 = 'AAI Pulse Width : '  # displayed parameter value on win2
            look5 = 'AAI Sensitivity : '  # displayed parameter value on win2
            look6 = 'AAI ARP : '  # displayed parameter value on win2
            look7 = 'AAI PVARP : '
            look8 = 'AAI Hysteresis : '  # displayed parameter value on win2
            look9 = 'AAI Rate Smoothing : '  # displayed parameter value on win2

            for i in reversed(para):
                if look1 in i:
                    l1 = Label(win2, text=i)
                    l1.grid(row=2, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str1 = ''
                        for digit in m1:
                            str1 += str(digit)
                    break
            for i in reversed(para):
                if look2 in i:
                    l2 = Label(win2, text=i)
                    l2.grid(row=3, column=2)
                    x = list(i)
                    m2 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m2.append(n)
                            str2 = ''
                            for digit in m2:
                                str2 += str(digit)
                    break
            for i in reversed(para):
                if look3 in i:
                    l3 = Label(win2, text=i)
                    l3.grid(row=4, column=2)
                    x = i.split()
                    l1 = "OFF"
                    l2 = "1.25"
                    l3 = '2.5'
                    l4 = '3.75'
                    l5 = '5.0'
                    if l1 in x:
                        str3 = "0"
                    if l2 in x:
                        str3 = '70'
                    if l3 in x:
                        str3 = '2'
                    if l4 in x:
                        str3 = '3'
                    if l5 in x:
                        str3 = '4'
                    break
            for i in reversed(para):
                if look4 in i:
                    l4 = Label(win2, text=i)
                    l4.grid(row=5, column=2)
                    x = list(i)
                    m4 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m4.append(n)
                            str4 = ''
                            for digit in m4:
                                str4 += str(digit)
                    break
            for i in reversed(para):
                if look5 in i:
                    l5 = Label(win2, text=i)
                    l5.grid(row=6, column=2)
                    x = list(i)
                    m5 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m5.append(n)
                            str5 = ''
                            for digit in m5:
                                str5 += str(digit)
                    break
            for i in reversed(para):
                if look6 in i:
                    l6 = Label(win2, text=i + " ms")
                    l6.grid(row=7, column=2)
                    x = list(i)
                    m6 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m6.append(n)
                            str6 = ''
                            for digit in m6:
                                str6 += str(digit)
                    break
            for i in reversed(para):
                if look7 in i:
                    l7 = Label(win2, text=i + " ms")
                    l7.grid(row=8, column=2)
                    x = list(i)
                    m7 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m7.append(n)
                            str7 = ''
                            for digit in m7:
                                str7 += str(digit)
                    break
            for i in reversed(para):
                if look8 in i:
                    l8 = Label(win2, text=i)
                    l8.grid(row=9, column=2)
                    x=i.split()
                    l1= "OFF"
                    if l1 in x:
                        str8 = "0"
                        break
                    x = list(i)
                    m8 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m8.append(n)
                            str8 = ''
                            for digit in m8:
                                str8 += str(digit)
                    break
            for i in reversed(para):
                if look9 in i:
                    l9 = Label(win2, text=i)
                    l9.grid(row=10, column=2)
                    x = list(i)
                    m9 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m9.append(n)
                            str9 = ''
                            for digit in m9:
                                str9 += str(digit)
                    break
            with open(user + " state", 'w') as f:
                f.write("10\n")
                f.write("6\n")  # 6 for AAI
                f.write(str1 + "\n")
                f.write(str2 + "\n")
                f.write("0\n")
                f.write("0\n")
                f.write(str3 + "\n")
                f.write(str4 + "\n")
                f.write('0\n')
                f.write(str6 + "\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.close()
            return

        if mode == "VOOR":
            look1 = 'VOOR Lower Rate Limit : '  # displayed parameter value on win2
            look2 = 'VOOR Upper Rate Limit : '  # displayed parameter value on win2
            look3 = 'VOOR Amplitude : '  # displayed parameter value on win2
            look4 = 'VOOR Pulse Width : '  # displayed parameter value on win2
            look5 = 'VOOR Activity Threshold :' # 70,90 by 5s
            look6 = 'VOOR Maximum Sensor Rate :'
            look7 = 'VOOR Reaction Time :'
            look8 = 'VOOR Response Factor :'
            look9 = 'VOOR Recovery Time :'

            for i in reversed(para):
                if look1 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=2, column=2)
                    x = list(i)
                    m1=[]
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str1 = ''
                        for digit in m1:
                            str1 += str(digit)
                    break
            for i in reversed(para):
                if look2 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=3, column=2)
                    x = list(i)
                    m2 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m2.append(n)
                            str2 = ''
                            for digit in m2:
                                str2 += str(digit)
                    break
            for i in reversed(para):
                if look3 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=4, column=2)
                    x = i.split()
                    l1 = "OFF"
                    l2 = "1.25"
                    l3 = '2.5'
                    l4 = '3.75'
                    l5 = '5.0'
                    if l1 in x:
                        str3 = "0"
                    if l2 in x:
                        str3 = '70'
                    if l3 in x:
                        str3 = '2'
                    if l4 in x:
                        str3 = '3'
                    if l5 in x:
                        str3 = '4'
                    break
            for i in reversed(para):
                if look4 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=5, column=2)
                    x = i.split()
                    l1 = "0.05"
                    if l1 in x:
                        str4 = '1000'
                        break

                    x = list(i)
                    m4 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m4.append(n)
                    str4 = ''
                    for digit in m4:
                        str4 += str(digit)
                    break
            for i in reversed(para):
                if look5 in i:
                    l5 = Label(win2, text=i)
                    l5.grid(row=6, column=2)
                    x = i.split()
                    l1= "V-Low"
                    l2= 'Low'
                    l3= 'Med-Low'
                    l4= 'Med'
                    l5= 'Med-High'
                    l6= 'High'
                    l7= 'V-High'
                    if l1 in x:
                        str5 = '10'
                    if l2 in x:
                        str5 = '15'
                    if l3 in x:
                        str5 = '17'
                    if l4 in x:
                        str5 = '18'
                    if l5 in x:
                        str5 = '19'
                    if l6 in x:
                        str5 = '20'
                    if l7 in x:
                        str5 = '23'
                    break
            for i in reversed(para):
                if look6 in i:
                    l6 = Label(win2, text=i)
                    l6.grid(row=7, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str6 = ''
                        for digit in m1:
                            str6 += str(digit)
                    break
            for i in reversed(para):
                if look7 in i:
                    l7 = Label(win2, text=i)
                    l7.grid(row=8, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str7 = ''
                        for digit in m1:
                            str7 += str(digit)
                    break
            for i in reversed(para):
                if look8 in i:
                    l8 = Label(win2, text=i)
                    l8.grid(row=9, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str8 = ''
                        for digit in m1:
                            str8 += str(digit)
                    break
            for i in reversed(para):
                if look9 in i:
                    l9 = Label(win2, text=i)
                    l9.grid(row=10, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str9 = ''
                        for digit in m1:
                            str9 += str(digit)
                    break
            with open(user + " state", 'w') as f:
                f.write("10\n")
                f.write("3\n")  # 3 for VOOR
                f.write(str1 + "\n")
                f.write(str2 + "\n")
                f.write(str3 + "\n")
                f.write(str4 + "\n")
                f.write('0\n')
                f.write('0\n')
                f.write('0\n')
                f.write('0\n')
                f.write('0\n')
                f.write(str5 + "\n")
                f.write(str6 + "\n")
                f.write(str7 + "\n")
                f.write(str8 + "\n")
                f.write(str9 + "\n")
                f.close()
            return

        if mode == "AOOR":
            look1 = 'AOOR Lower Rate Limit : '  # displayed parameter value on win2
            look2 = 'AOOR Upper Rate Limit : '  # displayed parameter value on win2
            look3 = 'AOOR Amplitude : '  # displayed parameter value on win2
            look4 = 'AOOR Pulse Width : '  # displayed parameter value on win2
            look5 = 'AOOR Activity Threshold :'
            look6 = 'AOOR Maximum Sensor Rate :'
            look7 = 'AOOR Reaction Time :'
            look8 = 'AOOR Response Factor :'
            look9 = 'AOOR Recovery Time :'

            for i in reversed(para):
                if look1 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=2, column=2)
                    x = list(i)
                    m1=[]
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str1 = ''
                        for digit in m1:
                            str1 += str(digit)
                    break
            for i in reversed(para):
                if look2 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=3, column=2)
                    x = list(i)
                    m2 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m2.append(n)
                            str2 = ''
                            for digit in m2:
                                str2 += str(digit)
                    break
            for i in reversed(para):
                if look3 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=4, column=2)
                    x = i.split()
                    l1 = "OFF"
                    l2 = "1.25"
                    l3 = '2.5'
                    l4 = '3.75'
                    l5 = '5.0'
                    if l1 in x:
                        str3 = "0"
                    if l2 in x:
                        str3 = '70'
                    if l3 in x:
                        str3 = '2'
                    if l4 in x:
                        str3 = '3'
                    if l5 in x:
                        str3 = '4'
                    break
            for i in reversed(para):
                if look4 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=5, column=2)
                    x = i.split()
                    l1 = "0.05"
                    if l1 in x:
                        str4 = '1000'
                        break

                    x = list(i)
                    m4 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m4.append(n)
                    str4 = ''
                    for digit in m4:
                        str4 += str(digit)
                    break
            for i in reversed(para):
                if look5 in i:
                    l5 = Label(win2, text=i)
                    l5.grid(row=6, column=2)
                    x = i.split()
                    l1= "V-Low"
                    l2= 'Low'
                    l3= 'Med-Low'
                    l4= 'Med'
                    l5= 'Med-High'
                    l6= 'High'
                    l7= 'V-High'
                    if l1 in x:
                        str5 = '10'
                    if l2 in x:
                        str5 = '15'
                    if l3 in x:
                        str5 = '17'
                    if l4 in x:
                        str5 = '18'
                    if l5 in x:
                        str5 = '19'
                    if l6 in x:
                        str5 = '20'
                    if l7 in x:
                        str5 = '23'
                    break
            for i in reversed(para):
                if look6 in i:
                    l6 = Label(win2, text=i)
                    l6.grid(row=7, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str6 = ''
                        for digit in m1:
                            str6 += str(digit)
                    break
            for i in reversed(para):
                if look7 in i:
                    l7 = Label(win2, text=i)
                    l7.grid(row=8, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str7 = ''
                        for digit in m1:
                            str7 += str(digit)
                    break
            for i in reversed(para):
                if look8 in i:
                    l8 = Label(win2, text=i)
                    l8.grid(row=9, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str8 = ''
                        for digit in m1:
                            str8 += str(digit)
                    break
            for i in reversed(para):
                if look9 in i:
                    l9 = Label(win2, text=i)
                    l9.grid(row=10, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str9 = ''
                        for digit in m1:
                            str9 += str(digit)
                    break
            with open(user + " state", 'w') as f:
                f.write("10\n")
                f.write("4\n")  # 4 for AOOR
                f.write(str1 + "\n")
                f.write(str2 + "\n")
                f.write("0\n")
                f.write("0\n")
                f.write(str3 + "\n")
                f.write(str4 + "\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write("0\n")
                f.write(str6 + "\n")
                f.write("0\n")
                f.write(str8 + "\n")
                f.write(str9 + "\n")
                f.close()
            return
        
        if mode == "VVIR":
            look1 = 'VVIR Lower Rate Limit : '  # displayed parameter value on win2
            look2 = 'VVIR Upper Rate Limit : '  # displayed parameter value on win2
            look3 = 'VVIR Amplitude : '  # displayed parameter value on win2
            look4 = 'VVIR Pulse Width : '  # displayed parameter value on win2
            look5 = 'VVIR Activity Threshold :'
            look6 = 'VVIR Maximum Sensor Rate :'
            look7 = 'VVIR Reaction Time :'
            look8 = 'VVIR Response Factor :'
            look9 = 'VVIR Recovery Time :'
            look0 = 'VVIR Sensitivity : '  # displayed parameter value on win2
            look11 = 'VVIR VRP : '  # displayed parameter value on win2
            look12 = 'VVIR Hysteresis : '  # displayed parameter value on win2
            look13 = 'VVIR Rate Smoothing : '  # displayed parameter value on win2

            for i in reversed(para):
                if look1 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=2, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str1 = ''
                        for digit in m1:
                            str1 += str(digit)
                    break
            for i in reversed(para):
                if look2 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=3, column=2)
                    x = list(i)
                    m2 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m2.append(n)
                            str2 = ''
                            for digit in m2:
                                str2 += str(digit)
                    break
            for i in reversed(para):
                if look3 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=4, column=2)
                    x = i.split()
                    l1 = "OFF"
                    l2 = "1.25"
                    l3 = '2.5'
                    l4 = '3.75'
                    l5 = '5.0'
                    if l1 in x:
                        str3 = "0"
                    if l2 in x:
                        str3 = '70'
                    if l3 in x:
                        str3 = '2'
                    if l4 in x:
                        str3 = '3'
                    if l5 in x:
                        str3 = '4'
                    break
            for i in reversed(para):
                if look4 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=5, column=2)
                    x = i.split()
                    l1 = "0.05"
                    if l1 in x:
                        str4 = '1000'
                        break

                    x = list(i)
                    m4 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m4.append(n)
                    str4 = ''
                    for digit in m4:
                        str4 += str(digit)
                    break
            for i in reversed(para):
                if look5 in i:
                    l5 = Label(win2, text=i)
                    l5.grid(row=6, column=2)
                    x = i.split()
                    l1 = "V-Low"
                    l2 = 'Low'
                    l3 = 'Med-Low'
                    l4 = 'Med'
                    l5 = 'Med-High'
                    l6 = 'High'
                    l7 = 'V-High'
                    if l1 in x:
                        str5 = '10'
                    if l2 in x:
                        str5 = '15'
                    if l3 in x:
                        str5 = '17'
                    if l4 in x:
                        str5 = '18'
                    if l5 in x:
                        str5 = '19'
                    if l6 in x:
                        str5 = '20'
                    if l7 in x:
                        str5 = '23'
                    break
            for i in reversed(para):
                if look6 in i:
                    l6 = Label(win2, text=i)
                    l6.grid(row=7, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str6 = ''
                        for digit in m1:
                            str6 += str(digit)
                    break
            for i in reversed(para):
                if look7 in i:
                    l7 = Label(win2, text=i)
                    l7.grid(row=8, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str7 = ''
                        for digit in m1:
                            str7 += str(digit)
                    break
            for i in reversed(para):
                if look8 in i:
                    l8 = Label(win2, text=i)
                    l8.grid(row=9, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str8 = ''
                        for digit in m1:
                            str8 += str(digit)
                    break
            for i in reversed(para):
                if look9 in i:
                    l9 = Label(win2, text=i)
                    l9.grid(row=10, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str9 = ''
                        for digit in m1:
                            str9 += str(digit)
                    break
            for i in reversed(para):
                if look0 in i:
                    l0 = Label(win2,text=i)
                    l0.grid(row=11,column=2)
                    x = list(i)
                    m5 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m5.append(n)
                            str0 = ''
                            for digit in m5:
                                str0 += str(digit)
                    break
            for i in reversed(para):
                if look11 in i:
                    l11 = Label(win2,text=i + " ms")
                    l11.grid(row=12,column=2)
                    x = list(i)
                    m6 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m6.append(n)
                            str11 = ''
                            for digit in m6:
                                str11 += str(digit)
                    break
            for i in reversed(para):
                if look12 in i:
                    l12 = Label(win2,text=i)
                    l12.grid(row=13,column=2)
                    x = i.split()
                    l1 = "OFF"
                    if l1 in x:
                        str12='0'
                        break

                    x = list(i)
                    m7 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m7.append(n)
                            str12 = ''
                            for digit in m7:
                                str12 += str(digit)
                    break
            for i in reversed(para):
                if look13 in i:
                    l13 = Label(win2,text=i)
                    l13.grid(row=14,column=2)
                    x = i.split()
                    l1 = "OFF"
                    if l1 in x:
                        str13 = "0"
                    x = list(i)
                    m8 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m8.append(n)
                            str13 = ''
                            for digit in m8:
                                str13 += str(digit)
                    break





            with open(user + " state", 'w') as f:
                f.write("10\n")
                f.write("7\n")  # 6 for VVIR
                f.write(str1 + "\n")
                f.write(str2 + "\n")
                f.write(str3 + "\n")
                f.write(str4 + "\n")
                f.write(str5 + "\n")
                f.write(str6 + "\n")
                f.write(str7 + "\n")
                f.write(str8 + "\n")
                f.write(str9 + "\n")
                f.write(str0 + "\n")
                f.write(str11 + "\n")
                f.write(str12+ "\n")
                f.write(str13 + "\n")
                for i in range(3):
                    f.write("0\n")
                f.close()
            return
                    
        if mode == "AAIR":
            look1 = 'AAIR Lower Rate Limit : '  # displayed parameter value on win2
            look2 = 'AAIR Upper Rate Limit : '  # displayed parameter value on win2
            look3 = 'AAIR Amplitude : '  # displayed parameter value on win2
            look4 = 'AAIR Pulse Width : '  # displayed parameter value on win2
            look5 = 'AAIR Sensitivity : '  # displayed parameter value on win2
            look6 = 'AAIR ARP : '  # displayed parameter value on win2
            look7 = 'AAIR PVARP : '
            look8 = 'AAIR Hysteresis : '  # displayed parameter value on win2
            look9 = 'AAIR Rate Smoothing : '  # displayed parameter value on win2
            look0 = 'AAIR Maximum Sensor Rate : '  # displayed parameter value on win2
            look11 = 'AAIR Activity Threshold : '  # displayed parameter value on win2
            look12 = 'AAIR Reaction Time : '  # displayed parameter value on win2
            look13 = 'AAIR Response Factor : '  # displayed parameter value on win2
            look14 = 'AAIR Recovery Time : '  # displayed parameter value on win2

            for i in reversed(para):
                if look1 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=2, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str1 = ''
                        for digit in m1:
                            str1 += str(digit)
                    break
            for i in reversed(para):
                if look2 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=3, column=2)
                    x = list(i)
                    m2 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m2.append(n)
                            str2 = ''
                            for digit in m2:
                                str2 += str(digit)
                    break
            for i in reversed(para):
                if look3 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=4, column=2)
                    x = i.split()
                    l1 = "OFF"
                    l2 = "1.25"
                    l3 = '2.5'
                    l4 = '3.75'
                    l5 = '5.0'
                    if l1 in x:
                        str3 = "0"
                    if l2 in x:
                        str3 = '70'
                    if l3 in x:
                        str3 = '2'
                    if l4 in x:
                        str3 = '3'
                    if l5 in x:
                        str3 = '4'
                    break
            for i in reversed(para):
                if look4 in i:
                    lrl = Label(win2, text=i)
                    lrl.grid(row=5, column=2)
                    x = i.split()
                    l1 = "0.05"
                    if l1 in x:
                        str4 = '1000'
                        break

                    x = list(i)
                    m4 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m4.append(n)
                    str4 = ''
                    for digit in m4:
                        str4 += str(digit)
                    break
            for i in reversed(para):
                if look5 in i:
                    l5 = Label(win2,text=i)
                    l5.grid(row=6,column=2)
                    x = list(i)
                    m5 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m5.append(n)
                            str5 = ''
                            for digit in m5:
                                str5 += str(digit)
                    break
            for i in reversed(para):
                if look6 in i:
                    l6 = Label(win2,text=i + " ms")
                    l6.grid(row=7,column=2)
                    x = list(i)
                    m6 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m6.append(n)
                            str6 = ''
                            for digit in m6:
                                str6 += str(digit)
                    break
            for i in reversed(para):
                if look7 in i:
                    l7 = Label(win2,text=i + " ms")
                    l7.grid(row=8,column=2)
                    x = list(i)
                    m6 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m6.append(n)
                            str7 = ''
                            for digit in m6:
                                str7 += str(digit)
                    break
            for i in reversed(para):
                if look8 in i:
                    l8 = Label(win2,text=i)
                    l8.grid(row=9,column=2)
                    x = i.split()
                    l1 = "OFF"
                    if l1 in x:
                        str8='0'
                        break

                    x = list(i)
                    m7 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m7.append(n)
                            str8 = ''
                            for digit in m7:
                                str8 += str(digit)
                    break
            for i in reversed(para):
                if look9 in i:
                    l9 = Label(win2,text=i)
                    l9.grid(row=10,column=2)
                    x = i.split()
                    l1 = "OFF"
                    if l1 in x:
                        str9 = "0"
                    x = list(i)
                    m8 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m8.append(n)
                            str9 = ''
                            for digit in m8:
                                str9 += str(digit)
                    break

            for i in reversed(para):
                if look0 in i:
                    l0 = Label(win2, text=i)
                    l0.grid(row=11, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str0 = ''
                        for digit in m1:
                            str0 += str(digit)
                    break

            for i in reversed(para):
                if look11 in i:
                    l11 = Label(win2, text=i)
                    l11.grid(row=12, column=2)
                    x = i.split()
                    l1 = "V-Low"
                    l2 = 'Low'
                    l3 = 'Med-Low'
                    l4 = 'Med'
                    l5 = 'Med-High'
                    l6 = 'High'
                    l7 = 'V-High'
                    if l1 in x:
                        str11 = '10'
                    if l2 in x:
                        str11 = '15'
                    if l3 in x:
                        str11 = '17'
                    if l4 in x:
                        str11 = '18'
                    if l5 in x:
                        str11 = '19'
                    if l6 in x:
                        str11 = '20'
                    if l7 in x:
                        str11 = '23'
                    break

            for i in reversed(para):
                if look12 in i:
                    l12 = Label(win2, text=i)
                    l12.grid(row=13, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str12 = ''
                        for digit in m1:
                            str12 += str(digit)
                    break
            for i in reversed(para):
                if look13 in i:
                    l13 = Label(win2, text=i)
                    l13.grid(row=14, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str13 = ''
                        for digit in m1:
                            str13 += str(digit)
                    break
            for i in reversed(para):
                if look14 in i:
                    l14 = Label(win2, text=i)
                    l14.grid(row=15, column=2)
                    x = list(i)
                    m1 = []
                    for n in x:
                        if n.isdigit() == TRUE:
                            m1.append(n)
                        str14 = ''
                        for digit in m1:
                            str14 += str(digit)
                    break
            with open(user + " state", 'w') as f:
                f.write("10\n")
                f.write("8\n")  # 7 for VVIR
                f.write(str1 + "\n")
                f.write(str2 + "\n")
                f.write("0\n")
                f.write("0\n")
                f.write(str3 + "\n")
                f.write(str4 + "\n")
                f.write("0\n")
                f.write(str6 + "\n")
                f.write("0\n")
                f.write("0\n")
                f.write(str0 + "\n")
                f.write(str12 + "\n")
                f.write(str13 + "\n")
                f.write(str14 + "\n")
                f.close()
            return


    def pace(value,user=user):
        if value == "VOO":
            display(user,value)
            with open(user, 'a+') as f:
                f.write(value + "\n")
        if value == "AOO":
            display(user,value)
            with open(user, 'a+') as f:
                f.write(value + "\n")
        if value == "VVI":
            display(user,value)
            with open(user, 'a+') as f:
                f.write(value + "\n")
        if value == "AAI":
            display(user,value)
            with open(user, 'a+') as f:
                f.write(value + "\n")
        if value == "VOOR":
            display(user,value)
            with open(user, 'a+') as f:
                f.write(value + "\n")
        if value == "AOOR":
            display(user,value)
            with open(user, 'a+') as f:
                f.write(value + "\n")
        if value == "VVIR":
            display(user,value)
            with open(user, 'a+') as f:
                f.write(value + "\n")
        if value == "AAIR":
            display(user,value)
            with open(user, 'a+') as f:
                f.write(value + "\n")




    def dd(type):
        clean = Label(win2,text = '                                                             ').grid(row=3,column=1)
        if type == 'Normal':
            para = StringVar(win2)
            choices = ['VOO', 'AOO','VVI','AAI']
            para.set('Choose Pacing Mode...')
            popupMenu = OptionMenu(win2, para, *choices, command=pace)
            popupMenu.grid(row=3, column=1)
        else:
            para = StringVar(win2)
            choices = ['VOOR', 'AOOR', 'VVIR', 'AAIR']
            para.set('Choose Pacing Mode...')
            popupMenu = OptionMenu(win2, para, *choices, command=pace)
            popupMenu.grid(row=3, column=1)

    para = StringVar(win2)
    choices = ['Normal','Rate Adaptive']
    para.set('Choose Pacing Mode...')
    popupMenu = OptionMenu(win2, para, *choices, command=dd)
    popupMenu.grid(row=2, column=1)
    parameters = Label(win2, text="Parameters")
    parameters.grid(row=1, column=2)


    from VOO import VOO
    from AOO import AOO
    from VVI import VVI
    from AAI import AAI
    from VOOR import VOOR
    from AOOR import AOOR
    from VVIR import VVIR
    from AAIR import AAIR


    #Win2 stuff #######

    def change(user=user):

        with open(user, 'r+') as f:  # displays a list of each line
            para = [line.strip() for line in f]
        for i in reversed(para):
            if i == 'VOO':
                VOO(user)
                return
            if i == 'AOO':
                AOO(user)
                return
            if i == 'VVI':
                VVI(user)
                return
            if i == 'AAI':
                AAI(user)
                return
            if i == 'VOOR':
                VOOR(user)
                return
            if i == 'AOOR':
                AOOR(user)
                return
            if i == 'VVIR':
                VVIR(user)
                return
            if i == 'AAIR':
                AAIR(user)
                return
    change = Button(win2, text="Change Parameters", command=change)
    change.grid(row=4, column=1)

    def refresh(user=user):
        with open(user, 'r+') as f:  # displays a list of each line
            para = [line.strip() for line in f]
        for i in reversed(para):
            if i == 'VOO':
                display(user,'VOO')
                return
            if i == 'AOO':
                display(user,'AOO')
                return
            if i == 'VVI':
                display(user,'VVI')
                return
            if i == 'AAI':
                display(user,'AAI')
                return
            if i == 'VOOR':
                display(user, 'VOOR')
                return
            if i == 'AOOR':
                display(user, 'AOOR')
                return
            if i == 'VVIR':
                display(user, 'VVIR')
                return
            if i == 'AAIR':
                display(user, 'AAIR')
                return

    refresh = Button(win2, text="REFRESH", command=refresh)
    refresh.grid(row=20, column=2)

   #------------
    #---------------

    def upload():
        try:
            with open(user+' state', 'r') as f:
                para = [line.strip() for line in f]
                for i in range(16):
                    print(para[i])

                ser = serial.Serial('/dev/tty.usbmodem000621000000', 115200)
                print(ser.name)

                ser.isOpen()
                print("Serial port opened")



                ser.write(struct.pack('<HHHHHHHHHHHHHHHH', int(1000), int(para[1]), int(para[2]), int(para[3]), int(para[4]), int(para[5]), int(para[6]), int(para[7]), int(para[8]), int(para[9]), int(para[10]), int(para[11]), int(para[12]), int(para[13]), int(para[14]), int(para[15])))
                #ser.write(struct.pack('<H', int(20)))
                # y=1
                # while (y):
                #     out = ''
                #     while ((ser.inWaiting()) > 0):
                #         print("INloop2")
                #         bytesToRead = 16
                #         out = ser.read(bytesToRead)
                #         x = struct.unpack('<dd', out)
                #         out = ''
                #         print(x)
                #         y=0
                #     break
                #
                # print("outloop")
                if (ser.is_open):
                    s1 = Tk()
                    s1.geometry("300x40")
                    s1.title("Serial Communication")
                    Label(s1,text = "Upload Successful!").pack()
        except:
                s1 = Tk()
                s1.geometry("300x40")
                s1.title("Serial Communication")
                Label(s1, text="Upload Failed,please connect device.").pack()



    upload = Button(win2,text = "Upload", command=upload)
    upload.grid(row=20,column=1)


    modes = Label(win2, text="Pacing Modes")
    modes.grid(row=1, column=1)
    f = font.Font(modes, modes.cget("font"))
    f.configure(underline=True)
    modes.configure(font=f)
    parameters = Label(win2, text="Parameters")
    parameters.grid(row=1, column=2)
    parameters.configure(font=f)

    fig = plt.figure()
    fig.set_size_inches(11, 6)
    axis = fig.add_subplot(1, 1, 1)
    # fig2 = plt.figure()
    # fig2.set_size_inches(11, 6)
    # axis2 = fig.add_subplot(1, 1, 1)


    x_axis = [] #time
    vent_axis = []
    atr_axis = []

    #from game import egram
    global gtime
    gtime = 0
    def streamdata():
        ser = serial.Serial('/dev/tty.usbmodem000621000000', 115200)
        ser.isOpen()
        ser.write(struct.pack('<HHHHHHHHHHHHHHHH', int(2000), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0), int(0)))
        data = ser.read(16)
        x = struct.unpack('<dd', data)
        global gtime
        if abs(x[0]) < 1:
            if abs(x[0]) > 0.1:
                vent_axis.append(x[0])
                atr_axis.append(x[1])
                x_axis.append(gtime * 0.05)

        # if abs(x[1]) < 1:
        #     if abs(x[1]) > 0.1:
        #         x_axis.append(gtime * 0.1)
        #         atr_axis.append(x[1])
        gtime = gtime +1
        if len(x_axis)>100:
            del (x_axis[0])
            del (vent_axis[0])
            del (atr_axis[0])

        print(x[0])
        print(x[1])
        datastream = threading.Timer(0.01, streamdata)  # Timer to call grab_data function every 0.1s
        datastream.start()
        def close(self):
            datastream.cancel()
        win2.bind("<Double-Button-1>",close)



    def animate(i):
        axis.clear()
        axis.plot(x_axis, vent_axis, label='Vent_Signal')
        axis.plot(x_axis, atr_axis, label='Atr_Signal')
        axis.set_xlabel('Time (s)')
        axis.set_ylabel('Amplitude (mV)')
        axis.set_ylim(bottom=0.5001, top=0.5019)
        axis.set_title('Egram')
        axis.legend(loc='upper right')


    def egram():
        global xtime
        global timer
        streamdata()
        ani = animation.FuncAnimation(fig, animate, interval=100)
        #timer.add_callback(close_event)
        #timer.start()
        plt.show()

        print("start graphing")





    egramb = Button(win2,text="Display E-Gram",command=egram)
    egramb.grid(row=21,column=1)

    win2.mainloop()
