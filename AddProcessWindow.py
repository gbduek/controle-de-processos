from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap


class Ui_AddProcessWindow(object):

    ############################# STYLES ##############################
    
    lineStyle = ("QLineEdit {\n"
				 "    border: 2px solid rgb(45, 45, 45);\n"
				 "    border-radius: 5px;\n"
				 "    padding: 15px;\n"
				 "    background-color: rgb(30, 30, 30);    \n"
				 "    color: rgb(100, 100, 100);\n"
				 "}\n"
				 "QLineEdit:hover {\n"
				 "    border: 2px solid rgb(55, 55, 55);\n"
				 "}\n"
				 "QLineEdit:focus {\n"
				 "    border: 2px solid rgb(43, 84, 126);    \n"
				 "    color: rgb(200, 200, 200);\n"
				 "}")



    checkbox = ("QCheckBox::indicator {\n"
				"    border: 3px solid rgb(100, 100, 100);\n"
				"    width: 15px;\n"
				"    height: 15px;\n"
				"    border-radius: 10px;    \n"
				"    background-color: rgb(135, 135, 135);\n"
				"}\n"
				"QCheckBox::indicator:checked {\n"
				"    border: 3px solid rgb(43, 84, 126);\n"
				"    background-color: rgb(83, 124, 166);\n"
				"}")

    ############################# STYLES ##############################




    #
    # FUNCTIONS
    #

    def createProcess(self):
        self.newpwindow = QtWidgets.QMainWindow()
        self.ui = Ui_AddProcessWindow()
        self.ui.setupUi(self.newpwindow)
        self.newpwindow.show()


    ### REGISTER ON FILE WHAT IS WRITTEN ###
    def makeRegister(self):
        if (str(self.search_bar.text()) and str(self.search_bar2.text()) and str(self.search_bar3.text())):
            with open('register.txt', 'a') as arq:
                arq.write(str(self.search_bar.text()) + ";" + str(self.search_bar2.text()) + ";" + str(self.search_bar3.text()) + "\n")
    ### REGISTER ON FILE WHAT IS WRITTEN ###



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
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
        ###  BLUE TOP BAR ###
        self.add_process = QtWidgets.QLabel(self.top_bar)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.add_process.setFont(font)
        self.add_process.setStyleSheet("background-color: rgb(43, 84, 126);\n")
        self.add_process.setGeometry(QtCore.QRect(0, 0, 16777215, 100))
        self.add_process.setObjectName("add_process")
        ###  BLUE TOP BAR ###



        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")



       ############## SEARCH BARS ##############
            # SEARCH BAR == TEXT INPUT BOX #

        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.search_bar.setFont(font)
        self.search_bar.setStyleSheet(self.lineStyle)
        self.search_bar.move(0,50)

        	### REMOVER DEPOIS ###
        self.remove_depois = QtWidgets.QLabel()
        self.remove_depois.setMaximumSize(QtCore.QSize(50,20))
        self.verticalLayout.addWidget(self.remove_depois)
        	### REMOVER DEPOIS ###

        self.verticalLayout.addWidget(self.search_bar)



        self.search_bar2 = QtWidgets.QLineEdit(self.content)
        self.search_bar2.setMinimumSize(QtCore.QSize(50, 20))
        self.search_bar2.setFont(font)
        self.search_bar2.setStyleSheet(self.lineStyle)
        self.search_bar2.move(0,100)

        	### REMOVER DEPOIS ###
        self.remove_depois = QtWidgets.QLabel()
        self.remove_depois.setMaximumSize(QtCore.QSize(50,20))
        self.verticalLayout.addWidget(self.remove_depois)
        	### REMOVER DEPOIS ###

        self.verticalLayout.addWidget(self.search_bar2)


        self.search_bar3 = QtWidgets.QLineEdit(self.content)
        self.search_bar3.setMinimumSize(QtCore.QSize(50, 20))
        self.search_bar3.setFont(font)
        self.search_bar3.setStyleSheet(self.lineStyle)
        self.search_bar3.move(0,150)

        	### REMOVER DEPOIS ###
        self.remove_depois = QtWidgets.QLabel()
        self.remove_depois.setMaximumSize(QtCore.QSize(50,20))
        self.verticalLayout.addWidget(self.remove_depois)
        	### REMOVER DEPOIS ###

        self.verticalLayout.addWidget(self.search_bar3)
       ############## SEARCH BARS ##############
 
 
       ############## CHECKBOX ##############
        self.checkbox_novo = QtWidgets.QCheckBox(self.content)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.checkbox_novo.setFont(font)
        self.checkbox_novo.move(20, 60)
        self.checkbox_novo.setStyleSheet(self.checkbox)

        self.checkbox_andamento = QtWidgets.QCheckBox(self.content)
        self.checkbox_andamento.setFont(font)
        self.checkbox_andamento.move(100, 60)
        self.checkbox_andamento.setStyleSheet(self.checkbox)
       ############## CHECKBOX ##############

        self.verticalLayout.addWidget(self.content)




        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")


        ############### EMAIL DIPAC ###############
        self.dipac = QtWidgets.QPushButton(self.content)
        self.dipac.setStyleSheet("QPushButton {\n"
            "background-color: rgb(43, 84, 126)"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgb(0, 0, 255)"
            "}\n")
        self.dipac.move(20, 20)
        self.dipac.setMaximumSize(QtCore.QSize(200, 70))
        ############### EMAIL DIPAC ###############


        ### PROCESS REGISTERING BUTTON ###
        self.registerNew_button = QtWidgets.QPushButton()
        self.registerNew_button.setStyleSheet("QPushButton {\n"
            "background-color: rgb(43, 84, 126)"
            "}\n"
            "QPushButton:pressed {\n"
            "background-color: rgb(0, 0, 255)"
            "}\n")
        self.registerNew_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.verticalLayout.addWidget(self.registerNew_button)


        	### MAKE THE PROCESS REGISTER IF CLICKED ###
        self.registerNew_button.clicked.connect(self.makeRegister)
        self.registerNew_button.clicked.connect(lambda: MainWindow.close())
        	### MAKE THE PROCESS REGISTER IF CLICKED ###

        ### PROCESS REGISTERING BUTTON ###



        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_credits = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(75, 75, 75);")
        self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.add_process.setAlignment(QtCore.Qt.AlignLeft)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_2.addWidget(self.label_credits)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)


        #
        # FUNCTIONS
        #

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Novo Processo"))
        self.label_credits.setText(_translate("MainWindow", "Created by: Gabriel B. Duek"))
        self.registerNew_button.setText(_translate("MainWindow", "REGISTRAR PROCESSO"))
        self.search_bar.setPlaceholderText(_translate("MainWindow", "Referência CNJ"))
        self.search_bar2.setPlaceholderText(_translate("MainWindow", "Referência CGJRJ"))
        self.search_bar3.setPlaceholderText(_translate("MainWindow", "Data Expediente"))
        self.checkbox_novo.setText(_translate("MainWindow", "Novo"))
        self.checkbox_andamento.setText(_translate("MainWindow", "Andamento"))
        self.dipac.setText(_translate("MainWindow", "E-mail ao DIPAC"))
        self.add_process.setText(_translate("MainWindow", "Registro de intimação CNJ"))