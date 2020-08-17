from PyQt5.QtWidgets import *
from tasarim1_python import Ui_MainWindow
from PyQt5.QtGui import *
import os 






class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fileTypes = []
        self.currentFileTypes = []
        self.lastfileTypes = []

        self.files = []
        

        self.ui.pushButton_gozAt.clicked.connect(self.openFileDialog)
        self.ui.pushButton_UzantilaraGore.clicked.connect(self.fileEditor)
        self.ui.pushButton_GeriAl.clicked.connect(self.takeItBack)
        self.ui.pushButton_Tr_flag.clicked.connect(self.translateToTurkish)
        self.ui.pushButton_Usa_flag.clicked.connect(self.translateToEnglish)
        





    def translateToTurkish(self):
        self.ui.pushButton_GeriAl.setText("Geri Al")
        self.ui.pushButton_UzantilaraGore.setText("Uzantıya Göre Düzenle")
        self.ui.label.setText("Düzenlemek istediğiniz klasörü seçiniz")
        MainWindow.setWindowTitle(self,"Klasör Düzenleyici")
        


    def translateToEnglish(self):
        self.ui.pushButton_GeriAl.setText("Undo")
        self.ui.pushButton_UzantilaraGore.setText("Edit by Extension")
        self.ui.label.setText("Select the folder you want to edit")
        MainWindow.setWindowTitle(self,"Folder Editor")


    



    def fileEditor(self):
        #self.fileTypes = []
        #self.currentFileTypes = []
        #self.lastfileTypes = []

        #self.files = []

        self.choosenFolder = self.ui.label_2.text()
        os.chdir(self.choosenFolder)
        for i in os.listdir(self.choosenFolder):
            if os.path.isdir(os.path.join(self.choosenFolder,i)):
                self.currentFileTypes.append(i)

        for i in os.listdir(self.choosenFolder):
            if os.path.isfile(os.path.join(self.choosenFolder,i)):
                self.files.append(i)            
                file,extention = os.path.splitext(i)
                if extention[1::] not in self.currentFileTypes:
                    self.fileTypes.append(extention[1::])


        #creating folders
        for i in self.fileTypes:
            if os.path.isdir(os.path.join(self.choosenFolder,i)):
                continue
            else:
                os.mkdir(i)

        #we did that for collect all file types
        for i in os.listdir(self.choosenFolder):
            if os.path.isdir(os.path.join(self.choosenFolder,i)):
                self.lastfileTypes.append(i)




        for i in self.lastfileTypes:
            for j in self.files:
                if i == j.split(".")[-1]:
                    os.replace(os.path.join(self.choosenFolder,j),os.path.join(self.choosenFolder,i,j))


    
    def takeItBack(self):
        for i in self.files:
            x,y = os.path.splitext(i)
            os.replace(os.path.join(self.choosenFolder,y[1::],i),os.path.join(self.choosenFolder,i))

        for i in set(self.fileTypes):
            os.rmdir(os.path.join(self.choosenFolder,i))
        self.fileTypes.clear()
        self.currentFileTypes.clear()
        self.lastfileTypes.clear()
        self.files.clear()
        
        
        


    def openFileDialog(self):
        folderD = QFileDialog.getExistingDirectory(self, 'Select directory')
        self.ui.label_2.setText(str(folderD))






app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
