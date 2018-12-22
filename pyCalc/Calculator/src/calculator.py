'''
Created on April 14, 2016
@author: Anthony Frazier 
'''

import tkinter;

gui = tkinter.Tk();
gui.title("Calculator")
entry = ""
entry = tkinter.StringVar()

topframe = tkinter.Frame(gui,  background = "Grey")
topframe.pack()
numberentry = tkinter.Entry(topframe, textvariable = entry, bd = 20)
numberentry.pack(side = "top")
numberentry.focus()

def clear():
    numberentry.delete(first = 0, last = "end");
    return

#Work on this function
def addNumber(number):
    newentry = ""
    newentry = entry.get() + number
    entry.set(newentry)
    return
def equal():
    try: 
        result = ""
        result = eval(entry.get())
        entry.set(result)
    except:
        entry.set("Error")
    return 
  
frame1 = tkinter.Frame(gui)
frame1.pack()
button1 = tkinter.Button(frame1, padx = 20, pady = 20, text = "1", 
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("1"))
button1.pack(side = "left")
button2 = tkinter.Button(frame1, text = "2", padx = 20, pady = 20,
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("2"))
button2.pack(side = "left")
button3 = tkinter.Button(frame1, text = "3", padx = 20, pady = 20,
                          fg ="Black", bg = "Grey", bd= 10, 
                        command = lambda : addNumber("3"))
button3.pack(side = "left")
buttonplus = tkinter.Button(frame1, text = "+", padx = 20, pady = 20, 
                            fg ="Black", bg = "Grey", bd= 10, 
                            command = lambda : addNumber("+"))
buttonplus.pack(side = "left")

frame2 = tkinter.Frame(gui)
frame2.pack()
button4 = tkinter.Button(frame2, text = "4", padx = 20, pady = 20, 
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("4"))
button4.pack(side = "left")
button5 = tkinter.Button(frame2, text = "5", padx = 20, pady = 20,  
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("5"))
button5.pack(side = "left")
button6 = tkinter.Button(frame2, text = "6", padx = 20, pady = 20,  
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("6"))
button6.pack(side = "left")
buttonminus = tkinter.Button(frame2, text = "-", padx = 20, pady = 20, 
                             fg ="Black", bg = "Grey", bd= 10, 
                             command = lambda : addNumber("-"))
buttonminus.pack(side = "left")


frame3 = tkinter.Frame(gui)
frame3.pack()
button7 = tkinter.Button(frame3, text = "7", padx = 20, pady = 20,  
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("7"))
button7.pack(side = "left")
button8 = tkinter.Button(frame3, text = "8", padx = 20, pady = 20, 
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("8"))
button8.pack(side = "left")
button9 = tkinter.Button(frame3, text = "9", padx = 20, pady = 20,  
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("9"))
button9.pack(side = "left")
buttonstar = tkinter.Button(frame3, text = "*", padx = 20, pady = 20, 
                            fg ="Black", bg = "Grey", bd= 10,
                             command = lambda : addNumber("*"))
buttonstar.pack(side = "left")

frame4 = tkinter.Frame(gui, background = "Grey")
frame4.pack()
buttondot = tkinter.Button(frame4, text = ".", padx = 20, pady = 20,  
                           fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("."))
buttondot.pack(side = "left")
button0 = tkinter.Button(frame4, text = "0", padx = 20, pady = 20,  
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = lambda : addNumber("0"))
button0.pack(side = "left")
button0 = tkinter.Button(frame4, text = "C", padx = 20, pady = 20,  
                         fg ="Black", bg = "Grey", bd= 10, 
                         command = clear)
button0.pack(side = "left")
buttondivide = tkinter.Button(frame4, text = "/", padx = 20, pady = 20, 
                              fg ="Black", bg = "Grey", bd= 10, 
                              command = lambda : addNumber("/"))
buttondivide.pack(side = "left")

frame5 = tkinter.Frame(gui, background = "Grey")
frame5.pack()
buttonequals = tkinter.Button(frame5, text = "=", padx = 80, pady = 20, 
                              fg ="Black", bg = "Grey", bd= 10, 
                              command = lambda : equal())
buttonequals.pack(side = "left")

#Creating a menu
guimenu = tkinter.Menu(gui)

guiview = tkinter.Menu(gui)
guihelp = tkinter.Menu(gui)
guiquit = tkinter.Menu(gui)

menuview = tkinter.Menu(guiview, tearoff = 0)
guiview.add_command(label = "Graphing Calculator")
guiview.add_command(label = "Scientific Calculator")

menuhelp = tkinter.Menu(guihelp, tearoff = 0)
guihelp.add_command(label = "About Calculator")

menuquit = tkinter.Menu(guiquit, tearoff = 0)

guimenu.add_cascade(label = "View", menu = guiview)
guimenu.add_cascade(label = "Help", menu = guihelp)
guimenu.add_cascade(label = "Quit", command = quit)
gui.config(menu = guimenu)

gui.mainloop();
