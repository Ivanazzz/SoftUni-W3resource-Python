def function():
    command = input()
    
    if command == "int":
        number = int(input())
        output = number * 2
        print(output)
    elif command == "real":
        number = int(input())
        output = number * 1.5
        print(f"{output:.2f}")
    else:
        text = input()
        print(f"${text}$")
        
function()
