day=int(input("enter a number (1-7):"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("sunday")
    case _:
        print("Invalid input")
        
