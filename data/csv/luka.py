#open SPECIFIC file (for test purposes, of course) and print out contents of file
with open('2022-2023.csv', 'r') as file:
    contents = file.read()
    print(contents)
