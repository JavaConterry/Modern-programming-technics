import tkinter as tk
import sys
from password_generator import PasswordGenerator


class Counter:
    # Fields: 
    #   - Text
    # (Buttons)
    #   - Update
    #   - Clear
    #   - Goodbye | close
    # (Slider)
    #   - Slider

    def __init__(self, parent):
	
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.frame.pack()
		
        self.state = tk.IntVar()
        self.state.set(0)
		
        self.label = tk.Label(self.frame, textvariable=self.state)
        self.label.pack()

        self.clr = tk.Button(self.frame, text='clear', command=self.clear_click)
        self.clr.pack(side='left')

        self.right = tk.Button(self.frame, text='Goodbye', command=self.quit_click)
        self.right.pack(side='left')

        self.upd = tk.Button(self.frame, text='Update', command=self.update_password)
        self.upd.pack(side='left')

        current_value = tk.DoubleVar()
        self.slider = tk.Scale(from_=4,to=100,orient='horizontal',variable=current_value, command=self.update_length)
        self.slider.pack(side='left')

    def update_length(self, length):
        self.pass_length = length
        self.update_password()
    def clear_click(self):
        self.state.set(0)		
    def quit_click(self):
        self.parent.destroy()
    def update_password(self):
        self.state.set(PasswordGenerator.new_password(int(self.pass_length)))


if __name__ == '__main__':
    try:
        window = tk.Tk()
        window.geometry('150x150')
        myapp = Counter(window)
        window.mainloop()

        sys.exit(0)
    except:
        print('Exception in interface loop', file=sys.stderr)