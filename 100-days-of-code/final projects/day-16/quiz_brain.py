class QuizBrain:
    def __init__(self, qst_list):
        # Initialize the question number to 0
        self.qst_number = 0
        # Initialize the score to 0
        self.score = 0
        # Initialize the question list with the provided input
        self.question_list = qst_list
    
    def still_has_questions(self):
        # Check if there are still questions left in the list
        return self.qst_number < len(self.question_list)

    # Method to retrieve the item at the current question number from the question list
    # Use the input() function to show the user the Question text and ask for the user's answer
    def next_question(self):
        # Locate the current question using the question number in the question list
        current_question = self.question_list[self.qst_number]
        # Increment the question number for the next question
        self.qst_number += 1
        # Display the question number and the question text, and get the user's answer
        user_answer = input(f"Q.{self.qst_number}: {current_question.text} (True/False): ")
        # Check the correct answer and compare it with the user's answer
        self.check_answer(user_answer, current_question.answer)

    # Method to check the user's answer against the correct answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            # If the answer is correct, increment the score
            self.score += 1
            print("You got it right!")
        else:
            # If the answer is incorrect, print that it is wrong
            print("That's wrong.")

        # Display the correct answer
        print(f"The correct answer was: {correct_answer}.")
        # Display the current score
        print(f"Your current score is: {self.score}/{self.qst_number}")
        print("\n")
