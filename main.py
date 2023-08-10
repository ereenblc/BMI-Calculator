import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)

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

# calculate button part
def user_information():

    try:
        user_weight = float(weight_entry.get())
        user_height = float(height_entry.get())

        bmi = ((user_weight) / (user_height * user_height)) * 10000

        if user_weight < 0 or user_height < 0:
            result_print = "You cannot have negative values."

        elif user_height > 250 or user_weight > 300:
            result_print = "Please enter real values!."

        elif bmi <= 18.5:
            result_print = "Your BMI is: %3.1f.\tYou are underweight." % (bmi)

        elif (bmi > 18.5) and (bmi <= 24.9):
            result_print = "Your BMI is: %3.1f.\tYou are normal." % (bmi)

        elif (bmi >= 25) and (bmi <= 30):
            result_print = "Your BMI is: %3.1f.\tYou are overweight." % (bmi)

        elif (bmi >= 30) and (bmi <= 34.9):
            result_print = "Your BMI is: %3.1f.\tYou are Obese (class 1)." % (bmi)

        elif (bmi >= 35) and (bmi <= 39.9):
            result_print = "Your BMI is: %3.1f.\tYou are Obese (class 2)." % (bmi)

        elif bmi >= 40:
            result_print = "Your BMI is: %3.1f.\tYou are obese (class 3)." % (bmi)

        else:
            result_print = "You are not in BMI interval for diagnosis"

    except:
        result_print = "Enter valid numbers!"

    result = tkinter.Label(text=result_print, font=("Arial", 11, "bold"))
    result.config(padx=10, pady=10)
    result.pack()

calculate_button = tkinter.Button(text="Calculate", command=user_information)
calculate_button.pack()




window.mainloop()