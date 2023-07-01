import itertools


def variants(n, collections, summ):
    """
    Перебирает всевозможные варианты сумм для клетки
    """
    result = list()
    for item in itertools.combinations(collections, n):
            if int(sum(item)) == int(summ):
                result.append(item)
    if int(summ) > 45 or int(summ) < 1:
        print("Некорректный ввод")
        return exit(1)
    return result


def find_same(arrays1, arrays2):
    """
    Возвращает массив из чисел,
    которые теоретически могут стоять на пересечении двух сумм
    """
    numbers = list()
    for el1 in arrays1:
        for ell2 in arrays2:
            set1 = set(el1)
            set2 = set(ell2)
            if len(set1 & set2) > 0:
                for num in set1 & set2:
                    numbers.append(num)
    if len(numbers) == 0:
        print("Некорректный ввод или какуро не имеет решения")
        exit(1)
    return list(set(numbers))


def choosing(arr, summ, pos):
    """
    Принимает массив всех потенциальных чисел в блоке
    и комбинирует их с учетом повторений, сужая круг поиска
    """
    array = list(itertools.product(*arr))
    perms = list()
    for item in array:
        setc = set(item)
        if len(setc) == len(item) and int(sum(item)) == int(summ):
            perms.append(item)
    result = list()
    for item in perms:
        if item[pos] not in result:
            result.append(item[pos])
    if len(result) == 0:
        print("Некорректный ввод или какуро не имеет решения")
        return exit(1)
    return result
