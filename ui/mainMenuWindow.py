import customtkinter as ctk


class YourApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Главное меню")
        self.createuielements()

    def createuielements(self):

        # Создаем фрейм для label
        self.framelefttop = ctk.CTkFrame(self.master)
        self.framelefttop.grid(row=0, column=0, padx=10, pady=10)

        self.label = ctk.CTkLabel(self.framelefttop, text="Админ", font=("Helvetica", 30))
        self.label.pack(padx=10, pady=10)

        # Создаем фрейм для кнопки
        self.frame_middle = ctk.CTkFrame(self.master)
        self.frame_middle.grid(row=0, column=1, padx=10, pady=10)

        self.buttonS = ctk.CTkButton(self.frame_middle, text="Склад", font=("Helvetica", 30))
        self.buttonS.grid(row=0, column=0, padx=10, pady=10)
        self.buttonD = ctk.CTkButton(self.frame_middle, text="Приход", font=("Helvetica", 30))
        self.buttonD.grid(row=0, column=1, padx=10, pady=10)
        self.buttonR = ctk.CTkButton(self.frame_middle, text="Расход", font=("Helvetica", 30))
        self.buttonR.grid(row=0, column=2, padx=10, pady=10)
        self.buttonS = ctk.CTkButton(self.frame_middle, text="Сервис", font=("Helvetica", 30))
        self.buttonS.grid(row=0, column=3, padx=10, pady=10)

        # Создаем фрейм для кнопки "Выйти"
        self.frame_exit = ctk.CTkFrame(self.master)
        self.frame_exit.grid(row=0, column=2, padx=10, pady=10)

        self.buttonE = ctk.CTkButton(self.frame_exit, text="Выйти", font=("Helvetica", 30))
        self.buttonE.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = ctk.CTk()
    app = YourApp(root)
    root.mainloop()