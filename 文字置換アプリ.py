import tkinter as tk
from tkinter import scrolledtext

class TextShifterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("文字列置換アプリ")
        self.create_widgets()

    def create_widgets(self):
        # A - 元のコード
        tk.Label(self.root, text="元のコード").grid(row=0, column=0, padx=5, pady=5)
        self.text_box_a = scrolledtext.ScrolledText(self.root, width=60, height=10)
        self.text_box_a.grid(row=0, column=1, padx=5, pady=5)

        # B - 置換する箇所
        tk.Label(self.root, text="置換する箇所").grid(row=1, column=0, padx=5, pady=5)
        self.text_box_b = tk.Entry(self.root, width=60)
        self.text_box_b.grid(row=1, column=1, padx=5, pady=5)

        # C - 文字位置
        tk.Label(self.root, text="指定する文字の番目").grid(row=2, column=0, padx=5, pady=5)
        self.entry_c = tk.Entry(self.root, width=10)
        self.entry_c.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # D - 進める回数
        tk.Label(self.root, text="進める回数").grid(row=3, column=0, padx=5, pady=5)
        self.entry_d = tk.Entry(self.root, width=10)
        self.entry_d.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        self.entry_d.insert(0, "1")

        # E - 出力結果
        tk.Label(self.root, text="出力結果").grid(row=4, column=0, padx=5, pady=5)
        self.text_box_e = scrolledtext.ScrolledText(self.root, width=60, height=10)
        self.text_box_e.grid(row=4, column=1, padx=5, pady=5)

        # 出力ボタン
        tk.Button(self.root, text="出力", command=self.process_text).grid(row=5, column=1, padx=5, pady=5, sticky='e')
        # コピー
        tk.Button(self.root, text="コピー", command=self.copy_to_clipboard).grid(row=5, column=1, padx=5, pady=5, sticky='w')

    def increment_character(self, char, steps):
        if char.isdigit():
            return str((int(char) + steps) % 10)
        elif char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            return chr((ord(char) - base + steps) % 26 + base)
        return char

    def process_text(self):
        text_a = self.text_box_a.get("1.0", tk.END).strip()
        text_b = self.text_box_b.get().strip()
        index_c = int(self.entry_c.get())
        steps_d = int(self.entry_d.get())

        if index_c <= len(text_b):
            char_to_replace = text_b[index_c - 1]
            new_char = self.increment_character(char_to_replace, steps_d)
            new_text = text_b[:index_c - 1] + new_char + text_b[index_c:]
            result = text_a.replace(text_b, new_text)

            self.text_box_e.delete("1.0", tk.END)
            self.text_box_e.insert(tk.END, result)

            self.entry_d.delete(0, tk.END)
            self.entry_d.insert(0, str(steps_d + 1))

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_box_e.get("1.0", tk.END).strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = TextShifterApp(root)
    root.mainloop()

