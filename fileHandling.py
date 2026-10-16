# Part 3 — File handling, CSV and JSON
# Question 10: Text file
# Create a file named notes.txt and write five lines into it. Then:

def writeFile():

    content = ["Hello this is a Sample Code \n" 
                "How are you doing today \n"
                "Playwright with Python is the best Automation Tool \n"
                "Vist Playwright website for more info \"http://playwright.dev/python/docs/intro\"."]
    
    # file = open("notes.txt", "w")
    # for line in content:
    #     file.write(line + "\n")
    # file.close()
    
    # or

    with open("notes.txt", "w") as file:
        for line in content:
            file.write(line + "\n")
        print("File created and content written successfully.")
        print("********************************************************")
writeFile()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ●	Read and print the complete file.
# ●	Print only the third line.

def readFile():
    with open("notes.txt", "r") as file:
        line = file.readlines()

        line = [l.replace("\n", "") for l in line]  # Remove newline characters

        print("Reading the entire File: ", line) #Read entire file

        #Print only third line 
        print("Third line of the file: ", line[2])

        print("********************************************************")

readFile()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ●	Append one more line without deleting existing content.

def writeFile():
    with open("notes.txt", "a") as file:
        file.write("Happy Coading! \n")

writeFile()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question 11: CSV file
# Create employees.csv with the columns id, name, and salary.

def writeCSV():
    import csv

    data = [
        ["id", "name", "salary"],
        ["Emp001", "John", 45000],
        ["Emp002", "Jakun", 60000],
        ["Emp003", "Jonithin", 55000],
        ["Emp004", "Jill", 70000]
    ]

    with open("employees.csv", "w", newline="") as file:
        write = csv.writer(file)
        write.writerows(data)

writeCSV()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
