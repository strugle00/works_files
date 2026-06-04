search_word = input("Введите слово для поиска: ")

count = 0
line_numbers = []

with open("text.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        occurrences = line.count(search_word)

        if occurrences > 0:
            count += occurrences
            line_numbers.append(number)

with open("search_results.txt", "w") as file:
    if count > 0:
        file.write("Слово найдено\n")
        file.write(f"Количество вхождений: {count}\n")

    else:
        file.write("Слово не найдено")

if count > 0:
    print("Слово найдено")
    print("Количество:", count)
    print("Строки:", line_numbers)
else:
    print("Слово не найдено")
