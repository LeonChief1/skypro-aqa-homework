from turtle import *

# Создание черепашки
my_turtle = Turtle()
my_turtle.speed(3)
my_turtle.screen.setup(1200, 800)

# Функция для рисования круга
def draw_circle(t, radius, color):
    t.begin_fill()
    t.color(color)
    t.circle(radius)
    t.end_fill()

# Рисование головы
my_turtle.penup()
my_turtle.goto(0, -50)
my_turtle.pendown()
draw_circle(my_turtle, 50, "gray")

# Рисование глаз
my_turtle.penup()
my_turtle.goto(-20, 10)
my_turtle.pendown()
draw_circle(my_turtle, 10, "white")

my_turtle.penup()
my_turtle.goto(20, 10)
my_turtle.pendown()
draw_circle(my_turtle, 10, "white")

# Зрачки
my_turtle.penup()
my_turtle.goto(-20, 15)
my_turtle.pendown()
draw_circle(my_turtle, 5, "black")

my_turtle.penup()
my_turtle.goto(20, 15)
my_turtle.pendown()
draw_circle(my_turtle, 5, "black")

# Нос
my_turtle.penup()
my_turtle.goto(0, 0)
my_turtle.pendown()
draw_circle(my_turtle, 5, "pink")

# Рот
my_turtle.penup()
my_turtle.goto(-10, -10)
my_turtle.pendown()
my_turtle.right(90)
my_turtle.circle(10, 180)
my_turtle.penup()
my_turtle.goto(10, -10)
my_turtle.pendown()
my_turtle.circle(10, 180)

# Уши
my_turtle.penup()
my_turtle.goto(-35, 35)
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.color("gray")
my_turtle.goto(-55, 75)
my_turtle.goto(-15, 75)
my_turtle.goto(-35, 35)
my_turtle.end_fill()

my_turtle.penup()
my_turtle.goto(35, 35)
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.color("gray")
my_turtle.goto(55, 75)
my_turtle.goto(15, 75)
my_turtle.goto(35, 35)
my_turtle.end_fill()

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()