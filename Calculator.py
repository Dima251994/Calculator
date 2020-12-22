
from PySide2.QtCore import Qt, Slot 
from PySide2.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QGridLayout()
window.setLayout(layout)


button_1 = QPushButton("1")
button_2 = QPushButton("2")
button_3 = QPushButton("3")
button_4 = QPushButton("4")
button_5 = QPushButton("5")
button_6 = QPushButton("6")
button_7 = QPushButton("7")
button_8 = QPushButton("8")
button_9 = QPushButton("9")
button_0 = QPushButton("0")
button_multiple = QPushButton("*")
button_divide = QPushButton("/")
button_plus = QPushButton("+")
button_minus = QPushButton("-")
button_equale = QPushButton("=")
button_restart = QPushButton("C")

layout.addWidget(button_1, 1,1)
layout.addWidget(button_2, 1,2)
layout.addWidget(button_3, 1,3)
layout.addWidget(button_4, 2,1)
layout.addWidget(button_5, 2,2)
layout.addWidget(button_6, 2,3)
layout.addWidget(button_7, 3,1)
layout.addWidget(button_8, 3,2)
layout.addWidget(button_9, 3,3)
layout.addWidget(button_0, 4,1)
layout.addWidget(button_plus, 1,4)
layout.addWidget(button_minus,2,4)
layout.addWidget(button_multiple,3,4)
layout.addWidget(button_divide,4,4)
layout.addWidget(button_equale, 5,4)








"""
layout.addWidget(button_1)
layout.addWidget(button_2)
layout.addWidget(button_3)
layout.addWidget(button_4)
layout.addWidget(button_5)
layout.addWidget(button_6)
layout.addWidget(button_7)
layout.addWidget(button_8)
layout.addWidget(button_9)
layout.addWidget(button_0)
layout.addWidget(button_plus)
layout.addWidget(button_minus)
layout.addWidget(button_multiple)
layout.addWidget(button_divide)
layout.addWidget(button_equale)
"""
"""
layout.addWidget(button_restart)


itemWidget_part_1 = QWidget() # Ствворює нове вікно віджетом 
hlayout_part_1 = QHBoxLayout() # Створює Бокс на якому буде все
itemWidget_part_1.setLayout(hlayout_part_1) # Команда для додавання іншого

hlayout_part_1.addWidget(button_1)
hlayout_part_1.addWidget(button_2)
hlayout_part_1.addWidget(button_3)




itemWidget_part_2 = QWidget()
hlayout_part_2 = QHBoxLayout()
itemWidget_part_2.setLayout(hlayout_part_2)

hlayout_part_2.addWidget(button_4)
hlayout_part_2.addWidget(button_5)
hlayout_part_2.addWidget(button_6)




itemWidget_part_3 = QWidget()
hlayout_part_3 = QHBoxLayout()
itemWidget_part_3.setLayout(hlayout_part_3)

hlayout_part_3.addWidget(button_7)
hlayout_part_3.addWidget(button_8)
hlayout_part_3.addWidget(button_9)




itemWidget_part_4 = QWidget()
hlayout_part_4 = QHBoxLayout()
itemWidget_part_4.setLayout(hlayout_part_4)

hlayout_part_4.addWidget(button_plus)
hlayout_part_4.addWidget(button_minus)
hlayout_part_4.addWidget(button_multiple)
hlayout_part_4.addWidget(button_divide)
hlayout_part_4.addWidget(button_equale)


layout.addWidget(itemWidget_part_1)
layout.addWidget(itemWidget_part_2)
layout.addWidget(itemWidget_part_3)
layout.addWidget(itemWidget_part_4)
"""

window.show()
app.exec_()



