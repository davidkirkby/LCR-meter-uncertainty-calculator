import tkinter as tk


font_size = 12  # Adjust the font size as needed
font = ("Arial", font_size)
standard_text = ("Arial", 12)

window = tk.Tk()
window.title("LCR meter uncertainty calculator")
window.configure(bg="#ffffff")
window.geometry("900x700")  # Set the initial window size


# Create a top frame for the program name in large text
top_frame = tk.Frame(window, bg="#fefefe")
top_frame.grid(row=0, column=0, sticky="nsew")
text_label = tk.Label(top_frame, text="LCR meter uncertainty calculator", bg="#ffffff", fg="red", font=standard_text)
text_label.grid(row=1, column=0, sticky=tk.W)
# Configure the font size for all menu items



# Create a bottom frmame
bottom_frame = tk.Frame(window, bg="#fefefe")
bottom_frame.grid(row=10, column=0, sticky="nsew")




meter_label = tk.Label(bottom_frame, text="LCR meter", bg="white", font=standard_text)
meter_label.grid(row=0, column=0, sticky=tk.W)
meter_var = tk.StringVar(value="HP/Agilent 4284A (20 Hz to 1 MHz. 0.05% basic accuracy)")  # Default value
meter = ["HP/Agilent 4284A (20 Hz to 1 MHz. 0.05% basic accuracy)","HP/Agilent 4285A (75 kHz to 30 MHz. 0.1% basic accuracy)"]
for i, choice in enumerate(meter):
    radio_button = tk.Radiobutton(bottom_frame, text=choice, variable=meter_var, value=choice, bg="white",font=standard_text)
    radio_button.grid(row= i, column=1, sticky=tk.W)

cable_length_label = tk.Label(bottom_frame, text="Cable length", bg="white", font=standard_text)
cable_length_label.grid(row=10, column=0, sticky=tk.W)
cable_length_var = tk.StringVar(value="0 m (fixture directly on meter terminals)")  # Default value
cable_length_ = ["0 m (fixture directly on meter terminals)","1 m", "2 m", "4 m (only on 4284A with option 006)"]
for i, choice in enumerate(cable_length_):
    radio_button = tk.Radiobutton(bottom_frame, text=choice, variable=cable_length_var, value=choice, bg="white",font=standard_text)
    radio_button.grid(row=10 + i, column=1, sticky=tk.W)

cable_length_label = tk.Label(bottom_frame, text="Cable length", bg="white", font=standard_text)
cable_length_label.grid(row=10, column=0, sticky=tk.W)
cable_length_var = tk.StringVar(value="0 m (fixture directly on meter terminals)")  # Default value
cable_length_ = ["0 m (fixture directly on meter terminals)","1 m", "2 m", "4 m (only on 4284A with option 006)"]
for i, choice in enumerate(cable_length_):
    radio_button = tk.Radiobutton(bottom_frame, text=choice, variable=cable_length_var, value=choice, bg="white",font=standard_text)
    radio_button.grid(row=10 + i, column=1, sticky=tk.W)

window.mainloop()