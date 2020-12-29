from autogui.main import Button

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
				x_ = self.x + (self.step + self.w) * (len(self.buttons) - 1)
				return (x_*Auto.x_, y_*Auto.y_, self.w * Auto.x_, self.h*Auto.y_)
			elif self.mode == 2:

				col = (len(self.buttons) -1) % self.maxX
				row = int((len(self.buttons) - 1) / self.maxX)

				x_ = self.x + (self.stepX + self.w) * col
				y_ = self.y + (self.stepY * self.h) * row

				return (x_*Auto.x_, y_*Auto.y_, self.w * Auto.x_, self.h*Auto.y_)


		def map(self, function):

			for x in range(len(self.buttons)):
				function(self.buttons[x])

