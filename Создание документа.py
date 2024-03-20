import customtkinter as ctk

class YourApp1:
    def __init__(self, master):
        self.master = master
        self.master.title("Документ прихода")
        self.master.geometry("200x470")
        self.createuielements()

    def createuielements(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(pady=10, padx=10)
        self.label = ctk.CTkLabel(self.frame, text="Контрагент", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="№ договора", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="Статус", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.label = ctk.CTkLabel(self.frame, text="Комментарий", font=("Helvetica", 15))
        self.label.pack(padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.entry_field.pack(padx=10, pady=10)
        self.buttonE1 = ctk.CTkButton(self.frame, text="Сохранить", font=("Helvetica", 30))
        self.buttonE1.pack( padx=10, pady=10)


if __name__ == "__main__":
    root = ctk.CTk()
    app = YourApp1(root)
    root.mainloop()