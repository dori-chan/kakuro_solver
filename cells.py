import cell_analize
#
#
# class Cell:
#     """
#     Здесь вычисляем и храним всю информацию, которую нужно знать о ячейке
#     """
#     def __init__(self, i, j, array):
#         horblocks = CellAnalize.horiz_block(array, i, j)
#         vertblocks = CellAnalize.vertic_block(array, i, j)
#         self.upsum = CellAnalize.found_vertical_sum(array, j, i)
#         self.leftsum = CellAnalize.found_gorizontal_sum(array, i, j)
#         self.corrds = (i, j, )
#         self.value = array[i][j]
#         self.vertblock = vertblocks[0]
#         self.horblock = horblocks[0]
#         self.vertblock_pos = CellAnalize.vert_sum_pos(array, i, j)
#         self.horblock_pos = CellAnalize.hor_sum_pos(array, i, j)
#         self.horblock_length = horblocks[1]
#         self.vertblock_length = vertblocks[1]


class CellsForRandom:
    """
         Здесь вычисляем и храним всю информацию, которую нужно знать о ячейке
    """
    def __init__(self, i, j, array):
        horblocks = cell_analize.horiz_block(array, i, j)
        vertblocks = cell_analize.vertic_block(array, i, j)
        self.corrds = (i, j,)
        self.value = 0
        self.vertblock = vertblocks[0]
        self.horblock = horblocks[0]
        self.vertblock_pos = cell_analize.vert_sum_pos(array, i, j)
        self.horblock_pos = cell_analize.hor_sum_pos(array, i, j)
        self.horblock_len = horblocks[1]
        self.vertblock_len = vertblocks[1]
        self.upsum = 0
        self.leftsum = 0
        self.horblock_digits = set()
        self.vertblock_digits = set()
