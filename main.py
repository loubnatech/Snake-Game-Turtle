from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from score import Score
window=Screen()
window.setup(width=1000, height=600, startx=0, starty=0)
window.bgcolor("black")
window.tracer(0)
snake=Snake()
food=Food()
score=Score()

game_on=True
while game_on:
    snake.move_snake()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake.move_up,"Up")
    window.onkey(snake.move_down,"Down")
    window.onkey(snake.move_right,"Right")
    window.onkey(snake.move_left,"Left")
    if snake.head.distance(food)<15:
        food.dispaly_random()
        snake.extend()
        score.score_raise()
    if snake.head.xcor()>470 or snake.head.xcor()< -470 or snake.head.ycor()>270 or snake.head.ycor()< -270:
        game_on=False
        score.game_over()
    for pieces in snake.turtles[:-1]:
        if snake.head.distance(pieces)<10:
            game_on=False
            score.game_over()



window.exitonclick()
