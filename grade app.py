import tkinter as tk

def calculate_gpax():
    try:
        grades = [float(grade_entry.get()) for grade_entry in grade_entries]
        credits = [int(credit_entry.get()) for credit_entry in credit_entries]

        if len(grades) != len(credits):
            result_label.config(text="จำนวนเกรดและหน่วยกิตไม่ตรงกัน")
        else:
            total_credits = sum(credits)
            weighted_grades = sum(grade * credit for grade, credit in zip(grades, credits))
            gpax = weighted_grades / total_credits
            result_label.config(text=f"GPAX คือ {gpax:.2f}")
    except ValueError:
        result_label.config(text="โปรดป้อนข้อมูลที่ถูกต้อง")

# สร้างหน้าต่าง GUI
window = tk.Tk()
window.title("คำนวณ GPAX")

# สร้างส่วนกรอกข้อมูล
grade_labels = [tk.Label(window, text=f"เกรด {i + 1}:") for i in range(5)]
credit_labels = [tk.Label(window, text=f"หน่วยกิต {i + 1}:") for i in range(5)]
grade_entries = [tk.Entry(window) for _ in range(5)]
credit_entries = [tk.Entry(window) for _ in range(5)]

for i in range(5):
    grade_labels[i].grid(row=i, column=0)
    grade_entries[i].grid(row=i, column=1)
    credit_labels[i].grid(row=i, column=2)
    credit_entries[i].grid(row=i, column=3)

# สร้างปุ่มคำนวณ
calculate_button = tk.Button(window, text="คำนวณ GPAX", command=calculate_gpax)
calculate_button.grid(row=5, column=1)

# ผลลัพธ์
result_label = tk.Label(window, text="")
result_label.grid(row=6, column=1)

window.mainloop()