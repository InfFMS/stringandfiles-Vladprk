# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
banned_str = '—@*%#'
f = open('task1.txt', 'r', encoding='utf8')
a = f.read()
x = a.count('\n') + 1
y = 1
ind = False
for i in range(len(a)):
    if a[i] != " ":
        ind = True
        if banned_str.find(a[i]) != -1:
            try:
                if a[i+1] == ' ' and a[i-1] == ' ':
                    y -= 1
            except:
                y -= 1
    else:
        y += 1
y -= x
z = len(a)
print(x)
print(y)
print(z)
f.close()
