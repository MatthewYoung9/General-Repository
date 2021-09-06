# Input PDF's and tpage numbers. result is a merging of the pages.


#Improvements include: 
# enter number of docs and then have fileN, fileNpage,... be auto generated (use dictionaries) 
# the only thing you'd then have to do to the doc would be to import the location, the number of docs and the page numbers.
# This could then be dev'd into an app with tkinter or similar. 
# 
import PyPDF2 as p


def pageAdder(source, target, zero_index_page_num):
    pageObj = source.getPage(zero_index_page_num)
    target.addPage(pageObj)
    
issues = ["_DNE","_overpaid","_refused"]
my_issue = issues[0]

location = "Hull"

# Here you need to create variables with the numbers upto what you have.

file1 = open(location +".pdf", "rb")
file2 = open(location+' 2.pdf','rb')
file3 = open(location+' 3.pdf','rb')
file4 = open(location+' 4.pdf','rb')
file5 = open(location+' 5.pdf','rb')
file6 = open(location+' 6.pdf','rb')
file7 = open(location+' 7.pdf','rb')
file8 = open(location+' 8.pdf','rb')
allFiles =[file1, file2, file3, file4,file5,file6,file7,file8]


# Here you need to create list variables with the numbers upto what you have.

file1Pages = [19,28]
file2Pages = [4]
file3Pages = [1,2]
file4Pages = [13,16]
file5Pages = []
file6Pages = []
file7Pages = []
file8Pages = []
allFilePages = [file1Pages, file2Pages, file3Pages,file4Pages, file5Pages,file6Pages,file7Pages,file8Pages]



for file in allFilePages:
    for i in range(len(file)):
        file[i]-= 1


# Here you need to create variables with the numbers upto what you have don't forget the list.
file1Reader = p.PdfFileReader(file1)
file2Reader = p.PdfFileReader(file2)
file3Reader = p.PdfFileReader(file3)
file4Reader = p.PdfFileReader(file4)
file5Reader = p.PdfFileReader(file5)
file6Reader = p.PdfFileReader(file6)
file7Reader = p.PdfFileReader(file7)
file8Reader = p.PdfFileReader(file8)
fileReaders= [file1Reader,file2Reader,file3Reader,file4Reader,file5Reader,file6Reader,file7Reader,file8Reader]



######

#WHERE THE MAGIC HAPPENS

newDoc = p.PdfFileWriter()

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




