import tkinter
import random



def draw_point(x,y,colour):
	x=x*70+window_height/2
	y=y*70
	canvas.create_oval(x,y,x+1,y,fill = colour)



window = tkinter.Tk()
global window_height
window_height = 800
canvas = tkinter.Canvas(window,height = window_height,width = window_height)
canvas.pack()

colour = 'black'

x1 = 0 
y1 = 0
draw_point(x1,y1,colour)

while True:
	window.update()

	r = random.random()
	if r<=0.1:
		x2 = 0	
		y2 = y1*0.16

	elif r<=0.86:
		x2 = x1*0.85 + y1*0.04
		y2 = x1*-0.04 + y1*0.85 + 1.6
	elif r<=0.93:
		x2 = x1*0.2 - y1*0.26
		y2 = x1*0.23 + y1*0.22 + 1.6
	elif r<=1:
		x2 = x1*-0.15 + y1*0.28
		y2 = x1*0.26 + y1*0.24 + 0.44
	
	draw_point(x2,y2,colour)
	x1 = x2
	y1 = y2
window.mainloop()
