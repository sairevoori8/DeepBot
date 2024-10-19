import easyocr
import cv2
import matplotlib.pyplot as plt

class TextExtract:
    def Textdata(self,loc):
        reader = easyocr.Reader(['en'], gpu=False)
        image = cv2.imread(loc)

        result = reader.readtext(image)
        mystring=''
        for (bbox, text, prob) in result:
            if prob >0.2:
               # print(f"Detected text: {text} with confidence {prob}")
                mystring=mystring+" "+text
        return mystring
        
