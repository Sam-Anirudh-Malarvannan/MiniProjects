from abc import ABC, abstractmethod


# Abstraction - Abstract Base Class
class QuizComponent(ABC):
    @abstractmethod
    def display(self):
        pass


# Question Class with Encapsulation
class Question(QuizComponent):
    def __init__(self, text, answer):
        self.__text = text
        self.__answer = answer

    @property
    def text(self):
        return self.__text

    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.__answer.lower()

    def display(self):
        print(f"Question: {self.__text}")


# Inheritance - Quiz class Inherits Component
class Quiz(QuizComponent):
    def __init__(self):
        self.questions = []  # List to hold Question objects

    def load_questions_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if ',' in line:
                        text, answer = line.strip().split(',', 1)
                        self.questions.append(Question(text, answer))
        except FileNotFoundError:
            print('Question file not found.')

    def add_question_to_file(self, filename, text, answer):
        with open(filename, 'a') as file:
            file.write(f"{text},{answer}\n")  # Removed extra space after comma

    def start_quiz(self):
        score = 0
        for q in self.questions:
            q.display()
            user_answer = input("Answer: ")
            if q.check_answer(user_answer):
                print("\nCorrect Answer!\n")
                score += 1
            else:
                print(f"Wrong Answer! The Correct Answer is: {q._Question__answer}\n")

        print(f"Your Final Score: {score}/{len(self.questions)}\n")

    def display(self):
        print(f"\nTotal Questions Loaded: {len(self.questions)}\n")
