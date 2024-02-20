import customtkinter as ctk
import tkinter as tk

ctk.set_default_color_theme("dark-blue")

def move_window(event):
    x, y = event.x_root - x_offset, event.y_root - y_offset
    app.geometry(f"+{x}+{y}")

def start_move(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def exit_app():
    app.destroy()

app = ctk.CTk()
app.overrideredirect(True)
app.attributes('-topmost', True)
app.geometry("1240x70")

# Создание фрейма для метки
label_frame = ctk.CTkFrame(app)
label_frame.grid(row=0, column=0, padx=10, pady=10)

# Создание метки
label = ctk.CTkLabel(label_frame, text="Артём Габитов", font=("Helvetica", 24))
label.pack(padx=10, pady=10)

# Создание фрейма для кнопок
button_frame = ctk.CTkFrame(app)
button_frame.grid(row=0, column=1, padx=10, pady=10)

# Кнопки
button1 = ctk.CTkButton(button_frame, text="Справочники", width=150, font=("Helvetica", 24))
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = ctk.CTkButton(button_frame, text="Документы", width=150, font=("Helvetica", 24))
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = ctk.CTkButton(button_frame, text="Отчеты", width=150, font=("Helvetica", 24))
button3.grid(row=0, column=2, padx=10, pady=10)

button4 = ctk.CTkButton(button_frame, text="Сервис", width=150, font=("Helvetica", 24))
button4.grid(row=0, column=3, padx=10, pady=10)

# Кнопка "Выход"
exit_button = ctk.CTkButton(button_frame, text="Выход", width=150, font=("Helvetica", 24), command=exit_app)
exit_button.grid(row=0, column=4, padx=10, pady=10)

# Создание отдельного фрейма для переключателя
switch_frame = ctk.CTkFrame(app)
switch_frame.grid(row=0, column=2, padx=10, pady=10)

# Переключатель
switch = ctk.CTkSwitch(switch_frame, text="Light|Dark", font=("Helvetica", 20), command=lambda: ctk.set_appearance_mode("dark" if switch.get() == 1 else "light"))
switch.pack(padx=0, pady=15, anchor=tk.E)

app.bind('<Button-1>', start_move)
app.bind('<B1-Motion>', move_window)

app.mainloop()
