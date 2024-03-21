from tkinter import ttk
import customtkinter as ctk

from consts import Constants


class ExpenseDocumentWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Документ расход")
        self.master.geometry("1600x800")
        self._createUIEelements()

    def _createUIEelements(self):
        self.buttonFrame = ctk.CTkFrame(self.master)
        self.buttonFrame.pack(side="top", fill="x", pady=10, padx=10)
        ctk.CTkLabel(self.buttonFrame, text="Документ расход", font=("Helvetica", 30)).pack(side="left", padx=10, pady=10)
        ctk.CTkLabel(self.buttonFrame, text=" " * 12, font=("Helvetica", 30)).pack(side="left", padx=10, pady=10)
        self.buttonCreateItem = ctk.CTkButton(self.buttonFrame, text="Добавить товар", font=("Helvetica", 30))
        self.buttonCreateItem.pack(side="left", padx=10, pady=10)
        self.buttonSearch = ctk.CTkButton(self.buttonFrame, text="Найти", font=("Helvetica", 30))
        self.buttonSearch.pack(side="left", padx=10, pady=10)
        self.buttonBack = ctk.CTkButton(self.buttonFrame, text="Назад", font=("Helvetica", 30),command=self.master.destroy)
        self.buttonBack.pack(side="right", padx=10, pady=10)
        self.searchEntry = ctk.CTkEntry(self.buttonFrame, font=("Helvetica", 25), width=200)
        self.searchEntry.pack(side="left", padx=10, pady=10)
        self.buttonClear = ctk.CTkButton(self.buttonFrame, text="Очистить", font=("Helvetica", 30))
        self.buttonClear.pack(side="left", padx=10, pady=10)
        self.buttonRemove = ctk.CTkButton(self.buttonFrame, text="Удалить", font=("Helvetica", 30))
        self.buttonRemove.pack(side="left", padx=10, pady=10)
        self.tableFrame = ctk.CTkFrame(self.master)
        self.tableFrame.pack(side="top", fill="both", expand=True, pady=10, padx=10)
        self.create_table()

    def create_table(self):
        self.tree = ttk.Treeview(self.tableFrame, columns=("Number", "Conter", "NumberTel", "Name", "Description", "Type", "Quantity", "Price", "Creation Date", "Modification Date", "numberHoursInStock"))
        print(Constants.EXPENSE_DOCUMENT_WINDOW_TREE_OPTIONS)
        for header, option in Constants.EXPENSE_DOCUMENT_WINDOW_TREE_OPTIONS.items():
            self.tree.heading(header, text=option["text"])
            self.tree.column(header, width=option["size"])
        self.tree.column("#0", width=0, stretch=False)

        self.tree_scroll = ttk.Scrollbar(self.tableFrame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree_scroll.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)
        self.tree.bind("<Double-1>")


if __name__ == "__main__":
    root = ctk.CTk()
    app = ExpenseDocumentWindow(root)
    root.mainloop()