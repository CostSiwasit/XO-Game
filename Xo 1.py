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
             button2["text"] == "X" and button3 ["text"] == "X." and button4 ["text"] == "X" or
             button3["text"] == "X" and button4 ["text"] == "X" and button5 ["text"] == "X" or
             button6["text"] == "X" and button7 ["text"] == "X" and button8 ["text"] == "X" or
             button7["text"] == "X" and button8 ["text"] == "X" and button9 ["text"] == "X" or
             button8["text"] == "X" and button9 ["text"] == "X" and button10 ["text"] == "X" or
             button11["text"] == "X" and button12 ["text"] == "X" and button13 ["text"] == "X" or
             button12["text"] == "X" and button13 ["text"] == "X" and button14 ["text"] == "X" or
             button13["text"] == "X" and button14 ["text"] == "X" and button15 ["text"] == "X" or
             button16["text"] == "X" and button17 ["text"] == "X" and button18 ["text"] == "X" or
             button17["text"] == "X" and button18 ["text"] == "X" and button19 ["text"] == "X" or
             button18["text"] == "X" and button19 ["text"] == "X" and button20 ["text"] == "X" or
             button21["text"] == "X" and button22 ["text"] == "X" and button23 ["text"] == "X" or
             button22["text"] == "X" and button23 ["text"] == "X" and button24 ["text"] == "X" or
             button23["text"] == "X" and button24 ["text"] == "X" and button25 ["text"] == "X" or
             button1["text"] == "X" and button6 ["text"] == "X" and button11 ["text"] == "X" or
             button6["text"] == "X" and button11 ["text"] == "X" and button16 ["text"] == "X" or
             button11["text"] == "X" and button16 ["text"] == "X" and button21 ["text"] == "X" or
             button2["text"] == "X" and button7 ["text"] == "X" and button12 ["text"] == "X" or
             button7["text"] == "X" and button12 ["text"] == "X" and button17 ["text"] == "X" or
             button12["text"] == "X" and button17 ["text"] == "X" and button22 ["text"] == "X" or
             button3["text"] == "X" and button8 ["text"] == "X" and button13 ["text"] == "X" or
             button8["text"] == "X" and button13 ["text"] == "X" and button18 ["text"] == "X" or
             button13["text"] == "X" and button18 ["text"] == "X" and button23 ["text"] == "X" or
             button4["text"] == "X" and button9 ["text"] == "X" and button14 ["text"] == "X" or
             button9["text"] == "X" and button14 ["text"] == "X" and button19 ["text"] == "X" or
             button14["text"] == "X" and button19 ["text"] == "X" and button24 ["text"] == "X" or
             button5["text"] == "X" and button10 ["text"] == "X" and button15 ["text"] == "X" or
             button10["text"] == "X" and button15 ["text"] == "X" and button20 ["text"] == "X" or
             button15["text"] == "X" and button20 ["text"] == "X" and button25 ["text"] == "X" or
             button1["text"] == "X" and button7 ["text"] == "X" and button13 ["text"] == "X" or
             button7["text"] == "X" and button13 ["text"] == "X" and button19 ["text"] == "X" or
             button13["text"] == "X" and button19 ["text"] == "X" and button25 ["text"] == "X" or
             button5["text"] == "X" and button9 ["text"] == "X" and button13 ["text"] == "X" or
             button9["text"] == "X" and button13 ["text"] == "X" and button17 ["text"] == "X" or
             button13["text"] == "X" and button17 ["text"] == "X" and button21 ["text"] == "X" ):
             return tkinter.messagebox.showinfo("WINNER X","PLAYER X WON THE GAME")        
                
    
    elif  (button1["text"] == "O" and button2 ["text"] == "O" and button3 ["text"] == "O" or
             button2["text"] == "O" and button3 ["text"] == "O" and button4 ["text"] == "O" or
             button3["text"] == "O" and button4 ["text"] == "O" and button5 ["text"] == "O" or
             button6["text"] == "O" and button7 ["text"] == "O" and button8 ["text"] == "O" or
             button7["text"] == "O" and button8 ["text"] == "O" and button9 ["text"] == "O" or
             button8["text"] == "O" and button9 ["text"] == "O" and button10 ["text"] == "O" or
             button11["text"] == "O" and button12 ["text"] == "O" and button13 ["text"] == "O" or
             button12["text"] == "O" and button13 ["text"] == "O" and button14 ["text"] == "O" or
             button13["text"] == "O" and button14 ["text"] == "O" and button15 ["text"] == "O" or
             button16["text"] == "O" and button17 ["text"] == "O" and button18 ["text"] == "O" or
             button17["text"] == "O" and button18 ["text"] == "O" and button19 ["text"] == "O" or
             button18["text"] == "O" and button19 ["text"] == "O" and button20 ["text"] == "O" or
             button21["text"] == "O" and button22 ["text"] == "O" and button23 ["text"] == "O" or
             button22["text"] == "O" and button23 ["text"] == "O" and button24 ["text"] == "O" or
             button23["text"] == "O" and button24 ["text"] == "O" and button25 ["text"] == "O" or
             button1["text"] == "O" and button6 ["text"] == "O" and button11 ["text"] == "O" or
             button6["text"] == "O" and button11 ["text"] == "O" and button16 ["text"] == "O" or
             button11["text"] == "O" and button16 ["text"] == "O" and button21 ["text"] == "O" or
             button2["text"] == "O" and button7 ["text"] == "O" and button12 ["text"] == "O" or
             button7["text"] == "O" and button12 ["text"] == "O" and button17 ["text"] == "O" or
             button12["text"] == "O" and button17 ["text"] == "O" and button22 ["text"] == "O" or
             button3["text"] == "O" and button8 ["text"] == "O" and button13 ["text"] == "O" or
             button8["text"] == "O" and button13 ["text"] == "O" and button18 ["text"] == "O" or
             button13["text"] == "O" and button18 ["text"] == "O" and button23 ["text"] == "O" or
             button4["text"] == "O" and button9 ["text"] == "O" and button14 ["text"] == "O" or
             button9["text"] == "O" and button14 ["text"] == "O" and button19 ["text"] == "O" or
             button14["text"] == "O" and button19 ["text"] == "O" and button24 ["text"] == "O" or
             button5["text"] == "O" and button10 ["text"] == "O" and button15 ["text"] == "O" or
             button10["text"] == "O" and button15 ["text"] == "O" and button20 ["text"] == "O" or
             button15["text"] == "O" and button20 ["text"] == "O" and button25 ["text"] == "O" or
             button1["text"] == "O" and button7 ["text"] == "O" and button13 ["text"] == "O" or
             button7["text"] == "O" and button13 ["text"] == "O" and button19 ["text"] == "O" or
             button13["text"] == "O" and button19 ["text"] == "O" and button25 ["text"] == "O" or
             button5["text"] == "O" and button9 ["text"] == "O" and button13 ["text"] == "O" or
             button9["text"] == "O" and button13 ["text"] == "O" and button17 ["text"] == "O" or
             button13["text"] == "O" and button17 ["text"] == "O" and button21 ["text"] == "O" ):
             return tkinter.messagebox.showinfo("WINNER O","PLAYER O WON THE GAME")
    else:
             return tkinter.messagebox.showinfo("DRAW","PLAYER DRAW")


button1=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button4))
button4.grid(row=1,column=3,sticky=S+N+E+W)

button5=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button5))
button5.grid(row=1,column=4,sticky=S+N+E+W)

button6=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button6))
button6.grid(row=2,column=0,sticky=S+N+E+W)

button7=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button7))
button7.grid(row=2,column=1,sticky=S+N+E+W)

button8=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button8))
button8.grid(row=2,column=2,sticky=S+N+E+W)

button9=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button9))
button9.grid(row=2,column=3,sticky=S+N+E+W)

button10=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button10))
button10.grid(row=2,column=4,sticky=S+N+E+W)

button11=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button11))
button11.grid(row=3,column=0,sticky=S+N+E+W)
 
button12=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button12))
button12.grid(row=3,column=1,sticky=S+N+E+W)

button13=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button13))
button13.grid(row=3,column=2,sticky=S+N+E+W)

button14=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button14))
button14.grid(row=3,column=3,sticky=S+N+E+W)
button15=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button15))
button15.grid(row=3,column=4,sticky=S+N+E+W)

button16=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button16))
button16.grid(row=4,column=0,sticky=S+N+E+W)
 
button17=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button17))
button17.grid(row=4,column=1,sticky=S+N+E+W)

button18=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button18))
button18.grid(row=4,column=2,sticky=S+N+E+W)

button19=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button19))
button19.grid(row=4,column=3,sticky=S+N+E+W)

button20=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button20))
button20.grid(row=4,column=4,sticky=S+N+E+W)

button21=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button21))
button21.grid(row=5,column=0,sticky=S+N+E+W)
 
button22=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button22))
button22.grid(row=5,column=1,sticky=S+N+E+W)

button23=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button23))
button23.grid(row=5,column=2,sticky=S+N+E+W)

button24=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button24))
button24.grid(row=5,column=3,sticky=S+N+E+W)

button25=Button(root, text= " ",font=('Arial 30 bold'),height=2,width=5,command=lambda:tictactoe(button25))
button25.grid(row=5,column=4,sticky=S+N+E+W)




root.mainloop()

