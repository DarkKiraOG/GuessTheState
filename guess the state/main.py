import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

entered_states = []
#CHECK THE ANSWER
def check_answer():
    with open("50_states.csv", mode= "r") as states:
        lines = states.readlines()
        for line in lines:
            state = line.split(",")[0].lower()
            if answer_state.lower() == state and answer_state.lower() not in entered_states:

                entered_states.append(answer_state.lower())
                display(line.split(",")[0])



def display(name):
    Head = turtle.Turtle()
    Head.hideturtle()
    Head.penup()
    Head.color("black")

# IMPROVEMENT NEEDED:
#Start
    data = pandas.read_csv("50_states.csv")
    ans = data[data.state == name]
    dict_ans = ans.to_dict()
    list_ans = list(dict_ans.items())
    last_dict_x = list_ans[1][1]
    x = list(last_dict_x.items())[0][1]
    print(x)
    last_dict_x = list_ans[2][1]
    y = list(last_dict_x.items())[0][1]
    print(y)
#End
    Head.goto(x, y)
    Head.write(f"{name}", align='center', font= ('Courier', 7, 'normal'))


game = True
while game:
    answer_state = screen.textinput(title= "Guess The State", prompt=f"Enter Name Of State:               "
                                                                     f"{len(entered_states)}/50  ")
    x = check_answer()
    if len(entered_states) == 50:
        print("CONGRATULATIONS, YOU NAMED ALL THE STATES")
        game = False


