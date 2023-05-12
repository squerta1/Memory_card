#создай приложение для запоминания информации
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QGroupBox, QHBoxLayout, QPushButton, QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.resize(600, 400)
main_win.setWindowTitle('Memory Card')

text = QLabel('Какой национальности не существует? ')
c1 = QRadioButton('Энцы')
c2 = QRadioButton('Чулымцы')
c3 = QRadioButton('Смурфы')
c4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(c1)
RadioGroup.addButton(c2)
RadioGroup.addButton(c3)
RadioGroup.addButton(c4)

answer = QPushButton('Ответить')
RadioGruopBox = QGroupBox('Варианты ответов')
vl1 = QVBoxLayout()
vl2 = QVBoxLayout()
hl1 = QHBoxLayout()
vl1.addWidget(c1)
vl1.addWidget(c3)
vl2.addWidget(c2)
vl2.addWidget(c4)
hl1.addLayout(vl1)
hl1.addLayout(vl2)

RadioGruopBox.setLayout(hl1)

AnsGroupBox = QGroupBox('Результат теста')
corect = QLabel('Правильно/Неправильно')
r_answer = QLabel('Правильный ответ')
vl3 = QVBoxLayout()
vl3.addWidget(corect)
vl3.addWidget(r_answer, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(vl3)
AnsGroupBox.hide()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v1 = QVBoxLayout()

h1.addWidget(text, alignment = Qt.AlignCenter)
h2.addWidget(RadioGruopBox)
h2.addWidget(AnsGroupBox)
h3.addWidget(answer, alignment = Qt.AlignCenter)
v1.addLayout(h1)
v1.addLayout(h2)
v1.addLayout(h3)
main_win.setLayout(v1)

main_win.cur_question = -1

def show_question():
    AnsGroupBox.hide()
    RadioGruopBox.show()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    c1.setChecked(False)
    c2.setChecked(False)
    c3.setChecked(False)
    c4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGruopBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')

def click_OK():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()

answers = [c1, c2, c3, c4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    r_answer.setText(q.right_answer)
    show_question()

def show_correct(res):
    corect.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    print('Статистиа')
    print('-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)
    print('Рейтинг', main_win.score / main_win.total * 100, '%')

def next_question():
    cur_question = randint(0, len(questions_list) -1)
    q = questions_list[cur_question]
    ask(q)
    main_win.total += 1
    print('Статистиа')
    print('-Всего вопросов:', main_win.total)
    print('-Правильных ответов:', main_win.score)


questions_list = []

main_win.total = 0
main_win.score = 0

q = Question('Государственный язык Бразилии', 'Португальский', 'Немецкий', 'Бразильский', 'Испанский')
q1 = Question('Какого цвета нет на флаге России', 'Коричневый', 'Красный', 'Синий', 'Белый')
q2 = Question('Какого урока нет школьной программе', 'Природоведение', 'Информатика', 'Математика', 'География')
q3 = Question('Какие страны не находятся в Европе', 'Канада', 'Англия', 'Франция', 'Германия')
q4 = Question('Кто напал на Россию в 1812 году', 'Наполеон', 'Трамп', 'Гитлер', 'Кутузов')
q5 = Question('Кто открыл Америку', 'Колумб', 'Трамп', 'Гитлер', 'Шварцнегер')
q6 = Question('Кто первый полетел в космос', 'Юрий Гагарин', 'Нил Армстронг', 'Кутузов', 'Трамп')
q7 = Question('Кто ты', 'Человек', 'Насекомое', 'Медведь', 'Акула')
q8 = Question('Какой сейчас год', '2022', '2100', '1991', '1965')
q9 = Question('Где ты живёшь', 'дома', 'в норе', 'в жигуле', 'в гостях')
q10 = Question('Ты дурак', 'да, конечно', 'нет,конечно', 'возможно', 'не знаю')
q11 = Question('Какого цвета небо', 'синий', 'красный','коричневый', 'фиолетовый')

questions_list.append(q)
questions_list.append(q1)
questions_list.append(q2)
next_question()
answer.clicked.connect(click_OK)
main_win.show()
app.exec_()

'''
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QMessageBox, QHBoxLayout

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')

#создание виджетов главного окна
text = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
c1 = QRadioButton('2005')
c2 = QRadioButton('2010')
c3 = QRadioButton('2015')
c4 = QRadioButton('2020')

#расположение виджетов по лэйаутам
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
v1 = QVBoxLayout()
h1.addWidget(text, alignment = Qt.AlignCenter)
h2.addWidget(c1, alignment = Qt.AlignCenter)
h2.addWidget(c2, alignment = Qt.AlignCenter)
h3.addWidget(c3, alignment = Qt.AlignCenter)
h3.addWidget(c4, alignment = Qt.AlignCenter)
v1.addLayout(h1)
v1.addLayout(h2)
v1.addLayout(h3)
main_win.setLayout(v1)

#обработка нажатий на переключатели
def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Верно! Вы выиграли гироскутер')
    victory_win.show()
    victory_win.exec_()
def show_lose():
    victory_lose =QMessageBox()
    victory_lose.setText('Нет, в 2015 году. Вы выиграли фирменный плакат')
    victory_lose.show()
    victory_lose.exec_()
c3.clicked.connect(show_win)
c1.clicked.connect(show_lose)
c2.clicked.connect(show_lose)
c4.clicked.connect(show_lose)


#отображение окна приложения 
main_win.show()
app.exec_()'''
