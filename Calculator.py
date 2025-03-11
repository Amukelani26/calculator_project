# Calculator options
print("Please choose from the following operations: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#User choice of operation and 2 numbers
UserOption = int(input("Please enter you choice"))
UserFirstNum = int(input("Please enter your first number."))
UserSecondNum = int(input("Please enter your second number."))

#If statement with calculation
if UserOption == 1:
    AdditionResult = UserFirstNum + UserSecondNum
    print(AdditionResult)
elif UserOption == 2:
    SubtractionResult = UserFirstNum - UserSecondNum
    print(SubtractionResult)
elif UserOption == 3:
    MultiplicationResult = UserFirstNum * UserSecondNum
    print(MultiplicationResult)
elif UserOption == 4:
    DivisionResult = UserFirstNum / UserSecondNum
    print(DivisionResult)
else:
    print("You have enter an invalid value!")

    