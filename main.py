# # var = Input
# question1 = input("Ask a question: ")
# answer = input("Give me the answer: ")
# my_answer = input(" " + question1)

# while answer != my_answer:
#     print("Try again!")
# else:
#     print("That's correct!")

# question2 = input("Ask a another question: ")
# answer2 = input("Give me the answer: ")
# my_answer2 = input(" " + question2)

# while answer2 != my_answer2:
#     print("Try again")
# else:
#     print("That correct!")

# question3 = input("Ask one more question: ")
# answer3 = input("Give me the answer: ")
# my_answer3 = input("" + question3)

# while answer3 != my_answer3:
#     print("Try again!")
# else:
#     print("That's correct!")

# if my_answer3 == answer3:
#     print("Correct!")
# else:
#     print("Incorrect!")
# ask for answer for every Question

# Save the questions

# test mode

# Submit for grade



another = True

while another:
    question1 = input("Ask a question: ")
    answer = input("Give me the answer:") 
    myanswer = input ("\n")
    again = input("Do you want to add another question? respond y or n: ")
    if again == 'y':
        another = True
    if again == 'n':
        another = False