from Tkinter import *


class Calculator:

    calc_value = 0.0

    plus_operacija = False
    minus_operacija = False

    def gumb_press(self, vrednost):

        vpisana_vrednost = self.stevilka_vpis.get()
        vpisana_vrednost += vrednost
        self.stevilka_vpis.delete(0, "end")
        self.stevilka_vpis.insert(0, vpisana_vrednost)

    def preveri_float(self, str_vrednost):
        try:
            float(str_vrednost)
            return True
        except ValueError:
            return False

    def math_gumb_press(self, vrednost):
        if self.preveri_float(str(self.stevilka_vpis.get())):

            self.plus_operacija = False
            self.minus_operacija = False

            self.calc_value = float(self.vpis_vrednost.get())

            if vrednost == "+":
                self.plus_operacija = True
            elif vrednost == "-":
                self.minus_operacija = True

            self.stevilka_vpis.delete(0, "end")

    def enako_gumb_press(self, operacija):
        if self.plus_operacija or self.minus_operacija:
            if self.plus_operacija:
                operacija = self.calc_value + float(self.vpis_vrednost.get())
            elif self.minus_operacija:
                operacija = self.calc_value - float(self.vpis_vrednost.get())

            self.stevilka_vpis.delete(0, "end")
            self.stevilka_vpis.insert(0, operacija)

    def __init__(self, root):

        self.vpis_vrednost = StringVar(root, value="")

        root.title('Calculator by BojPav')

        root.resizable(width=False, height=False)

        root.geometry('{}x{}'.format(260, 250))

        self.stevilka_vpis = Entry(root,font="Serif 18", textvariable=self.vpis_vrednost, width=20)

        self.stevilka_vpis.grid(row=0, columnspan=4)

        self.gumb_ena = Button(root, text="1", width=10, command=lambda: self.gumb_press('1')).grid(row=1, column=0)
        self.gumb_dva = Button(root, text="2", width=10, command=lambda: self.gumb_press('2')).grid(row=1, column=1)
        self.gumb_tri = Button(root, text="3", width=10, command=lambda: self.gumb_press('3')).grid(row=1, column=2)
        self.gumb_stiri = Button(root, text="4", width=10, command=lambda: self.gumb_press('4')).grid(row=2, column=0)
        self.gumb_pet = Button(root, text="5", width=10, command=lambda: self.gumb_press('5')).grid(row=2, column=1)
        self.gumb_sest = Button(root, text="6", width=10, command=lambda: self.gumb_press('6')).grid(row=2, column=2)
        self.gumb_sedem = Button(root, text="7", width=10, command=lambda: self.gumb_press('7')).grid(row=3, column=0)
        self.gumb_osem = Button(root, text="8", width=10, command=lambda: self.gumb_press('8')).grid(row=3, column=1)
        self.gumb_devet = Button(root, text="9", width=10, command=lambda: self.gumb_press('9')).grid(row=3, column=2)
        self.gumb_nula = Button(root, text="0", width=10, command=lambda: self.gumb_press('0')).grid(row=4, column=1)

        self.gumb_plus = Button(root, text="+", width=10, command=lambda: self.math_gumb_press('+')).grid(row=5, column=0)
        self.gumb_minus = Button(root, text="-", width=10, command=lambda: self.math_gumb_press('-')).grid(row=5, column=1)
        self.gumb_enako = Button(root, text="=", width=10, command=lambda: self.enako_gumb_press('=')).grid(row=5, column=2)


root = Tk()

calc = Calculator(root)

root.mainloop()