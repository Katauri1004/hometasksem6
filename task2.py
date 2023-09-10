# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

value_max = int(input('Please, input max value: '))
value_min = int(input('Please, input min value: '))

values = input('Please, input our values separeted by a space: ').split()
int_list_of_values = list(map(int, values))
list_of_index_values = []

for i in range (len(int_list_of_values)):
    if int_list_of_values[i] <= value_max and int_list_of_values[i] >= value_min:
        list_of_index_values.append(i)
print('Our result: ')
print(list_of_index_values)       
