# 种子

# 组成类
class Composition(object):
	"""docstring for Composition"""
	def __init__(self, arg):
		super(Composition, self).__init__()
		self.arg = arg

# 种皮
class SeedCoat(object):
	"""docstring for SeedCoat"""
	def __init__(self, arg):
		super(SeedCoat, self).__init__()
		self.arg = arg
		# 保护作用

# 胚乳
class Endosperm(object):
	"""docstring for Endosperm"""
	def __init__(self, arg):
		super(Endosperm, self).__init__()
		self.arg = arg
		# 营养物质

# 胚
class Embryo(object):
	"""docstring for Embryo"""
	def __init__(self, arg):
		super(Embryo, self).__init__()
		self.arg = arg
		# 胚芽
		self.germ = germ
		# 胚轴
		self.hypocotyl = hypocotyl
		# 胚根
		self.radicle = radicle
		# 子叶
		self.cotyledon = cotyledon
