	
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
