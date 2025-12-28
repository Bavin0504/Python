# fh = open("sample.txt", "xt")
# fh.write("This is a sample text file.")
# fh.write("\nIt contains multiple lines.")
# fh.close()

try:
    with open("sample.txt", "xt") as fh:
        fh.write("This is a sample text file.")
        fh.write("\nIt contains multiple lines.")

    with open("sample.txt", "rt") as content:
        print("Reading file content: ")
        for line_no, line in enumerate(content,start =1):
            print(f"Line {line_no}: {line.strip()}")
        
except Exception as Error:
    print(f"Error: The file 'sample.txt' was not found.")                