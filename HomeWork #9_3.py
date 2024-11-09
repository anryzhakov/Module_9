# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

result_first = (tf - ts for (i, j) in zip(first, second)
                        if ((tf := len(i)) != (ts := len(j))))
print(list(result_first))

result_second = (len(first[i]) == len(second[i])
                    for i in range(max(len(first), len(second))))
print(list(result_second))