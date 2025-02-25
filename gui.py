import tkinter as tk
from tkinter import messagebox

def calculate_land_tax(land_value, land_type):
    """
    ฟังก์ชันคำนวณภาษีที่ดินตามประเภทของที่ดิน
    """
    tax_rate = 0

    if land_type == 1:  # ที่ดินเพื่อการเกษตรกรรม
        if land_value <= 750000:
            tax_rate = 0
        elif land_value <= 50000000:
            tax_rate = 0.001
        elif land_value <= 100000000:
            tax_rate = 0.002
        else:
            tax_rate = 0.03

    elif land_type == 2:  # ที่ดินเพื่อการอยู่อาศัย
        if land_value <= 10000000:
            tax_rate = 0.002
        elif land_value <= 50000000:
            tax_rate = 0.003
        elif land_value <= 100000000:
            tax_rate = 0.005
        else:
            tax_rate = 0.01

    elif land_type == 3:  # ที่ดินเพื่อพาณิชยกรรม
        if land_value <= 50000000:
            tax_rate = 0.003
        elif land_value <= 100000000:
            tax_rate = 0.005
        else:
            tax_rate = 0.01

    elif land_type == 4:  # ที่ดินรกร้างว่างเปล่า
        if land_value <= 50000000:
            tax_rate = 0.005
        elif land_value <= 100000000:
            tax_rate = 0.01
        else:
            tax_rate = 0.015
    else:
        return "ประเภทที่ดินไม่ถูกต้อง กรุณาเลือก 1-4"

    return land_value * tax_rate

def calculate():
    try:
        land_value = float(entry_value.get())
        land_type = land_type_var.get()

        if land_type == 0:
            messagebox.showwarning("⚠️ ข้อผิดพลาด", "กรุณาเลือกประเภทที่ดิน")
            return

        tax = calculate_land_tax(land_value, land_type)

        if isinstance(tax, str):
            result_label.config(text=tax, fg="red")
        else:
            result_label.config(text=f"💵 ภาษีที่ต้องชำระคือ: {tax:,.2f} บาท", fg="green")
            status_bar.config(text="✅ คำนวณสำเร็จ")

    except ValueError:
        messagebox.showerror("❌ ข้อผิดพลาด", "กรุณากรอกมูลค่าที่ดินเป็นตัวเลข")
        status_bar.config(text="⚠️ เกิดข้อผิดพลาดในการคำนวณ")

def on_enter(event):
    event.widget.config(bg="#5F9EA0", fg="white")

def on_leave(event):
    event.widget.config(bg="#00bfff", fg="white")

def exit_program():
    if messagebox.askokcancel("ออก", "คุณต้องการปิดโปรแกรมหรือไม่?"):
        root.destroy()

# --- GUI ---
root = tk.Tk()
root.title("💰 เครื่องคำนวณภาษีที่ดิน")
root.geometry("500x600")
root.config(bg="#f0f8ff")

# --- ส่วนหัวโปรแกรม ---
header = tk.Label(root, text="💰 เครื่องคำนวณภาษีที่ดิน", font=("TH Sarabun New", 26, "bold"), bg="#4682B4", fg="white", pady=15)
header.pack(fill="x")

# --- กรอบข้อมูลหลัก ---
main_frame = tk.Frame(root, bg="#e6f2ff", padx=20, pady=20, highlightbackground="#87CEFA", highlightthickness=2)
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# มูลค่าที่ดิน
tk.Label(main_frame, text="💵 กรอกมูลค่าที่ดิน (บาท):", font=("TH Sarabun New", 16), bg="#e6f2ff").pack(pady=5)
entry_value = tk.Entry(main_frame, font=("TH Sarabun New", 16), width=20, justify='center')
entry_value.pack()

# ประเภทที่ดิน
tk.Label(main_frame, text="🏡 เลือกประเภทที่ดิน:", font=("TH Sarabun New", 16), bg="#e6f2ff").pack(pady=10)
land_type_var = tk.IntVar()

types = [
    ("1️⃣ ที่ดินเพื่อการเกษตรกรรม", 1),
    ("2️⃣ ที่ดินเพื่อการอยู่อาศัย", 2),
    ("3️⃣ ที่ดินเพื่อพาณิชยกรรม", 3),
    ("4️⃣ ที่ดินรกร้างว่างเปล่า", 4)
]

for text, value in types:
    tk.Radiobutton(main_frame, text=text, variable=land_type_var, value=value, font=("TH Sarabun New", 14),
                   bg="#e6f2ff", activebackground="#B0E0E6").pack(anchor='w')

# ปุ่มคำนวณภาษี
calculate_btn = tk.Button(main_frame, text="📊 คำนวณภาษี", command=calculate, font=("TH Sarabun New", 16), bg="#00bfff", fg="white", width=15)
calculate_btn.pack(pady=15)
calculate_btn.bind("<Enter>", on_enter)
calculate_btn.bind("<Leave>", on_leave)

# แสดงผลลัพธ์
result_label = tk.Label(main_frame, text="", font=("TH Sarabun New", 18, "bold"), bg="#e6f2ff")
result_label.pack(pady=10)

# ปุ่มออก
exit_btn = tk.Button(root, text="❌ ออก", command=exit_program, font=("TH Sarabun New", 14), bg="#ff6347", fg="white", width=10)
exit_btn.pack(pady=10)
exit_btn.bind("<Enter>", lambda e: exit_btn.config(bg="#CD5C5C"))
exit_btn.bind("<Leave>", lambda e: exit_btn.config(bg="#ff6347"))

# แถบสถานะ (Status Bar)
status_bar = tk.Label(root, text="💡 พร้อมใช้งาน", bd=1, relief="sunken", anchor="w", bg="#dcdcdc", font=("TH Sarabun New", 12))
status_bar.pack(side="bottom", fill="x")

root.mainloop()