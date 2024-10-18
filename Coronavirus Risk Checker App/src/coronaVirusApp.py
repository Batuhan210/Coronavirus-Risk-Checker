import tkinter as tk
from tkinter import messagebox

def check_symptoms_gui():
    fever_situation = float(entry_fever.get())
    cough = entry_cough.get().lower()
    headache = entry_headache.get().lower()
    sore_throat = entry_sore_throat.get().lower()
    difficulty_breathing = entry_difficulty_breathing.get().lower()
    day = int(entry_days.get())
    age = int(entry_age.get())
    health_condition = entry_health.get().lower()

    if fever_situation >= 39:
        if day >= 3:
            messagebox.showwarning("Warning", "Go to the hospital")
        else:
            messagebox.showwarning("Warning", "Your fever is at the limit; if it continues, please go to the hospital")

        if (fever_situation >= 39) and (cough == "y") and (headache == "y") and (day >= 3):
            messagebox.showerror("Emergency", "Go to the hospital immediately!\n You are at risk of coronavirus.")
        elif (cough == "y") or (headache == "y") or (sore_throat == "y") or (difficulty_breathing == "y") or (day >= 3):
            messagebox.showinfo("Info", "If it continues, please go to the hospital!")
        else:
            messagebox.showinfo("Info", "If your fever is above 39 degrees, go to the hospital immadiately!")

        if age >= 65 or health_condition == "y":
            messagebox.showinfo("Info", "You are at higher risk due to age or existing health conditions. Please consult a doctor.")


root = tk.Tk()
root.title("Coronavirus Risk Checker")

""" GUI Elements """
tk.Label(root, text="Fever (°C):").grid(row=0)
tk.Label(root, text="Cough (Y/N):").grid(row=1)
tk.Label(root, text="Headache (Y/N):").grid(row=2)
tk.Label(root, text="Sore Throat (Y/N):").grid(row=3)
tk.Label(root, text="Difficulty Breathing (Y/N):").grid(row=4)
tk.Label(root, text="Days with symptoms:").grid(row=5)
tk.Label(root, text="Age:").grid(row=6)
tk.Label(root, text="Existing Health Condition (Y/N):").grid(row=7)


entry_fever = tk.Entry(root)
entry_cough = tk.Entry(root)
entry_headache = tk.Entry(root)
entry_sore_throat = tk.Entry(root)
entry_difficulty_breathing = tk.Entry(root)
entry_days = tk.Entry(root)
entry_age = tk.Entry(root)
entry_health = tk.Entry(root)


entry_fever.grid(row = 0, column = 1)
entry_cough.grid(row = 1, column = 1)
entry_headache.grid(row = 2, column = 1)
entry_sore_throat.grid(row = 3, column = 1)
entry_difficulty_breathing.grid(row = 4, column = 1)
entry_days.grid(row = 5, column = 1)
entry_age.grid(row = 6, column = 1)
entry_health.grid(row = 7, column = 1)

tk.Button(root, text="Check", command = check_symptoms_gui).grid(row = 8, column = 1)

root.mainloop()