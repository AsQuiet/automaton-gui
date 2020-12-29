from autogui import *
import os

class Auto:
	x_ = 20
	y_ = 20

	ButtonGroupVertical = 0
	ButtonGroupHorizontal = 1
	ButtonGroupGrid = 2

	def set(x, y,):
		Auto.x_ = x
		Auto.y_ = y

	def place(obj, x, y, w, h, centerX=False, centerY=False):
		cy = (h*Auto.y_ * .5) if centerY else 0
		obj.setGeom(x*Auto.x_, y*Auto.y_ - cy, w*Auto.x_, h*Auto.y_)

	class ButtonGroup(object):

		def __init__(self, x, y, w, h, step, mode=0):
			self.x = x    # positions and sizes should be in grid coordinates!
			self.y = y
			self.w = w
			self.h = h
			self.step = step
			self.mode = mode

			self.buttons = []

			# for grid mode, should be set with a function
			self.stepX = 0
			self.stepY = 0
			self.maxX = 3

		def setGridOptions(self, stepx, stepy, maxx):
			self.stepX = stepx
			self.stepY = stepy
			self.maxX = maxx

		def addButton(self, app, text="A button", function=lambda:print("you pressed a button")):
			index = len(self.buttons)
			self.buttons.append(Button(app, function=function, text=text))
			self.buttons[index].setGeom(*self.getNewPosition())

		def addButtons(self, app, names=["A button"], functions=[lambda:print("you pressed a button")]):
			for x in range(len(names)):
				self.addButton(app, names[x], functions[x if len(functions) == len(names) else 0])

		def getNewPosition(self):

			if self.mode == 0:
				x_ = self.x
				y_ = self.y + (self.step + self.h) * (len(self.buttons) -1)

				return (x_*Auto.x_, y_*Auto.y_, self.w * Auto.x_, self.h*Auto.y_)
			elif self.mode == 1:
				y_ = self.y
				x_ = self.x + (self.step + self.x) * (len(self.buttons) - 1)
				return (x_*Auto.x_, y_*Auto.y_, self.w * Auto.x_, self.h*Auto.y_)
			elif self.mode == 2:

				col = (len(self.buttons) -1) % self.maxX
				row = int((len(self.buttons) - 1) / self.maxX)

				x_ = self.x + (self.stepX + self.x) * col
				y_ = self.y + (self.stepY * self.y) * row

				return (x_*Auto.x_, y_*Auto.y_, self.w * Auto.x_, self.h*Auto.y_)


		def map(self, function):

			for x in range(len(self.buttons)):
				function(self.buttons[x])


def setup(app):
	Auto.set(20, 20)

	buttongroup1 = Auto.ButtonGroup(2, 2, 3, 2, -1, Auto.ButtonGroupGrid)
	buttongroup1.setGridOptions(1, 1, 3)
	buttongroup1.addButtons(app, ["1","2","3","4","5","7","8","9","0"])

	plusButton = Button(app, "+")
	Auto.place(plusButton, 11, 2, 3, 2)

	minButton = Button(app, "-")
	Auto.place(minButton, 11, 4, 3, 2)

	# buttongroup1.buttons[0].setIcon("icon.png")
	# buttongroup1.buttons[1].setIcon("astro.png")

	#loading in font
	families = app.loadFont("geonms.ttf")				# reading the fucking file
	nms_font = Font.createFont(app, families[0], 24)	# getting the fucking font

	def function():
		print("whooo oo o o")

	def setup_button(button):
		button.setFont(nms_font)
		button.setIconSize(24, 24)
		button.setFunction(function)

		if button.text == "Astroneer": print("skdjksd")

	buttongroup1.map(setup_button)


	# dropdown1 = Dropdown(app, ["Red", "Blue", 'Orange', "Nope"])

	# button1 = Button(app, function=lambda:print("oooo"))
	# button1.setText("No Man's Sky")
	# button1.setIcon("icon.png")
	# button1.setIconSize(24, 24)

	# Auto.place(button1, 1, 1, 13, 2)

	# label1 = Label(app, "Fuck Yoouuu")
	# label1.setText("Relatively good game, shit ton of planets.")

	# Auto.place(label1, 14, 1, 20, 2)

	# button4 = Button(app, function=lambda:print("aaaa"))
	# button4.setText("Astroneer")
	# button4.setIcon("astro.png")
	# button4.setIconSize(24, 24)

	# Auto.place(button4, 1, 3, 13, 2)

	# label2 = Label(app, "Relatively shit game, good planets.")

	# Auto.place(label2, 14, 3, 20, 2)


	# families = app.loadFont("geonms.ttf")				# reading the fucking file
	# nms_font = Font.createFont(app, families[0], 24)	# getting the fucking font

	# button1.setFont(nms_font)
	# button4.setFont(nms_font)

	# check1 = Checkbox(app)
	# check1.setGeom(50, 160)

	# def displayPup():
	# 	msg = Popup(app)
	# 	msg.setText("fuck yo u no more icons, state of becoming god : " + str(check1.getValue()))
	# 	msg.setWarningIcon()
	# 	msg.init()

	# button2 = Button(app, function=displayPup)
	# button2.setGeom(100, 300)
	
	# inputfield1 = Inputfield(app)
	# inputfield1.setGeom(670, 55, 200, 20)

	# def getinputfieldtext():
	# 	Popup(app, "the text is : " + inputfield1.getValue()).init()
	# 	inputfield1.setText("oke, message received asshat")

	# button3 = Button(app, function=getinputfieldtext)
	# button3.setGeom(670,80, 100, 40)

	# slider1 = Slider(app, 5, 0, 1000, 100, type_=1)
	# Auto.place(slider1, 0.25, 0.25, 1, 20)

	# table1 = Table(app, 40, 40)

	# table1.setGeom(200, 150, 300, 300)

	# def double():
	# 	print(table1.getCell(4,4))
	# 	print("sd")
	# 	table1.hide()


	# table1.setFunction(double)


	# def loop():
	# 	if slider1.getValue() > 980:
	# 		table1.show()

	# app.loop(loop, 500)


	scl = 0.6
	app.window_size_min = (1600*scl, 900*scl)
	app.setWindowMin()
	app.window_icon_path = 'icon.png'
	app.setWindowIcon()
	app.init()



myApp = App(setup)



