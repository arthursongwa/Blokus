from tkinter import Tk,Canvas,Label,Button
from math import pow,sqrt
from os import system


info_blue = {
	"nbr_pt": 0,
	"score": 0
}

info_red = {
	"nbr_pt": 0,
	"score": 0
}

curseur = "red"

liste_points_rouge = []
liste_points_bleu = []
liste_center = []


#creation de l'objet point
class Point:
	#determine si le pt est lier ou pas
	def __init__(self,x,y, color="red"):
		self.x = x
		self.y = y
		self.color = color
		self.capturer = False
		
		#verifions si le pt existe avant de le creer
		if self.color == "red":
			cnv.create_oval(self.x-5, self.y-5, self.x+5, self.y+5,outline="#be0000", fill=self.color)
		else:
			cnv.create_oval(self.x-5, self.y-5, self.x+5, self.y+5,outline="blue", fill=self.color)

	#retourne le nombre de point qui peuvent etre relier a ce point
	def valence(self):
		nbr=0
		#retourne le nombre de point qui sont autour de ce point
		if liste_points_rouge != []:
			coor = list()
			for i in liste_points_rouge:
				coor.append((i.x,i.y))
			if (self.x-40,self.y-40) in coor:
				nbr+=1
			if (self.x,self.y-40) in coor:
				nbr+=1
			if (self.x+40,self.y-40) in coor:
				nbr+=1
			if (self.x+40,self.y) in coor:
				nbr+=1
			if (self.x+40,self.y+40) in coor:
				nbr+=1
			if (self.x,self.y+40) in coor:
				nbr+=1
			if (self.x-40,self.y) in coor:
				nbr+=1
			if (self.x-40,self.y+40) in coor:
				nbr+=1
			return nbr


	#renvoie la liste des points qui sont proche de lui
	def pt_proches(self):
		liste= list()
		if liste_points_rouge != []:
			coor = list()
			for i in liste_points_rouge:
				coor.append((i.x,i.y))
			if (self.x-40,self.y-40) in coor:
				liste.append(Point(self.x-40,self.y-40))
			if (self.x,self.y-40) in coor:
				liste.append(Point(self.x,self.y-40))
			if (self.x+40,self.y-40) in coor:
				liste.append(Point(self.x+40,self.y-40))
			if (self.x+40,self.y) in coor:
				liste.append(Point(self.x+40,self.y))
			if (self.x+40,self.y+40) in coor:
				liste.append(Point(self.x+40,self.y+40))
			if (self.x,self.y+40) in coor:
				liste.append(Point(self.x,self.y+40))
			if (self.x-40,self.y) in coor:
				liste.append(Point(self.x-40,self.y))
			return liste

class center_pt:
	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.etat = True
		self.color = "#6b6bff"
		self.sms = ["","","",""]
        #ici tout les pts centres sont creer des le debut du jeu
		#cnv.create_oval(self.x-5, self.y-5, self.x+5, self.y+5,outline="#6b6bff", fill= self.color)
	def write(self):
		global info_blue, info_red
		if True:#encadrement des pt red
			coor = []
			for i in liste_points_rouge:#on charge les pt existant
				coor.append((i.x, i.y))
			#pt en haut droite
			x_pt = self.x +20
			y_pt = self.y -20
			if (x_pt,y_pt) in coor:#on verifie sil ya un pt a cet endroit
				self.sms[0] = (x_pt, y_pt)
			
			#pt en haut gauche
			x_pt = self.x -20
			y_pt = self.y -20
			if (x_pt,y_pt) in coor:#on verifie sil ya un pt a cet endroit
				self.sms[1] = (x_pt, y_pt)
			
			#pt en bas gauche
			x_pt = self.x -20
			y_pt = self.y +20
			if (x_pt,y_pt) in coor:#on verifie sil ya un pt a cet endroit
				self.sms[2] = (x_pt, y_pt)
			
			#pt en bas droite
			x_pt = self.x +20
			y_pt = self.y +20
			if (x_pt,y_pt) in coor:#on verifie sil ya un pt a cet endroit
				self.sms[3] = (x_pt, y_pt)
			
			#determinons la nature des pt dans sms
			a = []
			for i in liste_points_rouge:
				a.append((i.x,i.y))
			if str(type(self.sms[0]))=="<class 'tuple'>" and str(type(self.sms[1]))=="<class 'tuple'>" and str(type(self.sms[2]))=="<class 'tuple'>" and str(type(self.sms[3]))=="<class 'tuple'>":
				
				if self.sms[0] in a and self.sms[1] in a and self.sms[2] in a and self.sms[3] in a:
					#on relie le box
					cnv.create_line(self.sms[0],self.sms[1],fill='red',width=2)
					cnv.create_line(self.sms[1],self.sms[2],fill='red',width=2)
					cnv.create_line(self.sms[2],self.sms[3],fill='red',width=2)
					cnv.create_line(self.sms[3],self.sms[0],fill='red',width=2)
					self.etat = False
					return "red"
					
					


		if True:#encadrement des pt blue
			coor = []
			for i in liste_points_bleu:#on charge les pt existant
				coor.append((i.x, i.y))
			#pt en haut droite
			x_pt = self.x +20
			y_pt = self.y -20
			if (x_pt,y_pt) in coor:#on verifie sil ya un pt a cet endroit
				self.sms[0] = (x_pt, y_pt)
			
			#pt en haut gauche
			x_pt = self.x -20
			y_pt = self.y -20
			if (x_pt,y_pt) in coor:#on verifie sil ya un pt a cet endroit
				self.sms[1] = (x_pt, y_pt)
			
			#pt en bas gauche
			x_pt = self.x -20
			y_pt = self.y +20
			if (x_pt,y_pt) in coor:#on verifie sil ya un pt a cet endroit
				self.sms[2] = (x_pt, y_pt)
			
			#pt en bas droite
			x_pt = self.x +20
			y_pt = self.y +20
			if (x_pt,y_pt) in coor:#on verifie sil ya un pt a cet endroit
				self.sms[3] = (x_pt, y_pt)
			#determinons la nature des pt dans sms
			a = []
			for i in liste_points_bleu:
				a.append((i.x,i.y))
			if str(type(self.sms[0]))=="<class 'tuple'>" and str(type(self.sms[1]))=="<class 'tuple'>" and str(type(self.sms[2]))=="<class 'tuple'>" and str(type(self.sms[3]))=="<class 'tuple'>":
				
				if self.sms[0] in a and self.sms[1] in a and self.sms[2] in a and self.sms[3] in a:
					#on relie le box
					cnv.create_line(self.sms[0],self.sms[1],fill='blue',width=2)
					cnv.create_line(self.sms[1],self.sms[2],fill='blue',width=2)
					cnv.create_line(self.sms[2],self.sms[3],fill='blue',width=2)
					cnv.create_line(self.sms[3],self.sms[0],fill='blue',width=2)
					self.etat = False
					
					return "blue"


fen = Tk()
fen.title('Blockus version 1.0')
fen.geometry('800x630+200+30')
fen.resizable(width=0, height=0)
#fen.iconbitmap("C:\\Users\\HP\\OneDrive\\Documents\\GitHub\\Blokus\\logo.png")



#creation du canvas qui va contenir tout les points
cnv = Canvas(fen, width= 558, height= 558, bg='#c9c9ff')
cnv.place(x=110, y=40)

#verifie si un pt est encadrable ou non
def encadrer():
	global curseur
	liste_cen= list()#contient les centres les plus proches du pt
	for i in liste_center:
		if i.etat:
			liste_cen.append(i)
	
	for i in liste_cen:
		if i.write() == "red":
			info_red["score"]+=10
			display()
			curseur = "red"
		elif i.write() == "blue":
			info_blue["score"]+=10
			display()
			curseur = "blue"

		

			
		

	cnv.after(100, encadrer)
	
encadrer()

#fonction qui affiche les information a lecran
def display():
    global info_blue, info_red
    def actu():
        a= info_red["score"]
        b= info_blue["score"]

        if a!= info_red["score"]:
            display()
	    
        cnv.after(3000, actu)

    #titre du jeu 
    title = Label(fen,text="Blokus v1.0", fg="#4f4fff",font=("Arial",15,"bold"))
    title.place(x= 350, y= 10)
    
    #nom de lauteur
    auteur = Label(fen,text="Créer par Arthur Songwa [---] version: 1.0  \t  © 2023 SNG Corporation. Tous droits réservés.", fg="#4f4fff",font=("Arial",9,"bold"))
    auteur.place(x= 110, y= 600)

    #titre des zone
    red_title = Label(fen,text="Vous", fg="red",font=("Arial",13,"bold"))
    red_title.place(x= 30, y= 50)

    blue_title = Label(fen,text="Enemis", fg="blue",font=("Arial",13,"bold"))
    blue_title.place(x= 710, y= 50)

    #affichage du nbr de pt
    #red
    pt_red = Label(fen,text="Points :"+str(info_red["nbr_pt"]), fg="red",font=("Arial",13,"bold"))
    pt_red.place(x= 5, y= 100)
    #blue
    pt_blue = Label(fen,text="Points :"+str(info_blue["nbr_pt"]), fg="blue",font=("Arial",13,"bold"))
    pt_blue.place(x= 685, y= 100)

    #affichage des scores
    #red
    score_red = Label(fen,text="Score :"+str(info_red["score"]), fg="red",font=("Arial",13,"bold"))
    score_red.place(x= 5, y= 150)
    #blue
    score_blue = Label(fen,text="Score :"+str(info_blue["score"]), fg="blue",font=("Arial",13,"bold"))
    score_blue.place(x= 685, y= 150)

#fonction qui creer une nouvelle partie
def nouveau():
	global fen
	fen.destroy()#on va se contenter de sa pour le moment
	
	system("start C:\\Users\\HP\\OneDrive\\Documents\\GitHub\\Blokus\\Blokus-v1.0.exe")


#fonction executer lors du click
def click(event):
	global curseur
	
	#on dessine un point a chaque click
	x= event.x
	y= event.y
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
		for i in liste_points_rouge:
			if i.x == x and i.y == y:
				exis = True
		for i in liste_points_bleu:
			if i.x == x and i.y == y:
				exis = True
		
		if exis == False and curseur == "red":
			liste_points_rouge.append(Point(x,y))
			#actualisation du nbr de pt
			print("Point rouge creer : "+str(x)+"--"+str(y))
			info_red["nbr_pt"]+=1
			curseur = "blue"

		elif exis == False and curseur == "blue":
			liste_points_bleu.append(Point(x,y,"blue"))
			#actualisation du nbr de pt
			print("Point bleu creer : "+str(x)+"--"+str(y))
			info_blue["nbr_pt"]+=1
			curseur = "red"

		else:
			print('impossible')
		
		display()
		
#fonction affiche le tour de chaque joueur
def qui_joue():
	global curseur
	x,y = 109,-15
	
	a = Button(fen, text="", bg=curseur, width=79, relief="flat")
	a.place(x=x, y=y)

	cnv.after(100, qui_joue)

qui_joue()



#creation de la grille de jeu 
def grille():
    #creation de la grille du jeu
	#arriere plan
	for i in range(0, 760, 10):
		cnv.create_line(i,0,i,560,fill='#a1b2ff',width=2)
	for i in range(0, 560, 10):
		cnv.create_line(0,i,760,i,fill='#a1b2ff',width=2)

	#avant plan
	for i in range(0, 760, 40):
		cnv.create_line(i,0,i,560,fill='#2684ff',width=2)
	for i in range(0, 560, 40):
		cnv.create_line(0,i,760,i,fill='#2684ff',width=2)
		
	cnv.create_line(2,0,2,560,fill='#2684ff',width=2)
	cnv.create_line(0,2,760,2,fill='#2684ff',width=2)
	cnv.create_line(0,560,760,560,fill='#2684ff',width=2)
	x,y = 20,20
	while y<=540:
		if x>540:
			x= 20
			y+=40
		liste_center.append(center_pt(x,y))
		x+=40
		
	liste_center.pop()
	
		

grille()
display()

#bouton de jeu 
#rejouer
new = Button(fen, text="Nouveau",command= nouveau,width=17,height=2, relief="flat", bg="#6b6bff",font=("Arial",9,"bold"),activebackground="#6b6bff",bd=0)
new.place(x= 673, y=270)
#pause 
clr = Button(fen, text="Pause",width=17,height=2, relief="flat", bg="#6b6bff",font=("Arial",9,"bold"),activebackground="#6b6bff",bd=0)
clr.place(x= 673, y=310)

cnv.bind('<Button-1>', click)

fen.mainloop()
