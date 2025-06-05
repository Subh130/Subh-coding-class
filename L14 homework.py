import turtle #importing library

paper = turtle.Screen() #make the paper or the screen
paper.bgcolor("purple") #Set the paper background color
paper.title("Turtle")

pen = turtle.Turtle()#make the pen

for i in range(361):
    pen.forward(1)
    pen.right(1)

pen.color("blue")

pen.up()
pen.forward(50)
pen.left(50)

pen.down()
pen.forward(90)
pen.left(90)

pen.forward(90)
pen.left(90)

pen.forward(90)
pen.left(90)

pen.forward(90)
pen.left(90)

pen.up()
pen.right(100)
pen.forward(50)

pen.down()
pen.color("yellow")
pen.fillcolor("blue")

num_sides = 5
side_length = 50
angle = 360 / num_sides
pen.begin_fill()
for i in range(num_sides):
    pen.forward(side_length)
    pen.left(angle)
pen.end_fill()

pen.up()
pen.forward(100)

pen.down()
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.forward(100)
turtle.done()
