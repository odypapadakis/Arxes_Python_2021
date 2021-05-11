# using the following video
# https://www.youtube.com/watch?v=YXPyB4XeYLA

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import os


# creating Tk window
root = tk.Tk()
root.withdraw()
root.title("Playing with tkinter")
# root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.eval('tk::PlaceWindow . center')



# setting geometry of tk window
root.geometry("800x500")
current_directory = os.getcwd()

mb.askquestion("Change directory ?", "Current directory is  " + str(current_directory) )
mb.place(relx =0.1, x =-10, y = 2, anchor = NE)








# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
mainloop()
root.mainloop()

# def call():
#     res=mb.askquestion('Exit Application', 'Do you really want to exit')
#     if res == 'yes' :
#         root.destroy()
#     else :
#         mb.showinfo('Return', 'Returning to main application')
#
# root=tk.Tk()
# canvas=tk.Canvas(root, width=400, height=200)
# canvas.pack()

# b=Button(root, text='Quit Application', command=call)
# canvas.create_window(100, 100, window=b)

# def deleteme():
#     result = tkMessageBox.askquestion("Delete", "Are You Sure?", icon='warning')
#     if result == 'yes':
#         print ("Deleted" )
#     else:
#         print ( "I'm Not Deleted Yet" )





root.mainloop()