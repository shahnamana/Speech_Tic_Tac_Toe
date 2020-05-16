# importing the required libraries
import pygame as pg
import sys
import time
from pygame.locals import *
import speech_recognition as sr
import re

# declaring the global variables

# for storing the 'x' or 'o'
# value as character
XO = 'x'

# storing the winner's value at
# any instant of code
winner = None

# to check if the game is a draw
draw = None

# to set width of the game window
width = 400

# to set height of the game window
height = 400

# to set background color of the
# game window
white = (255, 255, 255)

# color of the straightlines on that
# white game board, dividing board
# into 9 parts
line_color = (0, 0, 0)

# setting up a 3 * 3 board in canvas
board = [[None]*3, [None]*3, [None]*3]


def pmusic(file):
    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()
    pg.mixer.music.load(file)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        # print("Playing...")
        clock.tick(1000)

def stopmusic():
    pg.mixer.music.stop()


def getmixerargs():
    pg.mixer.init()
    freq, size, chan = pg.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pg 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pg.mixer.init(FREQ, SIZE, CHAN, BUFFER)


def get_position_from_speech():
	r2 = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening")
		audio = r2.listen(source)

		try:
			get = r2.recognize_google(audio)
			print(get)
			m = re.search(r'\d', get)
			if m is not None:
				print(get[m.start()])
				return get[m.start()]
			else:
				message = "Couldn't hear Properly Please Repeat"
				font = pg.font.Font(None,30)
				text = font.render(message,3,(255,255,255))
				screen.fill((0,0,0),(0,400,500,100))
				text_rect = text.get_rect(center = (width/2,500-50))
				screen.blit(text,text_rect)
				pg.display.update()
				get_position_from_speech
		except sr.UnknownValueError:
			print("Error")
			message = "Couldn't hear Properly Please Repeat"
			font = pg.font.Font(None,30)
			text = font.render(message,3,(255,255,255))
			screen.fill((0,0,0),(0,400,500,100))
			text_rect = text.get_rect(center = (width/2,500-50))
			screen.blit(text,text_rect)
			pg.display.update()
			get_position_from_speech
			get_position_from_speech()
		except sr.RequestError as e:
			print('failed'.format(e))


# initializing the pygame window
pg.init()

# setting fps manually
fps = 30

# this is used to track time
CLOCK = pg.time.Clock()

# this method is used to build the
# infrastructure of the display
screen = pg.display.set_mode((width, height + 100), 0, 32)

# setting up a nametag for the
# game window
pg.display.set_caption("My Tic Tac Toe")

# loading the images as python object
initiating_window = pg.image.load("13-oclrwziqba3x0hxuvkskbu45vr4c4m6ulzt2lnvqw8.png")
x_img = pg.image.load("X_modified.png")
y_img = pg.image.load("o_modified.png")

# resizing images
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))

def game_initiating_window():

	# displaying over the screen
	screen.blit(initiating_window, (0, 0))

	# updating the display
	pg.display.update()
	time.sleep(3)
	screen.fill(white)

	# drawing vertical lines
	pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
	pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

	# drawing horizontal lines
	pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
	pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
	draw_status()

def draw_status():

	# getting the global variable draw
	# into action
	global draw

	if winner is None:
		if XO.upper() == "X":
			try:
			    initMixer()
			    file = r'C:\Users\Naman Shah\Desktop\Speech_Tic_Tac_Toe\X-chance.mp3'
			    pmusic(file)
			except Exception:
			    print("unknown error")
		elif XO.upper() == "O":
			try:
			    initMixer()
			    file = r'C:\Users\Naman Shah\Desktop\Speech_Tic_Tac_Toe\O-chance.mp3'
			    pmusic(file)
			except Exception:
			    print("unknown error")
		message = XO.upper() + "'s Turn"+'    '+'Recording Audio'

	else:
		if winner.upper() == "X":
			try:
			    initMixer()
			    file = r'C:\Users\Naman Shah\Desktop\Speech_Tic_Tac_Toe\X-Won-Voice.mp3'
			    pmusic(file)
			except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
			    stopmusic()
			    print("\nPlay Stopped by user")
			except Exception:
			    print("unknown error")
		elif winner.upper() == "O":
			try:
			    initMixer()
			    file = r'C:\Users\Naman Shah\Desktop\Speech_Tic_Tac_Toe\o-won.mp3'
			    pmusic(file)
			except Exception:
			    print("unknown error")
		message = winner.upper() + " won !"

	if draw:
		message = "Game Draw !"
		try:
			initMixer()
			file = r'Speech_Tic_Tac_Toe\draw-game.mp3'
			pmusic(file)
		except KeyboardInterrupt:  # to stop playing, press "ctrl-c"
			stopmusic()
			print("\nPlay Stopped by user")
		except Exception:
			print("unknown error")


	# setting a font object
	font = pg.font.Font(None, 30)

	# setting the font properties like
	# color and width of the text
	text = font.render(message, 3, (255, 255, 255))

	# copy the rendered message onto the board
	# creating a small block at the bottom of the main display
	screen.fill ((0, 0, 0), (0, 400, 500, 100))
	text_rect = text.get_rect(center =(width / 2, 500-50))
	screen.blit(text, text_rect)
	pg.display.update()

def check_win():
	global board, winner, draw

	# checking for winning rows
	for row in range(0, 3):
		if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
			winner = board[row][0]
			pg.draw.line(screen, (250, 0, 0),
						(0, (row + 1)*height / 3 -height / 6),
						(width, (row + 1)*height / 3 - height / 6 ),
						4)
			break

	# checking for winning columns
	for col in range(0, 3):
		if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
			winner = board[0][col]
			pg.draw.line (screen, (250, 0, 0), ((col + 1)* width / 3 - width / 6, 0), \
						((col + 1)* width / 3 - width / 6, height), 4)
			break

	# check for diagonal winners
	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

		# game won diagonally left to right
		winner = board[0][0]
		pg.draw.line (screen, (250, 70, 70), (50, 50), (350, 350), 4)

	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):

		# game won diagonally right to left
		winner = board[0][2]
		pg.draw.line (screen, (250, 70, 70), (350, 50), (50, 350), 4)

	if(all([all(row) for row in board]) and winner is None ):
		draw = True
	draw_status()

def drawXO(row, col):
	global board, XO

	# for the first row, the image
	# should be pasted at a x coordinate
	# of 30 from the left margin
	if row == 1:
		posx = 30

	# for the second row, the image
	# should be pasted at a x coordinate
	# of 30 from the game line
	if row == 2:

		# margin or width / 3 + 30 from
		# the left margin of the window
		posx = width / 3 + 30

	if row == 3:
		posx = width / 3 * 2 + 30

	if col == 1:
		posy = 30

	if col == 2:
		posy = height / 3 + 30

	if col == 3:
		posy = height / 3 * 2 + 30

	# setting up the required board
	# value to display
	board[row-1][col-1] = XO

	if(XO == 'x'):

		# pasting x_img over the screen
		# at a coordinate position of
		# (pos_y, posx) defined in the
		# above code
		screen.blit(x_img, (posy, posx))
		XO = 'o'

	else:
		screen.blit(o_img, (posy, posx))
		XO = 'x'
	pg.display.update()

def user_click():
	# get coordinates of mouse click
	# x, y = pg.mouse.get_pos()
	#
	# # get column of mouse click (1-3)
	# if(x<width / 3):
	# 	col = 1
	#
	# elif (x<width / 3 * 2):
	# 	col = 2
	#
	# elif(x<width):
	# 	col = 3
	#
	# else:
	# 	col = None
	#
	# # get row of mouse click (1-3)
	# if(y<height / 3):
	# 	row = 1
	#
	# elif (y<height / 3 * 2):
	# 	row = 2
	#
	# elif(y<height):
	# 	row = 3
	#
	# else:
	# 	row = None

	ind = get_position_from_speech()
	if '1' == ind:
		row = 1
		col = 1
	elif '2' == ind:
		row = 1
		col = 2
	elif '3' == ind:
		row = 1
		col = 3
	elif '4' == ind:
		row = 2
		col = 1
	elif '5' == ind:
		row = 2
		col = 2
	elif '6' == ind:
		row = 2
		col = 3
	elif '7' == ind:
		row = 3
		col = 1
	elif '8' == ind:
		row = 3
		col = 2
	elif '9' == ind:
		row = 3
		col = 3
	else:
		row = None
		col = None

	# after getting the row and col,
	# we need to draw the images at
	# the desired positions
	if(row and col and board[row-1][col-1] is None):
		global XO
		drawXO(row, col)
		check_win()

def reset_game():
	global board, winner, XO, draw
	time.sleep(3)
	XO = 'x'
	draw = False
	game_initiating_window()
	winner = None
	board = [[None]*3, [None]*3, [None]*3]

game_initiating_window()

while(True):
	for event in pg.event.get():
		if event.type == QUIT:
			pg.quit()
			sys.exit()
		elif event.type is KEYUP:
			user_click()
			if(winner or draw):
				reset_game()
	pg.display.update()
	CLOCK.tick(fps)
