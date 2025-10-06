

list_of_questions = [
    "Vad heter huvudstaden i Sverige?",
    "Hur många ben har en spindel?",
    "Vilken planet är närmast solen?",
    "Vem skapade Python-programmeringsspråket?",
    "Vilket år startade andra världskriget?"
]

right_answers = [
    "Stockholm",
    "8",
    "Merkurius",
    "Guido van Rossum",
    "1939"
]

amount_of_questions = len(list_of_questions)
high_score = 0


while True:
    points = 0

    for q in range(amount_of_questions):
        print(list_of_questions[q])
        answer = input('Answer here:\t')
        if answer.title() == right_answers[q]:
            points += 1
            print(f'Right answer: {answer}')
        else:
            print(f'Wrong answer: {answer}')
    print(f'You got {points} points of {amount_of_questions}')
    break
