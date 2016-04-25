import tkinter as tk
import numpy as np

class Tic_Tac_Toe:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x400+400+400")
        self.turn= 1
        
        for i in range(5):
            if i < 3:
                self.window.rowconfigure(i,minsize=100,weight=1)
                self.window.columnconfigure(i,minsize=100,weight=1)
            else:
                self.window.rowconfigure(i,minsize=50,weight=1)
                
        self.buttons = []
        
        
        for i in range(3):
            for j in range(3):
                self.b = tk.Button(self.window)
                if i == 0:
                    z=0
                elif i == 1:
                    z=3
                elif i == 2:
                    z=6
                self.b.configure(command=lambda x = z+j, y=i, z=j: self.botao_clicado(x,y,z))
                self.b.grid(row=i, column=j, sticky="nsew")
                self.buttons.append(self.b)
                
        self.label_status = tk.Label()
        self.label_status.configure(text="Tic Tac Toe")
        self.label_status.grid(row=3,column=0,columnspan=3)
        
        self.label_player = tk.Label()
        self.label_player.configure(text="Vez de X")
        self.label_player.grid(row=4,column=0,columnspan=3)
            
        
        self.matriz = np.zeros(shape = [3,3])
        
    def start(self):
        self.window.mainloop()
        
    def botao_clicado(self,x,y,z):
        if self.turn % 2 != 0:
            self.buttons[x].configure(text="X")
            self.matriz[y][z] = 1
            self.label_player.configure(text="Vez de O")
        else:
            self.buttons[x].configure(text="O")
            self.matriz[y][z] = 4
            self.label_player.configure(text="Vez de X")
        self.buttons[x].configure(state="disabled")
        soma=soma2=soma3=soma4=soma5=soma6=soma7=soma8=soma9=0
        for h in range(3):
            soma+=self.matriz[0][h]
            soma2+=self.matriz[1][h]
            soma3+=self.matriz[2][h]
            soma4+=self.matriz[h][0]
            soma5+=self.matriz[h][1]
            soma6+=self.matriz[h][2]
            soma7+=self.matriz[h][h]
            if h == 0:
                soma8+=self.matriz[h][h-1]
            elif h == 1:
                soma8+=self.matriz[h][h]
            elif h == 2:
                soma8+=self.matriz[h][h-h]
        for s in range(3):
            for a in range(3):
                soma9+=self.matriz[s][a]
        if soma==3 or soma2==3 or soma3==3 or soma4==3 or soma5==3 or soma6==3 or soma7==3 or soma8==3:
            self.label_player.configure(text="X ganhou!")
            for r in range(9):
                self.buttons[r].configure(state="disabled")
        elif soma==12 or soma2==12 or soma3==12 or soma4==12 or soma5==12 or soma6==12 or soma7==12 or soma8==12:
            self.label_player.configure(text="O ganhou")
            for r in range(9):
                self.buttons[r].configure(state="disabled!")
        elif soma9==21:
            self.label_player.configure(text="Deu Velha!")
        self.turn += 1
        
jogo = Tic_Tac_Toe()
jogo.start()