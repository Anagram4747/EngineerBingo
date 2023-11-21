import tkinter as tk
from random import choice

class LogData:
    def __init__(self, id, isSelected, base):
        self.id = id
        self.isSelected = isSelected
        self.base = base

class RandomNumberGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ランダム数字ジェネレータ")

        self.log_data_list = []

        self.log = tk.Listbox(root, width=30, height=10)
        self.log.grid(row=0, column=1, rowspan=3, padx=10)

        self.generate_button = tk.Button(root, text="表示ボタン", command=self.generate_random_number)
        self.generate_button.grid(row=0, column=0, pady=10)

        self.reset_button = tk.Button(root, text="リセットボタン", command=self.reset_log)
        self.reset_button.grid(row=1, column=0, pady=10)

        self.number_label = tk.Label(root, text="")
        self.number_label.grid(row=2, column=0, pady=10)

    def generate_random_number(self):
        available_numbers = [data for data in range(1, 76) if not any(log.id == data and log.isSelected for log in self.log_data_list)]
        
        if not available_numbers:
            self.number_label.config(text="すべての数字が表示されました")
            return

        number = choice(available_numbers)
        base = choice(["2", "8", "10", "16"])

        log_data = LogData(id=number, isSelected=False, base=base)
        self.log_data_list.append(log_data)

        converted_number = self.convert_base(number, base)
        self.number_label.config(text=f"表示された数字: {converted_number}")
        self.log.insert(tk.END, f"{converted_number} (ID: {number}, Base: {base})")

    def reset_log(self):
        self.log_data_list.clear()
        self.number_label.config(text="")
        self.log.delete(0, tk.END)

    def convert_base(self, number, base):
        base = int(base)
        if base == 2:
            return f"{bin(number)[2:]}(2)"
        elif base == 8:
            return f"{oct(number)[2:]}(8)"
        elif base == 10:
            return f"{number}(10)"
        elif base == 16:
            return f"{hex(number)[2:]}(16)"

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGeneratorApp(root)
    root.mainloop()
