from PyQt5.QtWidgets import *

from PyQt5 import QtCore 
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui 
import sys, os  


class CustomWindow(QMainWindow):

	def __init__(self):
		super().__init__()

		# self.mouseX = 0
		# self.mouseY = 0

	# def mouseMoveEvent(self, event):
	# 	self.mouseX = e.x()
	# 	self.mouseY = e.y()
	# 	print(f"mouse position is {self.mouseX} : {self.mouseY}")

	def mousePressEvent(self, event): 	#removing the fucking focus 
		focused_widget = QApplication.focusWidget()
		if isinstance(focused_widget, QLineEdit):
			focused_widget.clearFocus()
		QMainWindow.mousePressEvent(self, event)



class App(object):

	def __init__(self, setup=None):

		self.app = QApplication(sys.argv)
		self.fontDB = QtGui.QFontDatabase()

		if setup==None:
			print("abort, no setup given idiot")
			return;

		# settings
		self.window_size = (960, 540)
		self.window_size_min = (960, 540)
		self.window_size_max = (960, 540)

		self.window_title = "Automaton"
		self.window_icon_path = "NO"

		self.window = CustomWindow()
		setup(self)

	def init(self):
		# setting the window settings
		self.window.setWindowTitle(self.window_title)
		# self.window.setWindowModified(True)
		self.window.show()

		sys.exit(self.app.exec_())

	def setWindowMax(self):
		self.window.setMaximumWidth(self.window_size_max[0])
		self.window.setMaximumHeight(self.window_size_max[1])

	def setWindowMin(self):
		self.window.setMinimumWidth(self.window_size_min[0])
		self.window.setMinimumHeight(self.window_size_min[1])

	def setWindowFixed(self):
		self.window.setMaximumWidth(self.window_size[0])
		self.window.setMaximumHeight(self.window_size[1])

	def setWindowIcon(self):
		if self.window_icon_path != "NO":
			self.app.setWindowIcon(QtGui.QIcon(self.window_icon_path))

	def loadFont(self, path):
		# returns all of the font families found at the path (use [0] to get default/Regular
		fontID = self.fontDB.addApplicationFont(os.path.abspath(path))
		return self.fontDB.applicationFontFamilies(fontID)

	def addScrollBar(self):
		print("creating")
		# self.scroll = QScrollArea()
		# self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		# self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		# self.scroll.setWidgetResizable(True)
		# # self.scroll.setWidget(self.window)

		# self.window.setCentralWidget(self.scroll)
		print("done")


	def loop(self, function, interval=16):
		self.timer = QtCore.QTimer(self.window)
		self.timer.setSingleShot(False)
		self.timer.setInterval(interval) # in milliseconds, so 5000 = 5 seconds
		self.timer.timeout.connect(function)
		self.timer.start()

class Button(object):

	def __init__(self, app, text="press me", function=lambda:print("fuck you")):
		self.app = app
		self.text = text
		self.function = function

		self.stylesheet = ""

		self.qbutton = QPushButton(text, self.app.window)
		self.qbutton.clicked.connect(function)

	def setGeom(self, x=30, y=30, w=100, h=30):
		self.qbutton.resize(w, h)
		self.qbutton.move(x, y)

	def setText(self, text="some new fucking text"):
		self.text = text
		self.qbutton.setText(text)

	def setFont(self, font):
		self.qbutton.setFont(font.qfont)

	def setIcon(self, path='NO'):
		if path != 'NO':
			self.qbutton.setIcon(QtGui.QIcon(path))

	def addStyle(self, style):
		self.stylesheet += style
		self.setStyle()

	def setStyle(self):
		self.qbutton.setStyleSheet(self.stylesheet)

	def resetStyle(self):
		self.stylesheet = ""
		self.setStyle()

	def setIconSize(self, w=23, h=23):
		self.qbutton.setIconSize(QtCore.QSize(w,h))

	def setFunction(self, function):
		self.qbutton.clicked.disconnect()
		self.qbutton.clicked.connect(function)



class Label(object):


	def __init__(self, app, text="oh, holy labelmaker"):
		self.app = app
		self.text = text

		self.qlabel = QLabel(text, self.app.window)

	def setGeom(self, x=30, y=30, w=100, h=30):
		self.qlabel.move(x, y)
		self.qlabel.resize(w, h)

	def setText(self, text="oooh getting creative are we???"):
		self.text = text
		self.qlabel.setText(text)

	def setFont(self, font):
		self.qlabel.setFont(font.qfont)


class Font(object):

	def __init__(self, app, name='Arial', size=64):
		self.app = app
		self.name = name
		self.size = size
		self.qfont = QtGui.QFont(name, size)

	@staticmethod
	def createFont(app, font_family, size=11):
		# getting the font from the fontdb
		font_ = app.fontDB.font(font_family, 'Regular', size)

		#creating the Font object & replacing the qfont 
		qfont = Font(app, size=size)
		qfont.qfont = font_

		return qfont


class Image(object):

	def __init__(self, app, path):
		self.app = app

		self.image_label = QLabel(self.app.window)
		self.pixmap = QtGui.QPixmap(os.path.abspath(path))  #loading in the fucking image
		self.image_label.setPixmap(self.pixmap)

		self.image_size = (self.pixmap.width(),self.pixmap.height())
		self.setSize(self.image_size[0],self.image_size[1])

	def move(self, x=0, y=0):
		self.image_label.move(x, y)

	def setSize(self, w=100, h=100):
		self.image_label.resize(w, h)

	def resize(self, w=100, h=100):
		#scaling the image pixmap
		n_pixmap = self.pixmap.scaled(w, h)     
		self.image_label.setPixmap(n_pixmap)
		self.pixmap = n_pixmap

		#scaling the image label / setting the size
		self.setSize(n_pixmap.width(), n_pixmap.height())

class Dropdown(object):

	def __init__(self, app, items):

		self.app = app
		self.items = items

		self.qdropdown = QComboBox(app.window)
		self.qdropdown.addItems(items)

	def setFont(self, font):
		self.qdropdown.setFont(font)

	def setGeom(x=0, y=0, w=100, h=30):
		self.qdropdown.move(x, y)

	def setEditable(self, v=True):
		self.qdropdown.setEditable(v)
	
	def getValue(self):
		return self.qdropdown.currentText()

class Popup(object):

	# Warning = QMessageBox.Warning 

	def __init__(self, app, text="Fee Fo Fi Fum Get Away You Scum"):
		self.app = app
		self.text = text

		self.qpopup = QMessageBox()
		self.qpopup.setText(text)
		
	def setText(self, text):
		self.qpopup.setText(text)

	def setWarningIcon(self):
		self.qpopup.setIcon(QMessageBox.Warning)

	# def setIcon(self, path='NO'):
	#   if path != 'NO':
	#       self.qpopup.setIcon(path)

	def init(self):
		self.qpopup.exec_()

class Inputfield(object):

	def __init__(self, app):
		self.app = app

		self.qinputfield = QLineEdit(self.app.window)
		self.setGeom()

	def setGeom(self, x=0, y=0, w=100, h=20):
		self.qinputfield.move(x, y)
		self.qinputfield.resize(w, h)

	def getValue(self):
		return self.qinputfield.text()

	def setText(self, text):
		self.qinputfield.setText(text)

class BigInputfield(object):

	def __init__(self, app):
		self.app = app

		self.qinputfield = QPlainTextEdit(self.app.window)
		self.setGeom()

	def setGeom(self, x=0, y=0, w=100, h=20):
		self.qinputfield.move(x, y)
		self.qinputfield.resize(w, h)

	def getValue(self):
		return self.qinputfield.toPlainText()

	def setText(self, text):
		self.qinputfield.setText(text)

class Slider(object):

	Horizontal = 0
	Vertical = 1

	def __init__(self, app, value, minvalue, maxvalue, width, type_=0, function=lambda x:print(x)):
		self.app = app
		self.value = value
		self.minvalue = minvalue
		self.maxvalue = maxvalue

		self.width = width

		self.qslider = QSlider(QtCore.Qt.Horizontal if type_ == 0 else QtCore.Qt.Vertical, self.app.window)
		self.qslider.setFocusPolicy(QtCore.Qt.NoFocus)

		self.qslider.setRange(minvalue, maxvalue)
		self.qslider.setPageStep(1)
		self.qslider.setValue(value)

		self.qslider.valueChanged.connect(self.setValue)

		

	def setGeom(self, x=0, y=0, w=100, h=20):
		self.qslider.move(x,y)
		self.qslider.resize(w,h)

	def getValue(self):
		return self.value

	def setValue(self, value):
		self.value = value





class Checkbox(object):


	def __init__(self, app, value=False, text='become god', function=lambda:print('becoming god...')):
		self.app = app
		self.text = text
		self.value = value

		self.qcheckbox = QCheckBox(self.app.window)
		self.qcheckbox.toggled.connect(function)
		self.setText(self.text)

	def getValue(self):
		return self.qcheckbox.isChecked()

	def setText(self, text):
		self.text = text
		self.qcheckbox.setText(text)

	def setValue(self, value=True):
		self.qcheckbox.setChecked()


	def setGeom(self, x=0, y=0, w=100, h=20):
		self.qcheckbox.move(x,y)
		self.qcheckbox.resize(w, h)


class Table(object):

	def __init__(self, app, rows, cols, function=lambda:print("somefucker doubleclicked")):
		self.app = app
		self.rows = rows 
		self.cols = cols

		self.qtable = QTableWidget(self.app.window)
		self.qtable.setRowCount(self.rows)
		self.qtable.setColumnCount(self.cols)
		self.qtable.doubleClicked.connect(function)

		for x in range(rows):
			for y in range(cols):
				# print(f"{x} - {y}")

				self.qtable.setItem(x, y, QTableWidgetItem(""))


	def setGeom(self, x=0, y=0, w=100, h=100):
		self.qtable.move(x,y)
		self.qtable.resize(w,h)

	def getCell(self, x, y):
		return self.qtable.item(x, y).text()

	def setCell(self, x, y, text):
		self.qtable.setItem(x,y, text)

	def setFunction(self, function):
		self.qtable.doubleClicked.connect(function)

	def hide(self):
		self.qtable.hide()

	def show(self):
		self.qtable.show()

		

