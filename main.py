i = input('Enter your image path')

while True:
   x = input('Enter the sentence or word you are looking for :')
   if x:
       if x == 'exit' or x == 'Exit':
           playsound('bye.mp3')
           print("Bye")
           break
       else:
           from playsound import playsound
           from PIL import Image
           # PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.
           import pytesseract

           try:
               img = Image.open(i)#Pytesseract cannot directly take the image so,we need to open the image
               pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract"  # The path of your tesseract executable file.
               result = pytesseract.image_to_string(img)
               print(result)
               wordFound = result.find(x)
               if wordFound > 0:
                   #playsound('myaudio.mp3')
                   print("Your searched has been found")
               else:
                   #playsound('notfound.mp3')
                   print("Oops!!! searched query not found")

           except:
               #playsound('path.mp3')
               print("Oops!!!The path you have provided for the image is not correct or path can not be found.")
               break
