file = open("notes.txt", "w")

file.write("Python\nAI\nMachine Learning")

file.close()

file = open("notes.txt", "r")

print(file.read())

file.close()