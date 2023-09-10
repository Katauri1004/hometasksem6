# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

first = int(input('Please, input value of first element in progression: '))
diff = int(input("Please, input difference of progression: "))
countvalues = int(input('Please, input count of values: '))

result = list(first + n * diff for n in range(countvalues))
print('Our Result: ')
print(result)
