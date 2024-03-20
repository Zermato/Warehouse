import customtkinter as ctk

class YourApp1:
    def __init__(self, master):
        self.master = master
        self.master.title("Документ прихода")
        self.master.geometry("200x750")
        self.createuielements()

    def createuielements(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(pady=10, padx=10)
        self.label = ctk.CTkLabel(self.frame, text="Контрагент", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="Номер телефона", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="Наименование груза", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="Описание груза", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="Тип тары", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.label = ctk.CTkComboBox(self.frame, values=["Контейнер", "Палет", "Ящик"], font=("Helvetica", 15), width=200)
        self.label.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="Количество единиц", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="Цена", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.buttonE1 = ctk.CTkButton(self.frame, text="Сохранить", font=("Helvetica", 30))
        self.buttonE1.pack( padx=10, pady=10)


if __name__ == "__main__":
    root = ctk.CTk()
    app = YourApp1(root)
    root.mainloop()