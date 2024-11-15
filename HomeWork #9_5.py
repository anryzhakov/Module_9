# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Итераторы"

class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):

        if step == 0:
            raise StepValueError('Шаг итерации не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step > 0:
            self.step_gz = True
        else:
            self.step_gz = False

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step_gz == True and self.pointer > self.stop:
            raise StopIteration()
        if self.step_gz == False and self.pointer < self.stop:
            raise StopIteration()
        iter_next = self.pointer
        self.pointer = self.pointer + self.step
        return iter_next

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()