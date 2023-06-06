from tkinter import Tk,Canvas,Label,Button
from math import pow,sqrt

#------------------------------------------------
#-Initialisation des variables globaux-----------
#------------------------------------------------
taille_grille = 658,558#taille de la grille min:500,278 
temps_jeu =  [0,1,31]#temps avant la fin du jeu en minute
#-----------------------------------------------
#------Informations sur les joueurs-------------
color_1, nbr_pt_player_1,score_player_1,etat_player_1 = "#cd021b",0,0,True
color_2, nbr_pt_player_2,score_player_2,etat_player_2 = "#9d6c36",0,0,True
color_3, nbr_pt_player_3,score_player_3,etat_player_3 = "#068520",0,0,False
color_4, nbr_pt_player_4,score_player_4,etat_player_4 = "#6f2c99",0,0,False

#---------------------------------
player_1 = {
    "couleur": color_1,
    "nbr_pt_player_1": nbr_pt_player_1,
    "score_player_1": score_player_1,
    "etat": etat_player_1
}
player_2 = {
    "couleur": color_2,
    "nbr_pt_player_2": nbr_pt_player_2,
    "score_player_2": score_player_2,
    "etat": etat_player_2
}
player_3 = {
    "couleur": color_3,
    "nbr_pt_player_3": nbr_pt_player_3,
    "score_player_3": score_player_3,
    "etat": etat_player_3
}
player_4 = {
    "couleur": color_4,
    "nbr_pt_player_4": nbr_pt_player_4,
    "score_player_4": score_player_4,
    "etat": etat_player_4
}
#-------------------------------------------------------
#--------------Variable d'etat de jeu ------------------
#-------------------------------------------------------
status = True       #definie si le jeu est en pause 
#------------
liste_points = []    #contient la liste des point du jeu
liste_centre = []    #contient la liste des centres de masse du jeu
liste_centre_actif = []    #contient la liste des centres de masse qui sont pret a encadrer
#------------
curseur = color_1
#------------------------------------------------
#-Initialisation des Classes --------------------
#------------------------------------------------
class Point:
	#determine si le pt est lier ou pas
	def __init__(self,x,y,cnv, color="red"):
		self.x = x
		self.y = y
		self.cnv = cnv
		self.color = color
		self.capturer = False
		
		cnv.create_oval(self.x-5, self.y-5, self.x+5, self.y+5,outline=self.color, fill=self.color)
		

#------------------------------------------------
#-Initialisation des fonctions ------------------
#------------------------------------------------
def put_pause(fen):#elle met le jeu en put_
    global status
    if status:
        status = False

        #titre du jeu 
        pause_txt = Label(fen,text="Pause",width=10, fg="#4f4fff",font=("Arial",35,"bold"))
        pause_txt.place(x= taille_grille[0]/2 - 100, y= taille_grille[1]/2 +30)
        pause = Button(fen,command=lambda: put_pause(fen), text="Jouer",width=17,height=2, relief="flat", bg="green",font=("Arial",9,"bold"),activebackground="#6b6bff",bd=0)
        pause.place(x= 160, y=70+taille_grille[1]+18)
        
        print("----------------------Jeu en Pause------------------------")
    else:
        status = True
        fen.children[str(fen.children.keys()).split(",")[-2].split("'")[1]].destroy()
        pause = Button(fen,command=lambda: put_pause(fen), text="Pause",width=17,height=2, relief="flat", bg="#6b6bff",font=("Arial",9,"bold"),activebackground="#6b6bff",bd=0)
        pause.place(x= 160, y=70+taille_grille[1]+18)
        print("----------------------Reprise du Jeu----------------------")

def display(fen):#gere laffichage des widget a lecran
    
    c1 = color_1
    c2 = color_2
    c3 = color_3
    c4 = color_4
    if not etat_player_1:
        c1 = "#eee"
    if not etat_player_2:
        c2 = "#eee"
    if not etat_player_3:
        c3 = "#eee"
    if not etat_player_4:
        c4 = "#eee"
        
    
             
    #titre du jeu 
    title = Label(fen,text="Blokus v1.1",width=10, fg="#4f4fff",font=("Arial",15,"bold"))
    title.place(x= taille_grille[0]/2 - 10, y= -2)
    #------------------------------------------------------------------------------------
    #--------------Affichage des infos joueurs-------------------------------------------
    #-------------PLAYER 1---------------------------------------------------------
    
    #affichage du nbr de pt
    nbr_pt_1 = Label(fen,text="Points : "+str(nbr_pt_player_1), fg=c1,font=("Arial",10,"bold"))
    nbr_pt_1.place(x= taille_grille[0]*0.1, y= 30)
    #affichage des scores
    score_1 = Label(fen,text="Score : "+str(score_player_1), fg=c1,font=("Arial",10,"bold"))
    score_1.place(x= taille_grille[0]*0.1, y= 55)

    #-------------PLAYER 2---------------------------------------------------------
    
    #affichage du nbr de pt
    nbr_pt_2 = Label(fen,text="Points : "+str(nbr_pt_player_2), fg=c2,font=("Arial",10,"bold"))
    nbr_pt_2.place(x= taille_grille[0]*0.35, y= 30)
    #affichage des scores
    score_2 = Label(fen,text="Score : "+str(score_player_2), fg=c2,font=("Arial",10,"bold"))
    score_2.place(x= taille_grille[0]*0.35, y= 55)

    #-------------PLAYER 3---------------------------------------------------------
    
    #affichage du nbr de pt
    nbr_pt_3 = Label(fen,text="Points : "+str(nbr_pt_player_3), fg=c3,font=("Arial",10,"bold"))
    nbr_pt_3.place(x= taille_grille[0]*0.6, y= 30)
    #affichage des scores
    score_3 = Label(fen,text="Score : "+str(score_player_3), fg=c3,font=("Arial",10,"bold"))
    score_3.place(x= taille_grille[0]*0.6, y= 55)

    #-------------PLAYER 4---------------------------------------------------------
    
    #affichage du nbr de pt
    nbr_pt_4 = Label(fen,text="Points : "+str(nbr_pt_player_4), fg=c4,font=("Arial",10,"bold"))
    nbr_pt_4.place(x= taille_grille[0]*0.85, y= 30)
    #affichage des scores
    score_4 = Label(fen,text="Score : "+str(score_player_4), fg=c4,font=("Arial",10,"bold"))
    score_4.place(x= taille_grille[0]*0.85, y= 55)
    print('----------------------Affichage OK------------------------')

def fin_jeu():
	pass

def fen_setting():
     pass	


def nouvelle_partie(taille, temps):
    #-------------------------------
    #Elle genere une nouvelle partie
    #-------------------------------
    
    fen = Tk()
    fen.title('Blockus version 1.0')
    #---------calculant la taille de la fenetre en fonction de la grille----------------
    fen.geometry(str(taille[0]+50)+'x'+str(taille[1]+130)+'+200+30')
    #------------------------------------------------------------------------------------  
    fen.resizable(width=0, height=0)
    
    #----------Creation du canvas de la grille--------------------------------------------
    cnv = Canvas(fen, width= taille_grille[0], height= taille_grille[1], bg='#c9c9ff')
    cnv.place(x=25, y=80)
    #-------------------------------------------------------------------------------------
    
    
    #-------------------------------------------------------------------------------------
    #----------Dessin de la grille de jeu ------------------------------------------------
    def grille():
        #creation de la grille du jeu
        #arriere plan
        for i in range(0, taille[0]+10, 10):
            cnv.create_line(i,0,i,taille[1]+5,fill='#a1b2ff',width=2)
        for i in range(0, taille[1]+10, 10):
           cnv.create_line(0,i,taille[0]+5,i,fill='#a1b2ff',width=2)

        #avant plan
        for i in range(0, taille[0]+10, 40):
            cnv.create_line(i,0,i,taille[1]+5,fill='#2684ff',width=2)
        for i in range(0, taille[1]+10, 40):
            cnv.create_line(0,i,taille[0]+5,i,fill='#2684ff',width=2)
        print('------------------------Grille OK-------------------------')
        

    
    grille()
    #-------------------------------------------------------------------------------------
    
    #-------------------------------------------------------------------------------------
    #----------Affichage des widget avec display------------------------------------------
    display(fen)
    #-------------------------------------------------------------------------------------

    #----------Affichage du temps et controle de la partie--------------------------------
    #affiche le temps et controle la partie 
    def time_play():
        global status
        
        if status:
            if temps == [0,0,0]:
                print("----------------------Temps Ecouler-----------------------")
                status = False
                fin_jeu()
                return 0
            t = ["","",""]
            col = "#4f4fff"
            if temps[1]<1 and temps[2]<60:
                col = 'red'
            if temps[2] == 0 and temps[1] != 0:
                temps[2] = 59
                temps[1] -= 1

            elif temps[1] == 0 and temps[2]==0:
                temps[1] = 59
                temps[2] = 59
                temps[0] -= 1
            else:
                temps[2] -= 1

            #affichage
            if temps[0]<10:
                t[0] = "0"+str(temps[0])
            else:
                t[0] = str(temps[0])
            if temps[1]<10:
                t[1] = "0"+str(temps[1])
            else:
                t[1] = str(temps[1])
            if temps[2]<10:
                t[2] = "0"+str(temps[2])
            else:
                t[2] = str(temps[2])


            tp = Label(fen,text="Temps: "+t[0]+":"+t[1]+":"+t[2], fg=col,font=("Arial",14,"bold"))
            tp.place(x= 25+taille_grille[0]-160, y= 70+taille_grille[1]+22)

        
        cnv.after(1000,time_play)
    time_play()
    
    #-------------------------------------------------------------------------------------
    #----------Evenement de click de la souris--------------------------------------------	
    #fonction executer lors du click
    def click(event):
        global curseur,nbr_pt_player_1,nbr_pt_player_2,nbr_pt_player_3,nbr_pt_player_4
         
        #on dessine un point a chaque click
        if status:
            x,y= event.x,event.y
        else:
            x,y = 12.2,12.2
        #determinons si le click est proche d'un point
        if x/40 > int(x/40)+0.5:
            x= 40*(int(x/40)+1)
        else:
            x= 40*int(x/40)

        if y/40 > int(y/40)+0.5:
            y= 40*(int(y/40)+1)
        else:
            y= 40*int(y/40)
        #verifions si le click est proche de ce point
        if sqrt(pow(event.x-x, 2)+pow(event.y-y, 2))<= 10:
            #on verifie si un point a deja ete dessine a cet emplacement
            exis = False
            for i in liste_points:
                if i.x == x and i.y == y:
                    exis = True
            #on fait evoluer le curseur
            if exis == False and curseur == color_1:
                liste_points.append(Point(x,y,cnv,color_1))
                print("Joueur 1: +1pt")
                #actualisons les donnees 
                nbr_pt_player_1 += 1
                display(fen)
                #on teste letat avant de passer le curseur
                if etat_player_2:
                    curseur = color_2
                elif etat_player_3:
                    curseur = color_3
                elif etat_player_4:
                    curseur = color_4
            elif exis == False and curseur == color_2:
                liste_points.append(Point(x,y,cnv,color_2))
                print("Joueur 2: +1pt")
                #actualisons les donnees 
                nbr_pt_player_2 += 1
                display(fen)
                #on teste letat avant de passer le curseur
                if etat_player_3:
                    curseur = color_3
                elif etat_player_4:
                    curseur = color_4
                elif etat_player_1:
                    curseur = color_1
            elif exis == False and curseur == color_3:
                liste_points.append(Point(x,y,cnv,color_3))
                print("Joueur 3: +1pt")
                #actualisons les donnees 
                nbr_pt_player_3+= 1
                display(fen)
                #on teste letat avant de passer le curseur
                if etat_player_4:
                    curseur = color_4
                elif etat_player_1:
                    curseur = color_1
                elif etat_player_2:
                    curseur = color_2
            elif exis == False and curseur == color_4:
                liste_points.append(Point(x,y,cnv,color_4))
                print("Joueur 4: +1pt")
                #actualisons les donnees 
                nbr_pt_player_4 += 1
                display(fen)
                #on teste letat avant de passer le curseur
                if etat_player_1:
                    curseur = color_1
                elif etat_player_2:
                    curseur = color_2
                elif etat_player_3:
                    curseur = color_3
            else:
                print('impossible de creer le pt')
            
            a = Button(fen, text="", bg=curseur,width=int(((25+taille_grille[0]-160)-177)*0.04), relief="flat")
            a.place(x=300, y=70+taille_grille[1]+23)    
            

            
    #-------------------------------------------------------------------------------------

    #bouton de jeu 
    #rejouer
    new = Button(fen, text="Nouveau",command= lambda:nouvelle_partie(taille_grille, temps_jeu),width=17,height=2, relief="flat", bg="#6b6bff",font=("Arial",9,"bold"),activebackground="#6b6bff",bd=0)
    new.place(x= 25, y=70+taille_grille[1]+18)
    #pause 
    pause = Button(fen,command=lambda: put_pause(fen), text="Pause",width=17,height=2, relief="flat", bg="#6b6bff",font=("Arial",9,"bold"),activebackground="#6b6bff",bd=0)
    pause.place(x= 160, y=70+taille_grille[1]+18)
    #parametre 
    setting = Button(fen,command=fen_setting, text="Edit",width=10,height=2, bg="#6b6bff",font=("Arial",9,"bold"),activebackground="#6b6bff",bd=0)
    setting.place(x= -10, y= 0)
    #indicateur de tour de jeu
    
    a = Button(fen, text="", bg=curseur,width=int(((25+taille_grille[0]-160)-177)*0.04), relief="flat")
    a.place(x=300, y=70+taille_grille[1]+23)  
    
    
    cnv.bind('<Button-1>', click)
    print("-----------------Nouvelle Partie Charger------------------")
    fen.mainloop()

nouvelle_partie(taille_grille, temps_jeu)
