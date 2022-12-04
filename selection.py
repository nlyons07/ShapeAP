from PyQt5.QtWidgets import *
from GUIMain import *
from Circle import *
from Rectangle import *
from Triangle import *
from Square import *

# learn how to change color of GUI

class Shapes(QMainWindow, Ui_Main):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        '''
        When any shape button is clicked it will lead to function to open a new window of information
        '''
        self.buttonCircle.clicked.connect(lambda: self.bCircle())
        self.buttonRectangle.clicked.connect(lambda: self.bRectangle())
        self.buttonTriangle.clicked.connect(lambda: self.bTriangle())
        self.buttonSquare.clicked.connect(lambda: self.bSquare())
        print('car')



    def bCircle(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowCircle()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushMainC.clicked.connect(lambda: self.goBack())
        self.ui.pushMCircle.clicked.connect(lambda: self.MeasureC())
        print('fish')

    def MeasureC(self):
        #  CIRCLE INPUTS
        pi = 3.14
        radius = float(self.ui.radius.toPlainText())

        if self.ui.radioPerimeterC.isChecked():
            #  CIRCLE MEASUREMENTS PER
            #  sets the amount and display text
            measureCircle = 2 * (pi * radius)  # perimeter
            measureCircle = "{:.2f}".format(measureCircle)
            self.ui.numCircle.setText(str(measureCircle))
            self.ui.textCircle.setText(str('The Perimeter of the Circle is...'))

        if self.ui.radioAreaC.isChecked():
            #  CIRCLE MEASUREMENTS AREA
            #  sets the amount and display text
            measureCircle = pi * (radius * radius)  # area
            measureCircle = "{:.2f}".format(measureCircle)
            self.ui.numCircle.setText(str(measureCircle))
            self.ui.textCircle.setText(str('The Area of the Circle is...'))
            print(measureCircle)

    def bRectangle(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowRectangle()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushMainR.clicked.connect(lambda: self.goBack())
        self.ui.pushMRectangle.clicked.connect(lambda: self.MeasureR())
        print('dog')

    def MeasureR(self):
        # RECTANGLE INPUTS
        length = float(self.ui.length.toPlainText())
        width = float(self.ui.width.toPlainText())

        if self.ui.radioPerimeterR.isChecked():
            #  RECTANGLE MEASUREMENTS PER
            measureRectangle = 2 * (length + width)
            measureRectangle = "{:.2f}".format(measureRectangle)
            self.ui.numRectangle.setText(str(measureRectangle))
            self.ui.textRectangle.setText(str('The Perimeter of the Rectangle is...'))

        if self.ui.radioAreaR.isChecked():
            measureRectangle = length * width
            measureRectangle = "{:.2f}".format(measureRectangle)
            self.ui.numRectangle.setText(str(measureRectangle))
            self.ui.textRectangle.setText(str('The Area of the Rectangle is...'))

    def bTriangle(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowTriangle()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushMainT.clicked.connect(lambda: self.goBack())
        self.ui.pushMTriangle.clicked.connect(lambda: self.MeasureT())

    def MeasureT(self):
        #  TRIANGLE INPUTS
        #  Triangle PER

        if self.ui.radioPerimeterT.isChecked():
            side1 = float(self.ui.side1.toPlainText())
            side2 = float(self.ui.side2.toPlainText())
            side3 = float(self.ui.side3.toPlainText())

            #  CIRCLE MEASUREMENTS PER
            measureTriangle = (side1 + side2 + side3)  # perimeter
            measureTriangle = "{:.2f}".format(measureTriangle)
            self.ui.numTriangle.setText(str(measureTriangle))
            self.ui.textTriangle.setText(str('The Perimeter of the Triangle is...'))

        #  Triangle Area

        if self.ui.radioAreaT.isChecked():
            base = float(self.ui.base.toPlainText())
            height = float(self.ui.height.toPlainText())

            #  CIRCLE MEASUREMENTS AREA
            measureTriangle = 0.5 * (base * height)  # area
            measureTriangle = "{:.2f}".format(measureTriangle)
            self.ui.numTriangle.setText(str(measureTriangle))
            self.ui.textTriangle.setText(str('The Area of the Triangle is...'))


    def bSquare(self):
        self.hide()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_WindowSquare()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.pushMainS.clicked.connect(lambda: self.goBack())
        self.ui.pushMSquare.clicked.connect(lambda: self.MeasureS())

    def MeasureS(self):
        #  SQUARE INPUTS
        sides = float(self.ui.sides.toPlainText())

        if self.ui.radioPerimeterS.isChecked():
            #  SQUARE MEASUREMENTS PER
            measureSquare = 4 * sides  # perimeter
            measureSquare = "{:.2f}".format(measureSquare)
            self.ui.numSquare.setText(str(measureSquare))
            self.ui.textSquare.setText(str('The Perimeter of the Square is...'))


        if self.ui.radioAreaS.isChecked():
            #  SQUARE MEASUREMENTS AREA
            measureSquare = sides * sides  # area
            measureSquare = "{:.2f}".format(measureSquare)
            self.ui.numSquare.setText(str(measureSquare))
            self.ui.textSquare.setText(str('The Area of the Square is...'))



    def goBack(self):
        print('person')
        '''self.hide()'''
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Main()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.buttonCircle.clicked.connect(lambda: self.bCircle())
        self.ui.buttonRectangle.clicked.connect(lambda: self.bRectangle())
        self.ui.buttonTriangle.clicked.connect(lambda: self.bTriangle())
        self.ui.buttonSquare.clicked.connect(lambda: self.bSquare())