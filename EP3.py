import tkinter as tk

class Tic_Tac_Toe:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("350x400+400+400")
        
        for i in range(4):
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
                self.b.configure(command=lambda x = z+j: self.botao_clicado(x))
                self.b.grid(row=i, column=j, sticky="nsew")
                self.buttons.append(self.b)
                
        self.label_status = tk.Label()
        self.label_status.configure(text="Tic Tac Toe")
        self.label_status.grid(row=3,column=0,columnspan=3)
            
        self.turn = 1
        self.lista =  [0,0,0,0,0,0,0,0,0]       
        
    def start(self):
        self.window.mainloop()
        
    def botao_clicado(self,x):
        if self.turn % 2 != 0:
            self.buttons[x].configure(text="X")
            self.lista[x] = 1
        else:
            self.buttons[x].configure(text="O")
            self.lista[x] = 2
        self.turn += 1
        self.buttons[x].configure(state="disabled")
    
jogo = Tic_Tac_Toe()
jogo.start()