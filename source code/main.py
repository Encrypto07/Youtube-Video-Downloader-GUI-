from tkinter import *
import pafy

root = Tk()
root.geometry('520x320')
root.iconbitmap('icon.ico')
root.title('Youtube Video Downloader')
root.resizable(0, 0)

lab1 = Label(root, text='Enter the Url...👇', font='Rockwell 20 bold', fg='red', padx=10, pady=10)
lab1.pack()

link = StringVar()
link_entry = Entry(root, width=76, textvariable=link).place(x=30, y=50)

def downloader():
    new_url = link.get()
    video = pafy.new(new_url)
    s = video.getbest()
    s.download()


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, relief=GROOVE, borderwidth=6, activebackground='RED', command=downloader).place(x=346, y=75)
root.mainloop()
