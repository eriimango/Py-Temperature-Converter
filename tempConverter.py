import tkinter as tk

#alogrithm to convert temp from f -> c
def fahrenheit_to_celsius():
#this function converts the value entered for fahrenheit to celsius and insert the result into lbl_result
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit)-32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

#set window
window = tk.Tk()
window.title("Temperature Converter")

#input field to enter fahrenheit reading
frm_entry = tk.Frame(master = window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

#arrow converter button
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command =fahrenheit_to_celsius, #sets command parameter
    bg="hot pink",
    fg="pink"
)

#result display converted Celsius
lbl_result = tk.Label(master=window, text= "\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10) #input forum
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()


