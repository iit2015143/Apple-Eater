import pygame,random,sys
pygame.init()

points = -10
eye = 4
notexit  = True
notquit = True
screen_w= 800
screen_h= 600
blk_s=10
blk_w = 180
fps = 15
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("anurag's snake :-)")

white1 = (0,0,0)
white = (50,255,20)
red = (255,0,0)
black = (0,0,0)
green = (0,55,0)
dgreen = (0,30,0)
tblue = (200,200,255,0)
blue = (0,0,200)

#screen.fill(white)
#pygame.display.update()

clock = pygame.time.Clock()
#	screen.fill(red, rect = [300,300,10,50])
# 	rectangle can be drawn this way

def drawpoints(msg,color,ccoord):
	font = pygame.font.Font('freesansbold.ttf',32)
	textsurface = font.render(msg,True,color)
	textrect = textsurface.get_rect()
	textrect.center = ccoord
	screen.blit(textsurface,textrect)
	#print(textrect)

def randcoord(applecoord):
	global points,fps
	apple_x = (random.randint(0,screen_w-1) // blk_s)*blk_s
	apple_y = (random.randint(0,screen_h-1) // blk_s)*blk_s
	applecoord.append(apple_x)
	applecoord.append(apple_y)
	#print(applecoord)
	points +=10
	fps+=1
	#print(fps)

def drawlist(list_move,lmove):
	#list_move = [[100,100,50,10],[200,200,50,10]]
	sl = list_move[len(list_move )- 1]
	for coord in list_move :
		pygame.draw.rect(screen,green,coord)
	if lmove == "left" or lmove == "up":
		pygame.draw.rect(screen,red,[sl[0]-eye/2,sl[1]-eye/2,blk_s+eye,blk_s+eye])
		pygame.draw.rect(screen,white1,[sl[0]+blk_s/2-eye/2,sl[1]+blk_s/2-eye/2,eye,eye])
		
	elif lmove == "down":
		pygame.draw.rect(screen,red,[sl[0]-eye/2,sl[1]+sl[3]-blk_s-eye/2,blk_s+eye,blk_s+eye])
		pygame.draw.rect(screen,white1,[sl[0]+blk_s/2-eye/2,sl[1]+sl[3]-blk_s+blk_s/2-eye/2,eye,eye])
	elif lmove == "right":
		pygame.draw.rect(screen,red,[sl[0]+sl[2]-eye/2-blk_s,sl[1]-eye/2,blk_s+eye,blk_s+eye])
		pygame.draw.rect(screen,white1,[sl[0]+sl[2]-blk_s+blk_s/2-eye/2,sl[1]+blk_s/2-eye/2,eye,eye])
		

def update(list_move,lmove,applecoord):
	global blk_w,notexit
	p=len(list_move)
	if p == 1:
		sl = list_move[0]
		if lmove =="right":
			list_move[0][0]+=blk_s
			if sl[0]+sl[2]==applecoord[0] and sl[1] == applecoord[1]:
				del applecoord[0]
				del applecoord[0]
				randcoord(applecoord) 
				sl[2]+=blk_s
				blk_w += blk_s
		elif lmove =="left":
			list_move[0][0]-=blk_s
			if sl[0]==applecoord[0] and sl[1] == applecoord[1]:
				del applecoord[0]
				del applecoord[0]
				randcoord(applecoord) 
				sl[2]+=blk_s
				blk_w += blk_s
		elif lmove =="up":
			list_move[0][1]-=blk_s
			# eating apple and drawing new one
			if sl[0]==applecoord[0] and sl[1] == applecoord[1]:
				del applecoord[0]
				del applecoord[0]
				randcoord(applecoord) 
				sl[3]+=blk_s
				blk_w += blk_s
		elif lmove =="down":
			list_move[0][1]+=blk_s
			if sl[0]==applecoord[0] and sl[1]+sl[3] == applecoord[1]:
				del applecoord[0]
				del applecoord[0]
				randcoord(applecoord) 
				sl[3]+=blk_s
				blk_w += blk_s
	elif p>1:
		# adding size and repositioning coordinates at last index
		sl = list_move[len(list_move)-1]
		if lmove == "up" and sl[3]<blk_w:
			sl[3]+=blk_s
			sl[1]-=blk_s
			# eating apple and drawing new one
			if sl[0]==applecoord[0] and sl[1] == applecoord[1]:
				del applecoord[0]
				del applecoord[0]
				randcoord(applecoord) 
				sl[3]+=blk_s
				blk_w += blk_s
		elif lmove == "down" and sl[3]<blk_w:
			if sl[0]==applecoord[0] and sl[1]+sl[3] == applecoord[1]:
				del applecoord[0]
				del applecoord[0]
				randcoord(applecoord) 
				sl[3]+=blk_s
				blk_w += blk_s
			sl[3]+=blk_s
		elif lmove == "left" and sl[2]<blk_w:
			sl[0]-=blk_s
			sl[2]+=blk_s
			if sl[0]==applecoord[0] and sl[1] == applecoord[1]:
				del applecoord[0]
				del applecoord[0]
				randcoord(applecoord) 
				sl[2]+=blk_s
				blk_w += blk_s
		elif lmove == "right" and sl[2]<blk_w:
			if sl[0]+sl[2]==applecoord[0] and sl[1] == applecoord[1]:
				del applecoord[0]
				del applecoord[0]
				randcoord(applecoord) 
				sl[2]+=blk_s
				blk_w += blk_s
			sl[2]+=blk_s

		# shortening the first index ans repositioning coordinates
		if list_move[0][2]>list_move[0][3] and list_move[1][0] > list_move[0][0]:
			list_move[0][2]-=blk_s
			list_move[0][0]+=blk_s
		elif list_move[0][2]>list_move[0][3] and list_move[1][0] == list_move[0][0]:
			list_move[0][2]-=blk_s
			#list_move[0][0]+=blk_s
		elif list_move[0][2]<list_move[0][3] and list_move[1][1] > list_move[0][1]:
			list_move[0][3]-=blk_s
			list_move[0][1]+=blk_s
		elif list_move[0][2]<list_move[0][3] and list_move[1][1] == list_move[0][1]:
			list_move[0][3]-=blk_s
			#list_move[0][1]+=blk_s
		else:
			del list_move[0]

	#checking for boundary touch
	if (lmove == "left" or lmove == "up") and (sl[0]<0 or sl[1]<0):
		notexit= False
	elif lmove == "right" and sl[0]+sl[2]>screen_w:
		notexit= False
	elif lmove == "down" and sl[1]+sl[3]>screen_h:
		notexit= False
		
def gameloop():
	global notexit
	lead_x = 400
	lead_y = 300
	x_mover = 0
	y_mover = 0
	notexit  = True
	lmove ="right"
	list_move = []
	list_move.append([lead_x,lead_y,blk_w,blk_s])
	applecoord = []
	randcoord(applecoord)
	while notexit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				notexit = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN and lmove != "up":
					if lmove == "right":
						sl = list_move[len(list_move)-1]
						list_move.append([sl[0]+sl[2]-blk_s,sl[1]+blk_s,blk_s,0])
					if lmove == "left":
						sl = list_move[len(list_move)-1]
						list_move.append([sl[0],sl[1]+blk_s,blk_s,0])
					lmove = "down"
					#y_mover = blk_h
					#x_mover = 0
				if event.key == pygame.K_UP and lmove != "down":
					if lmove == "right":
						sl = list_move[len(list_move)-1]
						list_move.append([sl[0]+sl[2]-blk_s,sl[1],blk_s,0])
					if lmove == "left":
						sl = list_move[len(list_move)-1]
						list_move.append([sl[0],sl[1],blk_s,0])
					lmove = "up"
		                        #y_mover = -blk_h
		                        #x_mover = 0
				if event.key == pygame.K_LEFT and lmove != "right":
					if lmove == "up":
						sl = list_move[len(list_move)-1]
						list_move.append([sl[0],sl[1],0,blk_s])
					if lmove == "down":
						sl = list_move[len(list_move)-1]
						list_move.append([sl[0],sl[1]+sl[3]-blk_s,0,blk_s])
					lmove = "left"
		                        #y_mover = 0
		                        #x_mover = -blk_h
				if event.key == pygame.K_RIGHT and lmove != "left":
					if lmove == "up":
						sl = list_move[len(list_move)-1]
						list_move.append([sl[0]+blk_s,sl[1],0,blk_s])
					if lmove == "down":
						sl = list_move[len(list_move)-1]
						list_move.append([sl[0]+blk_s,sl[1]+sl[3]-blk_s,0,blk_s])
					lmove = "right"
		                        #y_mover = 0
		                        #x_mover = blk_h
		#lead_x += x_mover
		#lead_y += y_mover
		#if lead_x<0 or lead_y <0 or lead_x>=screen_w or lead_y>=screen_h:
		#	notexit = False
		update(list_move,lmove,applecoord)
		#print(notexit)
		screen.fill(white) 
		drawpoints("SCORE : "+str(points),tblue,(100,20))
		pygame.draw.rect(screen,red,[applecoord[0],applecoord[1],blk_s,blk_s])
		drawlist(list_move,lmove)
		
		pygame.display.update()
		clock.tick(fps)
		#print(list_move)
gameloop()
while notquit:
	screen.fill(white) 
	drawpoints("SCORE : "+str(points),blue,(screen_w/2,screen_h/6))
	drawpoints("PRESS C TO CONTINUE AND Q TO QUIT",black,(screen_w/2,screen_h/2))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			notquit = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_c:
				points = -10
				notexit  = True
				blk_w = 180
				fps = 15
				gameloop()
			elif event.key == pygame.K_q:
				notquit = False
	
pygame.quit()
quit()
