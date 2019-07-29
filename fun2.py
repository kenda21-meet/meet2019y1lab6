import turtle
turtle.goto(0,0)
turtle.direction=None

def up():
    turtle.direction="Up"
    print("you pressed the up key.")
turtle.onkey(up, "Up")
turtle.listen()

def on_move():
    x,y=turtle.pos()
    if turtle.direction=="Up":
        turtle.goto(x,y+100)
def on_move2():
    x,y=turtle.pos()
    if turtle.direction=="Down":
        turtle.goto(x,y-100)
def on_move3():
    x,y=turtle.pos()
    if turtle.direction=="Right":
        turtle.goto(x+100,y)
def on_move4():
    x,y=turtle.pos()
    if turtle.direction=="Left":
        turtle.goto(x-100,y)

turtle.onkey(on_move,"Up")
turtle.onkey(on_move2,"Down")
turtle.onkey(on_move3,"Right")
turtle.onkey(on_move4,"Left")
turtle.listen()
