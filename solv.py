# import Cells
# import Calcs
# import sys
# import kakuro_gen


# def hor_block_variants(cell, arr):
#     """
#         Возвращает массив с последовательным набором потенциальных чисел
#         для каждой клетки в горизонтальном блоке
#     """
#     j = cell.corrds[1]
#     i = cell.corrds[0]
#     local_j = j
#     values = list()
#     while local_j >= cell.horblock[0]:
#         local_j -= 1
#     local_j += 1
#     while local_j < cell.horblock[1]:
#         for item in arr:
#             if item.corrds == (i, local_j,):
#                 values.append(item.value)
#                 local_j += 1
#     return values
#
#
# def vert_block_variants(cell, arr):
#     """
#     Возвращает массив с последовательным набором потенциальных чисел
#     для каждой клетки в вертикальном блоке
#     """
#     j = cell.corrds[1]
#     i = cell.corrds[0]
#     local_i = i
#     values = list()
#     while local_i >= cell.vertblock[0]:
#         local_i -= 1
#     local_i += 1
#     while local_i < cell.vertblock[1]:
#         for item in arr:
#             if item.corrds == (local_i, j,):
#                 values.append(item.value)
#                 local_i += 1
#     return values
#
#
# def choose_nums(cell, arr):
#     """
#     Вызывает функции, которые комбинируют числа и сужают круга поиска
#     """
#     vert_values = vert_block_variants(cell, arr)
#     vert_value = Calcs.choosing(vert_values, cell.upsum,
#                                 cell.vertblock_pos - 1)
#     hor_values = hor_block_variants(cell, arr)
#     hor_value = Calcs.choosing(hor_values, cell.leftsum,
#     cell.horblock_pos - 1)
#     return list(set(vert_value) & set(hor_value))
#
#
# def choose_numbers(cell):
#     """
#     Вызывает функции, которые возвращают массив
#     всех потенциальных чисел для клетки
#     """
#     vertsum_nums = Calcs.variants(cell.vertblock_length, range(1, 10),
#                                   cell.upsum)
#     horsum_nums = Calcs.variants(cell.horblock_length, range(1, 10),
#                                  cell.leftsum)
#     same_nums = Calcs.find_same(vertsum_nums, horsum_nums)
#     return same_nums
#
#
# def checker(array):
#     """
#     Проверяет, остались ли еще нерешенные клетки
#     """
#     for cell in array:
#         if len(cell.value) > 1:
#             return True
#     return False
#

# def solver(array):
#     """
#     Создает массив клеток. Вызывает все функции, решающие какуро.
#     Печаетет результат
#     """
#     i = 0
#     cells_arr = list()
#     while i < len(array):
#         j = 0
#         while j < len(array[i]):
#             if array[i][j] == '.':
#                 c = Cells.Cell(i, j, array)
#                 cells_arr.append(c)
#             j += 1
#         i += 1
#     for cell in cells_arr:
#         cell.value = choose_numbers(cell)
#     while checker(cells_arr):
#         for cell in cells_arr:
#             cell.value = choose_nums(cell, cells_arr)
#     #for cell in cells_arr:
#        # print(cell.value[0])
#     #for cell in cells_arr:
#        # print(
#           #  'Координата клетки:{0}, левая сумма: {1}, '
#           #  'верхняя сумма: {2}, число: {3}'.format(
#            #     cell.corrds,
#            #     cell.leftsum, cell.upsum, cell.value[0]))
#        # print('===========================================================')
#     for cell in cells_arr:
#         cell.value = cell.value[0]
#     return cells_arr

#
# def reader(filename):
#     """
#     Считывает какуро, возвращает ее массив
#     """
#     filename = str(filename)
#     result = list()
#     with open(filename) as f:
#         for line in f:
#             string = line.split(' ')
#             if string[-1][len(string[-1]) - 1:] == '\n':
#                 string[-1] = string[- 1][:-1]
#             result.append(string)
#     if len(result) == 0:
#         print('Некорректный ввод')
#         exit(1)
#     return result
#
#
# def main():
#     if sys.argv[1] == "--help":
#         print(helper())
#         return exit(0)
#     if sys.argv[1] == "pytest":
#         return exit(0)
#     #a = reader(sys.argv[1])
#     # a = kakuro_gen.reader(sys.argv[1])
#     # solver(a)
#
#
# def helper():
#     return """
#     Решает с нуля какуро. На ввод подается файл в формате txt,
#     помещенный в одну с solv.py папку.
#     Формат ввода: черная клетка - "#", пустая клетка - ".",
#     сумма записывается через "/". Если какая-либо из сумм отсутствует,
#     на ее месте ставится "-", например, "-/25", "15/-".
#     Каждая клетка пишется через пробел.
#     Формат вывода: для каждой пустой клетки выводятся ее координаты,
#     верхняя и левая суммы и вычисленное значение"""
#
#
# if __name__ == "__main__":
#     main()
