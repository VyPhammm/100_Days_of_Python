import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = r"Day25_Pandas\us-states-game-start\us-states-game-start\blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def write_result(result,position):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(position)
    t.write(f"{result}", align= "center", font= ("Arial", 10, "normal"))

data = pd.read_csv(r"Day25_Pandas\us-states-game-start\us-states-game-start\50_states.csv")
all_states = data.state.to_list()


score = 0
game_is_on = True
guessed_states = []
while game_is_on:
    answer_state = screen.textinput(title= f"{score}/50 Guess the State", prompt="What's another state's name? ").title()

    if answer_state in all_states :
        score += 1
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        position = (int(state_data.x), int(state_data.y))
        write_result(result= answer_state, position= position)

        

    if score == 50 :
        game_is_on = False
        print("You Won")

    if answer_state == "Exit" :
        game_is_on = False
        missing_states = []
        for state in all_states :
            if state not in guessed_states :
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(r"Day25_Pandas\us-states-game-start\us-states-game-start\States_to_learn.csv")








turtle.mainloop()


