from quiz import Quiz

quiz = Quiz()
filename = 'question.txt'

while True:
    print("\n--- Quiz Application ---")
    print("1) Load Questions From The File")
    print("2) Start The Quiz")
    print("3) Add Questions To File")
    print("4) Show Total Questions")
    print("5) Exit")

    choice = input("Select Option: ")

    if choice == '1':
        quiz.load_questions_from_file(filename)
        print("Questions Loaded Successfully.")

    elif choice == '2':
        if not quiz.questions:
            print("No Questions Loaded. Please Load First.")
        else:
            quiz.start_quiz()

    elif choice == '3':
        text = input("Enter Question: ")
        answer = input("Enter Correct Answer: ")
        quiz.add_question_to_file(filename, text, answer)
        print("Question Added Successfully.")

    elif choice == '4':
        quiz.display()

    elif choice == '5':
        print("Exiting Program.")
        break

    else:
        print("Invalid Choice. Try Again.")
