import tkinter as tk


def update_cable_length_options(*args):
    selected_meter = meter_var.get()

    if selected_meter == "HP/Agilent 4285A (75 kHz to 30 MHz. 0.1% basic accuracy)":
        cable_length_radio_buttons[3].config(state="disabled")  # Disable "4 m" option
    else:
        cable_length_radio_buttons[3].config(state="normal")  # Enable "4 m" option


# Configure the font size for all items
font_size = 12  # Adjust the font size as needed
font = ("Arial", font_size)
standard_text = ("Arial", 12)
large_text = ("Arial", 14, "bold")

window = tk.Tk()
window.title("LCR meter uncertainty calculator")
window.configure(bg="#ffffff")
window.geometry("900x700")  # Set the initial window size

# Create a top frame for the program name in large text
top_frame = tk.Frame(window, bg="#fefefe")
top_frame.grid(row=0, column=0, sticky="e")
text_label = tk.Label(top_frame, text="LCR meter uncertainty calculator", bg="#ffffff", fg="red", font=large_text)
text_label.grid(row=1, column=0, sticky=tk.W)

# Create a bottom frame
bottom_frame = tk.Frame(window, bg="#fefefe")
bottom_frame.grid(row=10, column=0, sticky="nsew")

# Create the first set of radio buttons and labels for "Meter"
meter_label = tk.Label(bottom_frame, text="LCR meter", bg="white", font=large_text)
meter_label.grid(row=0, column=0, sticky=tk.W)
meter_var = tk.StringVar(value="HP/Agilent 4284A (20 Hz to 1 MHz. 0.05% basic accuracy)")  # Default value
meter = ["HP/Agilent 4284A (20 Hz to 1 MHz. 0.05% basic accuracy)", "HP/Agilent 4285A (75 kHz to 30 MHz. 0.1% basic accuracy)"]
for i, choice in enumerate(meter):
    radio_button = tk.Radiobutton(bottom_frame, text=choice, variable=meter_var, value=choice, bg="white", font=standard_text)
    radio_button.grid(row=i, column=1, sticky=tk.W)

# Create the first gap
gap_label1 = tk.Label(bottom_frame, text="", bg="white")
gap_label1.grid(row=len(meter), column=0)

# Create the second set of radio buttons and labels for "Cable length"
cable_length_label = tk.Label(bottom_frame, text="Cable length", bg="white", font=large_text)
cable_length_label.grid(row=len(meter) + 1, column=0, sticky=tk.W)
cable_length_var = tk.StringVar(value="0 m (fixture directly on meter terminals)")  # Default value
cable_length = ["0 m (fixture directly on meter terminals)","1 m", "2 m", "4 m (only on 4284A with option 006)"]


cable_length_radio_buttons = []
for i, choice in enumerate(cable_length):
    radio_button = tk.Radiobutton(bottom_frame, text=choice, variable=cable_length_var, value=choice, bg="white", font=("Arial", 12))
    radio_button.grid(row=len(meter) + 1 + i, column=1, sticky=tk.W)
    cable_length_radio_buttons.append(radio_button)

# Create the second gap
gap_label2 = tk.Label(bottom_frame, text="", bg="white")
gap_label2.grid(row=len(meter) + len(cable_length) + 1, column=0)

# Create the third set of radio buttons and labels for "Temperature"
temperature_label = tk.Label(bottom_frame, text="Temperature", bg="white", font=large_text)
temperature_label.grid(row=len(meter) + len(cable_length) + 2, column=0, sticky=tk.W)
temperature_var = tk.StringVar(value="18-28 °C")  # Default value
temperature = ["0-8 °C","8-18 °C","18-28 °C","28-38 °C","38-48 °C","48-55 °C"]
for i, choice in enumerate(temperature):
    radio_button = tk.Radiobutton(bottom_frame, text=choice, variable=temperature_var, value=choice, bg="white",font=standard_text)
    radio_button.grid(row=len(meter) + len(cable_length) + 2 + i, column=1, sticky=tk.W)

# Create the third gap
gap_label3 = tk.Label(bottom_frame, text="", bg="white")
gap_label3.grid(row=len(meter) + len(cable_length) + len(temperature) + 2, column=0)

# Create the fourth set of radio buttons and labels for "Oscillator level"
oscillator_label = tk.Label(bottom_frame, text="Oscillator level", bg="white", font=large_text)
oscillator_label.grid(row=len(meter) + len(cable_length) + len(temperature) + 3, column=0, sticky=tk.W)
oscillator_var = tk.StringVar(value="≤ 1 Vrms")  # Default value
oscillator_levels = ["≤ 1 Vrms", "> 1 Vrms"]
for i, choice in enumerate(oscillator_levels):
    radio_button = tk.Radiobutton(bottom_frame, text=choice, variable=oscillator_var, value=choice, bg="white", font=standard_text)
    radio_button.grid(row=len(meter) + len(cable_length) + len(temperature) + 3 + i, column=1, sticky=tk.W)

# Add a trace to the meter_var StringVar to update cable length options visibility
meter_var.trace("w", update_cable_length_options)

window.mainloop()


