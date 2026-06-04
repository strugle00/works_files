with open("input.txt", "r+") as file:
    lines = file.readlines()

line_count = len(lines)

word_count = 0
for line in lines:
    word_count += len(line.split())

with open("statistics.txt", "w") as file:
    file.write(f"Количество строк: {line_count}\n")
    file.write(f"Количество слов: {word_count}\n")

print("Результат в statistics.txt")
