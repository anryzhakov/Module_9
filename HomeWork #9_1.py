# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    results = {}
    for function_item in functions:
        results[function_item.__name__] = function_item(int_list)
        print(function_item.__name__)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
