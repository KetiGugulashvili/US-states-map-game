import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Map Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_coor = data["x"].to_list()
y_coor = data["y"].to_list()

answers = []

while len(answers) < len(states):
    answer_state = screen.textinput(title=f"{len(answers)}/{len(states)} states correct", prompt="What's another state name?")
    if answer_state == "exit":
        diff = list(set(states) - set(answers))
        print(diff)
        break

    if answer_state.title() in states:
        if answer_state.title() not in answers:
            answers.append(answer_state.title())

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            index = states.index(answer_state.title())
            t.goto(int(x_coor[index]), int(y_coor[index]))
            t.write(answer_state)

screen.exitonclick()