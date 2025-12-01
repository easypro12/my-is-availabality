import random

def flash_quiz_app():
    questions = {
        "What is the capital of France?": {
            "a": "Paris",
            "b": "London",
            "c": "Bayern",
            "answer": "a"
        },
        "Which year did Nigeria receive independence?": {
            "a": "1950",
            "b": "1980",
            "c": "1960",
            "answer": "c"
        },
        "Which year did Ghana receive independence?": {
            "a": "1957",
            "b": "1970",
            "c": "1990",
            "answer": "a"
        }
    }

    while True:
        # pick random question
        question = random.choice(list(questions.keys()))
        options = questions[question]

        print("\nHISTORY QUIZ CLASS\n")
        print(question)
        print(f"a. {options['a']}")
        print(f"b. {options['b']}")
        print(f"c. {options['c']}")

        user_answer = input("\nEnter your answer (a/b/c): ").lower()

        if user_answer == options["answer"]:
            print("Correct!")
        else:
            print("Incorrect")
            print(f"The correct answer is: {options['answer']}. {options[options['answer']]}")

        # ask if user wants next question
        next_question = input("\nEnter next question (yes/no): ").lower()

        if next_question != "yes":
            print("Thanks for playing!")
            break
flash_quiz_app()
