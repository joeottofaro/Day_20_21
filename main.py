from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Turtle()
snake.color("white")
snake.shape("square")
snake_body_size = -3
snake.shapesize(stretch_len=snake_body_size)



screen.exitonclick()