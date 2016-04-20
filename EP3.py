import tkinter as tk
import numpy as np

class Game:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("350x400+400+400")
        self.window.rowconfigure(0,minsize=100,weight=1)
        self.window.rowconfigure(1,minsize=100,weight=1)
        self.window.rowconfigure(2,minsize=100,weight=1)
        self.window.rowconfigure(3,minsize=50,weight=1)
        self.window.columnconfigure(0,minsize=100,weight=1)
        self.window.columnconfigure(1,minsize=100,weight=1)
        self.window.columnconfigure(2,minsize=100,weight=1)
        
        self.botão_0_0 = tk.Button(self.window)
        self.botão_0_0.grid(row=0,column=0,sticky='nsew')
        self.botão_0_0.configure(command=self.botão_0_0_clicado)
        
        self.botão_0_1 = tk.Button(self.window)
        self.botão_0_1.grid(row=0,column=1,sticky='nsew')
        self.botão_0_1.configure(command=self.botão_0_1_clicado)
        
        self.botão_0_2 = tk.Button(self.window)
        self.botão_0_2.grid(row=0,column=2,sticky='nsew')
        self.botão_0_2.configure(command=self.botão_0_2_clicado)
        
        self.botão_1_0 = tk.Button(self.window)
        self.botão_1_0.grid(row=1,column=0,sticky='nsew')
        self.botão_1_0.configure(command=self.botão_1_0_clicado)
        
        self.botão_1_1 = tk.Button(self.window)
        self.botão_1_1.grid(row=1,column=1,sticky='nsew')
        self.botão_1_1.configure(command=self.botão_1_1_clicado)
        
        self.botão_1_2 = tk.Button(self.window)
        self.botão_1_2.grid(row=1,column=2,sticky='nsew')
        self.botão_1_2.configure(command=self.botão_1_2_clicado)
        
        self.botão_2_0 = tk.Button(self.window)
        self.botão_2_0.grid(row=2,column=0,sticky='nsew')
        self.botão_2_0.configure(command=self.botão_2_0_clicado)
        
        self.botão_2_1 = tk.Button(self.window)
        self.botão_2_1.grid(row=2,column=1,sticky='nsew')
        self.botão_2_1.configure(command=self.botão_2_1_clicado)
        
        self.botão_2_2 = tk.Button(self.window)
        self.botão_2_2.grid(row=2,column=2,sticky='nsew')
        self.botão_2_2.configure(command=self.botão_2_2_clicado)
        
        self.label_status = tk.Label()
        self.label_status.configure(text="Tic Tac Toe")
        self.label_status.grid(row=3,column=0,columnspan=3)
        
        self.turn = 1
        self.n = input("Qual é o nome do primeiro jogador?")
        self.n2 = input("Qual é o nome do segundo jogador?")
        #self.jogador.configure(command=self.jogador_TTT)
                
        
    def iniciar(self):
        self.window.mainloop()
        
    #def jogador_TTT(self):
    #    if self.turn%2 != 0:
    #        self.jogador = "X"
    #    else:
    #        self.jogador = "O"
    
    def botão_0_0_clicado(self):
        #self.botão_clicado(0,0)
        if self.turn%2 != 0:
            self.botão_0_0.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_0_0.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_0_0.configure(state="disabled")
        
    def botão_0_1_clicado(self):
        #self.botão_clicado(0,1)
        if self.turn%2 != 0:
            self.botão_0_1.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_0_1.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_0_1.configure(state="disabled")
        
    def botão_0_2_clicado(self):
        #self.botão_clicado(0,2)
        if self.turn%2 != 0:
            self.botão_0_2.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_0_2.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_0_2.configure(state="disabled")
        
    def botão_1_0_clicado(self):
        #self.botão_clicado(0,0)
        if self.turn%2 != 0:
            self.botão_1_0.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_1_0.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_1_0.configure(state="disabled")
        
    def botão_1_1_clicado(self):
        #self.botão_clicado(1,1)
        if self.turn%2 != 0:
            self.botão_1_1.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_1_1.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_1_1.configure(state="disabled")
        
    def botão_1_2_clicado(self):
        #self.botão_clicado(1,2)
        if self.turn%2 != 0:
            self.botão_1_2.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_1_2.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_1_2.configure(state="disabled")
        
    def botão_2_0_clicado(self):
        #self.botão_clicado(2,0)
        if self.turn%2 != 0:
            self.botão_2_0.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_2_0.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_2_0.configure(state="disabled")
        
    def botão_2_1_clicado(self):
        #self.botão_clicado(2,1)
        if self.turn%2 != 0:
            self.botão_2_1.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_2_1.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_2_1.configure(state="disabled")
        
    def botão_2_2_clicado(self):
        #self.botão_clicado(2,2)
        if self.turn%2 != 0:
            self.botão_2_2.configure(text="{0}".format(self.n[0]))
        else:
            self.botão_2_2.configure(text="{0}".format(self.n2[0]))
        self.turn+=1
        self.botão_2_2.configure(state="disabled")
        
    #def texto(self):
    #    if self.turn%2 != 0:
    #        return ("Vez do X")
    #    elif self.turn%2 == 0:
    #        return ("Vez do O")
    #    elif self.turn == -1:
    #        return ("O jogador {0} ganhou!".format(self.jogador))
    #    elif self.turn == -2:
    #        return ("Deu velha!")
        
        
jogo = Game()
jogo.iniciar()