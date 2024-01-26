Hidden_message = input("What message would you like to inscribe?: ")


Lines_of_code = int(input("enter a #: "))




# Specify the file name you want to create
file_name = "output.txt"

# Open the file in "write" mode
# This will create the file if it doesn't exist, or truncate (empty) it if it does.
with open(file_name, "w") as file:
    # Write data to the file
    
    for i in range(Lines_of_code):

        file.write(f"Hello, World! {i +1} \n")
