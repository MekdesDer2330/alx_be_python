

def draw_pattern(size):
    row = 0  # Initialize row counter

    while row < size:  # Loop through each row
        for col in range(size):  # Loop through each column in the current row
            print("*", end="")  # Print an asterisk without advancing to a new line
        print()  # Move to the next line after finishing the current row
        row += 1  # Increment the row counter

def main():
    try:
        # Prompt the user for the size of the pattern
        size = int(input("Enter the size of the pattern: "))
        
        if size <= 0:
            print("Please enter a positive integer.")
            return
        
        # Draw the pattern of the specified size
        draw_pattern(size)
    
    except ValueError:
        print("Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()
