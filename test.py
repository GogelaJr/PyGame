from ctypes import alignment
import sys
import os
from PyQt5 import QtMultimedia
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pickle
import time




class MyWindow(QMainWindow):
    def __init__(self):
        
        super(MyWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        



        

        self.initMenu()

    def start(self):
        self.optionsButton.deleteLater()
        self.exitButton.deleteLater()
        self.startButton.deleteLater()
        self.titlelayout.deleteLater()
        self.buttonlayout.deleteLater()
        self.mainlayout.deleteLater()
        self.label.deleteLater()
        self.widget.deleteLater()
        with open('Settings.p', 'rb') as f:
            musicCheck, fullScreenCheck = pickle.load(f)
        if musicCheck == True:

            self.label.setText('Okay...')

            self.sdir = os.path.dirname(os.path.realpath(__file__))
            self.background1 = os.path.join(self.sdir, 'soundtrack/Background1.mp3')
            self.background2 = os.path.join(self.sdir, 'soundtrack/Background2.mp3')


            self.player = QtMultimedia.QMediaPlayer()
            self.playlist = QtMultimedia.QMediaPlaylist()

            def state_handle(state):
                if state == QtMultimedia.QMediaPlayer.PlayingState:
                    print('playing')
                elif state == QtMultimedia.QMediaPlayer.StoppedState:
                    print('not playing')

            self.player.stateChanged.connect(state_handle)

            self.background1url = QUrl.fromLocalFile(self.background1)
            self.background2url = QUrl.fromLocalFile(self.background2)

            self.playlist.addMedia(QtMultimedia.QMediaContent(self.background1url))
            self.playlist.addMedia(QtMultimedia.QMediaContent(self.background2url))

            self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
            
            self.player.setVolume(100)
            self.player.setPlaylist(self.playlist)
            self.player.play()
            if fullScreenCheck == True:
                self.label.setText(str(fullScreenCheck))
                self.showFullScreen()
                
            else:
                self.label.setText('Non FullScreen')
        else:
            self.label.setText('No Music')
            if fullScreenCheck == True:
                self.label.setText('Full no music')
                self.showFullScreen()
                self.label.deleteLater()
                prologue.chapter_1(self)
            else:
                self.label.setText('No music no full')
        
        

    def optionMenu(self):
        global musicCheck
        global fullScreenCheck

        with open('Settings.p', 'rb') as f:
            musicCheck, fullScreenCheck = pickle.load(f)


        optionMenu = QWidget()
        optionsMainLayout = QVBoxLayout()
        optionsLayout = QHBoxLayout()
        buttonLayout = QVBoxLayout()
        self.fullScreenBox = QCheckBox('Full Screen')
        self.musicBox = QCheckBox('Sound')

        if fullScreenCheck==True:
            self.fullScreenBox.setChecked(True)
        else:
            self.fullScreenBox.setChecked(False)
        if musicCheck==True:
            self.musicBox.setChecked(True)
        else:
            self.musicBox.setChecked(False)

        
        

        self.applyButton = QPushButton(self)
        self.applyButton.setText('Apply')
        self.applyButton.setFont(QFont('android 7', 10))
        self.backButton = QPushButton(self)
        self.backButton.setText('Back')
        self.backButton.setFont(QFont('android 7', 10))
        

             
    
        
        def saveSettings():
            if self.fullScreenBox.isChecked():
                fullScreenCheck = True
            else:
                fullScreenCheck = False
            if self.musicBox.isChecked():
                musicCheck = True
            else:
                musicCheck = False
            
            pickle.dump([musicCheck, fullScreenCheck], open('Settings.p', 'wb'))


        self.applyButton.clicked.connect(saveSettings)
        self.backButton.clicked.connect(self.initMenu)

        optionsMainLayout.setAlignment(Qt.AlignCenter)
        
        buttonLayout.addWidget(self.applyButton)
        buttonLayout.addWidget(self.backButton)
        optionsLayout.addWidget(self.fullScreenBox)
        optionsLayout.addWidget(self.musicBox)

        optionsMainLayout.addLayout(optionsLayout)
        optionsMainLayout.addLayout(buttonLayout)
        
        optionMenu.setLayout(optionsMainLayout)
        self.setCentralWidget(optionMenu)


    def initMenu(self):
        self.widget = QWidget()
        screen = QDesktopWidget().screenGeometry()
        screenWidthCenter = screen.width()//2
        screenWidthCenter = screenWidthCenter - screenWidthCenter//2
        screenHeightCenter = screen.height()//2
        screenHeightCenter = screenHeightCenter - screenHeightCenter//2


        self.setGeometry(screenWidthCenter, screenHeightCenter, screen.width()//2, screen.height()//2)
        # self.move(screenWidthCenter, screenHeightCenter)
        self.mainlayout = QVBoxLayout()
        self.titlelayout = QHBoxLayout()
        self.buttonlayout = QVBoxLayout()
        
        self.setWindowTitle('Operation Starlight')

        # Menu Title
        self.label = QLabel('Operation Starlight')
        self.label.setFont(QFont('android 7', 50))
        self.label.setStyleSheet('color : #4D4DFF; background : transparent;')
        self.titlelayout.addWidget(self.label)

        


        # Menu Start Button
        self.startButton = QPushButton(self)
        self.startButton.setText('Play')
        self.startButton.setFont(QFont('android 7', 25))
        self.startButton.adjustSize()
        self.startButton.clicked.connect(self.start)
        self.startButton.setStyleSheet('color : #4D4DFF; background : transparent;')
        self.buttonlayout.addWidget(self.startButton)
        
        self.buttonlayout.setAlignment(Qt.AlignCenter)
        
        
        # Menu Options Button
        self.optionsButton = QPushButton(self)
        self.optionsButton.setText('Options')
        self.optionsButton.setFont(QFont('android 7', 25))
        self.optionsButton.adjustSize()
        self.optionsButton.clicked.connect(self.optionMenu)
        self.optionsButton.setStyleSheet('color : #4D4DFF; background : transparent;')
        
        self.buttonlayout.addWidget(self.optionsButton)

        # Menu Exit Button

        self.exitButton = QPushButton(self)
        self.exitButton.setText('Exit')
        self.exitButton.setFont(QFont('android 7', 25))
        self.exitButton.adjustSize()
        self.exitButton.setStyleSheet('color : #4D4DFF; background : transparent;')
        self.exitButton.clicked.connect(self.close)
        self.buttonlayout.addWidget(self.exitButton)


        self.mainlayout.addLayout(self.titlelayout)
        self.mainlayout.addLayout(self.buttonlayout)
        self.mainlayout.setAlignment(Qt.AlignCenter)
        self.widget.setLayout(self.mainlayout)

        self.widget.setStyleSheet("background-image : url(background.png); background-position : center;")

        self.setCentralWidget(self.widget)
        

class prologue():
    
    def chapter_1(self):

        self.widget = QWidget()
        self.chapter_1_mlayout = QVBoxLayout()
        
        self.chapter_1_vlayout = QVBoxLayout()

        self.chapter_1_Greeting1 = QLabel("")
        self.chapter_1_Greeting1.setFont(QFont('android 7', 15))
        self.chapter_1_Greeting1.setStyleSheet('color : white; background : transparent;')
        self.chapter_1_Greeting1.adjustSize()


        self.chapter_1_vlayout.addWidget(self.chapter_1_Greeting1)


        
        self.chapter_1_mlayout.addLayout(self.chapter_1_vlayout)
        self.chapter_1_mlayout.setAlignment(Qt.AlignCenter)
        
        self.widget.setLayout(self.chapter_1_mlayout)
        self.widget.setStyleSheet("background-image : url(background.png); background-position : center;")
        self.setCentralWidget(self.widget)


        def fade(self, widget):

            self.effect = QGraphicsOpacityEffect()
            widget.setGraphicsEffect(self.effect)

            self.animation = QPropertyAnimation(self.effect, b"opacity")

            self.animation.setDuration(1500)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.start()


        def unfade(self, widget):
            
            self.effect = QGraphicsOpacityEffect()
            widget.setGraphicsEffect(self.effect)
            
            self.animation = QPropertyAnimation(self.effect, b"opacity")
            self.animation.setDuration(1500)
            self.animation.setStartValue(0)
            self.animation.setEndValue(1)
            self.animation.start()
        
        @pyqtSlot()
        def chapter1update1(self, text1, newtext):
            
            thread = labelUpdate(self)
            thread.start()
            
            
            thread.updatelabel.connect(lambda label=text1 : fade(self, label))
            thread.updatelabel.connect(lambda label=text1 : label.setText(newtext))
            thread.updatelabel.connect(lambda label=text1 : unfade(self, label)) 
            
            



        # self.up1 = chapter1update1(self, self.chapter_1_Greeting1, " - (Static noises)... Is anybody ... (cut off) \n - George? \n - Yes? \n - I don't like this...")
        # QTimer.singleShot(3000, lambda : self.up1)
        # timer.start()
        
        # QTimer.singleShot(6000, lambda : chapter1update1(self, self.chapter_1_Greeting1, " - Are we dead?"))

        # QTimer.singleShot(9000, lambda : chapter1update1(self, self.chapter_1_Greeting1, " - No we're not, get your ass up! "))

        QTimer.singleShot(1, lambda : prologue.gameplay1_1(self))


    
    def gameplay1_1(self):
        # Delete garbage
        self.chapter_1_Greeting1.deleteLater()
        self.chapter_1_mlayout.deleteLater()
        self.chapter_1_vlayout.deleteLater()
        self.widget.deleteLater()
        

        # Layouts
        
        self.widget= QWidget()
        self.ingamescreen = QDesktopWidget().screenGeometry()
        self.midWidth = self.ingamescreen.width() - self.ingamescreen.width()//2
        self.midHeight = self.ingamescreen.height() - self.ingamescreen.height()//2


        self.mainLayout = QGridLayout()
        
        
        
        self.topFrame = QFrame()
        self.topFrame.setStyleSheet("background: blue;")
        
        self.leftFrame = QFrame()  
        self.leftFrame.setObjectName('leftFrame')
        self.leftFrame.setStyleSheet("QFrame#leftFrame {background : transparent; border-image: url(Artboard_1.png); background-repeat: no-repeat;}")
        
        
        self.leftLayout = QVBoxLayout()
        self.leftLayout.setSpacing(2)
        self.leftcommandFrame = QFrame()
        self.leftcommandFrame.setObjectName("leftcmdframe")
        self.leftcommandFrame.setStyleSheet(" QFrame#leftcmdframe {border-image: url(Artboard_11.png); background : transparent; background-repeat: no-repeat;}")
        
        self.leftCommandLayout = QVBoxLayout()
        self.leftCommand2Layout = QVBoxLayout()


        
        


        
        

        
        

        self.rightFrame = QFrame()
        self.rightFrame.setObjectName("rightFrame")
        self.rightFrame.setStyleSheet(" QFrame#rightFrame {border-image: url(Scanmap.png); background : transparent; background-repeat: no-repeat;} ")
        self.rightLayout = QVBoxLayout()
        
        

        self.bottomFrame = QFrame()
        self.bottomFrame.setStyleSheet("background: transparent;")
        self.bottomFrame.resize(50,50)
        self.bottomLayout = QVBoxLayout()
        

        # TOP LAYOUT
        self.exitButton = QPushButton("ABORT")
        self.exitButton.setFont(QFont('android 7', 10))
        self.exitButton.setStyleSheet("color : red; background : transparent;")
        
        self.exitButton.clicked.connect(self.close)

        self.exitButton.setObjectName("exitButton")
        self.exitButton.setParent(self.topFrame)

        # RIGHT LAYOUT

        self.map = QLabel(self.widget)
        self.map.setStyleSheet("border: 5px solid transparent;")
        

        self.map.setMaximumSize(QSize(480, 240))
        self.map.resize(QSize(480, 240))
        self.mapmovie = QMovie('test2.gif')
        self.map.setMovie(self.mapmovie)
        self.mapmovie.start()


        self.scanTool = QLabel("SCANTOOL")
        self.scanTool.setFont(QFont('android 7', 15))
        self.scanTool.setStyleSheet("background: transparent; color: white; margin-bottom:0px;")



        self.inputX = QLineEdit("")
        self.inputX.setFont(QFont('consolas-bold', 8))
        self.inputX.setStyleSheet("background: black; color: white; border: 2px solid #f0f")

        self.inputY = QLineEdit("")
        self.inputY.setFont(QFont('consolas-bold', 8, ))
        self.inputY.setStyleSheet("background: black; color: white; border: 2px solid #f0f;")

        self.coordinateResponse = QLabel("")
        self.coordinateResponse.setFont(QFont('Jura', 8))
        self.coordinateResponse.setStyleSheet("background: transparent; color: white;")
        self.coordinateFound = QLabel("")
        self.coordinateFound.setFont(QFont('Jura', 8))
        self.coordinateFound.setStyleSheet("background: transparent; color: white;")

        self.firstLocation = False

        
        


        def coordinateSearch():
            self.coordinateFound.setText("")
            if self.inputX.text() == "1.1" and self.inputY.text() == "1.1":
                

                if self.firstLocation == False:
                    self.firstLocation = True
                    self.coordinateResponse.setText("Connecting to Local UAV")
                    QTimer.singleShot(1500, lambda : self.coordinateResponse.setText("Coordinates found!"))
                    QTimer.singleShot(1501, lambda : self.coordinateFound.setText("Panama!"))
                    QTimer.singleShot(1502, lambda : self.line1.setText(self.line2.text()))
                    QTimer.singleShot(1503, lambda : self.line2.setText(self.line3.text()))
                    QTimer.singleShot(1504, lambda : self.line3.setText(self.line4.text()))
                    QTimer.singleShot(1505, lambda : self.line4.setText(self.line5.text()))
                    QTimer.singleShot(1506, lambda : self.line5.setText(self.line6.text()))
                    QTimer.singleShot(1507, lambda : self.line6.setText(self.line7.text()))
                    QTimer.singleShot(1508, lambda : self.line7.setText(self.line8.text()))
                    QTimer.singleShot(1509, lambda : self.line8.setText(self.line9.text()))
                    QTimer.singleShot(1510, lambda : self.line9.setText(self.line10.text()))
                    QTimer.singleShot(1511, lambda : self.line10.setText(self.line11.text()))
                    QTimer.singleShot(1512, lambda : self.line11.setText(self.line12.text()))
                    QTimer.singleShot(1513, lambda : self.line12.setText(self.line13.text()))
                    QTimer.singleShot(1514, lambda : self.line13.setText(self.line14.text()))
                    QTimer.singleShot(1515, lambda : self.line14.setText(self.line15.text()))
                    QTimer.singleShot(1517, lambda : self.line15.setText("You Found Panama"))
                    
                else:
                    QTimer.singleShot(1500, lambda : self.coordinateResponse.setText("Location is"))
                    QTimer.singleShot(1501, lambda : self.coordinateFound.setText("Already Found!"))
                    QTimer.singleShot(1502, lambda : self.line1.setText(self.line2.text()))
                    QTimer.singleShot(1503, lambda : self.line2.setText(self.line3.text()))
                    QTimer.singleShot(1504, lambda : self.line3.setText(self.line4.text()))
                    QTimer.singleShot(1505, lambda : self.line4.setText(self.line5.text()))
                    QTimer.singleShot(1506, lambda : self.line5.setText(self.line6.text()))
                    QTimer.singleShot(1507, lambda : self.line6.setText(self.line7.text()))
                    QTimer.singleShot(1508, lambda : self.line7.setText(self.line8.text()))
                    QTimer.singleShot(1509, lambda : self.line8.setText(self.line9.text()))
                    QTimer.singleShot(1510, lambda : self.line9.setText(self.line10.text()))
                    QTimer.singleShot(1511, lambda : self.line10.setText(self.line11.text()))
                    QTimer.singleShot(1512, lambda : self.line11.setText(self.line12.text()))
                    QTimer.singleShot(1513, lambda : self.line12.setText(self.line13.text()))
                    QTimer.singleShot(1514, lambda : self.line13.setText(self.line14.text()))
                    QTimer.singleShot(1515, lambda : self.line14.setText(self.line15.text()))
                    QTimer.singleShot(1517, lambda : self.line15.setText("Dumdum"))

                    
                    

            elif self.inputX.text() == "34" and self.inputY.text() == "35":
                self.coordinateResponse.setText("Connecting to Local UAV")
                QTimer.singleShot(1500, lambda : self.coordinateResponse.setText("Coordinates found!"))
                QTimer.singleShot(1500, lambda : self.coordinateFound.setText("Uganda!"))
            else: 
                self.coordinateResponse.setText("Connecting to Local UAV")
                QTimer.singleShot(1500, lambda : self.coordinateResponse.setText("Coordinates not found!"))
                QTimer.singleShot(1500, lambda : self.coordinateFound.setText(""))



        self.coordinateSearchButton = QPushButton("SEARCH")
        self.coordinateSearchButton.setFont(QFont('android 7', 8))
        self.coordinateSearchButton.setStyleSheet("background: black; color: white;")
        self.coordinateSearchButton.clicked.connect(coordinateSearch)





        self.dummyright = QLabel()
        self.dummyright.setStyleSheet("background: transparent;")

        self.rightLayout.setAlignment(Qt.AlignTop)
        self.rightLayout.addWidget(self.dummyright, 1, alignment=Qt.AlignLeft)
        self.rightLayout.addWidget(self.scanTool, 0, alignment=Qt.AlignCenter)
        self.rightLayout.addWidget(self.inputX, 0, alignment=Qt.AlignCenter)
        self.rightLayout.addWidget(self.inputY, 0, alignment=Qt.AlignCenter)
        self.rightLayout.addWidget(self.coordinateSearchButton, 0, alignment=Qt.AlignCenter)
        self.rightLayout.addWidget(self.coordinateResponse, 0, alignment=Qt.AlignCenter)
        self.rightLayout.addWidget(self.coordinateFound, 0, alignment=Qt.AlignCenter)


        # LEFT LAYOUT 

        self.line1 = QLabel("1")
        self.line1.setFont(QFont('consolas', 12))
        self.line1.setStyleSheet("background:transparent; color: white;")

        self.line2 = QLabel("2")
        self.line2.setFont(QFont('consolas', 12))
        self.line2.setStyleSheet("background:transparent; color: white;")

        self.line3 = QLabel("3")
        self.line3.setFont(QFont('consolas', 12))
        self.line3.setStyleSheet("background:transparent; color: white;")

        self.line4 = QLabel("4")
        self.line4.setFont(QFont('consolas', 12))
        self.line4.setStyleSheet("background:transparent; color: white;")

        self.line5 = QLabel("5")
        self.line5.setFont(QFont('consolas', 12))
        self.line5.setStyleSheet("background:transparent; color: white;")

        self.line6 = QLabel("6")
        self.line6.setFont(QFont('consolas', 12))
        self.line6.setStyleSheet("background:transparent; color: white;")

        self.line7 = QLabel("7")
        self.line7.setFont(QFont('consolas', 12))
        self.line7.setStyleSheet("background:transparent; color: white;")

        self.line8 = QLabel("8")
        self.line8.setFont(QFont('consolas', 12))
        self.line8.setStyleSheet("background:transparent; color: white;")

        self.line9 = QLabel("9")
        self.line9.setFont(QFont('consolas', 12))
        self.line9.setStyleSheet("background:transparent; color: white;")

        self.line10 = QLabel("10")
        self.line10.setFont(QFont('consolas', 12))
        self.line10.setStyleSheet("background:transparent; color: white;")

        self.line11 = QLabel("11")
        self.line11.setFont(QFont('consolas', 12))
        self.line11.setStyleSheet("background:transparent; color: white;")

        self.line12 = QLabel("12")
        self.line12.setFont(QFont('consolas', 12))
        self.line12.setStyleSheet("background:transparent; color: white;")

        self.line13 = QLabel("13")
        self.line13.setFont(QFont('consolas', 12))
        self.line13.setStyleSheet("background:transparent; color: white;")

        self.line14 = QLabel("14")
        self.line14.setFont(QFont('consolas', 12))
        self.line14.setStyleSheet("background:transparent; color: white;")

        self.line15 = QLabel("15")
        self.line15.setFont(QFont('consolas', 12))
        self.line15.setStyleSheet("background:transparent; color: white;")

        self.dummyline = QLabel("")
        self.line15.setFont(QFont('consolas', 12))
        self.line15.setStyleSheet("background:transparent; color: white;")

        self.dummyline2 = QLabel("")
        self.line15.setFont(QFont('consolas', 12))
        self.line15.setStyleSheet("background:transparent; color: white;")

        self.command = QLineEdit("")
        self.command.setFont(QFont('consolas', 12))
        self.command.setStyleSheet("background:transparent; color: white; margin-left: 40px; margin-top: -3px; border: transparent;")
        self.command.setPlaceholderText("/help")
        
        self.command.setFixedWidth(600)
        # self.command.returnPressed.connect()


        self.leftLayout.setAlignment(Qt.AlignTop)
        self.leftLayout.addWidget(self.line1, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line2, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line3, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line4, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line5, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line6, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line7, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line8, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line9, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line10, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line11, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line12, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line13, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line14, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.line15, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.dummyline, 0, alignment=Qt.AlignLeft)
        self.leftLayout.addWidget(self.dummyline2, 0, alignment=Qt.AlignLeft)


        self.leftcommandFrame.setLayout(self.leftCommandLayout)
        self.leftCommandLayout.addLayout(self.leftCommand2Layout)
        self.leftLayout.addWidget(self.leftcommandFrame, 0, alignment=Qt.AlignLeft)
        
        self.leftCommand2Layout.addWidget(self.command, 0, alignment=Qt.AlignCenter)
        
        


        

        


        
        
        
        
        

        # BOTTOM LAYOUT

        self.intelButton = QPushButton("INTEL")
        self.intelButton.setFont(QFont('android 7', 12))
        self.intelButton.setStyleSheet("background : black; color: white;")

        self.locationButton = QPushButton("LOCATION")
        self.locationButton.setFont(QFont('android 7', 12))
        self.locationButton.setStyleSheet(
                            "QPushButton"
                            "{"
                            "background : black;"
                            "color : white"
                            "}"
                            "QPushButton::hover"
                             "{"
                             "background-color : #f0f;"
                             "color : white;"
                             "}")

        

        self.helpButton = QPushButton("HELP")
        self.helpButton.setFont(QFont('android 7', 12))
        self.helpButton.setStyleSheet("background : black; color: white;")

        def helpSection():
            QTimer.singleShot(0, lambda : self.line1.setText(self.line2.text()))
            QTimer.singleShot(1, lambda : self.line2.setText(self.line3.text()))
            QTimer.singleShot(2, lambda : self.line3.setText(self.line4.text()))
            QTimer.singleShot(3, lambda : self.line4.setText(self.line5.text()))
            QTimer.singleShot(4, lambda : self.line5.setText(self.line6.text()))
            QTimer.singleShot(5, lambda : self.line6.setText(self.line7.text()))
            QTimer.singleShot(6, lambda : self.line7.setText(self.line8.text()))
            QTimer.singleShot(7, lambda : self.line8.setText(self.line9.text()))
            QTimer.singleShot(8, lambda : self.line9.setText(self.line10.text()))
            QTimer.singleShot(9, lambda : self.line10.setText(self.line11.text()))
            QTimer.singleShot(10, lambda : self.line11.setText(self.line12.text()))
            QTimer.singleShot(11, lambda : self.line12.setText(self.line13.text()))
            QTimer.singleShot(12, lambda : self.line13.setText(self.line14.text()))
            QTimer.singleShot(13, lambda : self.line14.setText(self.line15.text()))
            QTimer.singleShot(14, lambda : self.line15.setText("/scan [location]"))

        self.helpButton.clicked.connect(helpSection)


        self.bottomLayout.setAlignment(Qt.AlignCenter)
        self.bottomLayout.addWidget(self.intelButton, alignment=Qt.AlignCenter)
        self.bottomLayout.addWidget(self.locationButton, alignment=Qt.AlignCenter)
        self.bottomLayout.addWidget(self.helpButton, alignment=Qt.AlignCenter)
        
        
        self.bottomFrame.setLayout(self.bottomLayout)
        

        



        # Adding Widgets to main layout
        

        self.mainLayout.addWidget(self.topFrame, 0, 0, 1, 2)

        self.rightFrame.setLayout(self.rightLayout)
        self.mainLayout.addWidget(self.rightFrame, 0, 3, 2, 1)
        self.mainLayout.addWidget(self.map, 0, 3)
        self.map.lower()
        
        self.leftFrame.setLayout(self.leftLayout)
        
        self.mainLayout.addWidget(self.leftFrame, 1,0, 2, 3)
        self.leftFrame.setLineWidth(2)
        
        
        

        self.mainLayout.addWidget(self.bottomFrame, 2, 3)
        
        
        self.widget.setLayout(self.mainLayout)
        self.widget.setStyleSheet("background-image : url(background.png); background-position : center;")
        self.setCentralWidget(self.widget)
        

        



        
class labelUpdate(QThread):
    updatelabel = pyqtSignal()

    


    def run(self):

        time.sleep(3)
        self.updatelabel.emit()

    def stop(self):
        self.threadactive = False 
        self.wait()








if __name__ == '__main__':
    app = QApplication([])
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

