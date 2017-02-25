from Tkinter import *
import Tkinter
import tkMessageBox
import tkSimpleDialog
from scoreboard import scoreboard

root = Tkinter.Tk()
root.title("Tic Tac Toe")

global p1,p2

bclick = True
	
def tictactoe(buttons):
    global bclick,p1,p2
    
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True

    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
        tkMessageBox.showinfo("Tic Tac Toe","Hooray! "+p1+" Wins the Game")
        scoreboard(p1,10)

    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
        tkMessageBox.showinfo("Tic Tac Toe","Hooray! "+p2+" wins!")
        scoreboard(p2,10)




main_frame=Tkinter.Frame(root)
main_frame.pack()


p1=tkSimpleDialog.askstring("Enter Player1","Player1 Enter your Name")
p2=tkSimpleDialog.askstring("Enter Player2", "Player2 Enter your Name")


button1 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button1))
button1.grid(row=1, column=0,sticky = S+N+E+W)

button2 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button2))
button2.grid(row=1, column=1, sticky = S+N+E+W)

button3 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button3))
button3.grid(row=1, column=2, sticky = S+N+E+W)

button4 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button4))
button4.grid(row=2, column=0, sticky = S+N+E+W)

button5 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button5))
button5.grid(row=2, column=1, sticky = S+N+E+W)

button6 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button6))
button6.grid(row=2, column=2, sticky = S+N+E+W)

button7 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button7))
button7.grid(row=3, column=0, sticky = S+N+E+W)

button8 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button8))
button8.grid(row=3, column=1, sticky = S+N+E+W)

button9 = Button(main_frame,text=" ",font='Arial 30 bold', height=3,width=5,command=lambda:tictactoe(button9))
button9.grid(row=3, column=2, sticky = S+N+E+W)

root.mainloop()
