import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./day 25/Us state game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./day 25/Us state game/50_states.csv")
state_list = data.state.to_list()
correct_number = 0
correct_states = []


while correct_number < 50:
    answer_state = screen.textinput(title=f"{correct_number}/50 States Correct", prompt="What's another state's name?").lower()
    
    if answer_state == "exit":
        correct_number = 50
    for state in state_list:
        if answer_state == state.lower() and state not in correct_states:
            correct_number += 1
            correct_states.append(state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == state]
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            t.write(state)
