import turtle
turtle.goto(0,0)
turtle.direction=None

def up():
    turtle.direction="Up"
    print("you pressed the up key.")
    on_move()
turtle.onkey(up, "Up")
turtle.listen()

def down():
    turtle.direction="Down"
    on_move()
turtle.onkey(down,"Down")
turtle.listen()

def right():
    turtle.direction="Right"
    on_move()
turtle.onkey(right,"Right")
turtle.listen()

def left():
    turtle.direction="Left"
    on_move()
turtle.onkey(left,"Left")
turtle.listen()



def on_move():
    x,y=turtle.pos()
    if turtle.direction=="Up":
        turtle.goto(x,y+100)
    elif turtle.direction=="Down":
        turtle.goto(x,y-100)
    elif turtle.direction=="Right":
        turtle.goto(x+100,y)
    elif turtle.direction=="Left":
        turtle.goto(x-100,y)

