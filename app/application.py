import tkinter as tk
from random import randint

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
        number = randint(1, 75)
        self.generated_numbers.add(number)
        self.number_label.config(text=f"表示された数字: {number}")
        self.log.insert(tk.END, number)

    def reset_log(self):
        self.generated_numbers.clear()
        self.number_label.config(text="")
        self.log.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGeneratorApp(root)
    root.mainloop()
