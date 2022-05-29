from tkinter import *
from PIL import ImageTk, Image


class KellyV(Tk):

    def __init__(self):
        super().__init__()
        self.closeButtonWin = None
        self.overrideredirect(True)
        self.closeButton = None
        self.titleBar = None
        self.canvas = Canvas(self, width=1920, height=1080, bg="white", highlightthickness=0)
        self.bgImage = None
        self.bgImageLabel = None
        self.geometry("1920x1080")
        self.resizable(False, False)
        self.drawBackground()
        self.victims()
        self.initCustomTitleBar()
        self.canvas.pack()


    def initCustomTitleBar(self):
        self.canvas.create_line(10,40,1910,40, fill='gray')
        self.closeButtonImg = ImageTk.PhotoImage(Image.open("closeButton.png"))
        self.closeButton = self.canvas.create_image(1890, 35/2, image=self.closeButtonImg)
        self.canvas.tag_bind(self.closeButton, "<Button-1>", self.closeWindow)
        #self.closeButton = Button(self, image=self.closeButtonImg, highlightbackground="gray", bg="gray", command=self.destroy)
        #self.closeButtonWin = self.canvas.create_window(1910-20, 35/2, anchor=CENTER, window=self.closeButton, width=35, height=35)


    def moveWindow(self, event):
        self.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    def closeWindow(self, event):
        self.destroy()

    def drawBackground(self):
        self.bgImage = ImageTk.PhotoImage(Image.open("bg.png"))
        self.canvas.create_image(0, 0, anchor=NW, image=self.bgImage)

    def victims(self):
        pass


if __name__ == "__main__":
    KellyV = KellyV()
    KellyV.mainloop()
