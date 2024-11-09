# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

result_first = [rf for i in first_strings if (rf := len(i)) >= 5]
print(result_first)

result_second = [(i, k) for i in first_strings
                        for k in second_strings
                              if len(i) == len(k)]
print(result_second)

third_strings = first_strings + second_strings
result_third = [{n: rt} for n in third_strings if not (rt := len(n)) % 2]
print(result_third)

