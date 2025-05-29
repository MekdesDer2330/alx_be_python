

# Function to generate and print the multiplication table
def print_multiplication_table(number):
    for i in range(1, 11):  # Loop from 1 to 10
        product = number * i  # Calculate the product
        print(f"{number} * {i} = {product}")  # Print the result in the desired format

# Main function to run the script
def main():
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Print the multiplication table for the given number
        print_multiplication_table(number)
    
    except ValueError:
        print("Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()
