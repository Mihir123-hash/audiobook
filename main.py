#step1: In order to make python speak, GO to terminal> type pip install pyttsx3
#pyttsx3 stands for python text to speach version(3)


#step2


import pyttsx3 #import in order to make python speak

import PyPDF2 #to read a pdf file in python

book = open('AI.pdf' , 'rb') # book name that user wants to  read
pdfReader = PyPDF2.PdfFileReader(book) #pdfReader initiates the book assingned by user
pages = pdfReader.numPages  # to find number of pages and check whether py has selected correct pdf
print(pages)
speaker = pyttsx3.init() # initialize pyttsx3
for num in range(6, pages):
    page = pdfReader.getPage(num)  # to get the page number where to start from
    text = page.extractText()
    speaker.say(text)  # this function alllows speaker to speak
    speaker.runAndWait()  # the speaker will run and wait


#step3 Go to terminal and install package PyPDF2
# ie  pip install PyPDF2
#PyPDF2  is used to read any pdf file in your pc


