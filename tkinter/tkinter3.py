import tkinter as tk  # tkinterをインポート

# メインウィンドウの作成

root = tk.Tk()

root.title("メインウィンドウ")

root.geometry("300x200")


# サブウィンドウを表示する関数

def open_subwindow():
    sub = tk.Toplevel(root)  # 新しいウィンドウ（親は root）

    sub.title("サブウィンドウ")

    sub.geometry("200x100")

    # サブウィンドウ内にもラベルを配置

    label = tk.Label(sub, text="こんにちは！")

    label.pack(pady=50)


# ボタンの作成と配置

button = tk.Button(root, text="別ウィンドウを開く", command=open_subwindow)

button.pack(pady=60)

# ウィンドウを表示

root.mainloop()
