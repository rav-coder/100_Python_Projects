import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key='Up', fun=player.move_up)

game_is_on = True
counter = 4
while game_is_on:
    counter += 1
    if counter % 4 == 0:
        car_manager.generate_new_car()
    time.sleep(0.1)
    car_manager.move_cars()
    screen.update()

    # collision with car
    for car in car_manager.cars:
        if car.distance(player) < 23:
            game_is_on = False
            scoreboard.game_over()

    # successful crossing
    if player.ycor() > 270:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.update_score()

screen.exitonclick()


