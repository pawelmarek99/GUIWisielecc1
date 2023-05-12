# Form implementation generated from reading ui file 'hangman.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 511)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gallow_lb = QtWidgets.QLabel(parent=self.centralwidget)
        self.gallow_lb.setGeometry(QtCore.QRect(10, 10, 380, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gallow_lb.sizePolicy().hasHeightForWidth())
        self.gallow_lb.setSizePolicy(sizePolicy)
        self.gallow_lb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gallow_lb.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.gallow_lb.setText("")
        self.gallow_lb.setObjectName("gallow_lb")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 420, 551, 50))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.word_lb = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.word_lb.sizePolicy().hasHeightForWidth())
        self.word_lb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(False)
        self.word_lb.setFont(font)
        self.word_lb.setText("")
        self.word_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_lb.setObjectName("word_lb")
        self.horizontalLayout.addWidget(self.word_lb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 470, 551, 35))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.new_word_btn = QtWidgets.QPushButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_word_btn.setFont(font)
        self.new_word_btn.setObjectName("new_word_btn")
        self.horizontalLayout_2.addWidget(self.new_word_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.result_lb = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.result_lb.setFont(font)
        self.result_lb.setText("")
        self.result_lb.setObjectName("result_lb")
        self.horizontalLayout_2.addWidget(self.result_lb)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.quit_btn = QtWidgets.QPushButton(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.quit_btn.setFont(font)
        self.quit_btn.setObjectName("quit_btn")
        self.horizontalLayout_2.addWidget(self.quit_btn)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(400, 10, 160, 401))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.a_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a_btn.sizePolicy().hasHeightForWidth())
        self.a_btn.setSizePolicy(sizePolicy)
        self.a_btn.setObjectName("a_btn")
        self.letter_btn_grp = QtWidgets.QButtonGroup(MainWindow)
        self.letter_btn_grp.setObjectName("letter_btn_grp")
        self.letter_btn_grp.addButton(self.a_btn)
        self.horizontalLayout_3.addWidget(self.a_btn)
        self.ą_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ą_btn.sizePolicy().hasHeightForWidth())
        self.ą_btn.setSizePolicy(sizePolicy)
        self.ą_btn.setObjectName("ą_btn")
        self.letter_btn_grp.addButton(self.ą_btn)
        self.horizontalLayout_3.addWidget(self.ą_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.b_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_btn.sizePolicy().hasHeightForWidth())
        self.b_btn.setSizePolicy(sizePolicy)
        self.b_btn.setObjectName("b_btn")
        self.letter_btn_grp.addButton(self.b_btn)
        self.horizontalLayout_4.addWidget(self.b_btn)
        self.c_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_btn.sizePolicy().hasHeightForWidth())
        self.c_btn.setSizePolicy(sizePolicy)
        self.c_btn.setObjectName("c_btn")
        self.letter_btn_grp.addButton(self.c_btn)
        self.horizontalLayout_4.addWidget(self.c_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ć_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ć_btn.sizePolicy().hasHeightForWidth())
        self.ć_btn.setSizePolicy(sizePolicy)
        self.ć_btn.setObjectName("ć_btn")
        self.letter_btn_grp.addButton(self.ć_btn)
        self.horizontalLayout_5.addWidget(self.ć_btn)
        self.d_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_btn.sizePolicy().hasHeightForWidth())
        self.d_btn.setSizePolicy(sizePolicy)
        self.d_btn.setObjectName("d_btn")
        self.letter_btn_grp.addButton(self.d_btn)
        self.horizontalLayout_5.addWidget(self.d_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.e_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.e_btn.sizePolicy().hasHeightForWidth())
        self.e_btn.setSizePolicy(sizePolicy)
        self.e_btn.setObjectName("e_btn")
        self.letter_btn_grp.addButton(self.e_btn)
        self.horizontalLayout_6.addWidget(self.e_btn)
        self.ę_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ę_btn.sizePolicy().hasHeightForWidth())
        self.ę_btn.setSizePolicy(sizePolicy)
        self.ę_btn.setObjectName("ę_btn")
        self.letter_btn_grp.addButton(self.ę_btn)
        self.horizontalLayout_6.addWidget(self.ę_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.f_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.f_btn.sizePolicy().hasHeightForWidth())
        self.f_btn.setSizePolicy(sizePolicy)
        self.f_btn.setObjectName("f_btn")
        self.letter_btn_grp.addButton(self.f_btn)
        self.horizontalLayout_7.addWidget(self.f_btn)
        self.g_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_btn.sizePolicy().hasHeightForWidth())
        self.g_btn.setSizePolicy(sizePolicy)
        self.g_btn.setObjectName("g_btn")
        self.letter_btn_grp.addButton(self.g_btn)
        self.horizontalLayout_7.addWidget(self.g_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.h_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.h_btn.sizePolicy().hasHeightForWidth())
        self.h_btn.setSizePolicy(sizePolicy)
        self.h_btn.setObjectName("h_btn")
        self.letter_btn_grp.addButton(self.h_btn)
        self.horizontalLayout_8.addWidget(self.h_btn)
        self.i_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.i_btn.sizePolicy().hasHeightForWidth())
        self.i_btn.setSizePolicy(sizePolicy)
        self.i_btn.setObjectName("i_btn")
        self.letter_btn_grp.addButton(self.i_btn)
        self.horizontalLayout_8.addWidget(self.i_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.j_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.j_btn.sizePolicy().hasHeightForWidth())
        self.j_btn.setSizePolicy(sizePolicy)
        self.j_btn.setObjectName("j_btn")
        self.letter_btn_grp.addButton(self.j_btn)
        self.horizontalLayout_9.addWidget(self.j_btn)
        self.k_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.k_btn.sizePolicy().hasHeightForWidth())
        self.k_btn.setSizePolicy(sizePolicy)
        self.k_btn.setObjectName("k_btn")
        self.letter_btn_grp.addButton(self.k_btn)
        self.horizontalLayout_9.addWidget(self.k_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.l_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_btn.sizePolicy().hasHeightForWidth())
        self.l_btn.setSizePolicy(sizePolicy)
        self.l_btn.setObjectName("l_btn")
        self.letter_btn_grp.addButton(self.l_btn)
        self.horizontalLayout_10.addWidget(self.l_btn)
        self.ł_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ł_btn.sizePolicy().hasHeightForWidth())
        self.ł_btn.setSizePolicy(sizePolicy)
        self.ł_btn.setObjectName("ł_btn")
        self.letter_btn_grp.addButton(self.ł_btn)
        self.horizontalLayout_10.addWidget(self.ł_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.m_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_btn.sizePolicy().hasHeightForWidth())
        self.m_btn.setSizePolicy(sizePolicy)
        self.m_btn.setObjectName("m_btn")
        self.letter_btn_grp.addButton(self.m_btn)
        self.horizontalLayout_11.addWidget(self.m_btn)
        self.n_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_btn.sizePolicy().hasHeightForWidth())
        self.n_btn.setSizePolicy(sizePolicy)
        self.n_btn.setObjectName("n_btn")
        self.letter_btn_grp.addButton(self.n_btn)
        self.horizontalLayout_11.addWidget(self.n_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.ń_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ń_btn.sizePolicy().hasHeightForWidth())
        self.ń_btn.setSizePolicy(sizePolicy)
        self.ń_btn.setObjectName("ń_btn")
        self.letter_btn_grp.addButton(self.ń_btn)
        self.horizontalLayout_12.addWidget(self.ń_btn)
        self.o_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.o_btn.sizePolicy().hasHeightForWidth())
        self.o_btn.setSizePolicy(sizePolicy)
        self.o_btn.setObjectName("o_btn")
        self.letter_btn_grp.addButton(self.o_btn)
        self.horizontalLayout_12.addWidget(self.o_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.ó_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ó_btn.sizePolicy().hasHeightForWidth())
        self.ó_btn.setSizePolicy(sizePolicy)
        self.ó_btn.setObjectName("ó_btn")
        self.letter_btn_grp.addButton(self.ó_btn)
        self.horizontalLayout_13.addWidget(self.ó_btn)
        self.p_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p_btn.sizePolicy().hasHeightForWidth())
        self.p_btn.setSizePolicy(sizePolicy)
        self.p_btn.setObjectName("p_btn")
        self.letter_btn_grp.addButton(self.p_btn)
        self.horizontalLayout_13.addWidget(self.p_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.r_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.r_btn.sizePolicy().hasHeightForWidth())
        self.r_btn.setSizePolicy(sizePolicy)
        self.r_btn.setObjectName("r_btn")
        self.letter_btn_grp.addButton(self.r_btn)
        self.horizontalLayout_14.addWidget(self.r_btn)
        self.s_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.s_btn.sizePolicy().hasHeightForWidth())
        self.s_btn.setSizePolicy(sizePolicy)
        self.s_btn.setObjectName("s_btn")
        self.letter_btn_grp.addButton(self.s_btn)
        self.horizontalLayout_14.addWidget(self.s_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.ś_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ś_btn.sizePolicy().hasHeightForWidth())
        self.ś_btn.setSizePolicy(sizePolicy)
        self.ś_btn.setObjectName("ś_btn")
        self.letter_btn_grp.addButton(self.ś_btn)
        self.horizontalLayout_15.addWidget(self.ś_btn)
        self.t_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_btn.sizePolicy().hasHeightForWidth())
        self.t_btn.setSizePolicy(sizePolicy)
        self.t_btn.setObjectName("t_btn")
        self.letter_btn_grp.addButton(self.t_btn)
        self.horizontalLayout_15.addWidget(self.t_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.u_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.u_btn.sizePolicy().hasHeightForWidth())
        self.u_btn.setSizePolicy(sizePolicy)
        self.u_btn.setObjectName("u_btn")
        self.letter_btn_grp.addButton(self.u_btn)
        self.horizontalLayout_16.addWidget(self.u_btn)
        self.w_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_btn.sizePolicy().hasHeightForWidth())
        self.w_btn.setSizePolicy(sizePolicy)
        self.w_btn.setObjectName("w_btn")
        self.letter_btn_grp.addButton(self.w_btn)
        self.horizontalLayout_16.addWidget(self.w_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.y_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_btn.sizePolicy().hasHeightForWidth())
        self.y_btn.setSizePolicy(sizePolicy)
        self.y_btn.setObjectName("y_btn")
        self.letter_btn_grp.addButton(self.y_btn)
        self.horizontalLayout_17.addWidget(self.y_btn)
        self.z_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_btn.sizePolicy().hasHeightForWidth())
        self.z_btn.setSizePolicy(sizePolicy)
        self.z_btn.setObjectName("z_btn")
        self.letter_btn_grp.addButton(self.z_btn)
        self.horizontalLayout_17.addWidget(self.z_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.ź_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ź_btn.sizePolicy().hasHeightForWidth())
        self.ź_btn.setSizePolicy(sizePolicy)
        self.ź_btn.setObjectName("ź_btn")
        self.letter_btn_grp.addButton(self.ź_btn)
        self.horizontalLayout_18.addWidget(self.ź_btn)
        self.ż_btn = QtWidgets.QPushButton(parent=self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ż_btn.sizePolicy().hasHeightForWidth())
        self.ż_btn.setSizePolicy(sizePolicy)
        self.ż_btn.setObjectName("ż_btn")
        self.letter_btn_grp.addButton(self.ż_btn)
        self.horizontalLayout_18.addWidget(self.ż_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wisielec"))
        self.new_word_btn.setText(_translate("MainWindow", "Nowe słowo"))
        self.quit_btn.setText(_translate("MainWindow", "Wyjście"))
        self.a_btn.setText(_translate("MainWindow", "A"))
        self.ą_btn.setText(_translate("MainWindow", "Ą"))
        self.b_btn.setText(_translate("MainWindow", "B"))
        self.c_btn.setText(_translate("MainWindow", "C"))
        self.ć_btn.setText(_translate("MainWindow", "Ć"))
        self.d_btn.setText(_translate("MainWindow", "D"))
        self.e_btn.setText(_translate("MainWindow", "E"))
        self.ę_btn.setText(_translate("MainWindow", "Ę"))
        self.f_btn.setText(_translate("MainWindow", "F"))
        self.g_btn.setText(_translate("MainWindow", "G"))
        self.h_btn.setText(_translate("MainWindow", "H"))
        self.i_btn.setText(_translate("MainWindow", "I"))
        self.j_btn.setText(_translate("MainWindow", "J"))
        self.k_btn.setText(_translate("MainWindow", "K"))
        self.l_btn.setText(_translate("MainWindow", "L"))
        self.ł_btn.setText(_translate("MainWindow", "Ł"))
        self.m_btn.setText(_translate("MainWindow", "M"))
        self.n_btn.setText(_translate("MainWindow", "N"))
        self.ń_btn.setText(_translate("MainWindow", "Ń"))
        self.o_btn.setText(_translate("MainWindow", "O"))
        self.ó_btn.setText(_translate("MainWindow", "Ó"))
        self.p_btn.setText(_translate("MainWindow", "P"))
        self.r_btn.setText(_translate("MainWindow", "R"))
        self.s_btn.setText(_translate("MainWindow", "S"))
        self.ś_btn.setText(_translate("MainWindow", "Ś"))
        self.t_btn.setText(_translate("MainWindow", "T"))
        self.u_btn.setText(_translate("MainWindow", "U"))
        self.w_btn.setText(_translate("MainWindow", "W"))
        self.y_btn.setText(_translate("MainWindow", "Y"))
        self.z_btn.setText(_translate("MainWindow", "Z"))
        self.ź_btn.setText(_translate("MainWindow", "Ź"))
        self.ż_btn.setText(_translate("MainWindow", "Ż"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
