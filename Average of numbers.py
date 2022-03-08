from turtle import done


print("------ Calculate average of numbers! -----")
#list of numbers inserted by user:
numbers = []

#Input of first number and integration to list:
nr1 = input("Enter first number: ")
numbers.append(int(nr1))

#Adding subsequent numbers
question = input("Answer 'yes' or 'no': Want to insert another number?  ")

#Answer options
if question == "yes":
    nr2 = input("Enter second number: ")
    numbers.append(int(nr2))
    for nr in numbers:
        question1 = input("Answer 'yes' or 'no': Want to insert another number? ")
        if question1 == "yes":
            numbers.append(int(input("Another number: ")))
        elif question1 == "no":
            sum_of_nr = sum(numbers)
            print("Average of numbers inserted: ")
            print(int(sum_of_nr)/len(numbers))
            print("Done!")
            break
        else:
            print("Invalid answer.")
elif question == 'no':
    print("Average of numbers inserted:")
    print(int(nr1)/(len(numbers)))
    print("Done!")
else:
    print("Invalid answer.")










