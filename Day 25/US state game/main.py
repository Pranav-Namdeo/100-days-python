import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./day 25/Us state game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
print(answer_state)

data = pandas.read_csv("./day 25/Us state game/50_states.csv")
