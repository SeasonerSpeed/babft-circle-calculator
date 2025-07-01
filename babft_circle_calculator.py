def main():
    global root, entry, rotation_var, result_label

    root = tk.Tk()
    root.title(f"BABFT Circle Calculator v{CURRENT_VERSION}")
    root.geometry("400x400")

    tk.Label(root, text="Diameter:").pack(pady=5)

    vcmd = (root.register(validate_number), '%P')
    entry = tk.Entry(root, validate='key', validatecommand=vcmd)
    entry.pack()

    tk.Label(root, text="Select Rotation:").pack(pady=5)
    rotation_var = tk.StringVar()
    rotation_dropdown = ttk.Combobox(root, textvariable=rotation_var)
    rotation_dropdown['values'] = ("5°", "10°", "15°", "30°")
    rotation_dropdown.current(2)
    rotation_dropdown.pack()

    tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    tk.Button(root, text="Copy (One Side)", command=copy_one_side).pack(pady=2)
    tk.Button(root, text="Copy (Both Sides)", command=copy_both_sides).pack(pady=2)

    # Watermark
    watermark = tk.Label(root, text="Made by SeasonerSpeed", font=("Arial", 8), fg="gray")
    watermark.pack(side="bottom", pady=5)

    check_for_updates()

    root.mainloop()
