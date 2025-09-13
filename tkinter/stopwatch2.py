import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # 表示ラベル
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 40))
        self.label.pack(pady=20)

        # スタートボタン
        self.start_button = tk.Button(root, text="Start", command=self.start, width=10)
        self.start_button.pack(side="left", padx=5)

        # ストップボタン
        self.stop_button = tk.Button(root, text="Stop", command=self.stop, width=10)
        self.stop_button.pack(side="left", padx=5)

        # リセットボタン
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, width=10)
        self.reset_button.pack(side="left", padx=5)

    def update(self):
        if self.running:
            current_time = time.time() - self.start_time + self.elapsed_time
            mins, secs = divmod(int(current_time), 60)
            hours, mins = divmod(mins, 60)
            self.label.config(text=f"{hours:02d}:{mins:02d}:{secs:02d}")
            self.root.after(1000, self.update)

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.update()

    def stop(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

# 実行部分
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stopwatch")
    stopwatch = Stopwatch(root)
    root.mainloop()
