# simple pyqt application

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import sys

class HelloWorld(QtWidgets.QWidget): ## QWidget is the base class for all PyQt widgets
    def __init__(self,*args,**kwargs): ## If you are unfamiliar with python and are wondering what is *args, **kwargs,
                                       ## see https://realpython.com/python-kwargs-and-args/
        super(HelloWorld,self).__init__(*args,**kwargs) ## Initialize a QWidget instance.

        ## Creating a layout for other widgets/items/layouts to be placed in. 
        ## The layout determines where the objects will be placed.
        ## The QGridLayout is a quick and easy for a "tile-style" layout. 
        ## (see: https://doc.qt.io/qtforpython/PySide2/QtWidgets/QGridLayout.html)
        layout = QtWidgets.QGridLayout(self)

        ## Create a label
        ## (see: https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLabel.html)
        self.label = QtWidgets.QLabel("Hello World!")

        ## Create a text editor
        ## (see: https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLineEdit.html)
        self.edit = QtWidgets.QLineEdit()

        ## Create a listbox
        ## (see: https://doc.qt.io/qtforpython/PySide2/QtWidgets/QListWidget.html)
        self.list = QtWidgets.QListWidget()

        ## Create a push button
        ## (see: https://doc.qt.io/qtforpython/PySide2/QtWidgets/QPushButton.html)
        self.button = QtWidgets.QPushButton("Click Me")

        ## Add widgets to layout
        layout.addWidget(self.label,0,0)    ## Add to position row 0, column 0
        layout.addWidget(self.edit,1,0)     ## Add to position (1,0)
        layout.addWidget(self.list,2,0,3,1) ## Add to position (2,0) and extend 3 tiles down and 1 tile across. 
                                            ## If unspecified like above, the default value for the latter two arguments is 1.
        layout.addWidget(self.button,5,0)   ## Add to position (5,0)

        ## PyQt uses signals to communicate between widgets. You can create your own signals but in this case we will connect
        ## the push button's click signal to a function that adds an item to the listbox, whose text is whatever the user has in the
        ## line edit widget.

        self.button.clicked.connect(self.addToList) ## In this case, clicked is the signal and we are connecting it to the function addToList.

        ## Signals are very useful for PyQt applications. 
        ## (see: https://www.pythoncentral.io/pysidepyqt-tutorial-creating-your-own-signals-and-slots/)

    def addToList(self):
        ## This function adds an item to the list with the text set to whatever is in the line edit.
        self.list.addItem(self.edit.text())

## Code to run the widget
if __name__ == '__main__': ## Only run if the script is being called directly and not when imported.
    app = QtWidgets.QApplication([]) ## Create a QApplication instance. This is what is used to run the GUI.
    widget = HelloWorld() ## Create an instance of HelloWorld
    widget.show() ## Show the widget
    sys.exit(app.exec_())



