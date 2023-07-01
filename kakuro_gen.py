import itertools
import random
import cells


# def generate_sums(cells_array):
#     create_cells_values = run_for_cells(cells_array)
#     make_sums = get_sums(create_cells_values)
#     return make_sums


def create_cells_values(cells_array):
    """Рандомизирует цифры в клетках"""
    for i in range(len(cells_array)):
        if cells_array[i].value == 0:
            valid_value = set(range(1, 10))
            valid_value = valid_value.difference(
                cells_array[i].horblock_digits.union(
                    cells_array[i].vertblock_digits))
            cells_array[i].value = random.choice([x for x in valid_value])
            if len(cells_array[i].vertblock_digits) \
                    < cells_array[i].vertblock_len:
                cells_array[i].vertblock_digits.add(cells_array[i].value)
            if len(cells_array[i].horblock_digits) \
                    < cells_array[i].horblock_len:
                cells_array[i].horblock_digits.add(cells_array[i].value)
            for j in range(i + 1, len(cells_array)):
                if cells_array[j].corrds[1] == cells_array[i].corrds[1] and (
                        cells_array[j].corrds[0] - cells_array[i].corrds[0]
                        < cells_array[i].vertblock_len):
                    cells_array[j].vertblock_digits.add(cells_array[i].value)
                if cells_array[j].corrds[0] == cells_array[i].corrds[0] and \
                        cells_array[j].corrds[1] - cells_array[i].corrds[1] < \
                        cells_array[j].horblock_len:
                    cells_array[j].horblock_digits.add(cells_array[i].value)
    return cells_array


def fill_sums_of_cells(cells_array):
    """Считает суммы для каждой строки и каждого столбца"""
    for cell in cells_array:
        if len(cell.horblock_digits) == cell.horblock_len:
            cell.leftsum = sum(cell.horblock_digits)
        if len(cell.vertblock_digits) == cell.vertblock_len:
            cell.upsum = sum(cell.vertblock_digits)
    for i in range(len(cells_array)):
        if len(cells_array[i].horblock_digits) \
                != cells_array[i].horblock_len:
            cells_array[i].leftsum = cells_array[
                i + cells_array[i].horblock_len - cells_array[
                    i].horblock_pos].leftsum
        len_array = len(cells_array[i].vertblock_digits)
        if len_array != cells_array[i].vertblock_len:
            upsum = 0
            for j in range(i + 1, len(cells_array)):
                if cells_array[i].corrds[1] == cells_array[j].corrds[1] and \
                        cells_array[j].corrds[0] - cells_array[i].corrds[0] \
                        < cells_array[i].vertblock_len:
                    upsum = cells_array[j].upsum
            for j in range(i, len(cells_array)):
                if cells_array[i].corrds[1] == cells_array[j].corrds[1] and \
                        cells_array[j].corrds[0] - cells_array[i].corrds[0] \
                        < cells_array[i].vertblock_len:
                    cells_array[j].upsum = upsum
    return cells_array


def strings_formatter(array, cells_array):
    """Форматирует созданный какуро - заполняет пустые суммы
    найденными ранее"""
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == "-/-":
                if j + 1 < len(array[i]) and array[i][j + 1] == '.':
                    for cell in cells_array:
                        if cell.corrds[0] == i and cell.corrds[1] == j + 1:
                            array[i][j] = array[i][j][:-1]
                            array[i][j] += str(cell.leftsum)
                if i + 1 < len(array) and array[i + 1][j] == '.':
                    for cell in cells_array:
                        if cell.corrds[0] == i + 1 and cell.corrds[1] == j:
                            array[i][j] = array[i][j][1:]
                            sums = str(cell.upsum) + array[i][j]
                            array[i][j] = sums
    return array


def reader(filename):
    """
    Считывает карту для какуро, возвращает его массив
    """
    filename = str(filename)
    result = list()
    with open(filename) as f:
        for line in f:
            string = line.split(' ')
            if string[-1][len(string[-1]) - 1:] == '\n':
                string[-1] = string[-1][:-1]
            result.append(string)
    if len(result) == 0:
        print('Некорректный ввод')
        exit(1)
    return result


def get_cells_array(array):
    """
    Создает массив клеток. Возвращает его
    """
    i = 0
    cells_arr = list()
    while i < len(array):
        j = 0
        while j < len(array[i]):
            if array[i][j] == '.':
                c = cells.CellsForRandom(i, j, array)
                cells_arr.append(c)
            j += 1
        i += 1
    return cells_arr
