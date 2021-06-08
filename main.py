s# Este módulo permite extraer colores de una imagen dada
import turtle
import colorgram,random
from turtle import Turtle,Screen

coloresObj = colorgram.extract("image.jpg", 10)
colores = []
for color in coloresObj:
    colores.append((color.rgb.r,color.rgb.g,color.rgb.b))

colores.sort()

turtle.colormode(255)
manuelita = Turtle()
manuelita.hideturtle()
manuelita.shape("turtle")
manuelita.pensize(15)

manuelita.penup()
manuelita.left(180)
manuelita.forward(150)
manuelita.left(90)
manuelita.forward(200)
manuelita.left(90)
manuelita.pendown()
numero_de_puntos = 101
manuelita.speed(0)

for contador_Puntos in range(1,numero_de_puntos):
    color = random.choice(colores)
    manuelita.dot(15,color)
    manuelita.penup()
    manuelita.forward(50)
    manuelita.pendown()

    if contador_Puntos % 10 == 0:
        manuelita.setheading(90)
        manuelita.penup()
        manuelita.forward(50)
        manuelita.setheading(180)
        manuelita.forward(500)
        manuelita.setheading(0)
        manuelita.pendown()


mi_pantalla = Screen()
mi_pantalla.exitonclick()