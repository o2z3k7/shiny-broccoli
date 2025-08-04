import tkinter as tk  # tkinterをインポート
# ウィンドウの作成
root = tk.Tk()
root.title("ボタン付きウィンドウ")
root.geometry("400x1000")
# ボタンを押したときの処理
def on_button_click():
   print("ボタンが押されました！")
# ボタンを作成してウィンドウに配置
button = tk.Button(root, text="クリックしてね", command=on_button_click)
button.pack(pady=20)  # 上下に余白をもって中央に配置
# ウィンドウを表示
root.mainloop()