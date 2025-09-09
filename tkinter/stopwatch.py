import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ストップウォッチ")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 40))
        self.label.pack(pady=20)

        button_frame = tk.Frame(root)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="スタート", command=self.start)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(button_frame, text="ストップ", command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(button_frame, text="リセット", command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=10)

        self.update_clock()

    def update_clock(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        formatted_time = self.format_time(self.elapsed_time)
        self.label.config(text=formatted_time)
        self.root.after(10, self.update_clock)  # 1/100秒ごとに更新

    def format_time(self, seconds):
        total_centiseconds = int(seconds * 100)
        mins, cs = divmod(total_centiseconds, 6000)
        secs, centis = divmod(cs, 100)
        return f"{mins:02}:{secs:02}.{centis:02}"

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()