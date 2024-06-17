from question_model import Question 
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Create a list of Question objects
for question in question_data:
    # The value of text will be assigned to question_text 
    question_text = question["text"]
    # The value of answer will be assigned to question_answer
    question_answer = question["answer"]
    # Create a new Question object with question_text and question_answer
    new_question = Question(question_text, question_answer)
    # Use the append function to add new_question to the question_bank
    question_bank.append(new_question)

# Create a QuizBrain object with the question_bank
quiz = QuizBrain(question_bank)

# Run the next question while there are still questions left
while quiz.still_has_questions():
    quiz.next_question()

# Display the final score after completing the quiz
print("Hooray! You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
print("\n")
