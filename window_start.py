from io import BufferedRandom
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit
from beginGaming import Main 

class Window: 
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

    def game(self): 
        R = Main()                                                  # Make a game instance.
        R.run_game()                                                # Run the game.


    def runStartGameWindow(self): 
        self.startGameWindow = QtWidgets.QWidget()
        self.startGameWindow.resize(500, 667)
        self.startGameWindow.setFixedSize(500,667)
        self.startGameWindow.setStyleSheet("""
            background-image: url(Pictures/windowBackground.jpg);
            background-repeat:no-repeat;
            background-color: transparent
        """)
        self.startGameWindow.setWindowIcon(QtGui.QIcon("Pictures/logo1.png"))
        logo = QtWidgets.QLabel(self.startGameWindow)
        p = QPixmap("Pictures/logo1.png")
        logo.setPixmap(p)
        logo.move(160, 80)
        # logo.resize()
        logo.setStyleSheet("""
                background:transparent;
        """)
        self.buttonOfStartGame = QtWidgets.QPushButton("Start Game",self.startGameWindow)
        self.buttonOfStartGame.setStyleSheet("""
            QPushButton{
                font-size: 22px ; 
                border : 1px solid #44ff99 ; 
                border-radius:4px ; 
                color:#232323;
                padding:10px 20px ; 
                background:#49ff94;
            }
            QPushButton:hover{
                background:#44ff44
            }
        """) 
        self.buttonOfStartGame.move(180,450)
        self.buttonOfStartGame.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonOfStartGame.clicked.connect(lambda:[self.game(),self.startGameWindow.close()])
        
        self.outGame = QtWidgets.QPushButton("Exit",self.startGameWindow)
        self.outGame.setStyleSheet("""
                QPushButton{
                font-size: 18px ; 
                border-radius:4px ; 
                color:#ffff;
                padding:10px 20px; 
                background:#ff6666;
                padding:10px 20px ; 
                }
                QPushButton:hover{
                    background:#ff4444
                }
        """)
        self.outGame.move(220,520)
        self.outGame.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.outGame.clicked.connect(exit)
        self.startGameWindow.show()
        self.app.exec_()


x = Window()
x.runStartGameWindow()