from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QFont
from AddProcessWindow import Ui_AddProcessWindow
from P_Label import ProcessObj


class Ui_OtherWindow(object):
    #
    # STYLES
    #



    #
    # FUNCTIONS
    #

    def refresh(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def addProcessLabel(self):
        snarv = False

        with open("register.txt", 'r') as arq:
            for j in arq:
                self.remove_depois = QtWidgets.QLabel()
                self.remove_depois.setMaximumSize(QtCore.QSize(50,20))
                self.verticalLayout.addWidget(self.remove_depois)

                if("Arquivado" in j):
                    self.process = ProcessObj(j, 'y')
                else:
                    self.process = ProcessObj(j, 'n')

                self.verticalLayout.addWidget(self.process)



    ##Spawns a new process creation window
    def createProcess(self):
        self.newpwindow = QtWidgets.QMainWindow()
        self.ui = Ui_AddProcessWindow()
        self.ui.setupUi(self.newpwindow)
        self.newpwindow.show()



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

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.centralwidget)
        self.scroll.setStyleSheet("QScrollBar {\n"
                                  "    background-color: rgb(43, 84, 126);\n"
                                  "}")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.centralwidget.setLayout(self.verticalLayout)


        ### TO BE FIXED THE NON-SHOWING BAR WHEN MANY PROCESSES ARE ADDED ###
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.top_bar.setStyleSheet("background-color: rgb(43, 84, 126);\n")
        self.verticalLayout.addWidget(self.top_bar)
        ### TO BE FIXED THE NON-SHOWING BAR WHEN MANY PROCESS ARE ADDED ###


        self.refresh_button = QtWidgets.QPushButton(self.top_bar)
        icon = QtGui.QIcon("Images/refreshbutton.png")
        self.refresh_button.setIcon(icon)
        self.refresh_button.move(300, 10)
        self.refresh_button.clicked.connect(self.refresh)
        self.refresh_button.clicked.connect(lambda: MainWindow.close())

        self.button_newP = QtWidgets.QPushButton(self.top_bar)
        self.button_newP.setMinimumSize(QtCore.QSize(100, 100))
        self.button_newP.setMaximumSize(QtCore.QSize(100, 100))
        self.button_newP.setStyleSheet("QPushButton {\n"
                                       "    background-image: url(:/Close_Image/Images/cil-x.png);\n"
                                       "    background-position: center;    \n"
                                       "    background-color: rgb(60, 60, 60);\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(50, 50, 50);    \n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(35, 35, 35);    \n"
                                       "    color: rgb(200, 200, 200);\n"
                                       "}")

        self.button_newP.clicked.connect(self.createProcess)




        ### PROCESS AREA ###
        
        self.addProcessLabel()

        ### PROCESS AREA ###



        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")


 


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
        MainWindow.setCentralWidget(self.scroll)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Processos"))
        self.label_credits.setText(_translate("MainWindow", "Created by: Gabriel B. Duek"))