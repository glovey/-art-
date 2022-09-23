from random import randint
from random import choice
import turtle as t
import colorgram


tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tim.speed("fastest")
tim.up()
tim.hideturtle()
colours = colorgram.extract("images.jpg", 50)


grid = 10
dot = 20  



x = -200
y = -100

tim.setpos(x,y)
spacing = 50

for num in range(grid):
  
  for num in range(grid):
    
    tim.dot(dot,choice(colours).rgb)
    tim.forward(spacing)
    

  
  y = y + spacing
  tim.setpos(x,y)
  

 


  






screen.exitonclick()