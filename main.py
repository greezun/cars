import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()


screen.listen()
screen.onkey(player.move_player, "Up")
time_sleep = 0.1

cars = []
count = 0
speed = 5

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(time_sleep)
    count += 1
    if count == 6:
        new_car = CarManager()
        cars.append(new_car)
        count = 0
    for car in cars:
        car.run_car(speed)
        print(car.run_speed)
        if car.xcor() < -320:
            cars.remove(car)

        if player.ycor() > 280:
            scoreboard.score += 1
            scoreboard.print_score()
            player.start()
            speed +=10

        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()







screen.exitonclick()
