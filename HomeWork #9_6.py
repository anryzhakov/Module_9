# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Генераторы"

def all_variants(text):
    for i in range(len(text)):
        for n in range(len(text) - i):
            yield text[n:n+i+1]

a = all_variants("abc")
for i in a:
    print(i)

print(tuple(all_variants('сумасойти')))