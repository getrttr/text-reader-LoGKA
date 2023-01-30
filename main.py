#Import modules
import tkinter as tk
from tkinter import ttk
from  tkinter import font, colorchooser, filedialog, messagebox
import os
import pyttsx3
import speech_recognition as sr
import random
import pyaudio

main_application=tk.Tk()
main_application.iconbitmap('icons2/icon.ico')
main_application.geometry('1200x800')
main_application.title("Текстовый Редактор \"LOgka\"")



main_menu= tk.Menu()
#Иконки
new_icon= tk.PhotoImage(file="icons2/new.png")
open_icon= tk.PhotoImage(file="icons2/open.png")
save_icon= tk.PhotoImage(file="icons2/save.png")
save_as_icon= tk.PhotoImage(file="icons2/save_as.png")
exit_icon= tk.PhotoImage(file="icons2/exit.png")

file=tk.Menu(main_menu, tearoff=False)

## Редактирование
# Редактирование иконок
copy_icon=tk.PhotoImage(file="icons2/copy.png")
paste_icon=tk.PhotoImage(file="icons2/paste.png")
cut_icon=tk.PhotoImage(file="icons2/cut.png")
clear_all_icon=tk.PhotoImage(file="icons2/clear_all.png")
find_icon=tk.PhotoImage(file="icons2/find.png")

edit=tk.Menu(main_menu, tearoff=False)

### Иконки
tool_bar_icon = tk.PhotoImage(file="icons2/tool_bar.png")
status_bar_icon= tk.PhotoImage(file="icons2/status_bar.png")


view=tk.Menu(main_menu, tearoff=False)

###### Цветовые  тема  ####
light_default_icon=tk.PhotoImage(file="icons2/light_default.png")
light_plus_icon=tk.PhotoImage(file="icons2/light_plus.png")
dark_icon=tk.PhotoImage(file="icons2/dark.png")
red_icon=tk.PhotoImage(file="icons2/red.png")
monokai_icon=tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon=tk.PhotoImage(file="icons2/night_blue.png")

color_theme=tk.Menu(main_menu, tearoff=False)

theme_choice= tk.StringVar()
color_icons = (light_default_icon,light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict={
    "Светлая": ("#000000", "#ffffff"),
    "Серая": ("#474747", "#e0e0e0"),
    "Темная": ("#c4c4c4", "#2d2d2d"),
    "Красная": ("#2d2d2d", "#ffe8e8"),
    "Кремовая": ("#d3b774", "#FFFDD0"),
    "Синяя": ("#ededed", "#6b9dc2")
}



### Кнопочки сверху
main_menu.add_cascade(label="Файл", menu=file)
main_menu.add_cascade(label="Редактировать", menu=edit)
main_menu.add_cascade(label="Просмотр", menu=view)
main_menu.add_cascade(label="Темы", menu=color_theme)



######################   тулбар  ############### ############################.

tool_bar= ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)


font_tuple= tk.font.families()
font_family= tk.StringVar()
font_box= ttk.Combobox(tool_bar, width=30, textvariable=font_family, state="readonly")
font_box["values"]= font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5)


# Размер окна
size_var=tk.IntVar()
font_size= ttk.Combobox(tool_bar, width=14, textvariable=size_var, state="readonly")
font_size["values"]= tuple(range(8,80,2))
font_size.current(3)  #12 is at index 4
font_size.grid(row=0, column=1, padx=5)

# Кнопки
bold_icon= tk.PhotoImage(file="icons2/bold.png")
bold_btn= ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# Кнопка курсива
italic_icon= tk.PhotoImage(file="icons2/italic.png")
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# кнопка подчеркивания
underline_icon= tk.PhotoImage(file="icons2/underline.png")
underline_btn= ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# кнопка перечеркивания
strikeout_icon= tk.PhotoImage(file="icons2/strike.png")
strikeout_btn = ttk.Button(tool_bar, image=strikeout_icon)
strikeout_btn.grid(row=0, column=5, padx=5)

# кнопка смены цвета
font_color_icon= tk.PhotoImage(file="icons2/font_color.png")
font_color_btn= ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=6, padx=5)

# выравнивание по левой стороне

align_left_icon= tk.PhotoImage(file="icons2/align_left.png")
align_left_btn= ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=7, padx=5)

# выравнивание по центру
align_center_icon= tk.PhotoImage(file="icons2/align_center.png")
align_center_btn= ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=8, padx=5)

#выравнивание по правой стороне
align_right_icon= tk.PhotoImage(file="icons2/align_right.png")
align_right_btn= ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=9, padx=5)

#Прочитать тескт
speak_icon = tk.PhotoImage(file="icons2/read.png")
speak_btn = ttk.Button(tool_bar, image=speak_icon, text="Прочитать", compound="left")
speak_btn.grid(row=0, column=10, padx=5)

#Преобразование  в слова
talk_icon = tk.PhotoImage(file="icons2/speech.png")
talk_btn = ttk.Button(tool_bar, image=talk_icon, text="Диктовка", compound="left")
talk_btn.grid(row=0, column=11, padx=5)


text_editor=tk.Text(main_application)
text_editor.config(wrap="word", relief=tk.FLAT)

scroll_bar= tk.Scrollbar(main_application)  # колесо прокруткии
text_editor.focus_set() # Позиция курсора
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill= tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

current_font_family= "Arial"
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family= font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_font_size(event=None):
    global current_font_size
    current_font_size= size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))
font_box.bind("<<ComboboxSelected>>", change_font)

font_size.bind("<<ComboboxSelected>>", change_font_size)



# курсив
def change_italic():
    text_property=tk.font.Font(font=text_editor["font"])  #dictionary
    if text_property.actual()["slant"] == "roman":
        text_editor.config(font=(current_font_family, current_font_size, "italic"))
    if text_property.actual()["slant"] == "italic":
        text_editor.config(font=(current_font_family, current_font_size, "normal"))

italic_btn.configure(command= change_italic)

def change_bold():
    text_property=tk.font.Font(font=text_editor["font"])  #dictionary
    if text_property.actual()["weight"] == "normal":
        text_editor.config(font=(current_font_family, current_font_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text_editor.config(font=(current_font_family, current_font_size, "normal"))

bold_btn.configure(command= change_bold)

# Подчеркивание
def change_underline():
    text_property=tk.font.Font(font=text_editor["font"])  #dictionary
    if text_property.actual()["underline"] == 0:
        text_editor.config(font=(current_font_family, current_font_size, "underline"))
    if text_property.actual()["underline"] == 1:
        text_editor.config(font=(current_font_family, current_font_size, "normal"))

underline_btn.configure(command= change_underline)

def change_strikeout():
    text_property=tk.font.Font(font=text_editor["font"])  #dictionary
    if text_property.actual()["overstrike"] == 0:
        text_editor.config(font=(current_font_family, current_font_size, "overstrike"))
    if text_property.actual()["overstrike"] == 1:
        text_editor.config(font=(current_font_family, current_font_size, "normal"))

strikeout_btn.configure(command= change_strikeout)


# Цветовые темы

def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)
### Выравнивание

### По левый край
def align_left():
    text_content= text_editor.get(1.0, "end")
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "left")

align_left_btn.configure(command=align_left)

### По центру
def align_center():
    text_content= text_editor.get(1.0, "end")
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "center")
align_center_btn.configure(command=align_center)

### По правому краю
def align_right():
    text_content= text_editor.get(1.0, "end")
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")
align_right_btn.configure(command=align_right)

### Читка текста
def read_text(**kwargs):
    if 'text' in kwargs:
        text = kwargs['text']
    else:
        text = text_editor.get(1.0, 'end')
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
speak_btn.configure(command=read_text)

### Форматиирование текста
def text_formatter(phrase):
    interrogatives = ('как', 'почему', 'что', 'когда', 'кто', 'где',  'вы', "кому", "чья")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return (f'{capitalized}?')
    else:
        return (f'{capitalized}.')

### Преобразование читки в текст
def take_speech():
    errors=[
        "Я не понимаю, что ты имеешь в виду!",
        "Прошу прощения?",
        "Не могли бы повторить",
        "Повторите это еще раз, пожалуйста!",
        "Извините, я этого не понял"
        ]
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source: # set listening device to microphone
        read_text(text = 'Скажи текст, через две секунды после этого сообщения говорите четко')
        r.pause_threshold = 2 # delay two second from program start before listening
        audio= r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU')
        query = text_formatter(query)
    except Exception:
        error = random.choice(errors)
        read_text(text = error)
        query = take_speech()
    text_editor.insert(tk.INSERT, query, tk.END)
    return query
talk_btn.configure(command=take_speech)

text_editor.configure(font=("Arial", 12))






######################   Строка состояния  ############### ############################

status_bar=ttk.Label(main_application, text= "Строки")
status_bar.pack(side=tk.BOTTOM)

text_changed = False

def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words=len(text_editor.get(1.0, "end-1c").split())
        characters = len(text_editor.get(1.0, "end-1c"))
        status_bar.config(text=f'Символов : {characters}  Слов : {words}')
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>", changed)




url = ""

def new_file(event= None):
    global url
    url=""
    text_editor.delete(1.0, tk.END)



## Команды по работе с файлом

file.add_command(label="Новый файл", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N", command = new_file)

#открыть файл
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Выберите файл", filetypes=(("Текстовый файл", "*.txt"),("Все файлы", "*.*")))
    try:
        with open(url, "r") as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

file.add_command(label="Открыть", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O", command=open_file)

# Сохранение
def save_file(event= None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, "w", encoding="utf-8") as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode="w",defaultextension =".txt" , filetypes=(("Текстовый файл", "*.txt"),("Все файлы", "*.*")))
            content2= text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return
file.add_command(label="Сохранить", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S", command = save_file)

# Сохранить как
def save_as(event= None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode="w",defaultextension =".txt" , filetypes=(("Текстовый файл", "*.txt"),("Все файлы", "*.*")))
        url.write(content)
        url.close()
    except:
        return
file.add_command(label="Сохранить как", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S", command= save_as)
def exit_func(event= None):
    global url, text_changed #line239
    try:
        if text_changed:
            mbox= messagebox.askyesnocancel(title="Вы не сохранили файл!", message="Хотите сохраниить?",)
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, "w", encoding= "utf-8") as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2= text_editor.get(1.0, tk.END)
                    url = filedialog.asksaveasfile(mode="w",defaultextension =".txt" , filetypes=(("Текстовый файл", "*.txt"),("Все файлы", "*.*")))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label="Выход", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q", command=exit_func)
##Команды редактирования
def find_func(event =None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', "1.0", tk.END)
        matches =0
        if word:
            start_pos = "1.0"
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos =f"{start_pos}+ {len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches +=1
                start_pos = end_pos
                text_editor.tag_config("match", foreground ="yellow", background= "green")
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content= text_editor.get(1.0, tk.END)

        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)






## команды редактирования текста

edit.add_command(label="Копировать", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C", command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Вставить", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V",command = lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Вырезать", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X", command = lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Очистить все", image=clear_all_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+X", command= lambda: text_editor.delete(1.0, tk.END))
edit.add_command(label="Поиск", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F", command= find_func)

## просмотр команд

# тулбар  и статусбар
show_statusbar =tk.BooleanVar()
show_statusbar.set(True)

show_toolbar =tk.BooleanVar()
show_toolbar.set(True)

# Скрыть тулбар
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar= False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill= tk.X)
        text_editor.pack(fill= tk.BOTH, expand= True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

# Скрыть тулбар
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side= tk.BOTTOM)
        show_statusbar = True




view.add_checkbutton(label="Панель инструментов",onvalue=True,offvalue=False,  variable = show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command= hide_toolbar)
view.add_checkbutton(label="Строка состояния",onvalue=True, offvalue=False,variable = show_statusbar, image=status_bar_icon, compound=tk.LEFT, command= hide_statusbar)

## ВЫбор темы цветовой
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple= color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background= bg_color, fg=fg_color)

count= 0
for i in color_dict:
    color_theme.add_radiobutton(label= i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command= change_theme)
    count+=1



main_application.config(menu=main_menu)

## Привязка сочетаний клавиш
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)

main_application.mainloop()
