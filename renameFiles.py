import os

def rename_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Counter for renaming
    count = 1
    
    # Rename each file
    for filename in files:
        # Construct old and new file paths
        old_path = os.path.join(directory, filename)
        new_filename = str(count) + os.path.splitext(filename)[1]
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        # Increment count for the next file
        count += 1

# Main function
def main():
    # Take user input for directory path
    directory = input("Enter directory path: ")
    
    # Check if the directory exists
    if not os.path.exists(directory):
        print("Directory not found.")
        return
    
    # Rename files in the directory
    rename_files(directory)
    print("Files renamed successfully.")

# Run the main function
if __name__ == "__main__":
    main()