import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")
        
        self.label = tk.Label(self.root, text= "Hello DIP01",font=('Arial',18))
        self.label.pack()

        self.button = tk.Button(self.root, text="0",height=2,width=8,font=('Arial',9))
        self.button.place(x=20, y=30)

        self.button = tk.Button(self.root, text="1",height=2,width=8,font=('Arial',9))
        self.button.place(x=90, y=30)

        self.button = tk.Button(self.root, text="2",height=2,width=8,font=('Arial',9))
        self.button.place(x=160, y=30)

        self.button = tk.Button(self.root, text="3",height=2,width=8,font=('Arial',9))
        self.button.place(x=70, y=80)

        self.button = tk.Button(self.root, text="4",height=2,width=8,font=('Arial',9))
        self.button.place(x=130, y=80)


        self.root.mainloop()

MyCalculator()