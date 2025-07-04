# Function definition - creates utility function for input validation (procedural programming)
def input_is_valid(msg, start=0, end=None):
    # Infinite loop - continues until valid input is received
    while True:
        # Variable assignment - gets user input using built-in input function
        inp = input(msg)

        # Conditional statement - checks if input contains only decimal digits
        if not inp.isdecimal():
            # Built-in function - prints error message to console
            print("Invalid Input. Try again!")
            # Continue statement - skips rest of loop iteration and starts over
            continue

        # Conditional statement - checks if both start and end parameters are provided
        if start is not None and end is not None:
            # Conditional statement - validates input is within specified range
            if not (start <= int(inp) <= end):
                # Built-in function - prints range error message
                print("Invalid Range. Try again!")
                # Continue statement - restarts loop for new input
                continue
            # Else clause - executes when input is within valid range
            else:
                # Return statement - exits function with converted integer value
                return int(inp)
        # Else clause - executes when no range validation is needed
        else:
            # Return statement - exits function with converted integer (no range check)
            return int(inp)