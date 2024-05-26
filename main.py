import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
data.set_index('state', inplace=True)
screen.tracer(0)
turtle.penup()
turtle.hideturtle()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in data.index if state not in guessed_states]
        user_missed_states = pandas.DataFrame(missing_states, columns=["states to learn"])
        user_missed_states.to_csv('states_to_learn.csv')
        break
    if answer_state in data.index:
        if answer_state not in guessed_states:
            user_state = data.loc[answer_state]
            turtle.goto(user_state)
            turtle.write(f"{answer_state}", align='center', font=('Arial', 12, 'normal'))
            guessed_states.append(answer_state)

if len(guessed_states) == 50:
    turtle.goto(0, 0)
    turtle.write("Congratulations!", align='center', font=('Arial', 20, 'normal'))
