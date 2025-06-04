import turtle #importing library

paper = turtle.Screen() #make the paper or the screen
paper.bgcolor("light blue") #Set the paper background color
paper.title("Turtle")

pen = turtle.Turtle()#make the pen
size =  0 

while True:
    for i in range(4):
        pen.forward(size+1)
        pen.left(90)
        size = size - 5

    size = size +1