import Image, ImageDraw
from hashlib import md5


GRID_SIZE = 9
BORDER_SIZE = 10
SQUARE_SIZE = 10


class Identicon(object):
	def __init__(self, str_, background='#000'):
		"""
		str_ is the string used to generate the identicon
		background is the background of the identicon
		"""
		w = h = BORDER_SIZE * 2 + SQUARE_SIZE * GRID_SIZE
		self.image = Image.new('RGB', (w, h), background)
		self.draw = ImageDraw.Draw(self.image)
		self.hash = self.digest(str_)

	def digest(self, str_):
		"""
		returns a md5 numeric hash
		"""
		return int(md5(str_).hexdigest(), 16)

	def calculate(self):
		"""
		create the identicon
		first three bytes are used to generate the color
		remaining bytes are used to create the drawing
		"""
		color = (self.hash & 0xff, self.hash >> 8 & 0xff, self.hash >> 16 & 0xff)
		self.hash >>= 24 # skip first three bytes
		square_x = square_y = 0 # init square position
		for x in xrange(GRID_SIZE * (GRID_SIZE + 1) / 2):
			if self.hash & 1:
				x = BORDER_SIZE + square_x * SQUARE_SIZE
				y = BORDER_SIZE + square_y * SQUARE_SIZE
				self.draw.rectangle(
					(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE),
					fill=color,
					outline=color
				)
				# following is just for mirroring
				x = BORDER_SIZE + (GRID_SIZE - 1 - square_x) * SQUARE_SIZE
				self.draw.rectangle(
					(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE),
					fill=color,
					outline=color
				)
			self.hash >>= 1 # shift to right
			square_y += 1
			if square_y == GRID_SIZE: # done with first column
				square_y = 0
				square_x += 1

	def generate(self):
		"""
		save and show calculated identicon
		"""
		self.calculate()
		with open('identicon.png', 'w') as out:
			self.image.save(out, 'PNG')
		self.image.show()