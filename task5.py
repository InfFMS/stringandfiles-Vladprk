# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
# Выведите это слово и длину в консоль.
f = open('task5.txt', 'r', encoding='utf-8')
new_f = open('new_file_for_task_5.txt', 'w', encoding='utf-8')
a = f.read()
the_longest_word = ''
length_of_the_longest_word = -1
length = 0
word = ''
for i in range(len(a)):
    indi = False
    if a[i] != " " and a[i] != "\n":
        if a[i] != '.' and a[i] != ',':
            length += 1
            word += a[i]
    else:
        if length_of_the_longest_word < length:
            length_of_the_longest_word = length
            the_longest_word = word
        word = ''
        length = 0
new_f.write(f'Самое длинное слово: "{the_longest_word}" \n')
new_f.write(f'Его длина: {length_of_the_longest_word}')
