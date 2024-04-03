from tkinter import *
import pygame
from PIL import Image, ImageTk, ImageFilter
import random

pygame.mixer.init()
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x500+450+150")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        Menu_image = Image.open("images/game.jpg")
        Menu_image = Menu_image.resize((500, 400))
        self.Menu = ImageTk.PhotoImage(Menu_image)
        Label(self.root, image=self.Menu).place(x=0, y=60, width=500, height=380)

        top_label = Label(self.root, text="TIC TAC TOE", font=("Arial", 30, "bold"), bg="white", fg="black", width=22)
        top_label.place(x=0, y=20)

        self.frame = Frame(self.root, bg="dark slate gray", height=120, width=500)
        self.frame.place(x=0, y=380)

        self.Button1 = Button(self.frame, text="2 Player", font=("Arial", 15, "bold"), bd=2, relief=RIDGE, bg="white", width=15, cursor="hand2", command=self.btn1_command)
        self.Button1.place(x=160, y=13)

        self.Button2 = Button(self.frame, text="Computer", font=("Arial", 15, "bold"), bd=2, relief=RIDGE, bg="white", width=15, cursor="hand2",command=self.btn2_command)
        self.Button2.place(x=160, y=63)

    def btn1_command(self):
        self.root.destroy() 
        player_window = Tk()
        obj2 = GameBoard(player_window)
        player_window.mainloop()

    
    # def btn2_command(self):
    #     self.root.destroy() 
    #     computer_window = Tk()
    #     obj3 = GameBoard2(computer_window)
    #     computer_window.mainloop()

    def btn2_command(self):
        self.root.destroy() 
        computer_window = Tk()
        obj3 = GameBoard2(computer_window) 
        computer_window.mainloop()



class GameBoard:
    def __init__(self, player_window):
        self.player_window = player_window
        self.player_window.title("Enjoy with your friends")
        self.player_window.geometry("463x500+450+150")
        self.player_window.resizable(False,False)
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.name_frame=Frame(self.player_window,bg="dark slate gray",height=120,width=463)
        self.name_frame.place(x=0,y=380)

        replay_btn=Button(self.name_frame,text="Replay",font=("Arial",15,"bold"),bd=2,relief=RIDGE,width=10,fg="black",bg="lightcyan2",cursor="hand2",command=self.clear_board)
        replay_btn.place(x=165,y=70)

        exit_btn=Button(self.name_frame,text="Exit",font=("Arial",15,"bold"),bg="lightcyan2",fg="black",bd=2,relief=RIDGE,width=10,command=self.Exit,cursor="hand2")
        exit_btn.place(x=310,y=70)

        menu_btn=Button(self.name_frame,text="Menu",font=("Arial",15,"bold"),bg="lightcyan2",fg="black",bd=2,relief=RIDGE,width=10,command=self.show_menu,cursor="hand2")
        menu_btn.place(x=20,y=70)

        self.result_label = Label(self.name_frame, text="", font=("Arial", 25, "bold"), bg="dark slate gray", fg="white")
        self.result_label.place(x=125, y=13)

        self.win_sound = pygame.mixer.Sound("audio/win_sound.wav")
        self.click_sound = pygame.mixer.Sound("audio/click_sound.mp3")
        self.draw_sound=pygame.mixer.Sound("audio/draw_sound.mp3")

        for row in range(3):
            for col in range(3):
                button = Button(self.player_window, text="", font=("Arial", 30, "bold"), bg="lightcyan2",width=6, height=2,command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def handle_click(self, row, col):
        if self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.current_player = "X" if self.current_player == "O" else "O"
            self.result()
            self.click_sound.play()

    def result(self):
        result=""
        if (self.buttons[0][0]["text"]==self.buttons[0][1]["text"]==self.buttons[0][2]["text"]=="X") or \
           (self.buttons[1][0]["text"]==self.buttons[1][1]["text"]==self.buttons[1][2]["text"]=="X") or \
           (self.buttons[2][0]["text"]==self.buttons[2][1]["text"]==self.buttons[2][2]["text"]=="X") or \
           (self.buttons[0][0]["text"]==self.buttons[1][0]["text"]==self.buttons[2][0]["text"]=="X") or \
           (self.buttons[0][1]["text"]==self.buttons[1][1]["text"]==self.buttons[2][1]["text"]=="X") or \
           (self.buttons[0][2]["text"]==self.buttons[1][2]["text"]==self.buttons[2][2]["text"]=="X") or \
           (self.buttons[0][0]["text"]==self.buttons[1][1]["text"]==self.buttons[2][2]["text"]=="X") or \
           (self.buttons[0][2]["text"]==self.buttons[1][1]["text"]==self.buttons[2][0]["text"]=="X"):
            result="Player 1 Wins"
            self.win_sound.play()
            self.player_window.after(2000,self.clear_board)
    
        elif(self.buttons[0][0]["text"]==self.buttons[0][1]["text"]==self.buttons[0][2]["text"]=="O") or \
            (self.buttons[1][0]["text"]==self.buttons[1][1]["text"]==self.buttons[1][2]["text"]=="O") or \
            (self.buttons[2][0]["text"]==self.buttons[2][1]["text"]==self.buttons[2][2]["text"]=="O") or \
            (self.buttons[0][0]["text"]==self.buttons[1][0]["text"]==self.buttons[2][0]["text"]=="O") or \
            (self.buttons[0][1]["text"]==self.buttons[1][1]["text"]==self.buttons[2][1]["text"]=="O") or \
            (self.buttons[0][2]["text"]==self.buttons[1][2]["text"]==self.buttons[2][2]["text"]=="O") or \
            (self.buttons[0][0]["text"]==self.buttons[1][1]["text"]==self.buttons[2][2]["text"]=="O") or \
            (self.buttons[0][2]["text"]==self.buttons[1][1]["text"]==self.buttons[2][0]["text"]=="O"):
             result="Player 2 Wins"
             self.win_sound.play()
             self.player_window.after(2000,self.clear_board)
          
        else:
            is_draw = True
            for row in self.buttons:
                for button in row:
                    if button["text"] == "":
                        is_draw = False
                        break

            if is_draw:
                 result = "It is a Draw"
                 self.draw_sound.play()
        self.result_label.config(text=result)
    
    def show_menu(self):
        self.player_window.destroy()
        root=Tk()
        obj5 = Game(root)
        root.mainloop()

    def clear_board(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
                self.result_label.config(text="")

    def Exit(self):
       exit()
  
class GameBoard2():
    def __init__(self, computer_window):
        self.computer_window = computer_window
        self.computer_window.title("Enjoy with computer")
        self.computer_window.geometry("463x500+450+150")
        self.computer_window.resizable(False,False)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.name_frame=Frame(self.computer_window,bg="dark slate gray",height=120,width=463)
        self.name_frame.place(x=0,y=380)

        replay_btn=Button(self.name_frame,text="Replay",font=("Arial",15,"bold"),bd=2,relief=RIDGE,width=10,fg="black",bg="lightcyan2",cursor="hand2",command=self.clear_board)
        replay_btn.place(x=165,y=70)

        exit_btn=Button(self.name_frame,text="Exit",font=("Arial",15,"bold"),bg="lightcyan2",fg="black",bd=2,relief=RIDGE,width=10,command=self.Exit,cursor="hand2")
        exit_btn.place(x=310,y=70)

        menu_btn=Button(self.name_frame,text="Menu",font=("Arial",15,"bold"),bg="lightcyan2",fg="black",bd=2,relief=RIDGE,width=10,command=self.show_menu,cursor="hand2")
        menu_btn.place(x=20,y=70)

        self.result_label = Label(self.name_frame, text="", font=("Arial", 25, "bold"), bg="dark slate gray", fg="white")
        self.result_label.place(x=125, y=13)

        self.win_sound = pygame.mixer.Sound("audio/win_sound.wav")
        self.click_sound = pygame.mixer.Sound("audio/click_sound.mp3")
        self.draw_sound=pygame.mixer.Sound("audio/draw_sound.mp3")
        self.choices=['X','O']
        self.computer_choice = random.choice(self.choices)


        for row in range(3):
            for col in range(3):
                button = Button(self.computer_window, text="", font=("Arial", 30, "bold"), bg="lightcyan2",width=6, height=2,command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def show_menu(self):
        self.computer_window.destroy()
        root=Tk()
        obj5 = Game(root)
        root.mainloop()
    

    def clear_board(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
                self.result_label.config(text="")

    def Exit(self):
       exit()


    def switch_player(self):
        global current_player
        self.current_player = "O" if self.current_player == "X" else "X"

    def computer_move(self):
        available_moves = []

        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text'] == "":
                    available_moves.append((row, col))

        if available_moves:
            row, col = random.choice(available_moves)
            self.buttons[row][col]['text'] = "O"
            self.switch_player()
            self.result()
            self.click_sound.play()
        

    def handle_click(self, row, col):
        if self.buttons[row][col]["text"] == "" and self.current_player == "X":
            self.buttons[row][col]["text"] = self.current_player
            self.current_player = "O"
            self.result()
            self.click_sound.play()
            # self.computer_move()
            if self.current_player == "O":
                self.computer_window.after(2000, self.computer_move)
            

    def result(self):
        result=""
        if (self.buttons[0][0]["text"]==self.buttons[0][1]["text"]==self.buttons[0][2]["text"]=="X") or \
           (self.buttons[1][0]["text"]==self.buttons[1][1]["text"]==self.buttons[1][2]["text"]=="X") or \
           (self.buttons[2][0]["text"]==self.buttons[2][1]["text"]==self.buttons[2][2]["text"]=="X") or \
           (self.buttons[0][0]["text"]==self.buttons[1][0]["text"]==self.buttons[2][0]["text"]=="X") or \
           (self.buttons[0][1]["text"]==self.buttons[1][1]["text"]==self.buttons[2][1]["text"]=="X") or \
           (self.buttons[0][2]["text"]==self.buttons[1][2]["text"]==self.buttons[2][2]["text"]=="X") or \
           (self.buttons[0][0]["text"]==self.buttons[1][1]["text"]==self.buttons[2][2]["text"]=="X") or \
           (self.buttons[0][2]["text"]==self.buttons[1][1]["text"]==self.buttons[2][0]["text"]=="X"):
            result="Player  Wins"
            self.win_sound.play()
            self.computer_window.after(1500,self.clear_board)
    
        elif(self.buttons[0][0]["text"]==self.buttons[0][1]["text"]==self.buttons[0][2]["text"]=="O") or \
            (self.buttons[1][0]["text"]==self.buttons[1][1]["text"]==self.buttons[1][2]["text"]=="O") or \
            (self.buttons[2][0]["text"]==self.buttons[2][1]["text"]==self.buttons[2][2]["text"]=="O") or \
            (self.buttons[0][0]["text"]==self.buttons[1][0]["text"]==self.buttons[2][0]["text"]=="O") or \
            (self.buttons[0][1]["text"]==self.buttons[1][1]["text"]==self.buttons[2][1]["text"]=="O") or \
            (self.buttons[0][2]["text"]==self.buttons[1][2]["text"]==self.buttons[2][2]["text"]=="O") or \
            (self.buttons[0][0]["text"]==self.buttons[1][1]["text"]==self.buttons[2][2]["text"]=="O") or \
            (self.buttons[0][2]["text"]==self.buttons[1][1]["text"]==self.buttons[2][0]["text"]=="O"):
             result="Computer Wins"
             self.win_sound.play()
             self.computer_window.after(1500,self.clear_board)
          
        else:
            is_draw = True
            for row in self.buttons:
                for button in row:
                    if button["text"] == "":
                        is_draw = False
                        break

            if is_draw:
                 result = "It is a Draw"
                 self.draw_sound.play()
        self.result_label.config(text=result)
    



root = Tk()
obj = Game(root)
root.mainloop()
