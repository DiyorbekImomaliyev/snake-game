import time
from turtle import Screen
from diyorbek import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("blue")
screen.title("My snake game")

screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

sign = True
def stop_game(_,__):
    global sign
    sign = False

n = 0
screen.onclick(stop_game)
while sign:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segs[0].distance(food)<20:
        snake.extend()
        food.refresh()
        score.score+=1
        score.update()
    if snake.segs[0].xcor()<-280 or snake.segs[0].xcor()>280 or snake.segs[0].ycor()<-280 or snake.segs[0].ycor()>280:
            score.reset()
            snake.reset()
    for each in snake.segs[1:]:
        if snake.segs[0].distance(each)<10:
            score.reset()
            snake.reset()





screen.exitonclick()
