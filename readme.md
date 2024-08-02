# Boring snake game 


```python
import turtle
import random as rdm
import time as t

time_delay = 0.1
score = 0
game_high_score = 0
wn_width = 700
wn_height = 700
action = "Stop"
game_title = "Python snake game by Davistheweb"

game_window = turtle.Screen()
game_window.title(game_title)
game_window.bgcolor("black")
game_window.setup(width=wn_width, height=wn_height)
game_window.tracer(0)

turtle.speed(5)
turtle.pensize(10)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.penup()
turtle.hideturtle()

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape('square')
snake_head.color('white')
snake_head.penup()
snake_head.goto(0, 9)
snake_head.direction = action

snake_food = turtle.Turtle()
snake_food_color = rdm.choice(['yellow', 'green', 'tomato', 'red', 'brown'])
snake_food_shape = rdm.choice(['triangle', 'circle', 'square'])
snake_food.speed(0)
snake_food.color(snake_food_color)
snake_food.shape(snake_food_shape)
snake_food.penup()
snake_food.goto(20, 20)

game_score_board = turtle.Turtle()
game_score_board.speed(0)
game_score_board.shape('square')
game_score_board.color('white')
game_score_board.penup()
game_score_board.hideturtle()
game_score_board.goto(0, 270)
game_score_board.write("Player-Score : 0 High Score : 0", align='center', font=("Serif", 25, "bold"))


def snake_move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def snake_move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def snake_move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def snake_move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def snake_move():
    if snake_head.direction == "up":
        yaxis = snake_head.ycor()
        snake_head.sety(yaxis + 20)

    if snake_head.direction == "down":
        yaxis = snake_head.ycor()
        snake_head.sety(yaxis - 20)

    if snake_head.direction == "left":
        x_axis = snake_head.xcor()
        snake_head.setx(x_axis - 20)

    if snake_head.direction == "right":
        x_axis = snake_head.xcor()
        snake_head.setx(x_axis + 20)


game_window.listen()

game_window.onkeypress(snake_move_up, "Up")
game_window.onkeypress(snake_move_down, "Down")
game_window.onkeypress(snake_move_left, "Left")
game_window.onkeypress(snake_move_right, "Right")

segments = []

while True:
    game_window.update()

    if snake_head.xcor() > 280 or snake_head.xcor() < -300 or snake_head.ycor() > 240 or snake_head.ycor() < -240:
        t.sleep(1)
        game_window.clear()
        game_window.bgcolor('blue')
        game_score_board.goto(0, 0)
        game_score_board.write(f"Game Over\n Your Score is : {score}", align='center', font=("Serif", 30, "bold"))

    if snake_head.distance(snake_food) < 20:
        score += 5
        if score > game_high_score:
            game_high_score = score

        game_score_board.clear()
        game_score_board.write(f"Score : {score} High Score: {game_high_score}",
                               align="center", font=("Arial", 25, "bold"))

        x_cord = rdm.randint(-290, 270)
        y_cord = rdm.randint(-240, 240)
        snake_food_color = rdm.choice(['yellow', 'green', 'tomato'])
        snake_food_shape = rdm.choice(['triangle', 'circle', 'square'])
        snake_food.speed(0)
        snake_food.shape(snake_food_shape)
        snake_food.color(snake_food_color)
        snake_food.goto(x_cord, y_cord)

        snake_new_segment = turtle.Turtle()
        snake_new_segment.speed(0)
        snake_new_segment.shape('square')
        snake_new_segment.color("white smoke")
        snake_new_segment.penup()
        segments.append(snake_new_segment)

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)

    snake_move()

    for segment in segments:
        if segment.distance(snake_head) < 20:
            t.sleep(1)
            game_window.clear()
            game_window.bgcolor('blue')
            game_score_board.goto(0, 0)
            game_score_board.write(f"\t\t GAME OVER\n Your score is : {score}",
                                   align="center", font=("Arial", 10, 'bold'))

    t.sleep(time_delay)

    turtle.Terminator()
```