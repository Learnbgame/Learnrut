# 核酸

# 脱氧核糖核酸类 DNA
class DeoxyribonucleicAcid(object):
	"""docstring for DeoxyribonucleicAcid"""
	def __init__(self, name):
		super(DeoxyribonucleicAcid, self).__init__()
		self.name = name

# 核糖核酸类 RNA
class RibonucleicAcid(object):
	"""docstring for RibonucleicAcid"""
	def __init__(self, name):
		super(RibonucleicAcid, self).__init__()
		self.name = name

# 基因类
class Gene(object):
	"""docstring for Gene"""
	def __init__(self, name):
		super(Gene, self).__init__()
		self.name = name
