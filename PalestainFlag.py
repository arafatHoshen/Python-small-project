from turtle import *

setup(800,400)
speed(0)
penup()
goto(-400,200)
pendown()

#black
color("black")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#white
color("white")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#green
color("green")
begin_fill()
forward(800)
right(90)
forward(133)
right(90)
forward(800)
right(180)
end_fill()

#triangle

color("red")
begin_fill()
goto(-200,15)
left(318)
forward(-400)
end_fill()

done()