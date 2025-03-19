from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("450x500")
        self.root.configure(bg="#2C3E50")

        self.expression = ""
        self.entry_text = StringVar()

        self.interface()

    def interface(self):
        entry_frame = Frame(self.root, bg="#34495E")
        entry_frame.pack(side=TOP, fill=BOTH)

        entry = Entry(entry_frame, font=("Arial", 24), textvariable=self.entry_text, fg="aqua", bg="#34495E", justify=RIGHT, bd=10, relief=RIDGE)
        entry.pack(fill=BOTH, ipadx=8, ipady=10, padx=10, pady=10)

        buttons_frame = Frame(self.root, bg="#2C3E50")
        buttons_frame.pack(fill=BOTH, expand=True)
        
        buttons = [('7', '8', '9', '/'),
                  ('4', '5', '6', '*'),
                  ('1', '2', '3', '-'),
                  ('C', '0', '=', '+')]

        for line in buttons:
            linha_frame = Frame(buttons_frame, bg="#2C3E50")
            linha_frame.pack(fill=BOTH, expand=True)
            for button in line:
                btn = Button(linha_frame, text=button, font=("Arial", 18, "bold"), bg="#ECF0F1", fg="#2C3E50", height=2, width=6, command=lambda b=button: self.on_click(b))
                btn.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

    def on_click(self, button):
        if button == "C":
           self.expression = ""
        elif button == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expressao = "Erro"
        else:
            self.expression += button
        self.entry_text.set(self.expression)

if __name__ == "__main__":
    root = Tk()
    Calculator(root)
    root.mainloop()