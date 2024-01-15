# from turtle model import Turtle, Screen class
import random
from turtle import Turtle, Screen


# MY Functions
#draw_turtle
def draw_turtle(generic_name, turtle_color, y_pos):
    generic_name = Turtle()
    generic_name.color(turtle_color)
    generic_name.shape('turtle')
    generic_name.shapesize(1.5)
    generic_name.penup()
    generic_name.goto(-300, y_pos)
    generic_name.pendown()
    return generic_name


# move _turtle_func function to control the green turtle

game_end = False
def move_turtle_func():
    if game_end == False:
        g_turtle.forward(40)

# create object from Turtle class
my_turtle = Turtle()


#creat object from screen
my_screen = Screen()
#screen setup
my_screen.title('My Race Game')
my_screen.setup(800,500)
my_screen.bgcolor('forestgreen')

#write text [ heading ]
my_turtle.penup()
my_turtle.goto(-100, 205)
my_turtle.color('White')
#my_turtle.speed('slowest')
my_turtle.write('Turtle Race', font=('Arial', 20, 'bold'))

#The brown floor

my_turtle.goto(-350, 200)
my_turtle.pendown()
my_turtle.fillcolor('chocolate')
my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()

#draw the endline
my_turtle.goto(250, 200)
my_turtle.right(90)
my_turtle.forward(400)

# Drawing Turtles : calling draw_function : 4 times
b_turtle = draw_turtle("blue_turtle", "cyan", 150)
p_turtle = draw_turtle("blue_turtle", "pink", 50)
y_turtle = draw_turtle("yellow_turtle", "yellow", -50)
g_turtle = draw_turtle("greem_turtle", "green", -150)

# I need to control th green turtle
my_screen.listen()
my_screen.onkey(move_turtle_func, "Right")

while True:
    b_turtle.forward(random.randint(1,10))
    p_turtle.forward(random.randint(1,10))
    y_turtle.forward(random.randint(1,10))
    #g_turtle.forward(random.randint(1,10))

    # if anyone is a winner [ x pos == 230 ]
    if b_turtle.xcor() >= 230:
        winner = b_turtle
        break
    elif p_turtle.xcor() >= 230:
        winner = p_turtle
        break
    elif y_turtle.xcor() >= 230:
        winner = y_turtle
        break
    elif g_turtle.xcor() >= 230:
        winner =g_turtle
        break

# Celebrate the winner
game_end = True
winner.shapesize(2.5)
for i in range(1000):
    winner.left(5)

my_screen.exitonclick()