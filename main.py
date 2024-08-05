import math

another = True

hashmap = {} # '2+2': '4', '1+1': 2

# Add all Questions and answers
while another:
    question = input("Ask a question: ")
    answer = input("Give me the answer: ") 

    hashmap[question] = answer

    again = input("Do you want to add another question? respond y or n: ")
    if again == 'y':
        another = True
    if again == 'n':
        another = False

points = 100
wrongAmount = 0

# Ask every question in the hashmap
# check if the question is right
for q in hashmap:
    myAnswer = input(q)
    if hashmap[q] == myAnswer:
        print('correct')
    else:
        print("wrong")
        wrongAmount += 1


# (2-1) /2
score = (len(hashmap) - wrongAmount) / len(hashmap) * 100
print(math.ceil(score))


 

      
        

        
