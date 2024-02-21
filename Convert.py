import pytesseract as pyt
import cv2
from googletrans import Translator
import pyautogui as pg
import Socket

class Convert():
    def __init__(self, psm = 6, oem = 3, img = "./img.png"):
        self.config = fr"--psm {psm} --oem {oem}"
        self.img = img
        self.trans = Translator()
        self.server = Socket.socket

    def read(self, message, regeon):
        try:
            self.args = message.split(":")
            print (self.args)
            if self.args[0] == "TextRequest":            
                self.text = self.convert(regeon)
                
                if self.args[1] == "tr":
                    self.text = self.Translate(self.text, self.args[2])
                
            else:
                self.text = "NO Function"
                
        except Exception as E:
            print(E)
            return "Error code 184: Read"
        
        return self.text.encode()

        


    def Translate(self, text, language):
        try:
            print("translating")
            translated_text = self.trans.translate(text, src="en", dest=language)
            print(translated_text)
            return translated_text.text
        except Exception as E:
            print(E)
            
            return "Error code 692: Translate"

    def convert(self, regeon):
        try:
            image = pg.screenshot("img.png", regeon)
            image = cv2.imread(self.img)
            grayImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            text = pyt.image_to_string(grayImage, config=self.config)
            text = text.replace("\n", " ")
            print(text)
            return text
        except Exception as E:
            print(E)
            
            return "Error code 293: Convert err"
