from turtle import *
from snake import Snake
import time

#screen game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

#making snake object
snake = Snake(length=10)

# Keyboard bindings
screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.right, 'Right')

# game loop 
game = True
try:
    while game:
        time.sleep(0.05)
        if snake.alive:
            snake.movement()
            screen.update()
except Terminator:
    print("Window closed")


screen.exitonclick()
