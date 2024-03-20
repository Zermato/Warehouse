import customtkinter as ctk
from PIL import Image, ImageTk


class AuthorizationWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Авторизация")
        self.master.geometry("400x220")
        self._createUIEelements()

    def _createUIEelements(self):
        frameImage = ctk.CTkFrame(self.master)
        frameImage.pack(side="left", padx=10, pady=10)
        image = Image.open("../content/images/1.png")
        image = image.resize((200, 200))
        img = ImageTk.PhotoImage(image)
        labelImage = ctk.CTkLabel(frameImage, image=img)
        labelImage.image = img
        labelImage.pack(pady=1, padx=1)

        ctk.CTkLabel(self.master, text="Авторизация", font=("Helvetica", 20)).pack(pady=10)
        self.entryLogin = ctk.CTkEntry(self.master, placeholder_text="Логин", font=("Helvetica", 12))
        self.entryPassword = ctk.CTkEntry(self.master, placeholder_text="Пароль", font=("Helvetica", 12))
        self.button = ctk.CTkButton(self.master, text="Войти", font=("Helvetica", 16), command=self._login)

        self.button_exit = ctk.CTkButton(self.master, text="Выход", font=("Helvetica", 12), width=15, height=15)
        self.button_exit.pack(side="bottom", anchor="se", padx=1, pady=1)

        self.entryLogin.pack(pady=5)
        self.entryPassword.pack(pady=5)
        self.button.pack(pady=10)

        self.entryPassword.bind("<Enter>", self.show_password)
        self.entryPassword.bind("<Leave>", self.hide_password)

    def show_password(self, event):
        self.entryPassword.configure(show='')

    def hide_password(self, event):
        self.entryPassword.configure(show='-')

    def _login(self):
        loginData = self.entryLogin.get()
        passwordData = self.entryPassword.get()


if __name__ == "__main__":
    root = ctk.CTk()
    app = AuthorizationWindow(root)
    root.mainloop()
