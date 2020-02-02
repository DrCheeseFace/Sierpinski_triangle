import tkinter
import random

window = tkinter.Tk() 
window.title("cool huh")


canvas_height= 800
canvas = tkinter.Canvas(window,width = canvas_height,height = canvas_height)
canvas.pack()

x1 = random.randint(0,canvas_height)
y1 = random.randint(0,canvas_height)
x2 = random.randint(0,canvas_height)
y2 = random.randint(0,canvas_height)
x3 = random.randint(0,canvas_height)
y3 = random.randint(0,canvas_height)


canvas.create_oval(x1, y1, x1, y1, width = 2, fill = ('red'))
canvas.create_oval(x2, y2, x2, y2, width = 2, fill = ('red'))
canvas.create_oval(x3, y3, x3, y3, width = 2, fill = ('red'))


start_pointx = random.randint(0,canvas_height)
start_pointy = random.randint(0,canvas_height)

canvas.create_oval(start_pointx ,start_pointy,start_pointx,start_pointy, width = 2, fill = 'black')


while True:	
	choose_point = random.choice([1,2,3])


	if choose_point == 1:
		temp_pointx = (start_pointx + x1)/2
		temp_pointy = (start_pointy + y1)/2

		

	if choose_point == 2:
		temp_pointx = (start_pointx + x2)/2
		temp_pointy = (start_pointy + y2)/2



	if choose_point == 3:
		temp_pointx = (start_pointx + x3)/2
		temp_pointy = (start_pointy + y3)/2

	
	canvas.create_oval(temp_pointx ,temp_pointy,temp_pointx,temp_pointy, width = 1, fill = 'black')

	start_pointx = temp_pointx
	start_pointy = temp_pointy	


	window.update()
window.mainloop()
