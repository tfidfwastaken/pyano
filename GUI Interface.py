import tkinter as tk
from tkinter import font  as tkfont
import noteplayer
import trackGenerator
import functools

def noteEditCallback(name):
            trackGenerator.editTrack(name)


class SampleApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pick your Option", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10, padx = 50)

        button1 = tk.Button(self, text="Notes Editor",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Notes Player",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Notes Editor", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        mylist = trackGenerator.retTrackNames()
        for item in mylist:
            button = tk.Button(self,text=item,command=functools.partial(noteEditCallback,item))
            button.pack()
                
        button2 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Notes Player", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Play Notes from file",
                           command=lambda: noteplayer.main(1))
        button1.pack()

        button2 = tk.Button(self, text="Enter Notes to play",
                           command=lambda: noteplayer.main(2))
        button2.pack()

        button3 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button3.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
