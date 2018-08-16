import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(800,500)
turtle.penup()
turtle.pensize("10")
turtle.pencolor("blue")
turtle.bgcolor("black")
turtle.hideturtle()
turtle.goto(-200,-100)
turtle.pendown()
turtle.goto(200,-100)
turtle.goto(200,100)
turtle.goto(-200,100)
turtle.goto(-200,-100)

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.goto(-170,0)

turtle.penup()
turtle.goto(-160,50)
turtle.pendown()
turtle.goto(-120,50)
turtle.goto(-120,-10)

turtle.penup()
turtle.goto(-160,-50)
turtle.pendown()
turtle.goto(-40,-50)
turtle.penup()
turtle.goto(-70,-50)
turtle.pendown()
turtle.goto(-70,5)

turtle.penup()
turtle.goto(-75,50)
turtle.pendown()
turtle.goto(-40,50)

turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.goto(0,100)
turtle.penup()
turtle.goto(-25,0)
turtle.pendown()
turtle.goto(25,0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,-50)



turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.goto(170,0)

turtle.penup()
turtle.goto(160,50)
turtle.pendown()
turtle.goto(120,50)
turtle.goto(120,-10)

turtle.penup()
turtle.goto(160,-50)
turtle.pendown()
turtle.goto(40,-50)
turtle.penup()
turtle.goto(70,-50)
turtle.pendown()
turtle.goto(70,5)

turtle.penup()
turtle.goto(75,50)
turtle.pendown()

turtle.goto(40,50)

horizontal_walls = [(range(-200, 200),range(-115, -90)) ,(range(-200,200), range(90, 110)) , (range(-200,-170),range(-10, 10)) ,
                    (range(-160,-120), range(40, 60)) , (range(-170,-40), range(-65, -35)) , (range(-75, -40), range(40, 60)) ,
                     (range(-25, 25), range(-10, 10)) , (range(170, 200),range(-10, 10)) , (range(120, 160), range(35, 65)) ,
                     (range(40, 170), range(-60, -40)) , (range(40, 75), range(40, 60))]
vertical_walls = [(range(190, 210), range(-100, 100)) , (range(-210, -190), range(-100, 100)) , (range(-130, -110), range(-10, 50)) ,
                  (range(-80, -60), range(-50, 5)) , (range(-10, 10), range(50, 100)) , (range(-10, 10), range(-50, 3)) , (range(110, 130), range(-10, 50)) ,
                   (range(60, 80), range(-50, 5))]

all_walls = horizontal_walls + vertical_walls
turtle.penup()
turtle.goto(0,20)
turtle.pendown()

print(all_walls)
#turtle.register_shape('home/student/michal20_final-proj/meet2018y1final-proj/pacman.gif')
pac_man = turtle.clone()
pac_man.shape('circle')
pac_man.pensize(7)
pac_man.showturtle()
pac_man.color("yellow")
pac_man.penup()

UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 20
SPACEBAR = "space" 

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
direction = 5

def up():
    global direction
    direction=UP 
    print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    print("You pressed the down key!")

def right():
   global direction
   direction=RIGHT
   print("You pressed the right key!")

def left():
   global direction
   direction=LEFT
   print("You pressed the left key!")


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)

def check_overlap_horizontal(x,y):
    #pac_man_x = pac_man.pos()[0]
    #pac_man_y = pac_man.pos()[1]
    for horizontal_wall in horizontal_walls:
        if y in horizontal_wall[1]:#y coords are the same
            if x in horizontal_wall[0]:#x in the range of the wall
                return True
    return False

def check_overlap_vertical(x,y):
    #pac_man_x = pac_man.pos()[0]
    #pac_man_y = pac_man.pos()[1]
    for vertical_wall in vertical_walls:
        if x in vertical_wall[0]: #x coords are the same
            if y in vertical_wall[1]: #y in the range of the wall
                return True
    return False

turtle.listen()

SQUARE_SIZE = 2

food = turtle.Turtle()
food.color("white")
food.shape("square")
food.shapesize(0.2,0.2)
food.penup()
food.hideturtle()
food_stamps = []
food_pos = []
def make_food():
    y_pos_list = [-75,-25,25,75]
    min_x = -200
    max_x = 200
    space_food = 20
    for y_coord in  y_pos_list:
        for x_coord in range(min_x, max_x, space_food):
            #check if touching vert wall
            #draw food if not
            #make sure to save stamp ids and food positions
            if not check_overlap_vertical(x_coord,y_coord):
                food.goto(x_coord,y_coord)
                food_pos.append((x_coord,y_coord))
    
                foo = food.stamp()
                print("special stamp", foo)
                food_stamps.append(foo)
                print("appended", food_stamps)           

def eat_food():
    test = False
    for piece_food in food_pos:
        if piece_food[0]-12 < pac_man.pos()[0] < piece_food[0]+12:
            if piece_food[1]-12 < pac_man.pos()[1] < piece_food[1]+12:
                test = True
                position = piece_food
    if test:
        print(food_pos, food_stamps)
        food_ind=food_pos.index(position) #What does this do?
        print(food_ind)
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind)#Remove eaten food stamp
        print("You have eaten the food!")
    


def move_pac_man():
    global all_walls
    my_pos = pac_man.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    #if direction==RIGHT and not check_overlap_vertical() :
    if direction==RIGHT: 
        #pac_man.goto(x_pos + SQUARE_SIZE, y_pos)
        #print("You moved right!")
        new_x = x_pos + SQUARE_SIZE
        new_y = y_pos
    #elif direction==LEFT and not check_overlap_vertical():
    elif direction==LEFT:
        #pac_man.goto(x_pos - SQUARE_SIZE, y_pos)
        #print("You moved left!")
        new_x = x_pos - SQUARE_SIZE
        new_y = y_pos
    #elif direction==UP and not check_overlap_horizontal():
    elif direction==UP:
        #pac_man.goto(x_pos,y_pos + SQUARE_SIZE)
        #print("You moved up!")
        new_x = x_pos
        new_y = y_pos + SQUARE_SIZE
        
    #elif direction==DOWN and not check_overlap_horizontal():
    elif direction==DOWN:
        #pac_man.goto(x_pos,y_pos - SQUARE_SIZE)
        #print("You moved down!")
        new_x = x_pos
        new_y = y_pos - SQUARE_SIZE
    else:
        new_x = x_pos
        new_y = y_pos

    if not check_overlap_vertical(new_x,new_y) and not check_overlap_horizontal(new_x,new_y):
        pac_man.goto(new_x,new_y)
    eat_food()

    #check if about to hit wall
    #move the pacman
    

    #print('hitting wall: ' + str(check_overlap_horizontal()))
    #print('hitting wall: ' + str(check_overlap_vertical()))

    turtle.ontimer(move_pac_man,TIME_STEP)

ghost1 = turtle.Turtle()
ghost2 = turtle.Turtle()
ghost3 = turtle.Turtle()
ghost4 = turtle.Turtle()

ghost1.color("green")
ghost2.color("red")
ghost3.color("yellow")
ghost4.color("purple")

ghosts = [ghost1, ghost2, ghost3, ghost4]
ghosts_direction = [UP, LEFT, DOWN, RIGHT]

def generate_ghosts():
    start_x = random.randint(-200, 200)
    start_y = random.randint(-100, 100)

    while (start_x, start_y) is not check_overlap_horizantal or check_overlap_vertical :
            for ghost in ghosts :
                ghost.goto(start_x, start_y)
            
for ghost in ghosts:
    ghost.pu()
    ghost.goto(-100,20)
def move_ghosts():
    global ghosts
    for ghost in ghosts:
        move_ghost(ghost)
    turtle.ontimer(move_ghosts,TIME_STEP)
def move_ghost(ghost):
    global ghosts_direction, ghosts, all_walls
    ghost_index = ghosts.index(ghost)
    direction = ghosts_direction[ghost_index]
    my_pos = ghost.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    #if direction==RIGHT and not check_overlap_vertical() :
    if direction==RIGHT: 
        #pac_man.goto(x_pos + SQUARE_SIZE, y_pos)
        #print("You moved right!")
        new_x = x_pos + SQUARE_SIZE
        new_y = y_pos
    #elif direction==LEFT and not check_overlap_vertical():
    elif direction==LEFT:
        #pac_man.goto(x_pos - SQUARE_SIZE, y_pos)
        #print("You moved left!")
        new_x = x_pos - SQUARE_SIZE
        new_y = y_pos
    #elif direction==UP and not check_overlap_horizontal():
    elif direction==UP:
        #pac_man.goto(x_pos,y_pos + SQUARE_SIZE)
        #print("You moved up!")
        new_x = x_pos
        new_y = y_pos + SQUARE_SIZE
        
    #elif direction==DOWN and not check_overlap_horizontal():
    elif direction==DOWN:
        #pac_man.goto(x_pos,y_pos - SQUARE_SIZE)
        #print("You moved down!")
        new_x = x_pos
        new_y = y_pos - SQUARE_SIZE
    else:
        new_x = x_pos
        new_y = y_pos
        
    if check_overlap_horizontal(new_x, new_y) or check_overlap_vertical(new_x, new_y):
        ghosts_direction[ghost_index] = random.randint(UP, LEFT)

    else:
        ghost.goto(new_x, new_y)

    for ghost in ghosts:
        
        if pac_man.pos() == ghost.pos() :
            quit()

make_food()
#generate_ghosts()
move_pac_man()
move_ghosts()
turtle.mainloop()

'''changed the if statements and the checking functions, so the pac-man will be
able to move away from the walls, by making the new if statements look at the
coordinates that are infront of the pac-man, and else by making the functions
take arguments'''
test = turtle.clone()
turtle.penup()
test.goto(-100 , 100)


   



        







