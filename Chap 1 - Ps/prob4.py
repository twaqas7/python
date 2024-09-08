# import os

# def print_directory_contents(directory):
#     try:
#         # Get a list of entries in the directory
#         entries = os.listdir(directory)
        
#         # Print each entry in the directory
#         for entry in entries:
#             print(entry)
#     except FileNotFoundError:
#         print(f"The directory '{directory}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied: cannot access '{directory}'.")

# # Replace '.' with the path to the directory you want to list
# directory_path = '.'
# print_directory_contents(directory_path)


import os

# Select the directory whose content you want to list 
directory_path = '/ProgramData/Microsoft/Windows/Start Menu/Programs'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)