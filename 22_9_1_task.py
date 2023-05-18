#ввод данных
print('Ввод данных')
array = list(map(int, input('<- введите последовательность целых чисел: ').split()))
your_num = int(input ('<- введите число: '))

print('---------------------------------------------------')

def correct(array,your_num):
    #print(max(array), '  ', min(array))
    if your_num>max(array) or your_num<min(array):
        print('<!!!> Число ',your_num,' не входит в диапазон последовательности',array,' <!!!>')

#Быстрая сортировка
def partition(array, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = array[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1

        j -= 1
        while array[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        array[i], array[j] = array[j], array[i]

def quick_sort(array):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(array, 0, len(array) - 1)


#двоичный поиск
def binary_search(array, your_num, left, right):
    try:
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует
        middle = (right + left) // 2  # находимо середину
        if array[middle] == your_num:  # если элемент в середине,
            if your_num < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
                return binary_search(array, your_num, left, middle - 1)
            else:  # иначе в правой
                return binary_search(array, your_num, middle + 1, right)
    except IndexError:
        return 'Введенное число вне диапазона.'

#поиск номера позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше
#или равен этому числу
def lst_find_num(array, your_num):
    i=0
    for i in range(len(array) - 1):
        if your_num > array[i] and your_num <= array[i + 1]:
            print('-> искомый элемент: ',array[i])
            print('-> индекс элемента: ',array.index(array[i]))
            return i + 1
    return -1
print('Вывод данных')

quick_sort(array)
correct(array,your_num)
print('-> сортировка по возрастанию: ',array)
binary_search(array, your_num, 0, len(array)-1)
lst_find_num(array, your_num)