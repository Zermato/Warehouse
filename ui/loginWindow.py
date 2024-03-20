import customtkinter as ctk
from PIL import Image, ImageTk  # Необходимо установить библиотеку Pillow: pip install Pillow


class YourApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Авторизация")
        self.master.geometry("400x220")
        self.__createuielements()

    def __createuielements(self):
        # Создаем фрейм для лейбла и изображения
        frame_left = ctk.CTkFrame(self.master)
        frame_left.pack(side="left", padx=10, pady=10)

        # Загружаем изображение
        image = Image.open("../qss/images/1.png")  # Замените "resize.png" на путь к вашему изображению
        image = image.resize((200, 200))  # Размер изображения
        img = ImageTk.PhotoImage(image)

        # Создаем лейбл с изображением
        label_image = ctk.CTkLabel(frame_left, image=img)
        label_image.image = img
        label_image.pack(pady=1, padx=1)

        # Создаем кнопки
        self.label = ctk.CTkLabel(self.master, text="Авторизация", font=("Helvetica", 20))
        self.entry_login = ctk.CTkEntry(self.master, placeholder_text="Логин", font=("Helvetica", 12))
        self.entry_password = ctk.CTkEntry(self.master, placeholder_text="Пароль", font=("Helvetica", 12))
        self.button = ctk.CTkButton(self.master, text="Войти", font=("Helvetica", 16), command=self._login)

        self.button_exit = ctk.CTkButton(self.master, text="Выход", font=("Helvetica", 12), width=15, height=15)
        self.button_exit.pack(side="bottom", anchor="se", padx=1, pady=1)

        self.label.pack(pady=10)
        self.entry_login.pack(pady=5)
        self.entry_password.pack(pady=5)
        self.button.pack(pady=10)

        self.entry_password.bind("<Enter>", self.show_password)
        self.entry_password.bind("<Leave>", self.hide_password)

    def show_password(self, event):
        self.entry_password.configure(show='')

    def hide_password(self, event):
        self.entry_password.configure(show='-')

    def _login(self):
        login = self.entry_login.get()
        password = self.entry_password.get()


if __name__ == "__main__":
    root = ctk.CTk()
    app = YourApp(root)
    root.mainloop()
