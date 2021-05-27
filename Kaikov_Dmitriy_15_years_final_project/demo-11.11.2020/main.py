import sys, sqlite3, random

from PyQt5 import uic
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel, QListWidgetItem, QLineEdit, \
    QTableWidgetItem, QShortcut
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel

name = ''
name_path = ''
var = []
PATH_for_edit = ''

TEXT = "В вашем списке должно быть не менее 4-х слов\n                       для этого режима"

def cose_error(learn, x):
    pbox = [learn.lb6q, learn.lb3q, learn.lbq, learn.lb4q, learn.lb2q, learn.textEdit]
    box = [learn.pbq, learn.pb_next_error, learn.lbq, learn.lb5q, learn.lb7q]
    box.extend(pbox)
    if x:
        learn.lb5q.setText(learn.lb0.text())
        learn.lb6q.setText(learn.sender().text())
        learn.lb7q.setText(learn.dect[learn.lb0.text()])
        for i in box:
            i.show()
    else:
        for i in box:
            i.hide()


def error_Nofolder(self, x):
    list_of_widget = [self.lb_Nofolder_w, self.lb_Nofolder_s, self.lb_Nofolder_p]
    if x == 0:
        [widget.hide() for widget in list_of_widget]
    else:
        [widget.show() for widget in list_of_widget]


def convert_to_form():
    fl = sqlite3.connect(name)
    sql = fl.cursor()
    q = sql.execute(f"""SELECT id FROM folders WHERE name = '{name_path}';""").fetchall()
    q = q[0][0]
    sp = sql.execute(f"""SELECT orig, trans FROM lists WHERE id = {q};""").fetchall()
    fl.close()

    box = []
    for orig, trans in zip(sp[0][0].split(';'), sp[0][1].split(';')):
        box.append([orig, trans, 0])
    return box


def error_1(edit):
    edit.pushButton.hide()
    edit.pb_HaveModul.show()

print()
def insert_folders(edit):

    edit.list_of_folders.clear()
    con = sqlite3.connect(PATH_for_edit)
    cur = con.cursor()
    edit.r = cur.execute(
        """SELECT id, name FROM folders""").fetchall()
    n = len(edit.r)

    con.close()

    edit.box = []
    edit.box_of_widgetitem = []

    for i in range(n):
        itemN = QListWidgetItem()
        # Create widget

        widget = QWidget()
        edit.horizontalLayoutWidget = QtWidgets.QWidget(edit)
        edit.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 280, 311, 31))
        edit.horizontalLayout = QtWidgets.QHBoxLayout(edit.horizontalLayoutWidget)
        edit.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        edit.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        edit.horizontalLayout.setSpacing(60)
        edit.label = QtWidgets.QLabel(edit.horizontalLayoutWidget)
        edit.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit.label.sizePolicy().hasHeightForWidth())
        edit.label.setSizePolicy(sizePolicy)
        edit.label.setMinimumSize(QtCore.QSize(25, 25))
        edit.label.setMaximumSize(QtCore.QSize(25, 25))
        edit.label.setText("")
        edit.label.setPixmap(QtGui.QPixmap("list.png"))
        edit.label.setScaledContents(True)
        edit.horizontalLayout.addWidget(edit.label)
        edit.label_2 = QtWidgets.QLabel(edit.r[i][1], edit.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit.label_2.sizePolicy().hasHeightForWidth())
        edit.label_2.setSizePolicy(sizePolicy)
        edit.label_2.setMinimumSize(QtCore.QSize(100, 25))
        edit.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        edit.horizontalLayout.addWidget(edit.label_2)

        font = QtGui.QFont()
        font.setPointSize(12)
        edit.label_2.setFont(font)

        edit.pb_minus = QtWidgets.QPushButton("-", edit.horizontalLayoutWidget)
        edit.pb_minus.setMinimumSize(QtCore.QSize(25, 25))
        edit.pb_minus.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        edit.pb_minus.setFont(font)
        edit.pb_minus.setStyleSheet("color:rgb(255, 90, 90)")
        edit.pb_minus.setObjectName("pb_minus")
        edit.horizontalLayout.addWidget(edit.pb_minus)

        widget.setLayout(edit.horizontalLayout)
        itemN.setSizeHint(widget.sizeHint())

        # Add widget to QListWidget funList
        edit.list_of_folders.addItem(itemN)
        edit.list_of_folders.setItemWidget(itemN, widget)

        edit.pb_minus.clicked.connect(edit.del_folder)

        edit.box.append(edit.pb_minus)
        edit.box_of_widgetitem.append(itemN)

    itemN = QListWidgetItem()
    widget = QWidget()


    edit.horizontalLayoutWidget_2 = QtWidgets.QWidget(edit)
    edit.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 380, 341, 31))
    edit.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
    edit.horizontalLayout_2 = QtWidgets.QHBoxLayout(edit.horizontalLayoutWidget_2)
    edit.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
    edit.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
    edit.horizontalLayout_2.setSpacing(60)
    edit.pb_pluse = QtWidgets.QPushButton("+", edit.horizontalLayoutWidget_2)
    edit.pb_pluse.setMinimumSize(QtCore.QSize(25, 25))
    edit.pb_pluse.setMaximumSize(QtCore.QSize(25, 25))
    font = QtGui.QFont()
    font.setPointSize(18)
    font.setBold(True)
    font.setWeight(75)
    font.setStrikeOut(False)
    edit.pb_pluse.setFont(font)
    edit.pb_pluse.setStyleSheet("color:rgb(34, 197, 25)")
    edit.horizontalLayout_2.addWidget(edit.pb_pluse)

    widget.setLayout(edit.horizontalLayout_2)
    itemN.setSizeHint(widget.sizeHint())

    edit.list_of_folders.addItem(itemN)
    edit.list_of_folders.setItemWidget(itemN, widget)



    edit.list_of_folders.setStyleSheet("""QListView {
        show-decoration-selected: 1; /* make the selection span the entire width of the view */
    }

    QListView::item:alternate {
        background: #EEEEEE;
    }

    QListView::item:selected {
        border: 1px solid #6a6ea9;
    }

    QListView::item:selected:!active {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0 #ABAFE5, stop: 1 #8588B2);
    }

    QListView::item:selected:active {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0 #6a6ea9, stop: 1 #888dd9);
    }

    QListView::item:hover {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0 #FAFBFE, stop: 1 #DCDEF1);
    }""")

    QtCore.QMetaObject.connectSlotsByName(edit)

    _translate = QtCore.QCoreApplication.translate
    edit.setWindowTitle(_translate("edit", "edit"))
    __sortingEnabled = edit.list_of_folders.isSortingEnabled()
    edit.list_of_folders.setSortingEnabled(False)
    edit.list_of_folders.setSortingEnabled(__sortingEnabled)

    edit.pb_pluse.clicked.connect(edit.add_folder)

    edit.list_of_folders.itemDoubleClicked.connect(edit.build_tabel)
    edit.list_of_folders.itemClicked.connect(edit.get_index)


def pryatki(edit, n):
    edit.table_of_words.hide()
    edit.error_but.hide()
    edit.pb_to_folders.hide()
    if n:
        edit.list_of_folders.show()
        edit.pb_add_to_table.show()
        edit.pb_del_to_table.show()
        edit.pb_safe_to_table.show()
        edit.le_change_name.show()
        edit.pb_change_name.show()
    else:
        edit.list_of_folders.hide()
        edit.pb_add_to_table.hide()
        edit.pb_del_to_table.hide()
        edit.pb_safe_to_table.hide()
        edit.le_change_name.hide()
        edit.pb_change_name.hide()

def error_Nolist(self, n):
    list_of_widget = [self.lb_Nolist_w, self.lb_Nolist_s, self.lb_Nolist_p]
    if n:
        [widget.show() for widget in list_of_widget]
    else:
        [widget.hide() for widget in list_of_widget]


class Menu(QMainWindow):
    def __init__(self, *args):
        super(Menu, self).__init__()
        uic.loadUi('Menu.ui', self)

        self.pb_learn.clicked.connect(self.learnivaniye)
        self.pb_kart.clicked.connect(self.kartochki)
        self.pb_select.clicked.connect(self.select)
        self.pb_edit.clicked.connect(self.edit)
        self.pb_info.clicked.connect(self.info)
        self.pb_folder.clicked.connect(self.open_db)
        self.sp = []
        self.lb_No_4.hide()
        self.lb_No_4.setText(TEXT)
        self.le_folder.setText(name.split('/')[-1])
        self.pb_list.hide()
        self.list_of_folders.hide()
        self.pb_list.clicked.connect(self.build_list)
        self.le_list.hide()
        self.lb_No_1.hide()

        error_Nofolder(self, 0)
        error_Nolist(self, 0)

        if name_path != '':
            self.pb_list.show()
            self.le_list.show()
            self.le_list.setText(name_path)


    def error_chek_1_4(self):
        if name == '':
            error_Nofolder(self, 1)
            raise 1
        if name_path == '':
            self.list_of_folders.hide()
            error_Nolist(self, 1)
            raise 1


    def learnivaniye(self):
        self.list_of_folders.hide()
        try:
            self.error_chek_1_4()
            n = len(convert_to_form())
            if n >= 4:
                self.lb_No_4.hide()
                self.learnivaniye = Learning(self)
                self.hide()
                self.learnivaniye.show()
            else:
                self.lb_No_1.hide()
                self.lb_No_4.show()
        except:
            pass


    def kartochki(self):
        self.list_of_folders.hide()
        try:
            self.error_chek_1_4()
            n = convert_to_form()[0][0]
            if n != '':
                self.kartochki = Kartochki(self)
                self.hide()
                self.kartochki.show()
            else:
                self.lb_No_4.hide()
                self.lb_No_1.show()
        except:
            pass

    def select(self):
        self.list_of_folders.hide()
        try:
            self.error_chek_1_4()
            n = len(convert_to_form())
            if n >= 4:
                self.select = Selection(self)
                self.hide()
                self.select.show()
            else:
                self.lb_No_1.hide()
                self.lb_No_4.show()
        except:
            pass

    def edit(self):
        self.edit = Edit(self)
        self.hide()
        self.edit.show()

    def info(self):
        self.info = Info(self)
        self.info.show()

    def open_db(self):
        dialog_name = 'Please choose some file to open'
        folder_init_name = './'
        filename = QFileDialog.getOpenFileName(self, dialog_name, folder_init_name, "Data Base file (*.db)")
        filename = filename[0]
        if filename != '':
            self.le_folder.setText(filename.split('/')[-1])
            global name
            name = filename
            error_Nofolder(self, 0)
            self.pb_list.show()
        self.lb_No_4.hide()


    def build_list(self):
        self.lb_No_4.hide()
        self.lb_No_1.hide()
        self.le_list.hide()
        error_Nolist(self, 0)
        self.list_of_folders.show()
        self.list_of_folders.clear()
        con = sqlite3.connect(name)
        cur = con.cursor()
        self.r = cur.execute(
            """SELECT id, name FROM folders""").fetchall()
        n = len(self.r)

        con.close()

        self.box_of_widgetitem = []
                                   #эта часть запалняет list_of_folders названиями литов с картинкой
#-----------------------------------------------------------------------------------------------------------------------
        for i in range(n):
            itemN = QListWidgetItem()
            # Create widget

            widget = QWidget()
            self.horizontalLayoutWidget = QtWidgets.QWidget(self)
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 280, 311, 31))
            self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
            self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout.setSpacing(60)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.lab = QtWidgets.QLabel(self.horizontalLayoutWidget)
            self.lab.setEnabled(True)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.lab.sizePolicy().hasHeightForWidth())
            self.lab.setSizePolicy(sizePolicy)
            self.lab.setMinimumSize(QtCore.QSize(25, 25))
            self.lab.setMaximumSize(QtCore.QSize(25, 25))
            self.lab.setText("")
            self.lab.setPixmap(QtGui.QPixmap("list.png"))
            self.lab.setScaledContents(True)

            self.horizontalLayout.addWidget(self.lab)
            self.lab_2 = QtWidgets.QLabel(self.r[i][1], self.horizontalLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.lab_2.sizePolicy().hasHeightForWidth())
            self.lab_2.setSizePolicy(sizePolicy)
            self.lab_2.setMinimumSize(QtCore.QSize(100, 25))
            self.lab_2.setMaximumSize(QtCore.QSize(16777215, 25))

            self.horizontalLayout.addWidget(self.lab_2)

            font = QtGui.QFont()
            font.setPointSize(12)
            self.lab_2.setFont(font)


            widget.setLayout(self.horizontalLayout)
            itemN.setSizeHint(widget.sizeHint())

            # Add widget to QListWidget funList
            self.list_of_folders.addItem(itemN)
            self.list_of_folders.setItemWidget(itemN, widget)
#-----------------------------------------------------------------------------------------------------------------------
            self.box_of_widgetitem.append(itemN)
        self.list_of_folders.itemDoubleClicked.connect(self.user_choose)


    def user_choose(self, item):
        id = self.box_of_widgetitem.index(item)
        self.le_list.show()
        nm = self.r[id][1]
        global name_path
        name_path = nm
        if len(nm) > 16:
            nm = nm[:13] + '...'
        self.le_list.setText("Выбран список: " + nm)
        self.list_of_folders.hide()

        convert_to_form()


class Learning(QWidget):
    def __init__(learn, *argv):
        super(Learning, learn).__init__()
        uic.loadUi('Learning.ui', learn)
        learn.setWindowTitle('LiteLearn')

        learn.list_of_widget = [learn.pb0, learn.pb1, learn.pb2, learn.pb3]
        [widget.clicked.connect(learn.next_question) for widget in learn.list_of_widget]
        learn.pb.clicked.connect(learn.cose)

        learn.box = convert_to_form()
        learn.e = learn.box

        learn.tok = 0

        learn.qbox0 = []
        learn.qbox1 = []
        learn.dect = {}
        for i in learn.box:
            learn.dect[i[0]] = i[1]
            learn.dect[i[1]] = i[0]
            learn.qbox0.append(i[0])
            learn.qbox1.append(i[1])
        learn.n0 = random.randint(1, len(learn.box))
        learn.n1 = len(learn.box) - learn.n0

        sp0 = []
        for i in range(learn.n0):
            sp0.append(0)
        for i in range(learn.n1):
            sp0.append(1)
        random.shuffle(sp0)
        learn.bigSlov = {}
        learn.c = 0
        for i in range(len(learn.box)):
            learn.c += 1
            if sp0[i]:
                q = [learn.box[i][0]]
                r = learn.qbox0.copy()
                r.pop(r.index(learn.box[i][0]))
                q.extend(random.sample(r, 3))
            else:
                q = [learn.box[i][1]]
                r = learn.qbox1.copy()
                r.pop(r.index(learn.box[i][1]))
                q.extend(random.sample(r, 3))
            learn.bigSlov[learn.box[i][sp0[i]]] = q

                          #Эта часть кода выводит табличку ошибки ,где указаны слова в кот. сдел. ош и т.д.
#-----------------------------------------------------------------------------------------------------------------------
        learn.pbq = QtWidgets.QPushButton(learn)
        learn.pbq.setEnabled(False)
        learn.pbq.setGeometry(QtCore.QRect(70, 80, 831, 51))
        learn.pbq.setStyleSheet("background-color: #ff6e61;")
        learn.pbq.setText("")
        learn.textEdit = QtWidgets.QTextEdit(learn)
        learn.textEdit.setEnabled(False)
        learn.textEdit.setGeometry(QtCore.QRect(70, 130, 831, 391))
        learn.lbq = QtWidgets.QLabel("НЕПРАВИЛЬНО", learn)
        learn.lbq.setGeometry(QtCore.QRect(80, 100, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        learn.lbq.setFont(font)
        learn.lbq.setStyleSheet("color: white;")
        learn.lb5q = QtWidgets.QLabel(learn)
        learn.lb5q.setGeometry(QtCore.QRect(100, 170, 791, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        learn.lb5q.setFont(font)
        learn.lb7q = QtWidgets.QLabel(learn)
        learn.lb7q.setGeometry(QtCore.QRect(100, 260, 781, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        learn.lb7q.setFont(font)
        learn.lb6q = QtWidgets.QLabel(learn)
        learn.lb6q.setGeometry(QtCore.QRect(100, 360, 791, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        learn.lb6q.setFont(font)
        learn.pb_next_error = QtWidgets.QPushButton("Продолжить", learn)
        learn.pb_next_error.setGeometry(QtCore.QRect(340, 420, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        learn.pb_next_error.setFont(font)
        learn.pb_next_error.setStyleSheet("background-color:rgb(241, 241, 241);\n"
                                "border: 3px  solid rgb(241, 241, 241);\n"
                                "color:rgb(87, 137, 255);")
        learn.lb3q = QtWidgets.QLabel("ВЫ ОТВЕТИЛИ:", learn)
        learn.lb3q.setGeometry(QtCore.QRect(90, 330, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        learn.lb3q.setFont(font)
        learn.lb3q.setStyleSheet("color:rgb(255, 116, 103)")
        learn.lb2q = QtWidgets.QLabel(learn)
        learn.lb2q.setGeometry(QtCore.QRect(80, 310, 811, 3))
        learn.lb2q.setStyleSheet("background-color: rgb(181, 181, 181)")
        learn.lb2q.setText("")
        learn.lb4q = QtWidgets.QLabel("ПРАВИЛЬНЫЙ ОТВЕТ:", learn)
        learn.lb4q.setGeometry(QtCore.QRect(90, 220, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        learn.lb4q.setFont(font)
        learn.lb4q.setStyleSheet("color:rgb(95, 202, 78)")

        QtCore.QMetaObject.connectSlotsByName(learn)

        _translate = QtCore.QCoreApplication.translate
        learn.setWindowTitle(_translate("learn", "learn"))
        learn.textEdit.setHtml(_translate("learn",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))

                               #следуйщий отрезок отвечает за конец тренеровки прграммы (кнопки отр. ош. и продолжить)
#-----------------------------------------------------------------------------------------------------------------------
        learn.groupBox_2 = QtWidgets.QGroupBox(learn)
        learn.groupBox_2.setGeometry(QtCore.QRect(-1, -1, 981, 651))
        learn.groupBox_2.setTitle("")
        learn.label = QtWidgets.QLabel(learn.groupBox_2)
        learn.label.setGeometry(QtCore.QRect(430, 70, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        learn.label.setFont(font)
        learn.pb_work_error = QtWidgets.QPushButton(learn.groupBox_2)
        learn.pb_work_error.setGeometry(QtCore.QRect(329, 240, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        learn.pb_work_error.setFont(font)
        learn.pb_work_error.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(46, 226, 226);\n"
                                       "border: 3px  solid rgb(46, 226, 226);\n"
                                       "color: white\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "border: 2px  solid #26bdbd;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "background-color: #26bdbd;\n"
                                       "border: 3px  solid #26bdbd;\n"
                                       "color: white\n"
                                       "}")
        learn.pb_next_again = QtWidgets.QPushButton(learn.groupBox_2)
        learn.pb_next_again.setGeometry(QtCore.QRect(329, 310, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        learn.pb_next_again.setFont(font)
        learn.pb_next_again.setStyleSheet("QPushButton {\n"
                                         "background-color: rgb(46, 226, 226);\n"
                                         "border: 3px  solid rgb(46, 226, 226);\n"
                                         "color: white\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "border: 2px  solid #26bdbd;\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "background-color: #26bdbd;\n"
                                         "border: 3px  solid #26bdbd;\n"
                                         "color: white\n"
                                         "}\n"
                                         "")

        learn.label_2_2 = QtWidgets.QLabel(learn.groupBox_2)
        learn.label_2_2.setGeometry(QtCore.QRect(350, 130, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        learn.label_2_2.setFont(font)
        learn.label_3_2 = QtWidgets.QLabel(learn.groupBox_2)
        learn.label_3_2.setGeometry(QtCore.QRect(470, 170, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        learn.label_3_2.setFont(font)
        learn.label_4_2 = QtWidgets.QLabel(learn.groupBox_2)
        learn.label_4_2.setGeometry(QtCore.QRect(380, 70, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        learn.label_4_2.setFont(font)
        learn.label_5_2 = QtWidgets.QLabel(learn.groupBox_2)
        learn.label_5_2.setGeometry(QtCore.QRect(330, 70, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        learn.label_5_2.setFont(font)
        learn.label_6_2 = QtWidgets.QLabel(learn.groupBox_2)
        learn.label_6_2.setGeometry(QtCore.QRect(430, 70, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        learn.label_6_2.setFont(font)

        learn.list_of_error = QtWidgets.QListWidget(learn.groupBox_2)
        learn.list_of_error.setGeometry(QtCore.QRect(330, 410, 321, 192))
        font = QtGui.QFont()
        font.setPointSize(14)
        learn.list_of_error.setFont(font)

        learn.label_7_2 = QtWidgets.QLabel(learn.groupBox_2)
        learn.label_7_2.setGeometry(QtCore.QRect(330, 380, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        learn.label_7_2.setFont(font)



        _translate = QtCore.QCoreApplication.translate
        learn.label.setText(_translate("Form", "МОЛОДЕЦ"))
        learn.pb_work_error.setText(_translate("Form", "Отработать\n"
                                                    "ошибки"))
        learn.pb_next_again.setText(_translate("Form", "Продолжить"))
        learn.label_2_2.setText(_translate("Form", "ТВОЙ РЕЗУЛЬТАТ:"))
        learn.label_3_2.setText(_translate("Form", "0/0"))
        learn.label_4_2.setText(_translate("Form", "СТАРАЙСЯ ЛУЧШЕ"))
        learn.label_5_2.setText(_translate("Form", "ТЫ УВЕРННО ИДЁШЬ К ЦЕЛИ"))
        learn.label_6_2.setText(_translate("Form", "ОТЛИЧНО"))
        learn.label_7_2.setText(_translate("Form", "Ошибки"))
#-----------------------------------------------------------------------------------------------------------------------

        learn.label.hide()
        learn.label_4_2.hide()
        learn.label_5_2.hide()
        learn.label_6_2.hide()



        learn.groupBox_2.hide()

        learn.doc = list(learn.bigSlov)
        learn.doc1 = []

        learn.pb_close = QPushButton('<', learn)
        learn.pb_close.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        learn.pb_close.setFont(font)
        learn.pb_close.setStyleSheet("QPushButton {\n"
                                "background-color: #ffce3a;\n"
                                "border-radius: 5;\n"
                                "color: white\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "border: 3px  solid #dc9300;\n"
                                "}\n"
                                "QPushButton:pressed {\n"
                                "background-color: #f5b432;\n"
                                "}")

        learn.pb_close.hide()

        learn.pb_next_again.clicked.connect(learn.restart_error)
        learn.pb_work_error.clicked.connect(learn.restart_again)
        learn.pb_close.clicked.connect(learn.cose)
        learn.pb_next_error.clicked.connect(learn.start)

        cose_error(learn, 0)
        learn.start()


    def next_question(learn):
        if learn.lb0.text() != learn.dect[learn.sender().text()]:
            print('error')
            learn.pb.hide()
            [widget.hide() for widget in learn.list_of_widget]
            learn.lb0.hide()
            learn.lb1.hide()

            cose_error(learn, 1)
            learn.tok += 1

            learn.doc1.append(learn.lb0.text())

        elif learn.lb0.text() == learn.dect[learn.sender().text()]:

            learn.tok += 1
            learn.start()


    def restart_error(learn):
        learn.label.hide()
        learn.label_4_2.hide()
        learn.label_5_2.hide()
        learn.label_6_2.hide()

        learn.groupBox_2.hide()
        learn.tok = 0
        learn.c = len(list(learn.bigSlov))

        learn.doc1 = []

        learn.n0 = random.randint(1, len(learn.box))
        learn.n1 = len(learn.box) - learn.n0
        sp0 = []
        for i in range(learn.n0):
            sp0.append(0)
        for i in range(learn.n1):
            sp0.append(1)
        random.shuffle(sp0)
        learn.bigSlov = {}
        for i in range(len(learn.box)):
            if sp0[i]:
                q = [learn.box[i][0]]
                r = learn.qbox0.copy()
                r.pop(r.index(learn.box[i][0]))
                q.extend(random.sample(r, 3))
            else:
                q = [learn.box[i][1]]
                r = learn.qbox1.copy()
                r.pop(r.index(learn.box[i][1]))
                q.extend(random.sample(r, 3))
            learn.bigSlov[learn.box[i][sp0[i]]] = q
        learn.doc = list(learn.bigSlov)

        learn.list_of_error.clear()
        learn.pb_close.hide()

        learn.start()

    def restart_again(learn):
        learn.label.hide()
        learn.label_4_2.hide()
        learn.label_5_2.hide()
        learn.label_6_2.hide()

        learn.doc = learn.doc1

        learn.groupBox_2.hide()
        learn.tok = 0
        print(learn.doc1)
        learn.doc1 = []
        learn.c = len(learn.doc)

        learn.list_of_error.clear()
        learn.pb_close.hide()

        learn.start()



    def start(learn):
        if learn.tok != learn.c:
            learn.pb.show()
            [widget.show() for widget in learn.list_of_widget]
            learn.lb0.show()
            learn.lb1.show()
            cose_error(learn, 0)
            print(learn.doc, learn.tok, learn.bigSlov[learn.doc[0]])
            q = learn.tok
            w = learn.doc
            r = learn.bigSlov[w[q]].copy()


            learn.lb0.setText(w[q])
            learn.lb1.setText(str(q + 1) + '/' + str(learn.c))

            u = [learn.pb0, learn.pb1, learn.pb2, learn.pb3]
            uio = [i for i in range(len(r))]
            random.shuffle(uio)
            for i in range(len(r)):
                u[i].setText(r[uio[i]])

        else:
            if learn.doc1 == []:
                learn.pb_work_error.hide()
                learn.label_7_2.hide()
                learn.list_of_error.hide()
            else:
                learn.pb_work_error.show()
                learn.label_7_2.show()
                learn.list_of_error.show()
            learn.tok = 0
            learn.pb0.hide()
            learn.pb1.hide()
            learn.pb2.hide()
            learn.pb3.hide()
            learn.lb0.hide()
            learn.lb1.hide()
            cose_error(learn, 0)
            learn.groupBox_2.show()

            learn.label_3_2.setText(str(learn.c - len(learn.doc1)) + '/' + str(learn.c))
            pr = (learn.c - len(learn.doc1)) * (100 / learn.c)


            if learn.c - len(learn.doc1) == learn.c:
                learn.label_6_2.show()
            elif pr >= 70 and pr < 100:
                learn.label.show()
            elif pr >= 50 and pr < 70:
                learn.label_5_2.show()
            elif pr >= 0 and pr < 50:
                learn.label_4_2.show()

            for i in learn.doc1:
                if i in learn.qbox0:
                    q = i + '-' + learn.qbox1[learn.qbox0.index(i)]
                else:
                    q = learn.qbox0[learn.qbox1.index(i)] + '-' + i
                learn.list_of_error.addItem(q)

            learn.pb_close.show()
            learn.pb.hide()
            learn.pb.clicked.connect(learn.cose)


    def cose(learn):
        learn.menu = Menu(learn)
        learn.hide()
        learn.menu.show()


class Kartochki(QWidget):
    def __init__(kart, *args):
        super(Kartochki, kart).__init__()
        uic.loadUi('Kartochki.ui', kart)
        kart.tf = 0
        kart.n = 0

        kart.bqbox = []

        kart.pb_close.clicked.connect(kart.cose)
        kart.pb_kart.clicked.connect(kart.upend_kart)
        kart.pb_no.clicked.connect(kart.next_kart)
        kart.pb_yes.clicked.connect(kart.next_kart)
        kart.pb_back.clicked.connect(kart.back_kart)

        kart.group_of_widget = [kart.pb_close, kart.pb_kart, kart.pb_back, kart.pb_yes, kart.pb_no, kart.lb_count]

        kart.slov = convert_to_form()

        kart.num = len(kart.slov)
        print(kart.slov[kart.n][kart.tf])
        kart.cb_of_valuesox = kart.slov

                              #часть кода отвечает за меню после тренеровки в режиме (продолжить или начать заного)
#-----------------------------------------------------------------------------------------------------------------------
        kart.groupBox = QtWidgets.QGroupBox(kart)
        kart.groupBox.setGeometry(QtCore.QRect(0, 0, 980, 650))
        kart.groupBox.setTitle("")
        kart.label_2 = QtWidgets.QLabel(kart.groupBox)
        kart.label_2.setGeometry(QtCore.QRect(410, 60, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        kart.label_2.setFont(font)
        kart.pb_start_again = QtWidgets.QPushButton(kart.groupBox)
        kart.pb_start_again.setGeometry(QtCore.QRect(310, 390, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        kart.pb_start_again.setFont(font)
        kart.pb_start_again.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(46, 226, 226);\n"
                                        "border: 3px  solid rgb(46, 226, 226);\n"
                                        "color: white\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border: 2px  solid #26bdbd;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: #26bdbd;\n"
                                        "border: 3px  solid #26bdbd;\n"
                                        "color: white\n"
                                        "}\n"
                                        "")
        kart.label = QtWidgets.QLabel(kart.groupBox)
        kart.label.setGeometry(QtCore.QRect(380, 140, 521, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        kart.label.setFont(font)
        kart.label_5 = QtWidgets.QLabel(kart.groupBox)
        kart.label_5.setGeometry(QtCore.QRect(310, 60, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        kart.label_5.setFont(font)
        kart.pb_work_error = QtWidgets.QPushButton(kart.groupBox)
        kart.pb_work_error.setGeometry(QtCore.QRect(310, 290, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        kart.pb_work_error.setFont(font)
        kart.pb_work_error.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(46, 226, 226);\n"
                                        "border: 3px  solid rgb(46, 226, 226);\n"
                                        "color: white\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border: 2px  solid #26bdbd;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: #26bdbd;\n"
                                        "border: 3px  solid #26bdbd;\n"
                                        "color: white\n"
                                        "}\n"
                                        "")
        kart.label_4 = QtWidgets.QLabel(kart.groupBox)
        kart.label_4.setGeometry(QtCore.QRect(360, 60, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        kart.label_4.setFont(font)
        kart.label_6 = QtWidgets.QLabel(kart.groupBox)
        kart.label_6.setGeometry(QtCore.QRect(400, 60, 120, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        kart.label_6.setFont(font)
        kart.pb__2 = QtWidgets.QPushButton(kart.groupBox)
        kart.pb__2.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        kart.pb__2.setFont(font)
        kart.pb__2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        kart.pb__2.setStyleSheet("QPushButton {\n"
                                 "background-color: #ffce3a;\n"
                                 "border-radius: 5;\n"
                                 "color: white\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "border: 3px  solid #dc9300;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "background-color: #f5b432;\n"
                                 "}")

        QtCore.QMetaObject.connectSlotsByName(kart)

        _translate = QtCore.QCoreApplication.translate
        kart.setWindowTitle(_translate("kart", "kart"))
        kart.label_2.setText(_translate("kart", "МОЛОДЕЦ"))
        kart.pb_start_again.setText(_translate("kart", "Начать заного"))
        kart.label.setText(_translate("kart", "Вы выучили x\n"
                                              "      из y"))
        kart.label_5.setText(_translate("kart", "ТЫ УВЕРННО ИДЁШЬ К ЦЕЛИ"))
        kart.pb_work_error.setText(_translate("kart", "Продолжить"))
        kart.label_4.setText(_translate("kart", "СТАРАЙСЯ ЛУЧШЕ"))
        kart.label_6.setText(_translate("kart", "ОТЛИЧНО"))
        kart.pb__2.setText(_translate("kart", "<"))
#-----------------------------------------------------------------------------------------------------------------------
        kart.pb__2.clicked.connect(kart.cose)

        kart.pb_work_error.clicked.connect(kart.restart_again)
        kart.pb_start_again.clicked.connect(kart.restart_error)
        kart.groupBox.hide()

        kart.start()


    def upend_kart(kart):
        kart.tf = (kart.tf + 1) % 2
        kart.start()

    def next_kart(kart):
        if kart.sender().text() == "Запомнил":
            kart.cb_of_valuesox[kart.n][2] = 1
        else:
            kart.cb_of_valuesox[kart.n][2] = -1
        kart.n += 1
        kart.tf = 0
        kart.start()

    def back_kart(kart):
        kart.n -= 1
        kart.tf = 0
        kart.start()

    def restart_error(kart):
        [widget.show() for widget in kart.group_of_widget]

        kart.n = 0
        kart.tf = 0
        kart.cb_of_valuesox = kart.slov
        kart.num = len(kart.cb_of_valuesox)
        kart.bqbox = []
        kart.groupBox.hide()
        kart.start()

    def restart_again(kart):
        [widget.show() for widget in kart.group_of_widget]

        kart.n = 0
        kart.tf = 0
        kart.cb_of_valuesox = kart.bqbox
        kart.bqbox = []
        kart.num = len(kart.cb_of_valuesox)
        kart.groupBox.hide()
        kart.start()

    def start(kart):
        if len(kart.cb_of_valuesox) == kart.n:
            for i in kart.cb_of_valuesox:
                if i[2] == -1:
                    kart.bqbox.append(i)

            [widget.hide() for widget in kart.group_of_widget]

            num = len(kart.slov) -  len(kart.bqbox)

            kart.groupBox.show()
            kart.label.setText("Вы выучили x\n      из y".replace('x', str(num)).replace('y', str(len(kart.slov))))

            kart.label_2.hide()
            kart.label_6.hide()
            kart.label_4.hide()
            kart.label_5.hide()

            pr = num / len(kart.slov) * 100

            if num == len(kart.slov):
                kart.label_6.show()
            elif pr >= 0 and pr < 50:
                kart.label_4.show()
            elif pr >= 50 and pr < 75:
                kart.label_5.show()
            elif pr >= 75 and pr < 100:
                kart.label_2.show()


        elif kart.n == -1:
            kart.n = 0
            kart.tf = 0
            kart.start()
        else:
            print(kart.cb_of_valuesox)
            kart.lb_count.setText(str(kart.n + 1 ) + " / " + str(kart.num))
            kart.pb_kart.setText(kart.cb_of_valuesox[kart.n][kart.tf])


    def cose(kart):
        kart.menu = Menu(kart)
        kart.hide()
        kart.menu.show()


class Selection(QWidget):
    def __init__(select, *args):
        super().__init__()
        select.initUi()

    def initUi(select):
        select.box = []


        select.slov = convert_to_form()
        select.num = len(select.slov)
        select.mozno = select.get_values()

        select.setObjectName("select")
        select.resize(980, 650)
                   #эта часть кода отвечает за создание меню выбара размера поля для карточек
#-----------------------------------------------------------------------------------------------------------------------
        select.gb = QtWidgets.QGroupBox(select)
        select.gb.setGeometry(QtCore.QRect(260, 130, 460, 201))
        font = QtGui.QFont()
        font.setPointSize(11)
        select.gb.setFont(font)
        select.gb.setTitle("")
        select.gb.setObjectName("gb")
        select.cb_of_values = QtWidgets.QComboBox(select.gb)
        select.cb_of_values.setGeometry(QtCore.QRect(309, 54, 141, 24))
        select.cb_of_values.setStyleSheet("QComboBox {\n"
                                   "    border: 1px solid gray;\n"
                                   "    border-radius: 3px;\n"
                                   "    padding: 1px 18px 1px 3px;\n"
                                   "    min-width: 6em;\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox:editable {\n"
                                   "    background: white;\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                   "     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                   "                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                   "                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                   "}\n"
                                   "\n"
                                   "/* QComboBox gets the \"on\" state when the popup is open */\n"
                                   "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
                                   "    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                   "                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
                                   "                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox:on { /* shift the text when the popup opens */\n"
                                   "    padding-top: 3px;\n"
                                   "    padding-left: 4px;\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox::drop-down {\n"
                                   "    subcontrol-origin: padding;\n"
                                   "    subcontrol-position: top right;\n"
                                   "    width: 15px;\n"
                                   "\n"
                                   "    border-left-width: 1px;\n"
                                   "    border-left-color: darkgray;\n"
                                   "    border-left-style: solid; /* just a single line */\n"
                                   "    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                   "    border-bottom-right-radius: 3px;\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox::down-arrow {\n"
                                   "    image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);\n"
                                   "}\n"
                                   "\n"
                                   "QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
                                   "    top: 1px;\n"
                                   "    left: 1px;\n"
                                   "}")
        select.cb_of_values.addItems(select.mozno)
        select.lb = QtWidgets.QLabel(select.gb)
        select.lb.setGeometry(QtCore.QRect(10, 30, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        select.lb.setFont(font)
        select.le = QtWidgets.QLineEdit(select.gb)
        select.le.setGeometry(QtCore.QRect(309, 30, 141, 25))
        select.pb0 = QtWidgets.QPushButton(select.gb)
        select.pb0.setGeometry(QtCore.QRect(90, 160, 130, 30))
        select.pb0.setStyleSheet("QPushButton {\n"
                              "background-color: #e2e2e2;\n"
                              "border: 2px  solid #8f8f8f;\n"
                              "border-radius: 0;\n"
                              "color: #595959\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "background-color: #f5f5f5;\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "background-color: #8f8f8f;\n"
                              "border: 3px  solid #8f8f8f;\n"
                              "border-radius: 0;\n"
                              "color: #595959\n"
                              "}")
        select.pb1 = QtWidgets.QPushButton(select.gb)
        select.pb1.setGeometry(QtCore.QRect(240, 160, 130, 30))
        select.pb1.setStyleSheet("QPushButton {\n"
                              "background-color: #e2e2e2;\n"
                              "border: 2px  solid #8f8f8f;\n"
                              "border-radius: 0;\n"
                              "color: #595959\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "background-color: #f5f5f5;\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "background-color: #8f8f8f;\n"
                              "border: 3px  solid #8f8f8f;\n"
                              "border-radius: 0;\n"
                              "color: #595959\n"
                              "}")
        select.lb.raise_()
        select.le.raise_()
        select.pb0.raise_()
        select.pb1.raise_()
        select.cb_of_values.raise_()

        QtCore.QMetaObject.connectSlotsByName(select)

        _translate = QtCore.QCoreApplication.translate
        select.setWindowTitle(_translate("select", "select"))
        select.lb.setText(_translate("select", "Количество карточек"))
        select.pb0.setText(_translate("select", "Запустить"))
        select.pb1.setText(_translate("select", "Выйти"))
#-----------------------------------------------------------------------------------------------------------------------
        select.pb1.clicked.connect(select.cose)
        select.pb0.clicked.connect(select.start)
        select.le.setText(select.mozno[0])
        select.cb_of_values.activated[str].connect(select.choose_value)




    def get_values(select):
        est = [[5, 4], [4, 4], [3, 4], [2, 3]]
        mozno = []
        for i in range(len(est)):
            if est[i][0] <= (select.num * 2) // est[i][1]:
                mozno.append(str(est[i][0]) + "x" + str(est[i][1]))
        if mozno == []:
            mozno.append("2x3")
        return mozno

    def choose_value(select, text):
        select.le.setText(text)

    def start(select):
        global var
        var = list(map(int, select.le.text().split('x')))
        select.ran = Ran(select)
        select.hide()
        select.ran.show()


    def cose(select):
        select.menu = Menu(select)
        select.hide()
        select.menu.show()


class Ran(QWidget):
    def __init__(ran, *args):
        super().__init__()
        ran.resize(980, 650)

        ran.tok = 0
                           #эта чать отвечает за картинку и кнопку после конца тренероки
#-----------------------------------------------------------------------------------------------------------------------
        ran.groupBox = QtWidgets.QGroupBox(ran)
        ran.groupBox.setGeometry(QtCore.QRect(0, 0, 980, 650))
        ran.groupBox.setTitle("")
        ran.groupBox.setObjectName("groupBox")
        ran.label_2 = QtWidgets.QLabel(ran.groupBox)
        ran.label_2.setGeometry(QtCore.QRect(440, 110, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        ran.label_2.setFont(font)
        ran.label_2.setObjectName("label_2")
        ran.pb_again = QtWidgets.QPushButton(ran.groupBox)
        ran.pb_again.setGeometry(QtCore.QRect(340, 530, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        ran.pb_again.setFont(font)
        ran.pb_again.setStyleSheet("QPushButton {\n"
                                       "background-color: rgb(46, 226, 226);\n"
                                       "border: 3px  solid rgb(46, 226, 226);\n"
                                       "color: white\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "border: 2px  solid #26bdbd;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "background-color: #26bdbd;\n"
                                       "border: 3px  solid #26bdbd;\n"
                                       "color: white\n"
                                       "}\n"
                                       "")
        ran.pb_again.setObjectName("pb_work_error")
        ran.pb_2 = QtWidgets.QPushButton(ran.groupBox)
        ran.pb_2.setGeometry(QtCore.QRect(10, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        ran.pb_2.setFont(font)
        ran.pb_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ran.pb_2.setStyleSheet("QPushButton {\n"
                             "background-color: #ffce3a;\n"
                             "border-radius: 5;\n"
                             "color: white\n"
                             "}\n"
                             "QPushButton:hover {\n"
                             "border: 3px  solid #dc9300;\n"
                             "}\n"
                             "\n"
                             "QPushButton:pressed {\n"
                             "background-color: #f5b432;\n"
                             "}")
        ran.label = QtWidgets.QLabel(ran.groupBox)
        ran.label.setGeometry(QtCore.QRect(110, 0, 771, 601))
        ran.label.setText("")
        ran.label.setPixmap(QtGui.QPixmap("smailik.png"))
        ran.label.raise_()
        ran.pb_again.raise_()
        ran.label_2.raise_()
        ran.pb_2.raise_()
        ran.groupBox.hide()

        QtCore.QMetaObject.connectSlotsByName(ran)

        _translate = QtCore.QCoreApplication.translate
        ran.setWindowTitle(_translate("ran", "ran"))
        ran.label_2.setText(_translate("ran", "МОЛОДЕЦ"))
        ran.pb_again.setText(_translate("ran", "Продолжить"))
        ran.pb_2.setText(_translate("ran", "<"))
#-----------------------------------------------------------------------------------------------------------------------
        ran.pb_again.clicked.connect(ran.close_to_Selection)


        ran.pb = QPushButton('<', ran)
        ran.pb.resize(50, 50)
        ran.pb.move(10, 10)
        ran.pb.clicked.connect(ran.cose)
        ran.pb.setStyleSheet("QPushButton {\n"
                                 "background-color: #ffce3a;\n"
                                 "border-radius: 5;\n"
                                 "color: white\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "border: 3px  solid #dc9300;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "background-color: #f5b432;\n"
                                 "}")

        ran.slov = convert_to_form()
        global var

        txt = var

        ran.list_of_button = [QPushButton(ran) for i in range(txt[0] * txt[1])]
        [i.clicked.connect(ran.click) for i in ran.list_of_button]
        tok = 0
        for i in range(txt[1]):
            for j in range(txt[0]):
                w = 880 // txt[1]
                h = 500 // txt[0]
                ran.list_of_button[tok].resize(w, h)
                ran.list_of_button[tok].move(w * i + 50, h * j + 100)
                tok += 1

        car = random.sample(ran.slov, (txt[0] * txt[1]) // 2)
        box = []
        ran.dect = {}
        tok = 0
        for i in car:
            ran.dect[i[0]] = i[1]
            ran.dect[i[1]] = i[0]
            tok += 1
            box.extend(i[:2])
        random.shuffle(box)

        for i in range(len(box)):
            ran.list_of_button[i].setText(box[i])
            ran.list_of_button[i].setStyleSheet(
    """
        QPushButton {
background-color: #e2e2e2;
border: 1px  solid #8f8f8f;
border-radius: 0;
color: #595959
}
QPushButton:hover {
background-color: #f5f5f5;
}
QPushButton:pressed {
background-color: #8f8f8f;
border: 3px  solid #8f8f8f;
border-radius: 0;
color: #595959
}
    """
)


        ran.word = ''
        ran.button = ''

    def click(ran):
        sn = ran.sender()
        txt = sn.text()

        if ran.word == '':
            ran.word = txt
            ran.button = sn
            ran.button.setStyleSheet(
    """
        QPushButton {
background-color: #f5f5f5;
border: 1px  solid #8f8f8f;
border-radius: 0;
color: #595959
}
QPushButton:hover {
background-color: #f5f5f5;
}
QPushButton:pressed {
background-color: #8f8f8f;
border: 3px  solid #8f8f8f;
border-radius: 0;
color: #595959
}
    """
)

        elif sn == ran.button:
            ran.word = ''
            ran.button.setStyleSheet(
                """
                    QPushButton {
background-color: #e2e2e2;
border: 2px  solid #8f8f8f;
border-radius: 0;
color: #595959
}
QPushButton:hover {
background-color: #f5f5f5;
}
QPushButton:pressed {
background-color: #8f8f8f;
border: 3px  solid #8f8f8f;
border-radius: 0;
color: #595959
}
                """
            )
            ran.button = ''


        else:
            print(ran.dect[txt])
            print(txt)
            if ran.dect[txt] == ran.word:
                ran.tok += 2
                sn.hide()
                ran.button.hide()
                ran.word = ''
                ran.button = ''
            if ran.tok == len(ran.list_of_button):
                ran.groupBox.show()

    def close_to_Selection(ran):
        ran.ran = Selection(ran)
        ran.hide()
        ran.ran.show()


    def cose(ran):
        ran.menu = Menu(ran)
        ran.hide()
        ran.menu.show()
        



class Edit(QWidget):
    def __init__(edit, *args):
        super(Edit, edit).__init__()
        uic.loadUi('Edit.ui', edit)
                               #эта часть кода отвечает за формы в которых размещаются данные из БД ,а так же кнопка для перемещения между формами
#-----------------------------------------------------------------------------------------------------------------------
        edit.table_of_words = QtWidgets.QTableWidget(edit)
        edit.table_of_words.setGeometry(QtCore.QRect(20, 250, 701, 371))
        edit.table_of_words.setRowCount(1)
        edit.table_of_words.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        edit.table_of_words.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        edit.table_of_words.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        edit.table_of_words.setHorizontalHeaderItem(1, item)
        edit.table_of_words.horizontalHeader().setDefaultSectionSize(340)
        item = edit.table_of_words.horizontalHeaderItem(0)
        item.setText("Word")
        item = edit.table_of_words.horizontalHeaderItem(1)
        item.setText("Translate")

        edit.table_of_words.verticalHeader().setVisible(False)


        edit.list_of_folders = QtWidgets.QListWidget(edit)
        edit.list_of_folders.setEnabled(True)
        edit.list_of_folders.setGeometry(QtCore.QRect(150, 280, 311, 251))

        edit.le_change_name = QLineEdit(edit)
        edit.le_change_name.resize(281, 31)
        edit.le_change_name.move(500, 430)

        edit.pb_change_name = QPushButton("Переименовать", edit)
        edit.pb_change_name.resize(281, 51)
        edit.pb_change_name.move(500, 480)
        edit.pb_change_name.setStyleSheet("""QPushButton {
                background-color: #e2e2e2;
                border: 2px  solid #8f8f8f;
                border-radius: 0;
                color: #595959
                    }
                QPushButton:hover {
                background-color: #f5f5f5;
                }
                QPushButton:pressed {
                background-color: #8f8f8f;
                border: 3px  solid #8f8f8f;
                border-radius: 0;
                color: #595959
                }
                """)



        edit.error_but = QtWidgets.QPushButton("Empty line", edit)
        edit.error_but.setGeometry(QtCore.QRect(360, 404, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        edit.error_but.setFont(font)
        edit.error_but.setStyleSheet("QPushButton {\n"
                                     "background-color: ;\n"
                                     "border-radius: 0;\n"
                                     "color: #ff6060\n"
                                     "}")
#-----------------------------------------------------------------------------------------------------------------------
        edit.table_of_words.cellClicked.connect(edit.coords_for_del_table)
        edit.le2.textChanged.connect(edit.check_write_to_creat)
        edit.pb_open.clicked.connect(edit.open_modul)
        edit.pb_creat.clicked.connect(edit.create_modul)
        edit.pb_add_to_table.clicked.connect(edit.add_words_to_tabel)
        edit.pb_del_to_table.clicked.connect(edit.del_in_table)
        edit.pb_safe_to_table.clicked.connect(edit.safe_table)
        edit.pb_change_name.clicked.connect(edit.change_name_folder)
        edit.pb_toStart.clicked.connect(edit.back_to_start)
        edit.pb_to_folders.clicked.connect(edit.back_to_folders)
        edit.pb6_2.clicked.connect(edit.cose)

        pryatki(edit, 0)
        edit.error_but.hide()
        edit.le_change_name.hide()
        edit.pb_change_name.hide()
        edit.pb_HaveModul.hide()
        edit.table_of_words.hide()

        edit.global_token = 0

        edit.shortcut_open1 = QShortcut(QKeySequence('Ctrl+Q'), edit)
        edit.shortcut_open1.activated.connect(edit.add_words_to_tabel)


        edit.shortcut_open2 = QShortcut(QKeySequence('Ctrl+W'), edit)
        edit.shortcut_open2.activated.connect(edit.del_in_table)


        edit.shortcut_open3 = QShortcut(QKeySequence('Ctrl+E'), edit)
        edit.shortcut_open3.activated.connect(edit.safe_table)


    def add_folder(edit):
        global PATH_for_edit
        con = sqlite3.connect(PATH_for_edit)
        cur = con.cursor()
        edit.r = cur.execute(
            """SELECT * FROM folders;""").fetchall()

        if len(edit.r) == 0:
            n = 1
        else:
            edit.r = cur.execute(
                """SELECT id FROM folders;""").fetchall()
            n = edit.r[-1][0] + 1

        name = str(n) + '_New_list'

        edit.r = cur.execute(f"""INSERT INTO folders (id, name) VALUES ({str(n)}, '{name}');""")

        edit.r = cur.execute(f"""INSERT INTO lists (id, name, orig, trans) VALUES ({str(n)}, {str(n)}, '', '');""")

        con.commit()
        con.close()

        insert_folders(edit)

    def del_folder(edit):

        n = edit.r[edit.box.index(edit.sender())][0]

        con = sqlite3.connect(PATH_for_edit)
        cur = con.cursor()

        r = cur.execute(f"""SELECT name FROM folders WHERE id = {str(n)};""").fetchall()
        if r[0][0] == edit.le_change_name.text():
            edit.le_change_name.setText('')

        cur.execute(f"""DELETE FROM folders WHERE id = {str(n)};""")
        cur.execute(f"""DELETE FROM lists WHERE id = {str(n)};""")

        con.commit()
        con.close()

        insert_folders(edit)

    def open_modul(edit):
        dialog_name = 'Please choose some file to open'
        folder_init_name = './'
        filename = QFileDialog.getOpenFileName(edit, dialog_name, folder_init_name, "Data Base file (*.db)")
        global PATH_for_edit
        try:
            if filename[0] != '':
                PATH_for_edit = filename[0]
                insert_folders(edit)
                pryatki(edit, 1)
                edit.pb_add_to_table.hide()
                edit.pb_del_to_table.hide()
                edit.pb_safe_to_table.hide()
                edit.le2.setText(PATH_for_edit)
                edit.le2.setEnabled(False)
                edit.pb_creat.setEnabled(False)
        except:
            pass

    def check_write_to_creat(edit):
        txt = edit.le2.text()
        if txt:
            edit.pb_creat.setEnabled(True)
        else:
            edit.pb_creat.setEnabled(False)

    def create_modul(edit):
        try:
            con = sqlite3.connect(edit.le2.text() + ".db")
            cur = con.cursor()

            cur.execute("""CREATE TABLE folders (
                        id   INT  PRIMARY KEY
                            CONSTRAINT dict_pk UNIQUE
                            NOT NULL,
                        name TEXT);""")

            cur.execute("""CREATE TABLE lists (
                        id    INT  PRIMARY KEY
                            CONSTRAINT folder_pk UNIQUE
                            NOT NULL,
                        name  INT  REFERENCES folders (id),
                        orig  TEXT,
                        trans TEXT);""")

            con.commit()
            con.close()

            pryatki(edit, 1)
            global PATH_for_edit
            PATH_for_edit = edit.le2.text() + '.db'
            insert_folders(edit)
            edit.le2.setEnabled(False)
            edit.pb_open.setEnabled(False)
            edit.pb_add_to_table.hide()
            edit.pb_del_to_table.hide()
            edit.pb_safe_to_table.hide()
        except:
            error_1(edit)

    def build_tabel(edit, item):
        edit.global_token = 1
        con = sqlite3.connect(PATH_for_edit)
        cur = con.cursor()

        r = cur.execute(f"""SELECT orig, trans FROM lists""").fetchall()

        if item in edit.box_of_widgetitem:
            edit.id = edit.box_of_widgetitem.index(item)
            edit.orig, edit.trans = r[edit.id]
            edit.edit_table()
        con.close()

    def edit_table(edit):
        edit.global_token = 1
        pryatki(edit, 1)
        edit.pb_to_folders.show()
        edit.le_change_name.hide()
        edit.pb_change_name.hide()
        edit.table_of_words.show()
        edit.list_of_folders.hide()
        n = 0
        if ''.join(edit.orig.split()) != '':
            orig = edit.orig.split(';')
            trans = edit.trans.split(';')
            n = len(orig)
        edit.table_of_words.setRowCount(n)
        edit.number = n
        for i in range(n):
            edit.table_of_words.setItem(i, 0, QTableWidgetItem(orig[i]))
            edit.table_of_words.setItem(i, 1, QTableWidgetItem(trans[i]))

    def add_words_to_tabel(edit):
        if edit.global_token == 1:
            n = edit.table_of_words.rowCount()
            edit.table_of_words.insertRow(n)

    def safe_table(edit):
        if edit.global_token == 1:
            result = []
            num_rows, num_cols = edit.table_of_words.rowCount(), 2
            for col in range(num_cols):
                rows = []
                for row in range(num_rows):
                    item = edit.table_of_words.item(row, col)
                    if item:
                        if item.text() != '':
                            rows.append(item.text())
                result.append(rows)

            con = sqlite3.connect(PATH_for_edit)
            cur = con.cursor()

            r = cur.execute("""SELECT id, name FROM lists;""").fetchall()

            a, b = [], []

            a = ';'.join(result[0])
            b = ';'.join(result[1])

            cur.execute(f"""UPDATE lists SET orig = '{a}', trans = '{b}' 
                            WHERE id = {r[edit.id][0]};""")

            con.commit()
            con.close()

    def coords_for_del_table(edit, x, y):
        edit.y = x

    def del_in_table(edit):
        try:
            if edit.global_token == 1:
                edit.table_of_words.removeRow(edit.y)
        except:
            pass

    def get_index(edit, item):
        con = sqlite3.connect(PATH_for_edit)
        cur = con.cursor()

        if item in edit.box_of_widgetitem:
            r = cur.execute(f"""SELECT name, id FROM folders""").fetchall()
            id_l = edit.box_of_widgetitem.index(item)
            edit.le_change_name.setText(r[id_l][0])
            edit.id_now = r[id_l][1]
        else:
            edit.le_change_name.setText('')
        con.close()

    def change_name_folder(edit):
        con = sqlite3.connect(PATH_for_edit)
        cur = con.cursor()

        if edit.le_change_name.text() != '':
            cur.execute(f"""UPDATE folders SET name = '{edit.le_change_name.text()}'
                            WHERE id = {edit.id_now};""")
            edit.error_but.hide()
        else:
            edit.error_but.show()
        con.commit()
        con.close()

        insert_folders(edit)

    def back_to_start(edit):
        edit.global_token = 0
        edit.le2.setText('')
        edit.le2.setEnabled(True)
        edit.pb_open.setEnabled(True)
        edit.table_of_words.hide()
        edit.pb_add_to_table.hide()
        edit.pb_del_to_table.hide()
        edit.pb_safe_to_table.hide()
        edit.pb_HaveModul.hide()
        pryatki(edit, 0)

    def back_to_folders(edit):
        edit.global_token = 0
        pryatki(edit, 1)
        edit.pb_add_to_table.hide()
        edit.pb_del_to_table.hide()
        edit.pb_safe_to_table.hide()

    def cose(edit):
        edit.global_token = 0
        edit.menu = Menu(edit)
        edit.hide()
        edit.menu.show()

class Info(QWidget):
    def __init__(inf, *args):
        super(Info, inf).__init__()
        uic.loadUi('oprogramme.ui', inf)

        inf.box0 = ["1.png", "2.png", "3.png"]
        inf.box1 = ["1_1.png", "2_1.png"]
        inf.box2 = ["1_2.png", "2_2.png"]
                         #эта часть отвечает за изображение слайдов помощи , а также кнопок для навигации по ним
#-----------------------------------------------------------------------------------------------------------------------
        inf.lb = QtWidgets.QLabel(inf)
        inf.lb.setGeometry(QtCore.QRect(0, -1, 980, 650))
        inf.lb.setText("")
        inf.lb.setPixmap(QtGui.QPixmap("1.png"))

        set_style = ("QPushButton {\n"
                                     "    border: 2px solid #8f8f91;\n"
                                     "    border-radius: 6px;\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
                                     "    min-width: 80px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:flat {\n"
                                     "    border: none; /* no border for a flat push button */\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:default {\n"
                                     "    border-color: navy; /* make the default button prominent */\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:open { /* when the button has its menu open */\n"
                                     "    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                     "                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::menu-indicator {\n"
                                     "    image: url(menu_indicator.png);\n"
                                     "    subcontrol-origin: padding;\n"
                                     "    subcontrol-position: bottom right;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::menu-indicator:pressed, QPushButton::menu-indicator:open {\n"
                                     "    position: relative;\n"
                                     "    top: 2px; left: 2px; /* shift the arrow by 2 px */\n"
                                     "}")

        inf.pButton = QtWidgets.QPushButton(inf)
        inf.pButton.setGeometry(QtCore.QRect(5, 600, 84, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        inf.pButton.setFont(font)
        inf.pButton.setStyleSheet(set_style)
        inf.pButton_2 = QtWidgets.QPushButton(inf)
        inf.pButton_2.setGeometry(QtCore.QRect(890, 600, 84, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        inf.pButton_2.setFont(font)
        inf.pButton_2.setStyleSheet(set_style)

        QtCore.QMetaObject.connectSlotsByName(inf)

        _translate = QtCore.QCoreApplication.translate
        inf.setWindowTitle(_translate("inf", "inf"))
        inf.pButton.setText(_translate("inf", "<"))
        inf.pButton_2.setText(_translate("inf", ">"))

        inf.pButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        inf.pButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#-----------------------------------------------------------------------------------------------------------------------
        inf.lb.hide()
        inf.pButton.hide()
        inf.pButton_2.hide()



        inf.tok = 0
        inf.box = []

        inf.pButton.clicked.connect(inf.click)
        inf.pButton_2.clicked.connect(inf.click)
        inf.pb.clicked.connect(inf.cose)
        inf.pushButton.clicked.connect(inf.prestart)
        inf.pushButton_2.clicked.connect(inf.prestart)
        inf.pushButton_3.clicked.connect(inf.prestart)

    def click(inf):
        txt = inf.sender().text()
        if txt == '<' and inf.tok != 0:
            inf.tok -= 1
            inf.start()
        elif txt == '>' and inf.tok != len(inf.box) - 1:
            inf.tok += 1
            inf.start()
        elif inf.tok == len(inf.box) - 1:
            inf.label.show()
            inf.label_2.show()
            inf.pb.show()
            inf.pushButton.show()
            inf.pushButton_2.show()
            inf.pushButton_3.show()

            inf.lb.hide()
            inf.pButton.hide()
            inf.pButton_2.hide()
            inf.box = []
            inf.tok = 0
            inf.lb.setPixmap(QtGui.QPixmap(''))


    def prestart(inf):
        q = inf.sender().text()
        if q[0] == "1":
            inf.box = inf.box0
        elif q[0] == "2":
            inf.box = inf.box1
        elif q[0] == "3":
            inf.box = inf.box2

        inf.start()


    def start(inf):
        try:
            if inf.box != []:
                inf.label.hide()
                inf.label_2.hide()
                inf.pb.hide()
                inf.pushButton.hide()
                inf.pushButton_2.hide()
                inf.pushButton_3.hide()

                inf.lb.show()
                inf.pButton.show()
                inf.pButton_2.show()


                inf.lb.setPixmap(QtGui.QPixmap(inf.box[inf.tok]))
        except:
            pass


    def cose(inf):
        inf.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = Menu()
    cal.show()
    sys.exit(app.exec())