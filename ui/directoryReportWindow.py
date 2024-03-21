import customtkinter as ctk

# очистить окно
class DirectoryReportWindow:
    def __init__(self, master,):
        self.master = master
        self.master.title("Справочники")
        self.master.geometry("1980x1080")
        self.referenceList = []
        self._createUIEelements()

    def _createUIEelements(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(side="top",  pady=10, padx=10)
        self.buttonBack = ctk.CTkButton(self.frame, text="назад", font=("Helvetica", 30), command=self.master.destroy)
        self.buttonBack.pack(side="right", padx=10, pady=10)
        self.buttonCreateDoc = ctk.CTkButton(self.frame, text="Создать справочник", font=("Helvetica", 30), command=self.createReferenceWindow)
        self.buttonCreateDoc.pack(side="right", padx=10, pady=10)
        self.frameItems = ctk.CTkFrame(self.master)
        self.frameItems.pack(side="top", fill="both", expand=True, pady=0, padx=10)

    def createReferenceWindow(self):
        referenceWindow = ctk.CTk()
        referenceWindow.title("Создание справочника")
        ctk.CTkLabel(referenceWindow, text="Наименование:").pack()
        priceEntry = ctk.CTkEntry(referenceWindow)
        priceEntry.pack()
        buttonSave = ctk.CTkButton(referenceWindow, text="Сохранить", command=lambda: self.saveReference(priceEntry.get(), referenceWindow))
        buttonSave.pack(side="right", padx=10, pady=10)
        referenceWindow.mainloop()

    def saveReference(self, name, reference_window):
        new_reference = {"Наименование": name}
        self.referenceList.insert(0, new_reference)
        self.updateReferenceFrame()
        reference_window.destroy()

    def showReference(self, reference):
        selectedName = reference['Наименование']
        self.createReferenceInfoWindow(selectedName)

    def createReferenceInfoWindow(self, referenceName):
        referenceWindow = ctk.CTk()
        referenceApp = ReferenceWindow(referenceWindow, referenceName)
        referenceWindow.mainloop()

    def updateReferenceFrame(self):
        for widget in self.frameItems.winfo_children():
            widget.destroy()
        row, col = 0, 0
        for reference in self.referenceList:
            button = ctk.CTkButton(self.frameItems, text=reference['Наименование'], command=lambda ref=reference: self.showReference(ref))
            button.grid(row=row, column=col, padx=10, pady=10, sticky="w")
            row += 1
            if row * 50 > self.frameItems.winfo_height():
                row = 0
                col += 1
        self.frameItems.update_idletasks()


class ReferenceWindow:
    def __init__(self, master, reference_name):
        self.master = master
        self.master.title(reference_name)
        self.master.geometry("400x200")
        ctk.CTkLabel(self.master, text=f"Информация о справочнике: {reference_name}").pack(pady=20)
        buttonExit = ctk.CTkButton(self.master, text="Закрыть", command=self.master.destroy)
        buttonExit.pack()


if __name__ == "__main__":
    root = ctk.CTk()
    app = DirectoryReportWindow(root)
    root.mainloop()
