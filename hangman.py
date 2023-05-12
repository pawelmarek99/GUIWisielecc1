import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap
from ui_wisielecPL import Ui_MainWindow
from datastore import Datastore

class MainWindow:
    def __init__(self):
        # start okna
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # przypisanie zmiennych
        self.db = Datastore()
        self.word = ""
        self.guessed_word = []
        self.misses = 0

        # start okna z przypisanymi zmiennymi
        self.choose_word()
        self.display_guesses()
        self.display_gallow()
        self.signals()

    def show(self):
        # wyswietlenie okna
        self.main_win.show()

    def choose_word(self):
        # pobiera słowo z datastore i tworzy odpowiednią listę na litery
        self.word = self.db.get_word()
        self.guessed_word = ["_"] * len(self.word)
        # testtest print(self.word)

    def display_guesses(self):
        # wyswietla zgadywane litery
        display_word = ""
        for character in self.guessed_word:
            display_word = display_word + character + " "

        self.ui.word_lb.setText(display_word)

    def display_gallow(self):
        # wsywietla progress na szubienicy
        file_name = (f"./assets/{self.misses}.png")
        gallow = QPixmap(file_name)
        self.ui.gallow_lb.setPixmap(gallow)

    def set_button_enabled(self,val):
        self.ui.a_btn.setEnabled(val)
        self.ui.ą_btn.setEnabled(val)
        self.ui.b_btn.setEnabled(val)
        self.ui.c_btn.setEnabled(val)
        self.ui.ź_btn.setEnabled(val)
        self.ui.ć_btn.setEnabled(val)
        self.ui.d_btn.setEnabled(val)
        self.ui.e_btn.setEnabled(val)
        self.ui.ę_btn.setEnabled(val)
        self.ui.f_btn.setEnabled(val)
        self.ui.g_btn.setEnabled(val)
        self.ui.h_btn.setEnabled(val)
        self.ui.i_btn.setEnabled(val)
        self.ui.j_btn.setEnabled(val)
        self.ui.k_btn.setEnabled(val)
        self.ui.l_btn.setEnabled(val)
        self.ui.ł_btn.setEnabled(val)
        self.ui.m_btn.setEnabled(val)
        self.ui.n_btn.setEnabled(val)
        self.ui.ń_btn.setEnabled(val)
        self.ui.o_btn.setEnabled(val)
        self.ui.ó_btn.setEnabled(val)
        self.ui.p_btn.setEnabled(val)
        self.ui.r_btn.setEnabled(val)
        self.ui.s_btn.setEnabled(val)
        self.ui.ś_btn.setEnabled(val)
        self.ui.t_btn.setEnabled(val)
        self.ui.u_btn.setEnabled(val)
        self.ui.w_btn.setEnabled(val)
        self.ui.y_btn.setEnabled(val)
        self.ui.z_btn.setEnabled(val)
        self.ui.ż_btn.setEnabled(val)


    def signals(self):
        # polaczenie funkcji do przyciskow
        self.ui.quit_btn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.new_word_btn.clicked.connect(self.new_word_btn)

        self.ui.a_btn.clicked.connect(lambda: self.letter_btn(self.ui.a_btn))
        self.ui.ą_btn.clicked.connect(lambda: self.letter_btn(self.ui.ą_btn))
        self.ui.b_btn.clicked.connect(lambda: self.letter_btn(self.ui.b_btn))
        self.ui.c_btn.clicked.connect(lambda: self.letter_btn(self.ui.c_btn))
        self.ui.ź_btn.clicked.connect(lambda: self.letter_btn(self.ui.ź_btn))
        self.ui.ć_btn.clicked.connect(lambda: self.letter_btn(self.ui.ć_btn))
        self.ui.d_btn.clicked.connect(lambda: self.letter_btn(self.ui.d_btn))
        self.ui.e_btn.clicked.connect(lambda: self.letter_btn(self.ui.e_btn))
        self.ui.ę_btn.clicked.connect(lambda: self.letter_btn(self.ui.ę_btn))
        self.ui.f_btn.clicked.connect(lambda: self.letter_btn(self.ui.f_btn))
        self.ui.g_btn.clicked.connect(lambda: self.letter_btn(self.ui.g_btn))
        self.ui.h_btn.clicked.connect(lambda: self.letter_btn(self.ui.h_btn))
        self.ui.i_btn.clicked.connect(lambda: self.letter_btn(self.ui.i_btn))
        self.ui.j_btn.clicked.connect(lambda: self.letter_btn(self.ui.j_btn))
        self.ui.k_btn.clicked.connect(lambda: self.letter_btn(self.ui.k_btn))
        self.ui.l_btn.clicked.connect(lambda: self.letter_btn(self.ui.l_btn))
        self.ui.ł_btn.clicked.connect(lambda: self.letter_btn(self.ui.ł_btn))
        self.ui.m_btn.clicked.connect(lambda: self.letter_btn(self.ui.m_btn))
        self.ui.n_btn.clicked.connect(lambda: self.letter_btn(self.ui.n_btn))
        self.ui.ń_btn.clicked.connect(lambda: self.letter_btn(self.ui.ń_btn))
        self.ui.o_btn.clicked.connect(lambda: self.letter_btn(self.ui.o_btn))
        self.ui.ó_btn.clicked.connect(lambda: self.letter_btn(self.ui.ó_btn))
        self.ui.p_btn.clicked.connect(lambda: self.letter_btn(self.ui.p_btn))
        self.ui.r_btn.clicked.connect(lambda: self.letter_btn(self.ui.r_btn))
        self.ui.s_btn.clicked.connect(lambda: self.letter_btn(self.ui.s_btn))
        self.ui.ś_btn.clicked.connect(lambda: self.letter_btn(self.ui.ś_btn))
        self.ui.t_btn.clicked.connect(lambda: self.letter_btn(self.ui.t_btn))
        self.ui.u_btn.clicked.connect(lambda: self.letter_btn(self.ui.u_btn))
        self.ui.w_btn.clicked.connect(lambda: self.letter_btn(self.ui.w_btn))
        self.ui.y_btn.clicked.connect(lambda: self.letter_btn(self.ui.y_btn))
        self.ui.z_btn.clicked.connect(lambda: self.letter_btn(self.ui.z_btn))
        self.ui.ż_btn.clicked.connect(lambda: self.letter_btn(self.ui.ż_btn))

    def new_word_btn(self):
        # wybiera nowe slowo iresetuje gre
        self.choose_word()
        self.display_guesses()
        self.misses = 0
        self.display_gallow()
        self.set_button_enabled(True)
        self.ui.result_lb.setText("")

    def letter_btn(self,button):
        # pobierz litere
        guess = button.text().lower()
        # wyłącz litere
        button.setEnabled(False)
        # sprawdza czy litera jest w slowie
        if guess in self.word:
            # dodaj litere do guessed_word
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.guessed_word[index] = guess.upper()
            # wyswietla guessed_word
            self.display_guesses()
            # sprawdza czy wygrana
            if "_" not in self.guessed_word:
                self.ui.result_lb.setText("Wygrana!!!")
        else:
            # zwieksza poziom szubienicy
            self.misses += 1
            self.display_gallow()
            # sprawdza czy przegrana
            if self.misses == 11:
                self.ui.result_lb.setText(f"Hasłem było słowo {self.word.upper()}")
                self.set_button_enabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())