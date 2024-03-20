import customtkinter as ctk
from tkinter import ttk

class YourApp1:
    def __init__(self, master):
        self.master = master
        self.master.title("Склад")
        self.master.geometry("1600x800")
        self.reference_list = []
        self.createuielements()

    def createuielements(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(side="top", fill="x", pady=10, padx=10)
        self.label = ctk.CTkLabel(self.frame, text="Склад", font=("Helvetica", 30))
        self.label.pack(side="left", padx=10, pady=10)
        self.space = ctk.CTkLabel(self.frame, text=" " * 35, font=("Helvetica", 30))
        self.space.pack(side="left", padx=10, pady=10)
        self.buttonR = ctk.CTkButton(self.frame, text="Найти", font=("Helvetica", 30))
        self.buttonR.pack(side="left", padx=10, pady=10)
        self.buttonE = ctk.CTkButton(self.frame, text="Назад", font=("Helvetica", 30), command=self.master.destroy)
        self.buttonE.pack(side="right", padx=10, pady=10)
        self.entry_field = ctk.CTkEntry(self.frame, font=("Helvetica", 25), width=200)
        self.entry_field.pack(side="left", padx=10, pady=10)
        self.buttonC = ctk.CTkButton(self.frame, text="Очистить", font=("Helvetica", 30))
        self.buttonC.pack(side="left", padx=10, pady=10)
        self.buttonR = ctk.CTkButton(self.frame, text="Удалить", font=("Helvetica", 30))
        self.buttonR.pack(side="left", padx=10, pady=10)
        self.new_frame = ctk.CTkFrame(self.master)
        self.new_frame.pack(side="top", fill="both", expand=True, pady=10, padx=10)
        self.create_table()

    def create_table(self):
        self.tree = ttk.Treeview(self.new_frame, columns=("Number", "Conter","NumberTel", "Name", "Description", "Tar","Colvo", "Price", "Creation Date", "Modification Date"))
        self.tree.heading("Number", text="Номер")
        self.tree.heading("Conter", text="Контрагент")
        self.tree.heading("NumberTel", text="Номер телефона")
        self.tree.heading("Name", text="Наименование груза")
        self.tree.heading("Description", text="Описание груза")
        self.tree.heading("Tar", text="Тип тары")
        self.tree.heading("Colvo", text="Количество единиц")
        self.tree.heading("Price", text="Цена")
        self.tree.heading("Creation Date", text="Дата Создания")
        self.tree.heading("Modification Date", text="Дата Изменения")
        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("Number", width=100)
        self.tree.column("Conter", width=100)
        self.tree.column("NumberTel", width=100)
        self.tree.column("Name", width=150)
        self.tree.column("Description", width=150)
        self.tree.column("Tar", width=100)
        self.tree.column("Colvo", width=100)
        self.tree.column("Price", width=100)
        self.tree.column("Creation Date", width=150)
        self.tree.column("Modification Date", width=150)
        self.tree_scroll = ttk.Scrollbar(self.new_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<Double-1>")

if __name__ == "__main__":
    root = ctk.CTk()
    app = YourApp1(root)
    root.mainloop()