from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image,ImageTk,ImageGrab
from tkinter import colorchooser


def change_pen_color():
    global pen_color
    pen_color=colorchooser.askcolor(color=None)


def change_pen_size():
    global pen_thickness
    pen_thickness = pen_size.get()


def draw(event):
    global pen_thickness, pen_color
    try:
        if pen_size:
            size_entry = int(pen_thickness)
        x=event.x
        y=event.y
        canvas.create_oval(x, y, x + size_entry, y + size_entry, fill=pen_color[1], outline=pen_color[1])
    except ValueError:
        mb.showerror("Ошибка!", f"Значение {pen_thickness} не может быть преобразовано в целое число")


def load():
    try:
        file_path=fd.askopenfilename(filetypes=[("Image files",
                                                 "*.png;*.gif;*.jpeg;*.jpg;*.bmp")])
        if file_path:
            image=Image.open(file_path)
            image=image.resize((600,400))
            image_tk=ImageTk.PhotoImage(image)
            canvas.create_image(0,0,anchor=NW,image=image_tk)
            canvas.image=image_tk
    except Exception as e:
        mb.showerror("Ошибка!",f"Не удалось загрузить из-за ошибки {e}")


def save():
    try:
        file_path=fd.asksaveasfilename(defaultextension=".png",
                                       filetypes=[("PNG files","*.png;*.gif")])
        if file_path:
            x=window.winfo_rootx()
            y=window.winfo_rooty()
            x1=x+canvas.winfo_width()
            y1=y+canvas.winfo_height()
            ImageGrab.grab().crop((x,y,x1,y1)).save(file_path)
            mb.showinfo("Сохранено",
                        f"Изображение сохранено в {file_path}")
    except Exception as e:
        mb.showerror("Ошибка",f"Не удалось сохранить из-за ошибки {e}")

pen_thickness = 1
pen_color=((255, 0, 0),"#ff0000")

window=Tk()
window.title("Графический редактор")

canvas=Canvas(width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить изображение", command=load)
file_menu.add_command(label="Сохранить холст", command=save)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=window.destroy)

Label(text="Толщина линии:").pack(side=LEFT)
pen_size = Entry()
pen_size.pack(side=LEFT)
pen_size.insert(0, "1")

b1=Button(text="Установить толщину", command=change_pen_size)
b1.pack(side=LEFT)
b2=Button(text="Выбор цвета", command=change_pen_color)
b2.pack(side=RIGHT)

window.mainloop()
