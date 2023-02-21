#dare, elements
import daredive
import galacticschooter
import discordbot
import elementsunleashed


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('gawkgawk3000')
root.resizable(False, False) 
image2 = Image.open('Pixellet TH (4).png')
image1 = ImageTk.PhotoImage(image2)
w = image1.width()
h = image1.height()
root.geometry('%dx%d+0+0' % (w, h))

label1 = Label(root, image=image1).place(x=0, y=0, relwidth=1, relheight=1)

#daredive
btnimg1 = PhotoImage(file='Pixellet TH (12).png')
btn1 = Button(root, image=btnimg1, bd=0, command=lambda: daredive.daredive())
btn1.place(x=59, y=75)

#elements unleashed
btnimg2 = PhotoImage(file='Pixellet TH (14).png')
btn2 = Button(root, image=btnimg2, bd=0, command=lambda: elementsunleashed.elementsunleashed())
btn2.place(x=355, y=75)

#galactic shooter
btnimg3 = PhotoImage(file='Pixellet TH (15).png')
btn3 = Button(root, image=btnimg3, bd=0, command=lambda: galacticschooter.galacticshooter())
btn3.place(x=59, y=275)

#whimsybot
btnimg4 = PhotoImage(file='Pixellet TH (16).png')
btn4 = Button(root, image=btnimg4, bd=0, command=lambda: discordbot.discordbot())
btn4.place(x=355, y=275)


root.mainloop()