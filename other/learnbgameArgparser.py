import argparse
import os 
import sys 


__version__ = 1.0
nowdir = os.getcwd() #当前目录

parser = argparse.ArgumentParser(
        prog='learnbgame', 
        usage="python learnbgame.py [option]", 
        description="learnbgame help document", 
        epilog="And that’s how you‘d use learnbgame", 
        parents=[], 
        formatter_class=argparse.HelpFormatter, 
        prefix_chars='-', 
        fromfile_prefix_chars=None, 
        argument_default=None, 
        conflict_handler='error', 
        add_help=True, 
        allow_abbrev=True,
        )




parser.add_argument(
	'--txt',
	metavar='<filename>',
	dest='txtf',
	help="specify input filenamen with txt format")
parser.add_argument(
	'--pdf',
	metavar='<filename>',
	dest='pdff',
	help="specify input filenamen with pdf format")
parser.add_argument(
    '--ppt',
    metavar='<filename>',
    dest='pptf',
    help="specify input filenamen with ppt format")
parser.add_argument(
	'--csv',
	metavar='<filename>',
	dest='csvf',
	help="specify output filenamen with csv format")
parser.add_argument(
        '--docx',
        metavar='<filename>',
        dest='docxf',
        help="specify input filenamen with docx format")
parser.add_argument(
        '-version', 
        action='version',
         version='%(prog)s {0}'.format(__version__))
parser.add_argument(
        '-translate',
        metavar='',
        dest='tran',
        help="Achieve translation feature")
parser.add_argument(
        '-keyword',
        metavar='',
        dest='keyword',
        help="Achieve search keywords feature")


    
    

args = parser.parse_args()  


#txtf = args.txtf
#csvf = args.csvf
  
