import tkinter as tk
from random import choice

class LogData:
    def __init__(self, id, isSelected, base):
        self.id = id
        self.isSelected = isSelected
        self.base = base

class EngineerBingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("エンジニアビンゴ")

        self.log_data_list = []
        self.output_count = 0  # 出力回数のカウント

        self.log = tk.Listbox(root, width=20, height=20)  # 幅を調整
        self.log.grid(row=0, column=1, rowspan=3, padx=10)

        self.generate_button = tk.Button(root, text="表示ボタン", command=self.generate_random_number)
        self.generate_button.grid(row=0, column=0, pady=20)

        self.reset_button = tk.Button(root, text="リセットボタン", command=self.reset_log)
        self.reset_button.grid(row=1, column=0, pady=20)

        self.number_label = tk.Label(root, text="")
        self.number_label.grid(row=2, column=0, pady=20)

        self.update_button_state()  # ボタンの状態を更新

    def generate_random_number(self):
        if self.output_count >= 75:
            self.number_label.config(text="75回出力しました。")
            return

        available_numbers = [data for data in range(1, 76) if not any(log.id == data and log.isSelected for log in self.log_data_list)]
        
        if not available_numbers:
            self.number_label.config(text="すべての数字が表示されました")
            return

        number = choice(available_numbers)
        base = choice(["2", "8", "10", "16"])

        log_data = LogData(id=number, isSelected=False, base=base)
        self.log_data_list.append(log_data)

        converted_number = self.convert_base(number, base)
        log_entry = f"{converted_number.rjust(7)} (ID: {number}, Base: {base})"
        self.number_label.config(text=f"表示された数字: {converted_number}")
        self.log.insert(tk.END, log_entry)

        self.output_count += 1
        self.update_button_state()  # ボタンの状態を更新

    def reset_log(self):
        self.log_data_list.clear()
        self.output_count = 0
        self.number_label.config(text="")
        self.log.delete(0, tk.END)
        self.update_button_state()  # ボタンの状態を更新

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

    def update_button_state(self):
        if self.output_count >= 75:
            self.generate_button.config(state=tk.DISABLED)
        else:
            self.generate_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = EngineerBingoApp(root)
    root.mainloop()
