from tkinter import*

def buttdestory():
    window.destroy()

window = Tk()
window.title("2021/11/05")
window.geometry("1024x800+150+50")
window.config(bg = "#ccddff")
window.iconbitmap("hehehe.png")

btnexit = Button(window, width = 10, height = 10, text = "Exit", command = buttdestory)
btnexit.pack()

window.mainloop()