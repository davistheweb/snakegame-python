import main
import random as davis_random
import time

time_delay = 0.1
score = 0
game_high_score = 0
wn_width = 800
wn_height = 800
action = "Stop"

game_window = main.main.Screen()
game_window.title("Python snake game by Davistheweb")
game_window.bgcolor("black")
game_window.setup(width=wn_width, height=wn_height)
game_window.tracer(0)

main.main.speed(5)
main.main.pensize(4)
main.main.penup()
main.main.goto(-310, 250)
main.main.pendown()
main.main.color("black")
main.main.forward(600)
main.main.right(90)
main.main.forward(500)
main.main.right(90)
main.main.forward(500)
main.main.penup()
main.main.hideturtle()

snake_head = main.main.Turtle()
snake_head.speed(0)
snake_head.shape('square')
snake_head.color('white')
snake_head.penup()
snake_head.goto(0, 9)
snake_head.direction = action

