import turtle
turtle.speed(999999999999999999999999999999999999999999999999)
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()
turtle.goto(300,100)
turtle.penup()
turtle.goto(-100,300)
turtle.goto(-100,300)
turtle.pendown()
turtle.goto(-100,-300)
turtle.penup()
turtle.goto(100,300)
turtle.pendown()
turtle.goto(100,-300)
turtle.penup()
turtle.goto(-300,-100)
turtle.pendown()
turtle.goto(300,-100)

x_pos = []
o_pos = []



turtle.register_shape("1.gif")
num_1=turtle.clone()
num_1.shape('1.gif')
num_1.penup()
num_1.goto(-200,200)
num_1.pendown()



turtle.register_shape("2.gif")
num_2=turtle.clone()
num_2.shape('2.gif')
num_2.penup()
num_2.goto(0,200)
num_2.pendown()


turtle.register_shape("3.gif")
num_3=turtle.clone()
num_3.shape('3.gif')
num_3.penup()
num_3.goto(200,200)
num_3.pendown()

turtle.register_shape("4.gif")
num_4=turtle.clone()
num_4.shape('4.gif')
num_4.penup()
num_4.goto(-200,0)
num_4.pendown()

turtle.register_shape("5.gif")
num_5=turtle.clone()
num_5.shape('5.gif')
num_5.penup()
num_5.goto(0,0)
num_5.pendown()


turtle.register_shape("6.gif")
num_6=turtle.clone()
num_6.shape('6.gif')
num_6.penup()
num_6.goto(200,0)
num_6.pendown()


turtle.register_shape("7.gif")
num_7=turtle.clone()
num_7.shape('7.gif')
num_7.penup()
num_7.goto(-200,-200)
num_7.pendown()


turtle.register_shape("8.gif")
num_8=turtle.clone()
num_8.shape('8.gif')
num_8.penup()
num_8.goto(0, -200)
num_8.pendown()


turtle.register_shape("9.gif")
num_9=turtle.clone()
num_9.shape('9.gif')
num_9.penup()
num_9.goto(200,-200)
num_9.pendown()


turtle.register_shape("recycle.gif")
x=turtle.clone()
x.shape('recycle.gif')
x.hideturtle()

turtle.register_shape("trash.gif")
o=turtle.clone()
o.shape('trash.gif')
o.hideturtle()




def num1():
    x.penup()
    x.goto(-200,200)
    x.pendown()
    x.stamp()
    xpos_1=x.pos()
    x_pos.append(xpos_1)
    winning()

def num2():
    x.penup()
    x.goto(0,200)
    x.pendown()
    x.stamp()
    xpos_2=x.pos()
    x_pos.append(xpos_2)
    winning()

def num3():
    x.penup()
    x.goto(200,200)
    x.pendown()
    x.stamp()
    xpos_3=x.pos()
    x_pos.append(xpos_3)
    winning()


def num4():
    x.penup()
    x.goto(-200,0)
    x.pendown()
    x.stamp()
    xpos_4=x.pos()
    x_pos.append(xpos_4)
    winning()


def num5():
    x.penup()
    x.goto(0,0)
    x.pendown()
    x.stamp()
    xpos_5=x.pos()
    x_pos.append(xpos_5)
    winning()

def num6():
    x.penup()
    x.goto(200, 0)
    x.pendown()
    x.stamp()
    xpos_6=x.pos()
    x_pos.append(xpos_6)
    winning()

def num7():
    x.penup()
    x.goto(-200,-200)
    x.pendown()
    x.stamp()
    xpos_7=x.pos()
    x_pos.append(xpos_7)
    winning()

def num8():
    x.penup()
    x.goto(0,-200)
    x.pendown()
    x.stamp()
    xpos_8=x.pos()
    x_pos.append(xpos_8)
    winning()

def num9():
    x.penup()
    x.goto(200,-200)
    x.pendown()
    x.stamp()
    xpos_9=x.pos()
    x_pos.append(xpos_9)
    winning()
    


def winning():
    print(x_pos)
    if (-200 ,200) in x_pos and (0, 200) in x_pos and (200,200) in x_pos :
        print('x won!')
        quit()
        
    elif (-200,0) in x_pos and (0,0) in x_pos and (200,0) in x_pos:
        print('x won!')
        quit()

    elif (-200, -200) in x_pos and (0, -200) in x_pos and (200, -200) in x_pos:
        print('x won!')
        quit()

    elif (-200 ,200) in x_pos and (-200, 0) in x_pos and (-200, -200) in x_pos:
        print('x won!')
        quit()

    elif (0 ,200)  in x_pos and  (0, 0) in x_pos and (0, -200) in x_pos:
        print('x won!')
        quit()
    
    elif(200 ,200)  in x_pos and (200, 0) in x_pos and (200, -200) in x_pos:
        print('x won!')
        quit()

    elif (-200 ,200) in x_pos and (0, 0)  in x_pos and (200, -200) in x_pos:
        print('x won!')
        quit()

    elif (-200 , -200)  in x_pos and (0, 0) in x_pos and (200, 200) in x_pos :
        print('x won!')
        quit()


##player1 = o
##player2 = x
##
##counter = 0
##press_key
##counter+=1
##
##if counter %2==0:
##    player1
##else:
##    player2





def num1():
    o.penup()
    o.goto(-200,200)
    o.pendown()
    o.stamp()
    opos_1=o.pos()
    o_pos.append(opos_1)
    winning_2()


def num2():
    o.penup()
    o.goto(0,200)
    o.pendown()
    o.stamp()
    opos_1=x.pos()
    o_pos.append(opos_1)
    winning_2()



def num3():
    o.penup()
    o.goto(200,200)
    o.pendown()
    o.stamp()
    opos_1=x.pos()
    o_pos.append(opos_1)
    winning_2()



def num4():
    o.penup()
    o.goto(-200,0)
    o.pendown()
    o.stamp()
    winning_2()



def num5():
    o.penup()
    o.goto(0,0)
    o.pendown()
    o.stamp()
    winning_2()


def num6():
    o.penup()
    o.goto(200, 0)
    o.pendown()
    o.stamp()
    winning_2()


def num7():
    o.penup()
    o.goto(-200,-200)
    o.pendown()
    o.stamp()
    winning_2()


def num8():
    o.penup()
    o.goto(0,-200)
    o.pendown()
    o.stamp()
    winning_2()


def num9():
    o.penup()
    o.goto(200,-200)
    o.pendown()
    o.stamp()
    winning_2()


def winning_2():
    print(o_pos)
    if (-200,200) in o_pos  and (0,200) in o_pos  and (200,200) in o_pos:
        print('o  won!')
        quit()

    elif (-200,200) in o_pos and (-200,0) in o_pos and (-200,-200) in o_pos:
        print('o won!')
        quit()

    elif (-200,-200) in o_pos and (0,-200) in o_pos and (200,-200) in o_pos:
        print('o won!')
        quit()

    elif (200,200) in o_pos and (200,0) in o_pos and (200,-200) in o_pos:
        print('o won!')
        quit()

    elif (-200,200) in o_pos and (0,0) in o_pos and (200,-200) in o_pos:
        print('o won!')
        quit()

    elif (200,200) in o_pos and (0,0) in o_pos and (-200,-200) in o_pos:
        print('o won!')
        quit()

    elif  (0,200) in o_pos and (0,0) in o_pos and (0,-200) in o_pos:
        print('o  won!')
        quit()



    
turtle.onkeypress(num1,'1')
turtle.onkeypress(num2,'2')
turtle.onkeypress(num3,'3')
turtle.onkeypress(num4,'4')
turtle.onkeypress(num5,'5')
turtle.onkeypress(num6,'6')
turtle.onkeypress(num7,'7')
turtle.onkeypress(num8,'8')
turtle.onkeypress(num9,'9')


turtle.listen()



turtle.mainloop


