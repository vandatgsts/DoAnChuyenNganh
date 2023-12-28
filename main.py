
import tkinter as tk
from tkinter import ttk, messagebox

from tkinterdnd2 import DND_FILES, TkinterDnD

import model
import run_model  # Đây là script 'run.py' đã cập nhật

# Thiết lập màu sắc và phông chữ
BG_COLOR = "#f5f5f5"
FRAME_COLOR = "#e1e1e1"
BUTTON_COLOR = "#4e8fcb"
TEXT_COLOR = "#ffffff"
FONT = ("Arial", 12)
FONT_BOLD = ("Arial", 12, "bold")

file_path = None  # Lưu đường dẫn file được kéo vào


def on_drop(event):
    global file_path
    file_path = event.data
    label_file_drag_drop.config(text=f"Đã chọn: {file_path}")
    label_file_path.config(text=f"Đường dẫn file: {file_path}")


def run_model_script():
    # Nếu file_path là null, sử dụng file mặc định
    path = file_path if file_path else 'data\\dataset.csv'
    newmodel = model.Model(path)
    newmodel.create_model()
    messagebox.showinfo("Notice", "The model is created with" + path)


def forecast():
    try:
        # Lấy mô hình
        model_runner = run_model.RunModel()
        model_runner.load_model()

        # Lấy dữ liệu nhập từ người dùng
        X1 = float(entry_num1.get())
        X2 = float(entry_num2.get())
        X3 = float(entry_num3.get())

        # Thực hiện dự đoán
        total = model_runner.predict([X1, X2, X3])
        label_tong.config(text=f"Result: {total[0]} m^3/s")  # Điều chỉnh để hiển thị giá trị dự đoán

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


# Tạo cửa sổ chính với TkinterDnD
window = TkinterDnD.Tk()
window.title("Proposed Hydroelectric Applications")
window.configure(bg=BG_COLOR)

# Đường dẫn đến hình ảnh biểu tượng kéo và thả
icon_path = 'img.png'  # Thay đổi 'img.png' thành đường dẫn thực tế của hình ảnh bạn muốn sử dụng

# Tạo khung để kéo và thả file
frame_drag_drop = ttk.Frame(window, width=150, height=150, relief=tk.RAISED, borderwidth=2)
frame_drag_drop.pack(pady=20, expand=True)
frame_drag_drop.pack_propagate(False)

# Tạo label bên trong khung để hiển thị đường dẫn file
icon_image = tk.PhotoImage(file=icon_path)
icon_image = icon_image.subsample(6, 6)  # giảm kích thước hình ảnh
label_file_drag_drop = ttk.Label(frame_drag_drop, image=icon_image, relief=tk.SUNKEN, anchor='center')
label_file_drag_drop.image = icon_image
label_file_drag_drop.pack(expand=True, fill='both')

label_file_drag_drop.drop_target_register(DND_FILES)
label_file_drag_drop.dnd_bind('<<Drop>>', on_drop)

# Tạo một label để hiển thị đường dẫn file
label_file_path = ttk.Label(window, text="", font=FONT)
label_file_path.pack(pady=10)

run_button = tk.Button(window, text="Create Model", command=run_model_script)
run_button.pack(pady=10)

# Tạo một khung cho các ô nhập liệu
entries_frame = ttk.Frame(window)
entries_frame.pack(pady=10)

# Tạo các ô nhập liệu và nhãn tương ứng
entry_num1 = tk.Entry(entries_frame, font=FONT, width=10)
entry_num2 = tk.Entry(entries_frame, font=FONT, width=10)
entry_num3 = tk.Entry(entries_frame, font=FONT, width=10)

for i, entry in enumerate([entry_num1, entry_num2, entry_num3], start=1):
    text = ""
    if i == 1:
        text = "Upstream water level: "
    elif i == 2:
        text = "Downstream water level: "
    else:
        text = "Inflow rate"
    ttk.Label(entries_frame, text=text, font=FONT_BOLD).pack(side=tk.LEFT)
    entry.pack(side=tk.LEFT, padx=5)

# Nút để tính tổng
button_tinh_tong = tk.Button(window, text="Forecast", command=forecast, bg=BUTTON_COLOR, fg=TEXT_COLOR,
                             font=FONT_BOLD)
button_tinh_tong.pack(pady=10)

# Label để hiển thị tổng
label_tong = ttk.Label(window, text="Predicted outflow", font=FONT)
label_tong.pack(pady=10)

# Chạy vòng lặp chính của giao diện
window.mainloop()
