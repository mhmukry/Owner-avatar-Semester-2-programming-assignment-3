import turtle

#Method to draw square
def draw_square(my_turtle, line_color, fill_color, square_size, rotation_angle):

    my_turtle.color(line_color, fill_color)
    my_turtle.begin_fill()
    my_turtle.forward(square_size)
    my_turtle.left(rotation_angle)
    my_turtle.forward(square_size)
    my_turtle.left(rotation_angle)
    my_turtle.forward(square_size)
    my_turtle.left(rotation_angle)
    my_turtle.forward(square_size)
    my_turtle.end_fill()

#Setting up the turtle screen
wn = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape('classic')
#Printing squares of different sizes to show a cube feeling
for i in range(24):
    if i % 2 == 0:
        my_turtle.penup()
        my_turtle.left(90)
        my_turtle.forward(125 + (i * 2))
        my_turtle.left(90)
        my_turtle.forward(125 + (i * 2))
        my_turtle.pendown()
        draw_square(my_turtle,"red", "red", 100, 90)

    else:
        
        my_turtle.penup()
        my_turtle.left(90)
        my_turtle.forward(125)
        my_turtle.left(90)
        my_turtle.forward(125)
        my_turtle.pendown()
        draw_square(my_turtle,"yellow", "yellow", 75, 90)



wn.exitonclick()