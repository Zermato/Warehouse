import customtkinter as ctk


class MainMenuWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Главное меню")
        self._createUIEelements()

    def _createUIEelements(self):
        self.userRoleFrame = ctk.CTkFrame(self.master)
        self.userRoleFrame.grid(row=0, column=0, padx=10, pady=10)
        self.userRoleLabel = ctk.CTkLabel(self.userRoleFrame, text="Админ", font=("Helvetica", 30))
        self.userRoleLabel.pack(padx=10, pady=10)

        self.buttonFrame = ctk.CTkFrame(self.master)
        self.buttonStorage = ctk.CTkButton(self.buttonFrame, text="Склад", font=("Helvetica", 30))
        self.buttonParish = ctk.CTkButton(self.buttonFrame, text="Приход", font=("Helvetica", 30))
        self.buttonExpense = ctk.CTkButton(self.buttonFrame, text="Расход", font=("Helvetica", 30))
        self.buttonService = ctk.CTkButton(self.buttonFrame, text="Сервис", font=("Helvetica", 30))
        self.buttonFrame.grid(row=0, column=1, padx=10, pady=10)
        self.buttonStorage.grid(row=0, column=0, padx=10, pady=10)
        self.buttonParish.grid(row=0, column=1, padx=10, pady=10)
        self.buttonExpense.grid(row=0, column=2, padx=10, pady=10)
        self.buttonService.grid(row=0, column=3, padx=10, pady=10)

        self.exitFrame = ctk.CTkFrame(self.master)
        self.buttonExit = ctk.CTkButton(self.exitFrame, text="Выйти", font=("Helvetica", 30))
        self.exitFrame.grid(row=0, column=2, padx=10, pady=10)
        self.buttonExit.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = ctk.CTk()
    app = MainMenuWindow(root)
    root.mainloop()
