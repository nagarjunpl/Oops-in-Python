# Match case statement example
# Only available in Python 3.10 or later


# Match case statement example for number input
num = int(input("Enter a number: "))

match num:
    case 1:
        print("one")

    case 2:
        print("two")
    
    case 3:
        print("three")
    
    case _:
        print("Number is not one, two, or three")



# Match case statement example for fruit selection
value = input("Enter a fruit name: ")

match value:
    case "apple":
        print("You chose apple.")

    case "banana":
        print("You chose banana.")

    case "orange" | "tangerine":     # This line checks if the value is either "orange" or "tangerine"
        if value == "orange":     # This line checks if the value is "orange"
            print("You chose orange.")
        elif value == "tangerine":    # This line checks if the value is "tangerine"
            print("You chose tangerine.")
        
    case _:
        print("Unknown fruit.")