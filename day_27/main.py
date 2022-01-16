import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

input = tk.Entry()
input.config(width=20)
input.grid(column=1, row=0)


def button_clicked():
    miles = int(input.get())
    miles_to_km = miles * 1.60934
    result_label.config(text=miles_to_km)


miles_label = tk.Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=30, pady=0)

equality_label = tk.Label(text="is equal to", font=("Arial", 15, "normal"))
equality_label.grid(column=0, row=1)

result_label = tk.Label(text="0", font=("Arial", 15, "normal"))
result_label.grid(column=1, row=1)
result_label.config(padx=0, pady=20)

km_label = tk.Label(text="Km", font=("Arial", 15, "normal"))
km_label.grid(column=2, row=1)

calc_button = tk.Button(command=button_clicked)
calc_button.grid(column=1, row=2)
calc_button.config(text="Calculate", font=("Arial", 15), bg="gray")

window.mainloop()

# # Label
# label = tk.Label(text="I am a Label", font=("Arial", 30, "normal"))
# label.grid(column=0, row=0)
#
# # Modifying attributes of objects, any of the following methods
# label["text"] = "New text"
# label.config(text="Hello")
#
#
# # Button
# button = tk.Button(command=button_clicked)
# button.grid(column=2, row=0)
# button.config(text="Button", font=("Arial", 15), bg="gray")
#
#
# # Entry/Input
# input = tk.Entry()
# input.grid(column=3, row=2)
# input.config(width=30)
