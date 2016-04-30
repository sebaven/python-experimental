import turtle

def  draw_square(turtle):
    turtle.color("green")
    i = 0
    while (i <= 3) :
        turtle.forward(100);
        turtle.right(90);
        i = i + 1

def draw_circle(turtle):
    turtle.color("black")
    turtle.circle(100)

def draw_triangle(turtle):
    turtle.color("yellow")
    i = 0
    while (i <= 2) :
        turtle.forward(100);
        turtle.left(120);
        i = i + 1

def draw_art(turtle):
   for i in range(0,37):
       draw_square(turtle)
       turtle.right(10)

def draw_flower(turtle):
    turtle.shape("circle")
    turtle.left(90)
    turtle.forward(200)
    for i in range(0,24):
       draw_triangle(turtle)
       turtle.right(15)
    

window = turtle.Screen()
window.bgcolor("blue")
#aTurtle = turtle.Turtle() 
#draw_square(aTurtle)
#draw_circle(aTurtle)
#draw_triangle(aTurtle)
#draw_art(turtle)
#draw_flower(turtle)
window.exitonclick()
