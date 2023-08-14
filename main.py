import tkinter
from PIL import ImageTk, Image
from tkinter import messagebox


window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=380, height=380)
window.config(padx=30, pady=30)

#image part
my_image = Image.open("img.png")
resize_my_image = my_image.resize((90, 90))
my_new_image = ImageTk.PhotoImage(resize_my_image)
my_label = tkinter.Label(window, image=my_new_image)
my_label.pack()

#weight part
weight_label = tkinter.Label(text="Enter Your Weight (kg)")
weight_label.config(font=("Arial", 10, "bold"))
weight_label.pack()

weight_entry = tkinter.Entry()
weight_entry.config(width=15)
weight_entry.pack()

#height part
height_label = tkinter.Label(text="Enter Your Height (cm)")
height_label.config(font=("Arial", 10, "bold"))
height_label.pack()

height_entry = tkinter.Entry()
height_entry.config(width=15)
height_entry.pack()


def user_information():
    try:
        if len(weight_entry.get()) == 0 or len(height_entry.get()) == 0:
            messagebox.showinfo(title="Missing Info", message="Enter all info.")

        elif float(weight_entry.get()) < 0 or float(height_entry.get()) < 0:
            messagebox.showerror(title="ERROR!", message="Weight or height values cannot be negative.")

        elif float(weight_entry.get()) > 250 or float(height_entry.get()) > 250:
            messagebox.showerror(title="ERROR!", message="Enter real values.")

        else:
            user_weight = float(weight_entry.get())
            user_height = float(height_entry.get())
            bmi = (user_weight / (user_height * user_height)) * 10000

            if bmi <= 18.5:
                result_print = "\nYour BMI is: %3.1f.\nYou are underweight." % (bmi)

            elif (bmi > 18.5) and (bmi < 25):
                result_print = "\nYour BMI is: %3.1f.\nYou are normal." % (bmi)

            elif (bmi >= 25) and (bmi < 30):
                result_print = "\nYour BMI is: %3.1f.\nYou are overweight." % (bmi)

            elif (bmi >= 30) and (bmi < 35):
                result_print = "\nYour BMI is: %3.1f.\nYou are Obese (class 1)." % (bmi)

            elif (bmi >= 35) and (bmi < 40):
                result_print = "\nYour BMI is: %3.1f.\nYou are Obese (class 2)." % (bmi)

            elif bmi >= 40:
                result_print = "\nYour BMI is: %3.1f.\n\nYou are obese (class 3)." % (bmi)

            else:
                result_print = "\nYou are not in BMI interval for diagnosis"


            result = tkinter.Label(text=result_print, font=("Arial", 11, "bold"))
            result.config(padx=10, pady=10)
            result.pack()

    except:
        messagebox.showerror(title="ERROR", message="Enter valid numbers.")



calculate_button = tkinter.Button(text="Calculate", command=user_information)
calculate_button.pack()

window.mainloop()