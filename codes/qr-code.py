import pyqrcode 
from pyqrcode import QRCode 
  
s = input("Enter the url/text : ")
url = pyqrcode.create(s) 
name =  input("Enter the name of the qr code file : ")
url.svg(name + ".png", scale = 8)
