from tkinter import *
import tkinter.messagebox

root = Tk()
root.title ("TIC TAC TOE")


bclick = True

def tictactoe(buttons):
   
        global bclick
        if buttons ["text"]== " " and bclick == True:
            buttons ["text"] = "X"
            bclick = False
        elif buttons ["text"]== " " and bclick == False:
            buttons ["text"] = "O"
            bclick = True
        elif  (button1["text"] == "X" and button2 ["text"] == "X" and button3 ["text"] == "X" or
             button1["text"] == "X" and button5 ["text"] == "X" and button9 ["text"] == "X" or
             button1["text"] == "X" and button4 ["text"] == "X" and button7 ["text"] == "X" or
             button4["text"] == "X" and button5 ["text"] == "X" and button6 ["text"] == "X" or
             button7["text"] == "X" and button8 ["text"] == "X" and button9 ["text"] == "X" or
             button3["text"] == "X" and button5 ["text"] == "X" and button7 ["text"] == "X" or
             button2["text"] == "X" and button5 ["text"] == "X" and button8 ["text"] == "X" or
             button3["text"] == "X" and button6 ["text"] == "X" and button9 ["text"] == "X" ):
             return tkinter.messagebox.showinfo("WINNER X","PLAYER X WON THE GAME")
        
                
    
        elif  (button1["text"] == "O" and button2 ["text"] == "O" and button3 ["text"] == "O" or
             button1["text"] == "O" and button5 ["text"] == "O" and button9 ["text"] == "O" or
             button1["text"] == "O" and button4 ["text"] == "O" and button7 ["text"] == "O" or
             button4["text"] == "O" and button5 ["text"] == "O" and button6 ["text"] == "O" or
             button7["text"] == "O" and button8 ["text"] == "O" and button9 ["text"] == "O" or
             button3["text"] == "O" and button5 ["text"] == "O" and button7 ["text"] == "O" or
             button2["text"] == "O" and button5 ["text"] == "O" and button8 ["text"] == "O" or
             button3["text"] == "O" and button6 ["text"] == "O" and button9 ["text"] == "O" ):
             return tkinter.messagebox.showinfo("WINNER O","PLAYER O WON THE GAME")
        else:
             return tkinter.messagebox.showinfo("DRAW","PLAYER DRAW")

    
def game():
    button1=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button1))
    button1.grid(row=1,column=0,sticky=S+N+E+W)

    button2=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button2))
    button2.grid(row=1,column=1,sticky=S+N+E+W)

    button3=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button3))
    button3.grid(row=1,column=2,sticky=S+N+E+W)

    button4=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button4))
    button4.grid(row=2,column=0,sticky=S+N+E+W)

    button5=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button5))
    button5.grid(row=2,column=1,sticky=S+N+E+W)

    button6=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button6))
    button6.grid(row=2,column=2,sticky=S+N+E+W)
    button7=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button7))
    button7.grid(row=3,column=0,sticky=S+N+E+W)
     
    button8=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button8))
    button8.grid(row=3,column=1,sticky=S+N+E+W)

    button9=Button(root, text= " ",font=('Arial 30 bold'),height=4,width=8,command=lambda:tictactoe(button9))
    button9.grid(row=3,column=2,sticky=S+N+E+W)



class AppGame(Tk):
    def __init__(self,root):
        self.root = root
        self.f_menu = Frame(self.root)
        self.f_menu.pack()
        self.menu_canvas = Canvas(self.f_menu,width = 500,height = 500,bg = "LightCyan")
        self.menu_canvas.pack()
        self.logo = self.menu_canvas.create_text(250,200,text = "TIC TAC TOE!",font = ("fixedsys",120))
        self.bt_Goto = Button(self.menu_canvas,text = "> Play <",font = ("fixedsys",30),command = self.run)
        self.bt_Goto.place(x = 130 ,y = 300)
	
    def run(self):
        self.f_menu.destroy()
        game()


AppGame(root)

root.mainloop()

