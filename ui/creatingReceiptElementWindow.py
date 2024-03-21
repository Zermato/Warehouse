import customtkinter as ctk


class CreatingReceiptElementWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Документ прихода")
        self.master.geometry("200x750")
        self._createUIEelements()

    def _createUIEelements(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(pady=10, padx=10)
        ctk.CTkLabel(self.frame, text="Контрагент", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.contrEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.contrEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="Номер телефона", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.numberTelEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.numberTelEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="Наименование груза", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.nameEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.nameEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="Описание груза", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.descriptionEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.descriptionEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="Тип тары", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.typeEntry = ctk.CTkComboBox(self.frame, values=["Контейнер", "Палет", "Ящик"], font=("Helvetica", 15), width=200)
        self.typeEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="Количество единиц", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.numberEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.numberEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="Цена", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.costEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.costEntry.pack(padx=10, pady=10)
        self.buttonSave = ctk.CTkButton(self.frame, text="Сохранить", font=("Helvetica", 30))
        self.buttonSave.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = ctk.CTk()
    app = CreatingReceiptElementWindow(root)
    root.mainloop()
