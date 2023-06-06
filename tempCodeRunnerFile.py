
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
	