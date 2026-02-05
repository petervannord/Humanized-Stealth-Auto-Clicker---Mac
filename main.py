import time
import random
import numpy as np
from scipy import interpolate
import tkinter as tk
from threading import Thread
import Quartz.CoreGraphics as CG

def get_mouse_pos():
    loc = CG.CGEventGetLocation(CG.CGEventCreate(None))
    return loc.x, loc.y

def native_move(x, y):
    move = CG.CGEventCreateMouseEvent(None, CG.kCGEventMouseMoved, (x, y), CG.kCGMouseButtonLeft)
    CG.CGEventPost(CG.kCGHIDEventTap, move)

def native_click(x, y, down=True):
    etype = CG.kCGEventLeftMouseDown if down else CG.kCGEventLeftMouseUp
    click = CG.CGEventCreateMouseEvent(None, etype, (x, y), CG.kCGMouseButtonLeft)
    CG.CGEventPost(CG.kCGHIDEventTap, click)

class GhostClickV4:
    def __init__(self, root):
        self.root = root
        self.root.title("KikiClicker v4.1")
        self.root.geometry("320x260")
        self.root.configure(bg="#000000")
        self.active = False

        # Header
        tk.Label(root, text="Kiki Clicker V4.1", fg="#00FF41", bg="#000000", font=("Arial", 28, "bold")).pack(pady=20)
        
        # Hotkey Label
        tk.Label(root, text="CMD+G to START | CMD+H to STOP", fg="#888", bg="#000000", font=("Arial", 15)).pack()
        tk.Label(root, text="FAIL-SAFE: Slam mouse to TOP-LEFT", fg="#FF3333", bg="#000000", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Input Box
        tk.Label(root, text="Target CPM:", fg="#555", bg="#000000").pack(pady=5)
        self.cpm_entry = tk.Entry(root, justify='center', bg="#111", fg="white", insertbackground="white", highlightthickness=1)
        self.cpm_entry.insert(0, "60")
        self.cpm_entry.pack()

        # Visual Pulse Bar
        self.indicator = tk.Canvas(root, width=200, height=4, bg="#111", highlightthickness=0)
        self.bar = self.indicator.create_rectangle(0, 0, 0, 4, fill="#00FF41")
        self.indicator.pack(pady=30)

        # Bindings
        self.root.bind_all("<Command-g>", lambda e: self.toggle(True))
        self.root.bind_all("<Command-h>", lambda e: self.toggle(False))


    def toggle(self, state):
        self.active = state
        if self.active:
            self.indicator.itemconfig(self.bar, fill="#00FF41")
            Thread(target=self.run_loop, daemon=True).start()
        else:
            self.indicator.itemconfig(self.bar, fill="#FF0000")
            self.indicator.coords(self.bar, 0, 0, 0, 4)

    def move_human(self, x2, y2):
        x1, y1 = get_mouse_pos()
        # Simple Arc for stealth
        pts = np.array([[x1, y1], [x1+(x2-x1)*0.5, y1-5], [x2, y2]])
        tck, u = interpolate.splprep([pts[:,0], pts[:,1]], k=2, s=0)
        new_points = interpolate.splev(np.linspace(0, 1, 8), tck)
        for px, py in zip(new_points[0], new_points[1]):
            native_move(px, py)
            time.sleep(0.002)

    def run_loop(self):
        try:
            while self.active:
                # --- EMERGENCY STOP CHECK ---
                curr_x, curr_y = get_mouse_pos()
                if curr_x <= 2 and curr_y <= 2:
                    print("FAIL-SAFE TRIGGERED")
                    self.root.after(0, lambda: self.toggle(False))
                    break
                # -----------------------------

                cpm = int(self.cpm_entry.get())
                delay = 60 / (cpm + random.uniform(-cpm*0.1, cpm*0.1))
                
                # Visual Pulse
                self.root.after(0, lambda: self.indicator.coords(self.bar, 0, 0, 200, 4))
                
                self.move_human(curr_x + random.randint(-1, 1), curr_y + random.randint(-1, 1))
                
                native_click(curr_x, curr_y, True)
                time.sleep(random.uniform(0.04, 0.07))
                native_click(curr_x, curr_y, False)
                
                self.root.after(100, lambda: self.indicator.coords(self.bar, 0, 0, 0, 4))
                time.sleep(max(0.05, random.gauss(delay, delay*0.1)))
        except:
            self.root.after(0, lambda: self.toggle(False))

if __name__ == "__main__":
    root = tk.Tk()
    app = GhostClickV4(root)
    root.mainloop()

