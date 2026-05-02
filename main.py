# from turtle import Turtle, Screen
# import random
#
# # tim = Turtle()
# screen = Screen()
# screen.colormode(255)
# #
# # colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'cyan']
#
# # for numside in range(3, 8):
# #     angle = 360 / numside
# #     for i in range(numside):
# #         tim.forward(100)
# #         tim.right(angle)
#
# # dir = [0, 90, 180, 270]
# # tim.width(5)
# # tim.speed("fastest")
# #
# # def random_color():
# #     r = random.randint(0, 255)
# #     g = random.randint(0, 255)
# #     b = random.randint(0, 255)
# #     random_col = (r, g, b)
# #     return random_col
#
# # for i in range(0, 100):
# #     tim.color(random_color())
# #     tim.forward(30)
# #     tim.setheading(random.choice(dir))
# # tim.color(random.choice(colors))
# # size = 10
# # for _ in range(int(360 / size)):
# #     tim.color(random_color())
# #     tim.circle(100)
# #     tim.setheading(tim.heading() + size)
#
# # timmy_the_turtle.shape("turtle")
# #
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.left(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.left(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.left(90)
# # timmy_the_turtle.forward(100)
# #
# # screen = Screen()
# # screen.exitonclick()
#
# # import heroes
# # heroes = heroes.gen()
# # print(heroes)
#
# import colorgram as cg
#
# color_list = cg.extract("images.jpg", 30)
# color_palette = []
#
# for count in range(len(color_list)):
#     rgb = color_list[count]
#     color = rgb.rgb
#     color_palette.append(color)
#
# tim = Turtle()
# i=0
# tim.penup()
# tim.setheading(255)
# tim.forward(300)
# tim.setheading(0)
# num_of_dot = 100
#
# for dot in range(1, num_of_dot + 1):
#     color = random.choice(color_palette)
#     tim.dot(20, (color.r, color.g, color.b))
#     tim.forward(50)
#     if dot % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

# my_list = [10, 20, 30, 40, 50]
# for i in range(len(my_list)):
#     print(i)
#     print(my_list[i])

# new = [i*2 for i in range(1,5) if i == 2]
# print(new)

# import tkinter
# window = tkinter.Tk()
# window.title("Phonetic")
# window.minsize(400, 400)
#
# def mile_to_km():
#     re = int(entry.get()) * 1.60934
#     label1.config(text=re)
#
# label = tkinter.Label(window, text="Enter Mile: ")
# label.grid(row=0, column=0)
# entry = tkinter.Entry(width=30)
# entry.grid(row=0, column=1)
#
# button = tkinter.Button(text="convert", command=mile_to_km)
# button.grid(row=0, column=2)
#
# label1 = tkinter.Label()
# label1.grid(row=1, column=0)
#
# window.mainloop()

# def add(*args):
#     for n in args:
#         print(n)
#
# add(4,5,6)
#
# def calculate(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(f'{k} = {v}')
#
# calculate(add= 3, mul= 5)

import requests
res = requests.get(url="http://api.open-notify.org/iss-now.json")
res.raise_for_status()
jss = res.json()
print(jss["iss_position"]["longitude"])
print(jss["iss_position"]["latitude"])