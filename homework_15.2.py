# Write a function called new_lines that takes a file path, opens the file
# and adds a newline character (\n) once in 20 symbols
from time import time
string_convert = []


def new_lines(path: str):
    with open(path, 'r') as file:
        text = file.read()
        for num, letter in enumerate(text, start=1):
            string_convert.append(letter)
            if num % 20 == 0:
                string_convert.append("\n")
    with open(path, "w") as file_2:
        file_2.write("".join(string_convert))


new_lines('homework_directory/text.txt')


