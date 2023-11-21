import tkinter as tk
from tkinter import font
from tkinter import ttk
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

        self.log_tree = ttk.Treeview(root, columns=("Column1", "Column2", "Column3"), show="headings")
        self.log_tree.heading("Column1", text="出目")
        self.log_tree.heading("Column2", text="基数")
        self.log_tree.heading("Column3", text="出目(10進表記)")
        self.log_tree.column("Column1", width=60, anchor="e")
        self.log_tree.column("Column2", width=30)
        self.log_tree.column("Column3", width=100, anchor="e")
        self.log_tree.grid(row=0, column=1, rowspan=3, padx=10)

        self.generate_button = tk.Button(root, text="ランダムな数字を出力", command=self.generate_random_number)
        self.generate_button.grid(row=0, column=0, pady=20)

        self.reset_button = tk.Button(root, text="出力結果をリセット", command=self.reset_log)
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
        with_base = self.add_base(base)
        self.number_label.config(text=f"表示された数字: {converted_number}")
        self.log_tree.insert("", tk.END, values=(converted_number, with_base, number))

        self.output_count += 1
        self.update_button_state()  # ボタンの状態を更新

    def reset_log(self):
        self.log_data_list.clear()
        self.output_count = 0
        self.number_label.config(text="")
        for item in self.log_tree.get_children():
            self.log_tree.delete(item)
        self.update_button_state()  # ボタンの状態を更新

    def convert_base(self, number, base):
        base = int(base)
        if base == 2:
            return f"{bin(number)[2:]}"
        elif base == 8:
            return f"{oct(number)[2:]}"
        elif base == 10:
            return f"{number}"
        elif base == 16:
            return f"{hex(number)[2:]}"
        
    def add_base(self, base):
        base = int(base)
        if base == 2:
            return "(2)"
        elif base == 8:
            return "(8)"
        elif base == 10:
            return "(10)"
        elif base == 16:
            return "(16)"

    def update_button_state(self):
        if self.output_count >= 75:
            self.generate_button.config(state=tk.DISABLED)
        else:
            self.generate_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = EngineerBingoApp(root)
    root.mainloop()
