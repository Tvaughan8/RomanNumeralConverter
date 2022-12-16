#Roman Numeral Converter Pro by Thomas Vaughan

# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")


def cal_sum():
    t1 = int(a.get())
    x = type(t1)
    print(x)
    RomanNumerals.to_roman(t1)

def give_sum():
    t1 = a.get()
    x = type(t1)
    print(x)
    RomanNumerals.from_roman(t1)

def clear_sum():
    text.delete("1.0", "end")
    a.delete(0, END)

class RomanNumerals:

    def to_roman(val):  # This function adds the Roman numeral and subtracts the amount
        res = ''  # from the given value.
        while val >= 1000:
            res = res + 'M'
            val -= 1000
        while val >= 900:
            res = res + 'CM'
            val = val - 900
        while val >= 500:
            res = res + 'D'
            val = val - 500
        while val >= 400:
            res = res + 'CD'
            val = val - 400
        while val >= 100:
            res = res + 'C'
            val = val - 100
        while val >= 90:
            res = res + 'XC'
            val = val - 90
        while val >= 50:
            res = res + 'L'
            val = val - 50
        while val >= 40:
            res = res + 'XL'
            val = val - 40
        while val >= 10:
            res = res + 'X'
            val = val - 10
        while val >= 9:
            res = res + 'IX'
            val = val - 9
        while val >= 5:
            res = res + 'V'
            val = val - 5
        while val >= 4:
            res = res + 'IV'
            val = val - 4
        while val >= 3:
            res = res + 'III'
            val = val - 3
        while val >= 2:
            res = res + 'II'
            val = val - 2
        while val >= 1:
            res = res + 'I'
            val = val - 1
        while val == 1:
            res = res + 'I'
        text.insert(END, res)

    def from_roman(val):  # This function iterates through the given value backwards
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0  # and adds the value to the result.

        # Loop through the input string, starting from the last character
        for i in range(len(val) - 1, -1, -1):
            # Get the current character
            char = val[i]

            # If the current character has a lower value than the previous character,
            # subtract its value from the result
            if i > 0 and romans[char] < romans[val[i - 1]]:
                res -= romans[char]
            # Otherwise, add its value to the result
            else:
                res += romans[char]

        text.insert(END, res)



# Create an Entry widget
Label(win, text="--Roman Numeral Conveter Pro--", font=('Calibri 10')).pack()

#a.pack()
Label(win, text="Enter the Number or Roman Numeral to be converted.", font=('Calibri 10')).pack()
a = Entry(win, width=35)
a.pack()

label = Label(win, text="Result:", font=('Calibri 15'))
label.pack(pady=20)

# Create a text widget
text = Text(win, width=35, height=2, font=('Calibri 10'))
# text.insert(END, "")
text.pack()

Button(win, text="Convert to Roman", command= cal_sum).pack()
Button(win, text="Convert to Number", command= give_sum).pack()
Button(win, text="Clear", command= clear_sum).pack()

win.mainloop()
