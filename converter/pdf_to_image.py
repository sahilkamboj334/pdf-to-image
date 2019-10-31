from multiprocessing.pool import ThreadPool, Pool

from pdf2image import convert_from_path
import os
#get all the files of a directory
files=os.listdir("../pdfFiles/Old Server Reports/")


def processPDF(file):
    name=(file.split(".")[0])
    counter = 1
    pages=convert_from_path('../pdfFiles/Old Server Reports/'+file)
    for page in pages:
        page.save("../output/"+name+str(counter)+".png",'png')
        counter+=1

def main():
    #processing files parallely using threading
    pool=Pool(4)
    pool.map(processPDF,files)


if __name__ == '__main__':
    main()
