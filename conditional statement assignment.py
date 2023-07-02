#----------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print("--------------------")
        print(key)
        for i in options[question_num-1] :
            print(i)
            guess = input("Enter (A, B, C, or D): ")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses+=check_answer(question.get(key),guess)
            question_num += 1

    display_score(correct_guesses, guesses)


#----------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
#-----------------------------
def display_score(correct_guesses, guesses):
    print("--------------------")
    print("RESULTS")
    print("---------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()
#------------------------------
def play_again():
    pass
#------------------------------


question = {
    "who created python?: ": "A",
    "what year was python created?: ": "B",
    "python is tributed to which comedy group?: ": "C",
    "Is the earth round?: ": "A"
}

options = [["A. Guido Van Rossum", "B. Mos", "C. Moslove", "D. Solomon"],
           ["A. 1998", "B. 1991", "C. 1997", "D. 2006"],
           ["A. pick", "B. Na so", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Ask me", "D. What's Earth"]]

new_game()