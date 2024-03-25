class Context:
    def __init__(self, window, data):
        self._window = window
        self._data = data

    def clear(self):
        for widget in self._window.winfo_children():
            widget.destroy()
        self._window = None
