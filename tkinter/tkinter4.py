import tkinter as tk
import winsound  # Windowsで音を鳴らすための標準モジュール
# メインウィンドウの作成
root = tk.Tk()
root.title("メインウィンドウ")
root.geometry("300x200")
# サブウィンドウを表示＆音を鳴らす関数
def open_subwindow():
   winsound.MessageBeep()  # ピッという音を鳴らす（Windows専用）
   sub = tk.Toplevel(root)
   sub.title("サブウィンドウ")
   sub.geometry("200x100")
   label = tk.Label(sub, text="こんにちは！")
   label.pack(pady=10)
# ボタンの作成と配置
button = tk.Button(root, text="別ウィンドウを開く", command=open_subwindow)
button_width = 120
button_height = 30
root.update_idletasks()
button.place(x=300 - button_width - 10, y=200 - button_height - 10)
# メインループ
root.mainloop()