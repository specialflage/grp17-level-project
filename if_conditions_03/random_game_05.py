import random
print(random.randint(1, 100))
count_correct =0
count_wrong = 0
for i in range(5):
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)

    print(first_number, " + " , second_number, " = ")

    user_result = input()
    user_result = int(user_result)
    correct_result = first_number + second_number
    if user_result == correct_result:
        print("Congrats. correct answer")
        count_correct = count_correct + 1
    else:
        print("failed, Wrong answer")
        count_wrong = count_wrong + 1
print("End of the program")
print("Correct answers = ", count_correct)
print("wrong answers = ", count_wrong)
