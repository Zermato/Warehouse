import customtkinter as ctk

class YourApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Главное меню")
        self.__createuielements()

    def __createuielements(self):

        self.frame_left_top = ctk.CTkFrame(self.master)
        self.frame_left_top.grid(row=0, column=0, padx=10, pady=10)

        self.label = ctk.CTkLabel(self.frame_left_top, text="Админ", font=("Helvetica", 25))
        self.label.pack(padx=10, pady=10)


        self.frame_middle = ctk.CTkFrame(self.master)
        self.frame_middle.grid(row=0, column=1, padx=10, pady=10)

        # Создаем кнопки внутри фрейма
        self.buttonS = ctk.CTkButton(self.frame_middle, text="Справочники", font=("Helvetica", 25))
        self.buttonS.grid(row=0, column=0, padx=10, pady=10)
        self.buttonD = ctk.CTkButton(self.frame_middle, text="Документы", font=("Helvetica", 25))
        self.buttonD.grid(row=0, column=1, padx=10, pady=10)
        self.buttonR = ctk.CTkButton(self.frame_middle, text="Отчеты", font=("Helvetica", 25))
        self.buttonR.grid(row=0, column=2, padx=10, pady=10)
        self.buttonS = ctk.CTkButton(self.frame_middle, text="Сервис", font=("Helvetica", 25))
        self.buttonS.grid(row=0, column=3, padx=10, pady=10)


        # Создаем фрейм для кнопки "Выйти" и размещаем его в верхнем правом углу
        self.frame_exit = ctk.CTkFrame(self.master)
        self.frame_exit.grid(row=0, column=2, padx=10, pady=10)

        self.buttonE = ctk.CTkButton(self.frame_exit, text="Выйти", font=("Helvetica", 25))
        self.buttonE.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = ctk.CTk()
    app = YourApp(root)
    root.mainloop()
