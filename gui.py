import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, \
    QAction, QGridLayout, QMessageBox
from PyQt5 import QtGui
import cell_analize
import solv
import sockclient
import kakuro_gen


def get_array(solution):
    i = 0
    result = list()
    while i < len(solution):
        result.append(1)
        i += 1
    return result


player_result = list()
kakuro_level = "Easy.txt"
reading_kakuro = kakuro_gen.reader(kakuro_level)
cells_array = kakuro_gen.get_cells_array(reading_kakuro)
create_cells_values = kakuro_gen.create_cells_values(cells_array)
right_solution = kakuro_gen.fill_sums_of_cells(create_cells_values)

reading_kakuro = kakuro_gen.strings_formatter(reading_kakuro, right_solution)
array_for_widget = get_array(right_solution)
counter = 0


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.make_game()

    def make_game(self):
        """Создает игру"""
        main_widget = KakuroWidget()
        self.setCentralWidget(main_widget)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle('加算クロス')
        checker = QAction(QtGui.QIcon('check.png'), 'Проверить решение', self)
        solution = QAction(QtGui.QIcon('solution.png'),
                           'Показать правильное решение', self)
        newlevel = QAction(QtGui.QIcon('new.png'),
                           'Получить случайный уровень', self)
        generate = QAction(QtGui.QIcon('random.png'), 'Сгенерировать какуро',
                           self)
        kakuro1 = QAction(QtGui.QIcon('red.png'), 'Hard', self)
        kakuro2 = QAction(QtGui.QIcon('green.png'), 'Easy', self)
        kakuro3 = QAction(QtGui.QIcon('yellow.png'), 'Medium', self)

        kakuro1.triggered.connect(self.slot_for_level)
        kakuro2.triggered.connect(self.slot_for_level)
        kakuro3.triggered.connect(self.slot_for_level)
        checker.triggered.connect(self.slot_for_check)
        solution.triggered.connect(self.slot_fot_solution)
        newlevel.triggered.connect(self.slot_for_newlevel)
        generate.triggered.connect(self.slot_for_gen_lvl)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Выбрать какуро')
        fileMenu.addAction(kakuro2)
        fileMenu.addAction(kakuro3)
        fileMenu.addAction(kakuro1)

        toolbar = self.addToolBar('Tools')
        toolbar.addAction(checker)
        toolbar.addAction(solution)
        toolbar.addAction(newlevel)
        toolbar.addAction(generate)
        self.show()

    def slot_for_newlevel(self):
        global reading_kakuro, right_solution, array_for_widget, player_result
        temporary_kakuro = sockclient.sockets()
        if temporary_kakuro is None:
            KakuroWidget().msg('Соединение с сервером не установлено')
            return
        right_solution = kakuro_gen.get_cells_array(reading_kakuro)
        array_for_widget = get_array(right_solution)
        player_result = list()
        self.setCentralWidget(KakuroWidget())
        for i in range(0, 10):
            QApplication.processEvents()
        self.resize(self.minimumSizeHint())

    def slot_for_gen_lvl(self):
        global reading_kakuro, right_solution, array_for_widget, \
            player_result, kakuro_level
        reading_kakuro = kakuro_gen.reader(kakuro_level)
        cells_array = kakuro_gen.get_cells_array(reading_kakuro)
        create_cells_values = kakuro_gen.create_cells_values(cells_array)
        right_solution = kakuro_gen.fill_sums_of_cells(create_cells_values)
        reading_kakuro = kakuro_gen.strings_formatter(reading_kakuro,
                                                      right_solution)
        array_for_widget = get_array(right_solution)
        player_result = list()
        self.setCentralWidget(KakuroWidget())
        for i in range(0, 10):
            QApplication.processEvents()
        self.resize(self.minimumSizeHint())

    def slot_fot_solution(self):
        global array_for_widget, player_result
        i = 0
        while i < len(right_solution):
            array_for_widget[i] = right_solution[i].value
            i += 1
        player_result = list()
        self.setCentralWidget(KakuroWidget())

    def slot_for_check(self):
        flag = True
        i = 0
        while i < len(player_result):
            if int(right_solution[i].value) != int(player_result[i].text()):
                flag = False
                KakuroWidget().msg('Неверно')
                break
            i += 1
        if flag is True:
            KakuroWidget().msg('Верно')

    def slot_for_level(self):
        sender = self.sender()
        self.level(sender)

    def level(self, action):
        name = action.text()+'.txt'
        global array_for_widget, player_result, kakuro_level, right_solution, \
            reading_kakuro
        kakuro_level = name
        reading_kakuro = kakuro_gen.reader(kakuro_level)
        s = kakuro_gen.get_cells_array(reading_kakuro)
        create_cells_values = kakuro_gen.create_cells_values(s)
        right_solution = kakuro_gen.fill_sums_of_cells(create_cells_values)
        reading_kakuro = kakuro_gen.strings_formatter(reading_kakuro,
                                                      right_solution)
        array_for_widget = get_array(right_solution)
        player_result = list()
        self.setCentralWidget(KakuroWidget())
        for i in range(0, 10):
            QApplication.processEvents()
        self.resize(self.minimumSizeHint())


class KakuroWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.make_widget()

    def make_widget(self):
        """Создает виджет с сеткой"""
        global player_result
        grid = QGridLayout()
        grid.setSpacing(0)
        self.setLayout(grid)
        names = list()
        for item in reading_kakuro:
            names += item
        positions = [(i, j) for i in range(len(reading_kakuro)) for j in
                     range(len(reading_kakuro[0]))]
        for position, name in zip(positions, names):
            if name == '#':
                btn = QPushButton(' ')
                btn.setStyleSheet("background-color: black")
                grid.addWidget(btn, *position)
            elif name == '.':
                global counter
                btn = QPushButton(str(array_for_widget[counter]))
                btn.clicked.connect(self.slot)
                btn.setStyleSheet("background-color: white")
                player_result.append(btn)
                grid.addWidget(btn, *position)
                counter += 1
            elif cell_analize.is_number(name[-1:]) \
                    and cell_analize.is_number(name[:1]):
                btn = QPushButton('↓' + name + '→')
                btn.setStyleSheet("background-color: black; color: white")
                grid.addWidget(btn, *position)
            elif not cell_analize.is_number(name[0:1]):
                btn = QPushButton(name[2:] + '→')
                btn.setStyleSheet("background-color: black; color: white")
                grid.addWidget(btn, *position)
            else:
                btn = QPushButton('↓' + name[:-2])
                btn.setStyleSheet("background-color: black; color: white")
                grid.addWidget(btn, *position)
        counter = 0

    def msg(self, txt):
        QMessageBox.question(self, 'Проверка:', txt, QMessageBox.Yes)

    def slot(self):
        sender = self.sender()
        self.changer(sender)

    def changer(self, btn):
        num = int(btn.text())
        if num < 9:
            num += 1
        else:
            num = 1
        btn.setText(str(num))


def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
