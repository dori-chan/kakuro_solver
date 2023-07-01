import unittest
import cell_analize
import calcs
# import Cells
# import solv
import kakuro_gen
import sockclient
import sender


class Testcell_analize(unittest.TestCase):
    def test_found_vertical_sum(self):
        with self.assertRaises(SystemExit) as cm:
            cell_analize.found_vertical_sum(
                [['#', '#', '#', '#', ], ['15/-', '.', '.', '.', ]], 2, 1)
            self.assertEqual(cm.exception.code, 1)
        self.assertEqual(cell_analize.found_vertical_sum(
            [['#', '20/-', '11/', '3/-', ], ['-/15', '.', '.', '.', ]], 1, 1),
                         '20')
        self.assertEqual(cell_analize.found_vertical_sum(
                [['#', '20/-', '11/', '3/-', ], ['-/15', '.', '.', '.', ],
                 ['.', '.', '.', '.']], 1, 2), '20')

    def test_found_gorizontal_sum(self):
        with self.assertRaises(SystemExit) as cm:
            cell_analize.found_gorizontal_sum([['#', '#', '-/20', '#'],
                                               ['#', '.', '.', '.']], 1, 2)
            self.assertEqual(cm.exception.code, 1)
        self.assertEqual(cell_analize.found_gorizontal_sum(
            [['#', '20/-', '11/', '3/-', ], ['-/15', '.', '.', '.', ]], 1, 1),
                         '15')
        self.assertEqual(cell_analize.found_gorizontal_sum(
            [['#', '20/-', '11/', '3/-', ], ['-/15', '.', '.', '.', ]], 1, 3),
                         '15')

    def test_vertic_block(self):
        self.assertEqual(cell_analize.vertic_block(
            [['#', '#', '#', '#'], ['-/15', '.', '.', '.'],
             ['-/20', '.', '.', '.']], 2, 1), [[1, 2], 2])

    def test_horiz_block(self):
        self.assertEqual(cell_analize.horiz_block(
            [['#', '#', '#', '#'], ['-/15', '.', '.', '.']], 1, 2),
                         [[1, 3], 3])

    def test_vert_sum_pos(self):
        self.assertEqual(cell_analize.vert_sum_pos(
            [['#', '#', '#', '#'], ['-/15', '.', '.', '.'],
             ['-/20', '.', '.', '.']], 2, 1), 2)

    def test_hor_sum_pos(self):
        self.assertEqual(cell_analize.hor_sum_pos(
            [['#', '#', '#', '#'], ['-/15', '.', '.', '.'],
             ['-/20', '.', '.', '.']], 2, 3), 3)

    def test_is_number(self):
        self.assertEqual(cell_analize.is_number(5), True)
        self.assertEqual(cell_analize.is_number('ab'), False)


class Testcalcs(unittest.TestCase):
    def test_variants(self):
        self.assertEqual(calcs.variants(3, range(1, 10), 7), [(1, 2, 4)])
        with self.assertRaises(SystemExit) as cm:
            calcs.variants(9, range(1, 10), 46)
            self.assertEqual(cm.exception.code, 1)
        with self.assertRaises(SystemExit) as cm:
            calcs.variants(2, range(1, 10), -10)
            self.assertEqual(cm.exception.code, 1)

    def test_find_same(self):
        with self.assertRaises(SystemExit) as cm:
            calcs.find_same([(1, 5, 6), (3, 7, 2)], [(9, 8, 4)])
            self.assertEqual(cm.exception.code, 1)
        self.assertEqual(calcs.find_same([(1, 5, 6), (3, 7, 2)], [(3, 5, 4)]),
                         [3, 5])

    def test_choosing(self):
        with self.assertRaises(SystemExit) as cm:
            calcs.choosing([[1], [1]], 2, 1)
            self.assertEqual(cm.exception.code, 1)
        self.assertEqual(calcs.choosing(
            [[2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9], [8, 9], [6, 7, 8],
             [2, 5, 6], [2], [3, 4]], 39, 0), [3, 4])


class Testkakuro_gen(unittest.TestCase):
    def test_reader(self):
        with self.assertRaises(SystemExit) as cm:
            kakuro_gen.reader('kak0.txt')
            self.assertEqual(cm.exception.code, 1)

    def test_get_cells_array(self):
        array = [['#', '-/-', '-/-', '-/-'], ['-/-', '.', '.', '.'],
                 ['-/', '.', '.', '.'], ['-/', '.', '.', '.']]
        cells_array = kakuro_gen.get_cells_array(array)
        self.assertEqual(cells_array[0].corrds[0], 1)
        self.assertEqual(cells_array[0].corrds[1], 1)
        self.assertEqual(cells_array[3].corrds[0], 2)
        self.assertEqual(cells_array[3].corrds[1], 1)
        self.assertEqual(cells_array[8].corrds[0], 3)
        self.assertEqual(cells_array[8].corrds[1], 3)

    def test_create_cells_values(self):
        array = [['#', '-/-', '-/-', '-/-'], ['-/-', '.', '.', '.'],
                 ['-/', '.', '.', '.'], ['-/', '.', '.', '.']]
        for _ in range(50):
            cells_array = kakuro_gen.get_cells_array(array)
            cells_array = kakuro_gen.create_cells_values(cells_array)
            for cell in cells_array:
                if cell.value == 0:
                    return True
                i = cell.corrds[0]
                j = cell.corrds[1]
                for other_cell in cells_array:
                    i_other = other_cell.corrds[0]
                    j_other = other_cell.corrds[1]
                    if (i_other == i and j_other != j) \
                            or (j_other == j and i_other != i):
                        self.assertTrue(other_cell.value != cell.value)

    def test_fill_sums_of_cells(self):
        array = [['#', '-/-', '-/-', '-/-'], ['-/-', '.', '.', '.'],
                 ['-/', '.', '.', '.'], ['-/', '.', '.', '.']]
        cells_array = kakuro_gen.get_cells_array(array)
        cells_array = kakuro_gen.create_cells_values(cells_array)
        cells_array = kakuro_gen.fill_sums_of_cells(cells_array)
        for _ in range(50):
            for cell in cells_array:
                leftsum = 0
                upsum = 0
                for other_cell in cells_array:
                    if other_cell.corrds[0] == cell.corrds[0] and (
                            other_cell.corrds[
                                0] - cell.horblock_pos <= cell.horblock_len):
                        leftsum += other_cell.value

                    if other_cell.corrds[1] == cell.corrds[1] and (
                            other_cell.corrds[
                                1] - cell.vertblock_pos <= cell.vertblock_len):
                        upsum += other_cell.value
                self.assertTrue(
                    cell.leftsum == leftsum and cell.upsum == upsum)

    def test_strings_formatter(self):
        array = [['#', '-/-', '-/-', '-/-'], ['-/-', '.', '.', '.'],
                 ['-/', '.', '.', '.'], ['-/', '.', '.', '.']]
        cells_array = kakuro_gen.get_cells_array(array)
        cells_array = kakuro_gen.create_cells_values(cells_array)
        cells_array = kakuro_gen.fill_sums_of_cells(cells_array)
        new_array = kakuro_gen.strings_formatter(array, cells_array)
        for _ in range(50):
            for index_j, string in enumerate(new_array):
                for index_i, el in enumerate(string):
                    if el != '#' and el != '.':
                        leftsum = el.split('/')[0]
                        upsum = el.split('/')[1]
                        if leftsum.isdigit():
                            for cell in cells_array:
                                if cell.corrds[0] == index_j:
                                    self.assertTrue(int(leftsum) == cell.value)
                                    break
                        if upsum.isdigit():
                            for cell in cells_array:
                                if cell.corrds[1] == index_i:
                                    self.assertTrue(int(upsum) == cell.value)
                                    break


class Testsockclient(unittest.TestCase):
    def test_sockets(self):
        result = sockclient.sockets()
        self.assertTrue(result is None)


class Testsender(unittest.TestCase):
    def test_reader(self):
        with self.assertRaises(SystemExit) as cm:
            sender.reader('kak0.txt')
            self.assertEqual(cm.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
