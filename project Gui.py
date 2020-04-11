from tkinter import *
from tkinter.ttk import *
window=tkinter.Tk()
Label(window, text = 'GeeksforGeeks', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
window.title("Text recognition system")
top_frame=tkinter.Frame(window).pack()
tkinter.Label(window, text="Text recognition system", fg="white",bg="black" ,font=30).pack(fill="x")
def build_upfun():
    window=tkinter.Tk()
    window.title("The end Result")
    tkinter.Label(window, text="The Executed Result is", fg="black",bg="white" ,font=30).pack(fill="x")
    
        
  
    
tkinter.Button(top_frame, text='Build_up',font=14,command=build_upfun).pack()

window.mainloop()
