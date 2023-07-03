'''
Необходимо написать функцию, которая берет массив и перемещает все нули в конец,
сохраняя порядок остальных элементов
'''
random_array = [0, 1, 0, 3, 9, 0, 5, 0, 13, 56, 0, 4, 7, 8]   # for example


def move_zeroes(array):
    zeroes_count = array.count(0)
    for i in range(zeroes_count):
        array.remove(0)
    array.extend([0 for i in range(zeroes_count)])
    return array


print(move_zeroes(random_array))
