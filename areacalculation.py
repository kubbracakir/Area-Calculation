import math
import tkinter as tk

class CircleAreaCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Daire Alanı Hesaplayıcı")

        self.radius_label = tk.Label(master, text="Dairenin Yarıçapı:")
        self.radius_label.pack()

        self.radius_entry = tk.Entry(master)
        self.radius_entry.pack()

        self.calculate_button = tk.Button(master, text="Hesapla", command=self.calculate_area)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_area(self):
        try:
            radius = float(self.radius_entry.get())
            if radius <= 0:
                raise ValueError("Yarıçap pozitif bir sayı olmalıdır.")
            area = math.pi * radius ** 2
            self.result_label.config(text=f"Dairenin Alanı: {area:.2f}")
        except ValueError as e:
            self.result_label.config(text=str(e))

def main():
    root = tk.Tk()
    app = CircleAreaCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()