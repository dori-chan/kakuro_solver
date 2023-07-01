import re


def found_vertical_sum(array, j, i):
    """
    Возвращает верхнюю сумму
    """
    while i >= 0:
        pattern = re.search(r'[0-9]?[0-9]?[/][0-9]?[0-9]?', array[i][j])
        if pattern is not None:
            cells = array[i][j].split('/')
            return cells[0]
        i -= 1
    print("Некорректный ввод или какуро не имеет решения")
    return exit(1)


def found_gorizontal_sum(arr, i, j):
    """
    Возвращает левую сумму
    """
    while j >= 0:
        pattern = re.search(r'[0-9]?[0-9]?[/][0-9]?[0-9]?', arr[i][j])
        if pattern is not None:
            cells = arr[i][j].split('/')
            return cells[1]
        j -= 1
    print("Некорректный ввод или какуро не имеет решения")
    return exit(1)


def vertic_block(array, i, j):
    """
    Возвращает координаты начала и конца вертикального блока и его длину
    """
    local_i = i
    result = list()
    counter = 0
    coords_change = list()
    while local_i >= 0:
        if array[local_i][j] == '.' or array[local_i][j] is list or is_number(
                array[local_i][j]):
            counter += 1
            local_i -= 1
        else:
            coords_change.append(local_i + 1)
            break
    if len(coords_change) == 0:
        coords_change.append(local_i)
    local_i = i + 1
    while local_i < len(array):
        if array[local_i][j] == '.' or array[local_i][j] is list or is_number(
                array[local_i][j]):
            counter += 1
            local_i += 1
        else:
            coords_change.append(local_i - 1)
            break
    if len(coords_change) == 1:
        coords_change.append(local_i - 1)
    result.append(coords_change)
    result.append(counter)
    return result


def horiz_block(array, i, j):
    """
    Возвращает координаты начала и конца горизонтального блока и его длину
    """
    local_j = j
    counter = 0
    result = list()
    coords_change = list()
    while local_j >= 0:
        if array[i][local_j] == '.' or array[i][local_j] is list or is_number(
                array[i][local_j]):
            local_j -= 1
            counter += 1
        else:
            coords_change.append(local_j + 1)
            break
    if len(coords_change) == 0:
        coords_change.append(local_j)
    local_j = j + 1
    while local_j < len(array[i]):
        if array[i][local_j] == '.' or array[i][local_j] is list or is_number(
                array[i][local_j]):
            local_j += 1
            counter += 1
        else:
            coords_change.append(local_j - 1)
            break
    if len(coords_change) == 1:
        coords_change.append(local_j - 1)
    result.append(coords_change)
    result.append(counter)
    return result


def is_number(value):
    """
    Проверяет, является ли value числом
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def vert_sum_pos(array, i, j):
    """
    Определяет, на какой позиции находится клетка в вертикальном блоке
    """
    counter = 0
    while array[i][j] == '.' or array[i][j] is list or is_number(array[i][j]):
        counter += 1
        i -= 1
    return counter


def hor_sum_pos(array, i, j):
    """
    Определяет, на какой позиции находится клетка в горизонтальном блоке
    """
    counter = 0
    while array[i][j] == '.' or array[i][j] is list or is_number(array[i][j]):
        counter += 1
        j -= 1
    return counter
