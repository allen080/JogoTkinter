from tkinter import *
import random
cores = ['lime green','orange','gray','snow2','yellow','light blue']
larg = 500
al = 500
canvas_larg = 400
canvas_al = 400

class Jogo(object):
    def __init__(self):
        #interface padrao:
        self.root = Tk()
        self.root.geometry('%dx%d'%(larg,al))
        self.root.resizable('False','False')
        self.root.title('jogo top')

        #frame dos retangulos que serao destruidos
        self.frame = Frame(bg='black')
        self.frame.pack()

        #cria o canvas do programa
        self.canvas = Canvas(self.frame,bg='black',width=canvas_larg,height=canvas_al)
        self.canvas.pack()

        #botao start:
        self.start = Button(self.root,text='START',width=11,font=('Verdana','10'),command=self.começa)
        self.start.focus_force()
        #self.start.bind('<Motion>',self.começa)
        self.start.pack()
        
        self.Novojogo()
        
        self.root.mainloop()
        
    def Novojogo(self):
        '''
        cria os elementos de um novo jogo 
        '''
        #cria o retangulo principal do player:
        self.player = self.canvas.create_rectangle((canvas_larg//2,350),(canvas_larg//2+100,370),fill='dark green',tag='player')
        #self.canvas.bind('<Motion>',self.move_player)
        #self.canvas.move('player',5,5)
        
        #cria os retangulos para destruir:
        self.ret=[]
        linhas,col,espaçam = 5,8,2
        base,h,y0 = 48,20,50
        for i in range(linhas):
            cor = random.choice(cores)
            for j in range(col):
                r = self.canvas.create_rectangle(base*j+(j+1)*espaçam, i*h+(i+1)*espaçam+y0, base*j+(j+1)*espaçam+base, i*h+(i+1)*espaçam+y0+h, fill=cor,tag='ret')
                self.ret.append(r)
                
        #mensagem principal do jogo:
        #self.canvas.create_text(canvas_larg/2,canvas_al/2, text = 'Hello Friend', fill='white')

        #variavel para saber se o player esta jogando
        self.jogando=True

        #bola do jogo:
        raio = 30
        posicao = (100,200)
        self.bola_vx = self.bola_vy = 5
        self.bola_x, self.bola_y = posicao
        self.canvas.create_oval(self.bola_x,self.bola_y ,self.bola_x+raio, self.bola_y+raio, fill='red',outline='red',tag='bola')
        
    def move_player(self):
        pass
        return
        '''
        self.player_x = 100
        self.player_b=(canvas_larg//2)
        if event.x > 0 and event.x < canvas_larg - self.player_b:
            self.player_x = event.x
        '''
    
        
    def começa(self):
        #inicia o jogo:
        self.jogar()

    def jogar(self):
        if self.jogando:
            self.update()
            self.desenhar()
            
            self.root.after(10,self.jogar)
        
    def desenhar(self):
        #redesenha a tela do canvas 
        self.canvas.delete('player')
        
        #self.player = self.canvas.create_rectangle(self.player_x,self.player_y,self.player_x1,self.player_y1,fill='dark green',tag='player')        
        
        #self.player = self.canvas.create_rectangle((canvas_larg//2,350),(canvas_larg//2+100,370),fill='dark green',tag='player')
        self.canvas.create_oval(self.bola_x,self.bola_y ,self.bola_x+30, self.bola_y+30, fill='red',outline='red',tag='bola')
        
    def update(self):
        #move a bola:
        
        self.canvas.move('bola',self.bola_vx,self.bola_vy)
        #self.canvas.move('player',5,5)
        #self.canvas.itemconfig('bola',fill=random.choice(cores))

        self.player_x=canvas_larg//2
        self.player_y=350
        self.player_x1=self.player_x+100
        self.player_y1=370
        
        #self.player_x += self.player_vx
        #self.player_y += self.player_vy
        
        self.bola_x += self.bola_vx
        self.bola_y += self.bola_vy
        
        if self.bola_x > canvas_al-30 or self.bola_x < 0:
            self.bola_vx*=-1
        if self.bola_y > canvas_al-30 or self.bola_y < 0:
            self.bola_vy*=-1
        self.verifica_colisao()
        
    def verifica_colisao(self):
        #verificar se houve colisao entre os elementos do jogo:

        #criar coordenada pra bola
        cord=self.canvas.bbox('bola')
        cord2=self.canvas.bbox('player')
        

        colisoes = self.canvas.find_overlapping(*cord)

        if len(colisoes)!=0:
            
            if colisoes[0]!=self.player:
                
                #checar o elemento mais proximo que a bola colidiu
                obj_mp = self.canvas.find_closest(cord[0],cord[1])
                #checar com qual ret a bola colidiu
                for retan in self.ret:
                
                    if retan == obj_mp[0]:
                        
                        self.ret.remove(retan)
                        self.canvas.delete(retan)

                        #inverter o sentido da velocidade da bola
                        self.bola_vy *= -1

                        return
            else:
                self.bola_vy*=-1
        
            
            
        
if __name__ == '__main__':
    Jogo()
