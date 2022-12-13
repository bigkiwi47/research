# I found this code very interesting as it was nothing like what we had practiced thus far in our course
# The use of turtle is quite a new concept to me, but it seems like could be useful for making low level .gifs etc.
# I don't understand how a lot of concepts in this code work (e.g fillcolor)
# I'm quite inspired by the concept of turtle and want to delve in to more of these sorts of features python holds
import turtle

t = turtle.Turtle()

t.color("red")
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90, 200)
# left (120)

t.setheading(60)
t.circle(-90, 200)
t.forward(180)
t.end_fill()
a = input()
