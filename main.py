class Conversation():
    name = str(input("Enter your name: "))
    print("Woooow, " + name + " is a superb name!")
    occupation = str(input("Enter your occupation: "))
    question = input("Do you like being a " + occupation + " ?")
    if question == "Yes":
        print("That's great!")
    elif question == "No":
        print("No Worries, You Work Hard Though!")
    else:
        print("Wrong input!")