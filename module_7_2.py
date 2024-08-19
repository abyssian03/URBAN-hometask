def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}
    i = 0
    for string in strings:
        strings_position.update({(i, file.tell()): string})
        file.write(f"{string}\n")
        i += 1
    file.close()
    return (strings_position)

print(custom_write("new_file.txt", ["Мама мыла раму", "Сиреневенький с подвыподвертом", "ω-непротиворечивость"]))