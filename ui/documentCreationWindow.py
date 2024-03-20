import customtkinter as ctk


class DocumentCreationWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Документ прихода")
        self.master.geometry("200x470")
        self._createuielements()

    def _createuielements(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(pady=10, padx=10)
        ctk.CTkLabel(self.frame, text="Контрагент", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.counterpartyEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.counterpartyEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="№ договора", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.docNumberEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.docNumberEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="Статус", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.statusEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.statusEntry.pack(padx=10, pady=10)
        ctk.CTkLabel(self.frame, text="Комментарий", font=("Helvetica", 15)).pack(padx=10, pady=10)
        self.commentEntry = ctk.CTkEntry(self.frame, font=("Helvetica", 15), width=200)
        self.commentEntry.pack(padx=10, pady=10)
        self.buttonSave = ctk.CTkButton(self.frame, text="Сохранить", font=("Helvetica", 30))
        self.buttonSave.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = ctk.CTk()
    app = DocumentCreationWindow(root)
    root.mainloop()
