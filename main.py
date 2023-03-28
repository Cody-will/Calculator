import customtkinter as ctk
import funco

class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.appearance = ctk.set_appearance_mode('dark')
        self.height = 250
        self.width = 300
        self.geometry(f'{self.width}x{self.height}')
        self.padx = 5
        self.pady = 5
        self.resultsText = ctk.StringVar()
        self.x = None
        self.y = None
        self.modulo = ''

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.results = ctk.CTkEntry(self, state='disabled', textvariable=self.resultsText)
        self.results.grid(row=0, column=0, columnspan=4, padx=self.padx, pady=(20, 0), sticky='nsew')

        self.clear = ctk.CTkButton(self, text='Clear', command=self.clear)
        self.clear.grid(row=1, column=0, padx=self.padx, pady=self.pady)

        self.delete = ctk.CTkButton(self, text='Del', command=self.delete)
        self.delete.grid(row=1, column=1, padx=self.padx, pady=self.pady)

        self.percent = ctk.CTkButton(self, text='%', command=lambda: self.mod('%'))
        self.percent.grid(row=1, column=2, padx=self.padx, pady=self.pady)

        self.divide = ctk.CTkButton(self, text='/', command=lambda: self.mod('/'))
        self.divide.grid(row=1, column=3, padx=self.padx, pady=self.pady)

        self.seven = ctk.CTkButton(self, text='7', command=lambda: self.update_results('7'))
        self.seven.grid(row=2, column=0, padx=self.padx, pady=self.pady)

        self.eight = ctk.CTkButton(self, text='8', command=lambda: self.update_results('8'))
        self.eight.grid(row=2, column=1, padx=self.padx, pady=self.pady)

        self.nine = ctk.CTkButton(self, text='9', command=lambda: self.update_results('9'))
        self.nine.grid(row=2, column=2, padx=self.padx, pady=self.pady)

        self.times = ctk.CTkButton(self, text='X', command=lambda: self.mod('x'))
        self.times.grid(row=2, column=3, padx=self.padx, pady=self.pady)

        self.four = ctk.CTkButton(self, text='4', command=lambda: self.update_results('4'))
        self.four.grid(row=3, column=0, padx=self.padx, pady=self.pady)

        self.five = ctk.CTkButton(self, text='5', command=lambda: self.update_results('5'))
        self.five.grid(row=3, column=1, padx=self.padx, pady=self.pady)

        self.six = ctk.CTkButton(self, text='6', command=lambda: self.update_results('6'))
        self.six.grid(row=3, column=2, padx=self.padx, pady=self.pady)

        self.minus = ctk.CTkButton(self, text='-', command=lambda: self.mod('-'))
        self.minus.grid(row=3, column=3, padx=self.padx, pady=self.pady)

        self.one = ctk.CTkButton(self, text='1', command=lambda: self.update_results('1'))
        self.one.grid(row=4, column=0, padx=self.padx, pady=self.pady)

        self.two = ctk.CTkButton(self, text='2', command=lambda: self.update_results('2'))
        self.two.grid(row=4, column=1, padx=self.padx, pady=self.pady)

        self.three = ctk.CTkButton(self, text='3', command=lambda: self.update_results('3'))
        self.three.grid(row=4, column=2, padx=self.padx, pady=self.pady)

        self.plus = ctk.CTkButton(self, text='+', command=lambda: self.mod('+'))
        self.plus.grid(row=4, column=3, padx=self.padx, pady=self.pady)

        self.zero = ctk.CTkButton(self, text='0', command=lambda: self.update_results('0'))
        self.zero.grid(row=5, column=0, columnspan=2, padx=self.padx, pady=self.pady)

        self.period = ctk.CTkButton(self, text='.', command=lambda: self.update_results('.'))
        self.period.grid(row=5, column=2, padx=self.padx, pady=self.pady)

        self.equal = ctk.CTkButton(self, text='=', command= self.calculate)
        self.equal.grid(row=5, column=3, padx=self.padx, pady=self.pady)

    def update_results(self):
        pass

    def clear(self):
        self.resultsText.set('')
        self.x = None
        self.y = None
        self.modulo = ''

    def delete(self):
        pass

    def calculate(self):
        pass


if __name__ == '__main__':
    gui = Gui()
    gui.mainloop()