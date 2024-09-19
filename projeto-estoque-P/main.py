import tkinter as tk
from controller.controller import EstoqueController

def main():
    root = tk.Tk()
    app = EstoqueController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
