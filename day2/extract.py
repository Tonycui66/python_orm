from PIL import Image
import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Load the image from file
print(__file__)
img_path = "D:/tools/PycharmProjects/testexec/day2/1.png"
img = Image.open(img_path)
# print(img)
# Use tesseract to do OCR on the image
text = pytesseract.image_to_string(img)

print(text)
