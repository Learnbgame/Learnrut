import csv 
import os 
from googletrans import Translator
from learnbgameArgparser import args
from languageHash import LANGUAGES


nowdir = os.getcwd() #当前目录

def txTranCsv(txtf,csvf):
    filro = open(txtf,'r')
    filwo = open(csvf,'w')
    translator = Translator()
    contents = filro.read()
    dst = ''
    src = 'auto'
    # 当输入内容超过限制的时候的解决 分段处理
    if len(contents) > 4891:    
        print("翻译的长度超过限制！！！") 
    else:
        for lan in LANGUAGES:
            dst = lan
            transcontent = translator.translate(contents,dest=dst,src=src)
            print(transcontent.text,'----',lan)
            csvWriter = csv.writer(filwo)
            csvWriter.writerow([c for c in transcontent.text.split('\n')])
            #filwo.write(transcontent.text+'\n')
    filro.close()  
    filwo.close()

def inputuptuo1(intuo):    
    # '\User\Desktop\test.txt'-->['\User\Desktop','test.txt']    
    (dirName,fileName) = os.path.split(intuo)
    if dirName:  # 完整路径
        fileDirName = intuo
        dirnNme = dirName 
    else: # 只给一个文件名['','test.txt']
        fileDirName = nowdir + '/' + intuo
        dirName = nowdir
    # 'test.txt' -->['test','.txt']
    (shortname,extension) = os.path.splitext(fileName) # 以最后一个点作为分割标志
    name = shortname + '.csv'
    fileList = []
    fileOutList = []



def main():
    txTranCsv(args.txtf,args.csvf)




if __name__ == '__main__':
    main()




