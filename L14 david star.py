import turtle #importing turtle

paper = turtle.Screen()# make the paper
paper.bgcolor("cyan") # Set the paper background color
paper.setup(500,500)# width = 300 height = 400
paper.title("Star of David")

pen = turtle.Turtle()# make the pen

#First triangle for star
pen.down()
pen.forward(100)#Draw base

pen.left(120)
pen.forward(100)

pen.left(120)
pen.forward(100)

#Change the position of pen
pen.up()
pen.right(150)
pen.forward(50)

#Second triangle for star
pen.pendown()
pen.right(90)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.forward(100)

turtle.done()