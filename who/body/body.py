from .eye import Eye
from .ear import Ear
from .mouth import Mouth
from .hand import Hand
from .leg import Leg
#身体部位
class body(object):
	"""docstring for body"""
	def __init__(self, name):
		super(body, self).__init__()
		# 名字
		self.name = name
		# 鼻子
		self.nose = Nose()
		# 眼
		self.eye =Eye()
		# 脚
		self.leg = Leg()
		# 手
		self.hand = Hand()
		# 耳朵
		self.ear = Ear()
		# 嘴
		self.mouth = Mouth()
	# 受伤
