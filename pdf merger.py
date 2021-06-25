# Input PDF's and tpage numbers. result is a merging of the pages.

import PyPDF2 as p


def pageAdder(source, target, zero_index_page_num):
    pageObj = source.getPage(zero_index_page_num)
    target.addPage(pageObj)
    
issues = ["_DNE","_overpaid","_refused"]
my_issue = issues[2]

location = "Doncaster"

file1 = open(location +".pdf", "rb")
file1Pages = [117]


file2 = open(location+' 2.pdf','rb')
file2Pages = []

file3 = open(location+' 3.pdf','rb')
file3Pages = [26,27,28,29,30]

allFiles =[file1, file2, file3]
allFilePages = [file1Pages, file2Pages, file3Pages]



for file in allFilePages:
    for i in range(len(file)):
        file[i]-= 1


file1Reader = p.PdfFileReader(file1)
file2Reader = p.PdfFileReader(file2)
file3Reader = p.PdfFileReader(file3)

fileReaders= [file1Reader,file2Reader,file3Reader]
newDoc = p.PdfFileWriter()



######

#WHERE THE MAGIC HAPPENS

for i in range(len(allFiles)):
    source = fileReaders[i]
    pages = allFilePages[i]
    for k in pages:
            pageAdder(source,newDoc,k)

########
output = open(location+my_issue+'.pdf','wb')

newDoc.write(output)
output.close()

for file in allFiles:
    file.close()


