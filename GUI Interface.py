#GUI Interface

from tkinter import *
import trackGenerator
import functools

def noteEditCallback(name):
            trackGenerator.editTrack(name)

class noteEditFrame(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Creates a list of buttons
        label = Label(self, text = "Click on the SoundTrack you wish to edit")
        label.pack(side="top", fill="x", pady=10)
        
        mylist = trackGenerator.retTrackNames()
        for item in mylist:
            button = Button(self,text=item,command=functools.partial(noteEditCallback,item))
            button.pack()
        



root = Tk()
root.title("Pyano - Note Edit")
root.geometry("250x300")

app = noteEditFrame(root)
root.mainloop()
