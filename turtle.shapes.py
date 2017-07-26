import turtle
turtle.tracer(1, 0)
turtle.ht()
num_pts = 1000 #number sides to your drawing
for i in range (num_pts) :
    turtle.left(360/num_pts)
    turtle.forward(1)

turtle.mainloop()
