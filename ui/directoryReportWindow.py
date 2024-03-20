import customtkinter as ctk
class YourApp:
    def __init__(self, master,):
        self.master = master
        self.master.title("Справочники")
        self.master.geometry("1980x1080")
        self.reference_list = []
        self.createuielements()
    def createuielements(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(side="top",  pady=10, padx=10)
        self.buttonE = ctk.CTkButton(self.frame, text="назад", font=("Helvetica", 30), command=self.master.destroy)
        self.buttonE.pack(side="right", padx=10, pady=10)
        self.buttonS = ctk.CTkButton(self.frame, text="Создать справочник", font=("Helvetica", 30), command=self.create_reference_window)
        self.buttonS.pack(side="right", padx=10, pady=10)
        self.new_frame = ctk.CTkFrame(self.master)
        self.new_frame.pack(side="top", fill="both", expand=True, pady=0, padx=10)
    def create_reference_window(self):
        reference_window = ctk.CTk()
        reference_window.title("Создание справочника")
        label_price = ctk.CTkLabel(reference_window, text="Наименование:")
        label_price.pack()
        entry_price = ctk.CTkEntry(reference_window)
        entry_price.pack()
        button_save = ctk.CTkButton(reference_window, text="Сохранить", command=lambda: self.save_reference(entry_price.get(), reference_window))
        button_save.pack(side="right", padx=10, pady=10)
        reference_window.mainloop()
    def save_reference(self, name, reference_window):
        new_reference = {"Наименование": name}
        self.reference_list.insert(0, new_reference)
        self.update_reference_frame()
        reference_window.destroy()
    def show_reference(self, reference):

        selected_name = reference['Наименование']
        print(f"Выбран справочник: {reference['Наименование']}")
        self.create_reference_info_window(selected_name)
    def create_reference_info_window(self, reference_name):
        reference_window = ctk.CTk()
        reference_app = ReferenceWindow(reference_window, reference_name)
        reference_window.mainloop()
    def update_reference_frame(self):
        for widget in self.new_frame.winfo_children():
            widget.destroy()
        row, col = 0, 0
        for reference in self.reference_list:
            button = ctk.CTkButton(self.new_frame, text=reference['Наименование'],
                                   command=lambda ref=reference: self.show_reference(ref))
            button.grid(row=row, column=col, padx=10, pady=10, sticky="w")
            row += 1
            if row * 50 > self.new_frame.winfo_height():
                row = 0
                col += 1
        self.new_frame.update_idletasks()
class ReferenceWindow:
    def __init__(self, master, reference_name):
        self.master = master
        self.master.title(reference_name)
        self.master.geometry("400x200")
        label_info = ctk.CTkLabel(self.master, text=f"Информация о справочнике: {reference_name}")
        label_info.pack(pady=20)
        button_close = ctk.CTkButton(self.master, text="Закрыть", command=self.master.destroy)
        button_close.pack()

if __name__ == "__main__":
    root = ctk.CTk()
    app = YourApp(root)
    root.mainloop()
