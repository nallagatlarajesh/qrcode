import qrcode
from pyzbar.pyzbar import decode
from PIL import Image



myqr=qrcode.make("https://channeli.in/placement_and_internship/resume/")
myqr1=qrcode.make("https://www.coursera.org/articles/what-is-python-used-for-a-beginners-guide-to-using-python")

myqr.save("myqr.png",scale=8)
myqr1.save("myqr1.png",scale=7)

b=decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))
