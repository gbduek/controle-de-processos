from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class ProcessObj(QtWidgets.QPushButton):

	def __init__(self, j, p):
		super().__init__()
		self.setMinimumSize(QtCore.QSize(50, 70))
		self.setMaximumSize(QtCore.QSize(16777215, 70))

		if (p == 'n'):
			self.setStyleSheet("QPushButton {\n"
							   "background-color: rgb(43, 84, 126);\n"
							   "border: 3px solid rgb(100, 100, 100);\n"
							   "padding-top: 5px; \n"
							   "text-align: left; \n"
							   "}\n"
							   "QPushButton:hover {\n"
							   "background-color: rgb(35, 35, 35);    \n"
							   "}\n"
							   "QPushButton:pressed {\n"
							   "background-color: rgb(50, 50, 200);    \n"
								"}")
		else:
			self.setStyleSheet("QPushButton {\n"
							   "background-color: rgb(200, 50, 50);\n"
							   "border: 3px solid rgb(100, 100, 100);\n"
							   "padding-top: 5px; \n"
							   "text-align: left; \n"
							   "}\n"
							   "QPushButton:hover {\n"
							   "background-color: rgb(35, 35, 35);    \n"
							   "}\n"
							   "QPushButton:pressed {\n"
							   "background-color: rgb(50, 50, 200);    \n"
								"}")

		self.font = QtGui.QFont()
		self.font.setFamily("Segoe UI")
		self.font.setPointSize(11)
		self.setFont(self.font)
		self._translate = QtCore.QCoreApplication.translate
		self.setText(self._translate("MainWindow", j.replace(";", "\n")))
		self.clicked.connect(self.access_P)


	def proccess_Ui(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setMinimumSize(QtCore.QSize(500, 200))
		MainWindow.setMaximumSize(QtCore.QSize(500, 200))
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		font.setPointSize(12)
		MainWindow.setFont(font)
		icon = QtGui.QIcon("Images/Icon.ico")
		icon.addPixmap(QtGui.QPixmap("/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(icon)
		MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
								 "background-color: rgb(10, 10, 10);")

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.top_bar = QtWidgets.QFrame(self.centralwidget)
		self.top_bar.setMaximumSize(QtCore.QSize(16777215, 50))
		self.top_bar.setStyleSheet("")
		self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
		self.top_bar.setObjectName("top_bar")
		self.top_bar.setStyleSheet("background-color: rgb(43, 84, 126);\n")
		self.verticalLayout.addWidget(self.top_bar)
		self.content = QtWidgets.QFrame(self.centralwidget)
		self.content.setStyleSheet("")
		self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.content.setFrameShadow(QtWidgets.QFrame.Raised)
		self.content.setObjectName("content")

		self.lbtext = QtWidgets.QLabel(self.content)
		self.lbtext.setFont(font)
		self.lbtext.setText(self.text())

		self.removeb = QtWidgets.QPushButton(self.content)
		self.removeb.setStyleSheet("QPushButton {\n"
								   "    background-position: center;    \n"
								   "    background-color: rgb(60, 20, 20);\n"
								   "}\n")
		self.removeb.move(10,70)
		self.removeb.setFont(font)
		self.removeb.setText("Arquivar")
		#self.removeb.clicked.connect(self.arquivado(j))
		self.removeb.clicked.connect(lambda: MainWindow.close())

		self.verticalLayout.addWidget(self.content)
		self.bottom = QtWidgets.QFrame(self.centralwidget)
		self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
		self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
		self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
		self.bottom.setObjectName("bottom")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label_credits = QtWidgets.QLabel(self.bottom)
		font = QtGui.QFont()
		font.setFamily("Segoe UI")
		self.label_credits.setFont(font)
		self.label_credits.setStyleSheet("color: rgb(75, 75, 75);")
		self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.label_credits.setObjectName("label_credits")
		self.verticalLayout_2.addWidget(self.label_credits)
		self.verticalLayout.addWidget(self.bottom)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self._translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(self._translate("MainWindow", "Processos"))
		self.label_credits.setText(self._translate("MainWindow", "Created by: Gabriel B. Duek"))


	def access_P(self):
		self.access_window = QtWidgets.QMainWindow()
		self.proccess_Ui(self.access_window)
		self.access_window.show()


	def arquivado(self, j):
		with open("register.txt", 'r') as arq:
			if('arquivado' in arq[j]):
				print('arquivado')
			else:
				arq[j] = arq[j] + ';arquivado'