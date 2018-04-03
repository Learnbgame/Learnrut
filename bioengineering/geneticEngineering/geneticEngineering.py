# 基因工程

# 基因工程（DNA重组技术）的一般步骤：
	# 1目的基因的获取
	# 2将目的基因与质粒重组
	# 3将重组DNA引入到宿主细胞
	# 4筛选能表达的目的基因	
class GeneticEngineering(object):
		"""docstring for GeneticEngineering"""
		def __init__(self, targetGene):
			super(GeneticEngineering, self).__init__()
			#目的基因
			self.targetGene = targetGene
			#质粒
			self.plasmid = plasmid
			#重组DNA
			self.reccombinationGene = None
			# 宿主细胞
			self.hostCell = hostCell
		# 获取目的基因
		def getTargetGene():
			pass
		# 目的基因与质粒重组
		def recombination(gene=None,plasmid=None):
			pass
		# 将重组DNA导入到宿主细胞
		def leadIn(gene=None,cell=None):
			pass
		# 筛选能表达的目的基因
		def filter(gene=list()):
			pass