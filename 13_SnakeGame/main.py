
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
running = True

snake = Snake(3)
food = Food()
sb = ScoreBoard()
screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")

while running:
    screen.update()
    time.sleep(0.12)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        sb.update_score()
        snake.extend_snake()
        food.new_food()

    # collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 295 or x_cor < -295 or y_cor > 295 or y_cor < -295:
        sb.game_over()
        running = False

    # collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            sb.game_over()
            running = False

screen.exitonclick()
