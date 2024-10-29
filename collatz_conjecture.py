#user to enter a number
number = int(input("Enter a number:"))
count = 0  # Initialize a count variable to keep track of steps

while True:
    # Check if the number is even
    if number % 2 == 0:  # Corrected the syntax error here
        number = number // 2  # Divide the number by 2
        count += 1  # Increment the count
    else:  # Corrected the syntax error here
        number = number * 3 + 1  # Apply the 3n + 1 rule
        count += 1  # Increment the count
    
    # Optionally, you may want to break the loop when the number reaches 1
    if number == 1:
        break  # Exit the loop when the sequence reaches 1

print(count)
