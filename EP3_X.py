import tkinter as tk
import numpy as np

class Game:
    
    def __init__(self):
        self.matriz = np.zeros(shape = [3,3])
        self.turn = 1
        self.player = ""
        
        
    def recieves_play(self):
        if self.turn % 2 != 0:
            self.turn+=1
            self.player="X"
            return "X"
        else:
            self.turn+=1
            self.player="O"
            return "O"
        
    def verify_winner(self):
        soma=soma2=soma3=soma4=soma5=soma6=soma7=soma8=soma9=0
        for h in range(3):
            soma+=self.matriz[0][h]
            soma2+=self.matriz[1][h]
            soma3+=self.matriz[2][h]
            soma4+=self.matriz[h][0]
            soma5+=self.matriz[h][1]
            soma6+=self.matriz[h][2]
            soma7+=self.matriz[h][h]
            soma8+=self.matriz[h][2-h]
        for s in range(3):
            for a in range(3):
                soma9+=self.matriz[s][a]
        if soma==3 or soma2==3 or soma3==3 or soma4==3 or soma5==3 or soma6==3 or soma7==3 or soma8==3:
            return 1
        elif soma==12 or soma2==12 or soma3==12 or soma4==12 or soma5==12 or soma6==12 or soma7==12 or soma8==12:
            return 2
        elif soma9==21:
            return 0
        else:
            return -1
    
    def clean_game(self):
        if self.verify_winner()==1 or self.verify_winner()==2 or self.verify_winner()==0:
            return False
        return True
        
    

class Tabuleiro:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x500+500+500")
        
        self.nome1 = tk.StringVar()
        self.nome2 = tk.StringVar()
        self.n1 = ""
        self.n2 = ""
        
        self.label_nome1 = tk.Label(self.window,text="Primeiro Jogador:")
        self.label_nome1.grid(padx=140, pady=50)
        self.text1 = tk.Entry(self.window)
        self.text1.configure(textvariable=self.nome1)
        self.text1.grid(padx=140)
        self.label_nome2 = tk.Label(self.window,text="Segundo Jogador:")
        self.label_nome2.grid(padx=140, pady=50)
        self.text2 = tk.Entry(self.window)
        self.text2.configure(textvariable=self.nome2)
        self.text2.grid(padx=140)
        
        self.botao_nomes = tk.Button(self.window,width=10,height=4,text="JOGAR")
        self.botao_nomes.configure(command=self.nomes)
        self.botao_nomes.grid(padx=140, pady=50)
                
    def tabuleiro(self):
        self.game = Game()
                
        for i in range(6):
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
        self.label_status.configure(text="Tic Tac Toe", font="BodoniMTBlack 22 bold",bg="yellow")
        self.label_status.grid(row=3,column=0,columnspan=3)
        
        self.label_player = tk.Label()
        self.label_player.configure(text="Vez de {0}".format(self.n1), font="BrandleyHandITC 18")
        self.label_player.grid(row=4,column=0,columnspan=3)
        
        self.botao_revanche = tk.Button()
        self.botao_revanche.configure(text="Rematch",height=2,width=10,state="disabled")
        self.botao_revanche.configure(command=self.rematch_tabuleiro)
        self.botao_revanche.grid(row=5,column=1)
        
        self.placar_X = tk.Label()
        self.placar_X.configure(text="{0}".format(self.n1),font="Arial 16 bold")
        self.placar_X.grid(row=3,column=0)
        
        self.placar_O = tk.Label()
        self.placar_O.configure(text="{0}".format(self.n2),font="Arial 16 bold")
        self.placar_O.grid(row=3,column=2)
        
        self.ponto_X = tk.Label()
        self.ponto_X.configure(text="0")
        self.ponto_X.grid(row=4,column=0)
        
        self.ponto_O = tk.Label()
        self.ponto_O.configure(text="0")
        self.ponto_O.grid(row=4,column=2)
        
        self.X=0
        self.O=0
            
    def nomes(self):
        self.n1 = self.nome1.get()
        self.n2 = self.nome2.get()
        self.label_nome1.grid_forget()
        self.text1.grid_forget()
        self.label_nome2.grid_forget()
        self.text2.grid_forget()
        self.botao_nomes.grid_forget()
        self.tabuleiro()
        
    def start(self):
        self.window.mainloop()
        
    def botao_clicado(self,x,y,z):
        self.buttons[x].configure(text="{0}".format(self.game.recieves_play()), font = "Forte 25 bold")
        if self.game.player=="X":
            self.game.matriz[y][z] = 1
            self.label_player.configure(text="Vez de {0}".format(self.n2), font="BrandleyHandITC 18")
        else:
            self.game.matriz[y][z] = 4
            self.label_player.configure(text="Vez de {0}".format(self.n1), font="BrandleyHandITC 18")
        self.buttons[x].configure(state="disabled")
        self.end_match()
    
    def end_match(self):
        if self.game.verify_winner()==1:
            self.label_player.configure(text="{0} ganhou!".format(self.n1), font="BrandleyHandITC 18")
            self.X+=1
            self.botao_revanche.configure(state="active")
            for r in range(9):
                self.buttons[r].configure(state="disabled")
        elif self.game.verify_winner()==2:
            self.label_player.configure(text="{0} ganhou!".format(self.n2), font="BrandleyHandITC 18")
            self.O+=1
            self.botao_revanche.configure(state="active")
            for r in range(9):
                self.buttons[r].configure(state="disabled")
        elif self.game.verify_winner()==0:
            self.label_player.configure(text="Deu Velha!", font="BrandleyHandITC 18")
            self.botao_revanche.configure(state="active")
        self.pontuacao()
        
    def pontuacao(self):
        self.ponto_X.configure(text="{0}".format(self.X))
        self.ponto_O.configure(text="{0}".format(self.O))
    
    def rematch_tabuleiro(self):
        if self.game.clean_game()==False:
            for r in range(9):
                self.buttons[r].configure(text="",state="active")
            self.label_player.configure(text="Vez de {0}".format(self.n1), font="BrandleyHandITC 18")
            self.game.turn=1
            self.game.matriz=np.zeros(shape=[3,3])
        
tabuleiro = Tabuleiro()
tabuleiro.start()