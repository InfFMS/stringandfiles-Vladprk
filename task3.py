# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
# Убедитесь, что слова записаны в алфавитном порядке.
f = open('task3.txt', 'r', encoding='utf-8')
new_f = open('new_file_for_task_3.txt', 'w', encoding='utf-8')
m = f.read()
a = m.lower()
mas_words = []
mas_int = []
final_mas = []
word = ''
for i in range(len(a)):
    indi = False
    if a[i] != " " and a[i] != "\n":
        if a[i] != '.' and a[i] != '' and a[i] != ',':
            word += a[i]
    elif word != '':
        for j in range(len(mas_words)):
            if word == mas_words[j]:
                mas_int[j] += 1
                indi = True
                break
        if not indi:
            mas_int.append(1)
            mas_words.append(word)
        word = ''
for i in range(len(mas_words)):
    final_mas.append(f'{mas_words[i]}: {mas_int[i]} \n')
final_mas.sort()
for i in range(len(mas_words)):
    new_f.write(final_mas[i])

