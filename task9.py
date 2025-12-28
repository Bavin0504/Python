import os


try:
    with open("output.txt","xt") as fh:
        content = input("Enter text to write to the file: ")
        fh.write(content)
        print("Data successfully written to 'output.txt'.")
        print(" ")

except Exception as error:
    print(f"Error: The file 'output.txt' already exists.")         

if os.path.exists("output.txt"):
    with open("output.txt", "at") as fh:
        additional_content = input("Enter additional text to append to the file: ")
        fh.write("\n" + additional_content)
        print("Data successfully appended.")
        print(" ")



with open("output.txt", "rt") as fh:
    print("Reading the final content of the file: ")
    print(fh.read())
    

        

      
