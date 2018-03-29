import os
import sys

def readBase():
	""" 返回数据库列表 
	"""
	fileList = []
	nowDir = os.getcwd() #当前目录
	for filename in os.listdir(r'../materialDatabase'):
		#print(filename)
		path = os.path.split(nowDir)[0] + '/materialDatabase/{}'.format(filename)
		fileList.append(path)
	#print(fileList)
	return fileList

readBase()



