import math_functions as math
import os

def create_file(name, content): # Create a file
    with open(name, "w") as f: # Open the file in write mode
        f.write(content) # Write the content
        print("Successfully created", name) # Print success

def main(): # Main function

    print("How many files do you want to create?")
    print("Proceed with caution, don't create too many files!")
    print("At the end, you will be asked if you want to delete all files in case you created too many.") # Starting info

    range_input = input("Enter an integer: ") # Input

    if math.is_integer(range_input): # Check if input is an integer
        range_input = int(range_input)
    else:
        print("Invalid input") # Invalid input
    
    for i in range(0, range_input): # Create files
        create_file(f"file-{i}.txt", f"content of file-{i}.txt")
    
    if input("Do you want to delete all files? (y/n)") == "y": # Ask if user wants to delete files
        for i in range(0, range_input): # Delete files
            os.remove(f"file-{i}.txt")
            print(f"Successfully deleted file-{i}.txt") # Print success
    
    else:
        print("You chose to not delete files, have a nice day!")

main()