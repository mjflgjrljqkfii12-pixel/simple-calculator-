print("welcome to my first calculator😊")
while True:
    
    num1=float(input("enter first number:   "))
    num2=float(input("enter second number:   "))
    choice=input("choose operation(+ - * / )or q to quit:   ")
    if choice=="q":
        break
    elif choice == "+":
        print(num1 + num2)
    elif choice == "-":
        print(num1 - num2)
    elif choice =="*":
        print(num1 * num2)

    elif choice =="/":
        if num2==0:
            print("cannot divide by zero")
        else:
            print(num1/num2)

    else:
        print("not available")
