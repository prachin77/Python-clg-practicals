import time

class Quiz:
    def __init__(self, questions, answers):
        self.questions = questions
        self.answers = answers
        self.start_time = 0
        self.end_time = 0
        
    def start_quiz(self):
        print("Quiz started!")
        self.start_time = time.time()

    def end_quiz(self):
        self.end_time = time.time()
        print("Quiz ended!")

    def generate_quiz(self):
        for i, question in enumerate(self.questions):
            print(f"Question {i + 1}: {question}")
            user_answer = input("Your answer: ")
            self.check_answer(i, user_answer)
            
    def check_answer(self, index, user_answer):
        correct_answer = self.answers[index]

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
        else:
            print(f"Wrong! Correct answer is: {correct_answer}")
            
    def get_time_spent(self):
        return self.end_time - self.start_time

# Example usage
questions_list = [
    "What is the capital of France?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the largest mammal in the world?",
    "What is the formula for water?",
    "Who is known as the 'Father of Computer Science'?"
]

answers_list = [
    "Paris",
    "William Shakespeare",
    "Blue Whale",
    "H2O",
    "Alan Turing"
]

quiz = Quiz(questions_list, answers_list)
quiz.start_quiz()
quiz.generate_quiz()
quiz.end_quiz()

time_spent = quiz.get_time_spent()
print(f"Time spent on the quiz: {time_spent} seconds")



