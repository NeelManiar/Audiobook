import pyttsx3
import PyPDF2

book = open("RWCC.pdf", "rb")
pdfReader = PyPDF2 .PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()
page = pdfReader.getPage(0 and 1)
text = page.extractText()
friend.say(text)

friend.runAndWait()
