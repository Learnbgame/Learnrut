# 器官类
class Organ(object):
	"""docstring for Organ"""
	def __init__(self, name):
		super(Organ, self).__init__()
		self.name = name
		


# 组织类
class Tisssue(object):
	"""docstring for Tisssue"""
	def __init__(self, name):
		super(Tisssue, self).__init__()
		self.name = name
		# 组织类型


#细胞类

class Cell(object):
	"""
	docstring for Cell
	"""
	def __init__(self, name):
		super(Cell, self).__init__()
		self.name = name
		# 拥有细胞器的类型(叶绿体，线粒体。。。)
		self.ORGANELLES = []
		# 细胞类型(动物，植物，。。。)
		# 细胞大小(直径)
		self.CELLSIZE = 0
		# 细胞膜
		# 含有化学成分(C,H,O...)
		self.CHEMICALELEMNETS=[]
		# 人工培养和自然状态
		# 染色体
		# 所含基因
		# 全能性
		
	#细胞融合
	def cellFusion():
		pass
	#细胞繁殖
	def cellReproduction():
		pass
#细胞器类
class Organelle(object):
	"""docstring for Organelle"""
	def __init__(self, name):
		super(Organelle, self).__init__()
		self.name = name
		
		