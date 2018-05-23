from unicurses import *
from time import sleep
from random import randint

while True:

	stdscr = initscr()
	start_color()
	init_pair(1,COLOR_RED,COLOR_WHITE)
	init_pair(2,COLOR_WHITE,COLOR_RED)
	init_pair(3,COLOR_RED,COLOR_GREEN)
	headX, headY = 0, 0
	xV, yV = 1, 0
	appleX, appleY = 0, 0
	lx = 0
	SnakeLen = 3
	Score = 0

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

	cbreak()
	keypad(stdscr,True)
	noecho()
	hold = getch()
	curs_set(0)

	appleX = randint(0,79)
	appleY = randint(0,24)
	while True:
		clear()

		mvaddstr(12, 82, "Score = " + str(Score))
		headX += xV
		headY += yV

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

		for lx in range(0, SnakeLen):
			mvaddch(ArrY[lx], ArrX[lx], ord(' '),color_pair(1))
			if not ((ArrY[lx] == appleY) and (ArrX[lx] == appleX)):
				mvaddch(appleY, appleX, ord(' '),color_pair(2))
		mvaddch(ArrY[SnakeLen], ArrX[SnakeLen], ord(' '),color_pair(3))
		timeout(10)
		cha = getch()

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
		elif cha == ord('x'):
			clear()
			refresh()
			break
		if (headY == appleY) and (headX == appleX):
			Score += 1
			appleX = randint(0,79)
			appleY = randint(0,24)
		
			if SnakeLen < 100:
				SnakeLen += 1
		else:
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

	timeout(-1)
	curs_set(1)
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
