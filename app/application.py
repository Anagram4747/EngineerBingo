import tkinter as tk
from random import randint, choice

class RandomNumberGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ランダム数字ジェネレータ")

        self.log = tk.Listbox(root, width=20, height=10)
        self.log.grid(row=0, column=1, rowspan=3, padx=10)

        self.generate_button = tk.Button(root, text="表示ボタン", command=self.generate_random_number)
        self.generate_button.grid(row=0, column=0, pady=10)

        self.reset_button = tk.Button(root, text="リセットボタン", command=self.reset_log)
        self.reset_button.grid(row=1, column=0, pady=10)

        self.number_label = tk.Label(root, text="")
        self.number_label.grid(row=2, column=0, pady=10)

        self.generated_numbers = set()

    def generate_random_number(self):
        base = choice(["2", "8", "10", "16"])
        number = randint(1, 75)
        self.generated_numbers.add(number)
        self.number_label.config(text=f"表示された数字: {self.convert_base(number, base)}")
        self.log.insert(tk.END, f"{number} ({self.convert_base(number, base)})")

    def reset_log(self):
        self.generated_numbers.clear()
        self.number_label.config(text="")
        self.log.delete(0, tk.END)

    def convert_base(self, number, base):
        base = int(base)
        if base == 2:
            return bin(number)[2:]
        elif base == 8:
            return oct(number)[2:]
        elif base == 10:
            return str(number)
        elif base == 16:
            return hex(number)[2:]

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGeneratorApp(root)
    root.mainloop()
