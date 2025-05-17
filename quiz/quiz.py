import random

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)
play_again_box = Rect(490, 350, 300, 100)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 558)
answer_box4.move_ip(735, 558)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10
game_over_flag = False
game_over_message = ""

q1 = ["What is the capital of France?",
      "London", "Paris", "Berlin", "Tokyo", 2]

q2 = ["What color is the sky on a clear day?",
      "red", "purple", "blue", "green", 3]

q3 = ["How many legs does a spider have?",
      "8", "6", "2", "12", 1]

q4 = ["How many days are there in a week?",
      "10", "12", "8", "7", 4]

q5 = ["What is 6+8?",
      "14", "10", "16", "18", 1]

all_questions = [q1, q2, q3, q4, q5]
questions = []
question = []

def reset_game():
    global score, time_left, questions, question, game_over_flag, game_over_message
    score = 0
    time_left = 10
    questions = all_questions.copy()
    random.shuffle(questions)
    question = questions.pop(0)
    game_over_flag = False
    game_over_message = ""

reset_game()

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    if game_over_flag:
        screen.draw.textbox(game_over_message, main_box, color="black")
        screen.draw.filled_rect(play_again_box, "green")
        screen.draw.textbox("Play Again", play_again_box, color="white")
    else:
        for box in answer_boxes:
            screen.draw.filled_rect(box, "orange")

        screen.draw.textbox(str(time_left), timer_box, color=("black"))
        screen.draw.textbox(question[0], main_box, color=("black"))

        for i, box in enumerate(answer_boxes, start=1):
            screen.draw.textbox(str(question[i]), box, color=("black"))

def game_over():
    global question, time_left, game_over_flag, game_over_message
    if not questions:
        game_over_message = "You answered all questions correctly! Final Score: %s" % str(score)
    else:
        game_over_message = "Game over. You got %s questions correct" % str(score)
    question = [game_over_message, "-", "-", "-", "-", 5]
    time_left = 0
    game_over_flag = True

def correct_answer():
    global question, score, time_left

    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions!", "You Won!")
        game_over()
    pass

def on_mouse_down(pos):
    global game_over_flag
    if game_over_flag:
        if play_again_box.collidepoint(pos):
            reset_game()
        return

    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1
    pass

def update_time_left():
    global time_left

    if not game_over_flag:
        if time_left:
            time_left = time_left - 1
        else:
            game_over()

clock.schedule_interval(update_time_left, 1.0)
