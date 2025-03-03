import turtle #Importing turtle

#Method to draw sphere
def draw_circle(my_turtle, line_color, fill_color, circle_radius, value_to_decrease_circle_size):

    my_turtle.color(line_color, fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(circle_radius - (value_to_decrease_circle_size))
    my_turtle.end_fill()

#Setting up the turtle screen
wn = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape()
#Printing circles of two different sizes to show a sphere feeling
for i in range(50):
    if i % 2 == 0:
        my_turtle.penup()
        my_turtle.left(90)
        my_turtle.forward(150)
        my_turtle.left(90)#
        my_turtle.forward(150)
        my_turtle.pendown()
        if i % 20  == 0:
            draw_circle(my_turtle,"#FFFFCB", "#FFFFCB", 100, i)
        else:   
            draw_circle(my_turtle,"#FFFF01", "#FFFF01", 100, i)

    else:
        my_turtle.penup()
        my_turtle.left(90)
        my_turtle.forward(150)
        my_turtle.left(90)#
        my_turtle.forward(150)
        my_turtle.pendown()
        if i % 3 == 0 or i % 5  or i % 7== 0:
            draw_circle(my_turtle,"#FF4500", "#FF4500", 50, i)
        else:
            draw_circle(my_turtle,"#FF7F50", "#FF7F50", 50, i)
my_turtle.shape()
wn.exitonclick()