import time
from tkinter import *


def check(event):
    global i
    if event.char==phrase[i]:
        i+=1
        if i==len(phrase):
            difference=time.time()-t
            allowed_time=len(phrase)
            if difference<=allowed_time:
                label.config(text=f"Вы молодец! Ваше время:{difference:.2f} сек")
                w.unbind("Key")
            else:
                label.config(text=f"Тренируйтесь! Отведенное время:{allowed_time} сек!\n" f"Ваше время:{difference:.2f} сек")
                w.unbind("Key")
        else:
            label.config(text=phrase[i])
            w.unbind("Key")
    else:
        label.config(text=f"Ошибка! Ожидалась буква {phrase[i]}\n"
                    f"Нажмите любую клавишу для продолжения")
        w.bind("<Key>", cont)


def cont(event):
    label.config(text=phrase[i])
    w.bind("<Key>",check)

phrase='quickbrownfox'
i=0
t=time.time()

w=Tk()
w.title("Клавиатурный тренажер")
w.geometry("800x150")

label=Label(text=phrase[i], font=("Geogia",25))
label.pack()
label.config(text=phrase[i])
w.bind("<Key>",check)

w.mainloop()