import customtkinter as ctk
from tkinter import ttk

class YourApp1:
    def __init__(self, master):
        self.master = master
        self.master.title("Расход")
        self.master.geometry("1600x800")
        self._createUIEelements()

    def _createUIEelements(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(side="top", fill="x", pady=10, padx=10)
        self.label = ctk.CTkLabel(self.frame, text="Расход", font=("Helvetica", 30))
        self.label.pack(side="left", padx=10, pady=10)
        self.space = ctk.CTkLabel(self.frame, text=" " * 18, font=("Helvetica", 30))
        self.space.pack(side="left", padx=10, pady=10)
        self.buttonR = ctk.CTkButton(self.frame, text="Создать документ", font=("Helvetica", 30))
        self.buttonR.pack(side="left", padx=10, pady=10)
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
        self.tree = ttk.Treeview(self.new_frame, columns=("Num", "Cont", "Number", "Conter", "NumberTel", "Name"))
        self.tree.heading("Num", text="№ документа")
        self.tree.heading("Cont", text="Контрагент")
        self.tree.heading("Number", text="№ договора")
        self.tree.heading("Conter", text="Дата создания")
        self.tree.heading("NumberTel", text="Статус")
        self.tree.heading("Name", text="Комментарий")

        self.tree.column("#0", width=0, stretch=False)
        self.tree.column("Num", width=100)
        self.tree.column("Number", width=100)
        self.tree.column("Cont", width=100)
        self.tree.column("Conter", width=100)
        self.tree.column("NumberTel", width=100)
        self.tree.column("Name", width=150)
        self.tree_scroll = ttk.Scrollbar(self.new_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<Double-1>")

if __name__ == "__main__":
    root = ctk.CTk()
    app = YourApp1(root)
    root.mainloop()