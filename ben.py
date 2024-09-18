import random
number = random.randint (1,12)
x=0
print ("lets go gambling!")
import time
time.sleep(0.5)
print("CHK")
time.sleep(0.5)
print("CHK")
time.sleep(0.5)
print("CHK")
time.sleep(0.5)
print(number)
if number<4:
    print ("you win!") 
else: print("aw dang it!")
import turtle
t = turtle.Turtle()
painter = turtle.Turtle()
painter2 = turtle.Turtle()
painter3 = turtle.Turtle()



if number<4:
    t.speed(1)
    club_size = 25
    t.penup()
    t.goto(0, 60)
    t.forward(club_size * (2 ** (1/2)))
    t.left(135)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.forward(club_size * 2)
    t.left(90)
    t.forward(club_size * 2)
    t.circle(club_size, 180)
    t.right(90)
    t.circle(club_size, 180)
    t.penup()
    t.left(90)
    t.forward(club_size * 2)
    t.left(45)
    t.pendown()
    t.circle(club_size * 1.3, 45)
    t.right(135)
    t.forward(club_size * .75)
    t.right(135)
    t.circle(club_size * 1.3, 45)
    t.end_fill()
    t.ht()
    painter.write("YOU WIN!!!", False, 'center', font = ('Candara', 50, 'bold')
else: 

    painter2.write("YOU LOSE!!!", False, 'center', font= ('Candara', 50, 'bold'))
    ## you need to win if you want to see the cool thing
    
















wn = turtle.Screen()
wn.mainloop()
