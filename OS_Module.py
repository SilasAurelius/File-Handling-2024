# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.

# Code Example:
import os

def list_directory_contents():
    path = input("Enter directory path: ")
    try:
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    list_directory_contents()
    
# Keep getting errors when trying to call list_directory_contents(). Did some research and it was suggested to use __name__ == "_main__". After using that, I didn't get an error when calling my function.

