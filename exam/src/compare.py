# -*- coding: utf-8 -*-

# python2 vs python3
from sys import version_info
from tkinter import CENTER
if version_info.major == 2: #python2
		import Tkinter as tkinter
elif version_info.major == 3: #python3
		import tkinter as tkinter
        

def operating(num1, num2):
            if num1>num2:
             res = num1, ">", num2
            elif num1<num2:
             res = num1, "<", num2
            else:
             res = num1, "=", num2
            return res






def clicked():
           num1=txt.get()
           num2=txt2.get()
           
           
           result = operating(num1, num2)
           tkinter.Label(window, text=result).grid(row=3)





def main():
    # create a main window
    global window
    window  = tkinter.Tk() # window is the name of the main window object
    window.title("Assesment test")
    window.geometry('350x200')
    
  
    
    tkinter.Label(window, text='first number:').grid(row=0) 
    tkinter.Label(window, text='second number:').grid(row=1) 
    
    global txt, txt2
    
    # Add textbox
    txt = tkinter.Entry(window,width=15)
    txt.grid(column=1, row=0)
    txt.focus() # Set focus to entry widget
    
    # Add another textbox
    txt2 = tkinter.Entry(window,width=15)
    txt2.grid(column=1, row=1)
    
    
    
    
           
            
    
    # add a button in the application
    btn = tkinter.Button(window, text="Compare Numbers", command=clicked) 
    btn.grid(column=0, row=2)
    




    window.mainloop()   # infinite loop used to run the application, wait for an 
                        # event to occur and process the event till the window is
                        # not closed
                            
if __name__ == '__main__':
    main()                       