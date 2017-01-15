#################################################################################
# CREATOR:   HALEY HAGLER
# DATE:      JANUARY 2017
# TITLE:     read_file.py
# PURPOSE:   Holds useful commands for use in other functions 
################################################################################
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(path):           # Converts the original PDF to a texts file 
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    print "File uploaded"

    f = open("out_put.txt", 'w')
    f.write(text)
    f.close()
    print "File written"



def remove_non_ascii(text):                 # Removes  non-ascii elements for Regex                                
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

def next_important_line( comp, f):          # Skips blank lines
    comp = remove_non_ascii(f.readline())
    while comp == '\n':
        comp = remove_non_ascii(f.readline())
    return comp




