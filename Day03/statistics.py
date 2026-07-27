with open("notes.txt", "r") as file:
    lines = file.readlines()

lines_num = len(lines)

letters_num = 0
words_num = 0

for i in range(lines_num):
    letters_num += len(lines[i])
    words_num += len(lines[i].split())

print(f"The number of lines:{lines_num}\nThe number of letters:{letters_num}\nThe number of words:{words_num}")