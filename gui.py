from tkinter import *

# TKINTER
root = Tk()
root.title("Admin Panel - KellyV")
root.geometry("500x400")
root.resizable(False, False)

class KellyV:
    def __init__(self, master):
        mainFrame = Frame(master)
        mainFrame.pack()

        # COMMAND HEADING
        heading1 = Label(master, text="Command:")
        heading1.pack()
        heading1.place(x=30, y=350)

        # VICTIM HEADING
        heading2 = Label(master, text="Victims:")
        heading2.pack()
        heading2.place(x=350, y=15)

        # OUTPUT HEADING
        heading3 = Label(master, text="Output:")
        heading3.pack()
        heading3.place(x=30 ,y=15)

        # COMMAND ENTRY
        commandInput = Entry(master, width=60)
        commandInput.pack()
        commandInput.place(x=30, y=365)

        # EXECUTE BUTTON
        executeButton = Button(master, text="EXECUTE")
        executeButton.pack()
        executeButton.place(x=420, y=361)

e = KellyV(root)
root.mainloop()