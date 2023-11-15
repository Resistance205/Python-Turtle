from turtle import *


bgcolor("cyan")

circle(200)
penup()
left(90)
forward(100)
left(90)
forward(30)
right(180)
pendown()
#Step one
#Balls
color("pink")
begin_fill()


circle(50)
forward(100)
circle(50)
end_fill()

color("blue")
#shaft up
begin_fill()
left(90)
forward(250)

#shaft tip across
left(90)
forward(90)

#shaft tip down
left(90)
forward(250)
#works before this point
end_fill()


#back up
left(90)
forward(90)
left(90)
forward(250)







#tip
color("pink")
begin_fill()
circle(45)
left(90)
forward(90)
end_fill()



# #background circle
# left(90)

# forward(90)
# left(90)

done()
