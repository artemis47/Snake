from unicurses import *
from time import sleep
from random import randint

while True:

	stdscr = initscr() #Initialising Screen

	start_color() #Initialising Default Color Set
	init_pair(1,COLOR_RED,COLOR_WHITE)
	init_pair(2,COLOR_WHITE,COLOR_RED)
	init_pair(3,COLOR_RED,COLOR_GREEN)

	headX, headY = 0, 0 #Coordinates of Head of Snake
	xV, yV = 1, 0 #Horizontal and Vertical velocities
	appleX, appleY = 0, 0 #Coordinates of "Apple"
	lx = 0
	SnakeLen = 3 #Initial Length
	Score = 0 #Initial Score

	ArrX = []
	ArrY = []
	for i in range(80):
		ArrX.append(0)
	for i in range(80):
		ArrY.append(0)


	addstr("This Program will make a Snake Game with Wrap-Around\n")
	addstr("Use Arrow Keys to Move and x to quit\n")
	sleep(1)
	addstr("Press Any Key To Start\n")

	cbreak() #Accept Input without pressing Enter
	keypad(stdscr,True) #Accept Keypad Strokes
	noecho() #Disable printing of KeyStrokes on Screen
	hold = getch() #Dummy Variable to wait for input before Starting
	curs_set(0) #Disable Blinking Cursor

	appleX = randint(0,79) #Random Position for Apple
	appleY = randint(0,24)
	while True:
		clear() #Clear Screen of previous Output

		mvaddstr(12, 82, "Score = " + str(Score)) #Score Counter
		mvaddstr(13, 82, "Press X to Exit")
		mvaddstr(14, 82, "Press Space to PAUSE")
		headX += xV #Changing the position of Head of Snake
		headY += yV

		#Wrap-Around Conditions
		if headX == -1:
			headX = 79
		if headY == -1:
			headY = 24
		if headX == 80:
			headX = 0
		if headY == 25:
			headY = 0

		ArrX[SnakeLen] = headX
		ArrY[SnakeLen] = headY
		for lx in range(0,SnakeLen):
			ArrX[lx] = ArrX[lx + 1]
			ArrY[lx] = ArrY[lx + 1]

		#Display the Snake's body on screen

		if(has_colors()):
			for lx in range(0, SnakeLen):
				mvaddch(ArrY[lx], ArrX[lx], ord(' '),color_pair(1))
				if not ((ArrY[lx] == appleY) and (ArrX[lx] == appleX)):
					mvaddch(appleY, appleX, ord(' '),color_pair(2))
			mvaddch(ArrY[SnakeLen], ArrX[SnakeLen], ord(' '),color_pair(3))

		else: #For Terminals that can't display color
			for lx in range(0, SnakeLen):
				mvaddch(ArrY[lx], ArrX[lx], ord('O'))
				if not ((ArrY[lx] == appleY) and (ArrX[lx] == appleX)):
					mvaddch(appleY, appleX, ord('@'))
			mvaddch(ArrY[SnakeLen], ArrX[SnakeLen], ord('X'))

		timeout(1) #Timeout so that snake's movement can carry on
		cha = getch()

		#Changing Velocity based on input
		if cha == KEY_UP and yV != 1:
			yV = -1
			xV = 0
		elif cha == KEY_DOWN and yV != -1:
			yV = 1
			xV = 0
		elif cha == KEY_LEFT and xV != 1:
			yV = 0
			xV = -1
		elif cha == KEY_RIGHT and xV != -1:
			yV = 0
			xV = 1

		elif cha == ord('x'): #Exit Condition
			clear()
			refresh()
			break

		elif cha == ord(' '): #Pause Condition
			timeout(-1)
			mvaddstr(14, 82, "PAUSED. Press Space Again to Unpause")
			cha = getch()
			while cha != ord(' '):
				cha = getch()
				continue
			timeout(1)

		if (headY == appleY) and (headX == appleX): #When Snake "eats" the apple
			Score += 1 #Increase Score
			appleX = randint(0,79) #New Position for Apple
			appleY = randint(0,24)
		
			if SnakeLen < 80: #Increase Snake's Length
				SnakeLen += 1

		else: #Conditions for when the Snake "bites" itself
			if (headX in ArrX[:SnakeLen-1]):
				if(headY == ArrY[ArrX.index(headX)]):
					clear()
					refresh()
					break
			if (headY in ArrY[:SnakeLen-1]):
				if(headX == ArrX[ArrY.index(headY)]):
					clear()
					refresh()
					break

	timeout(-1) #Disabling Timeout and waiting indefinitely for input
	mvaddstr(12,40, "Your Score is " + str(Score))
	mvaddstr(13,25, "Press Y To Play Again.Press Any other key to Quit.")
	hold = getch()

	if hold == ord('y'):
		clear()
		refresh()
		endwin()
		continue
	else:
		endwin()
		break