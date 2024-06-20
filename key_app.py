from tkinter import *
import re

class KeyValue:
    def __init__(self):
        self.i = self.i1()
        self.count = self.count11()
        self.z = -1

    def i0(self):
        random = 0
        with open("a.txt", 'r') as a:
            for line in a:
                match = re.findall(r'\d+', line)
                for num in match:
                    if random < int(num):
                        random = int(num)
        return random

    def i1(self):
        random = self.i0()
        count1 = 0
        x = 0
        with open("a.txt", 'r') as a:
            for line in a:
                if str(random) in line:
                    count1 += 1
                    if count1 == 2:
                        x = random + 1
                    else:
                        x = random
        return x

    def count11(self):
        random = self.i1()
        count1 = 0
        x = 0
        with open("a.txt", 'r') as a:
            for line in a:
                if str(random) in line:
                    count1 += 1
                    if count1 == 1:
                        x = 1
                    else:
                        x = 0
        return x

    def set1(self, t1, t2):
        if self.count < 1:
            self.count += 1
            print(self.i)
            with open(f"a{self.i}.txt", 'a') as a:
                a.writelines(f"{t1}:{t2}\n")
            b = self.i
        else:
            self.count = 0
            print(self.i)
            with open(f"a{self.i}.txt", 'a') as a:
                a.writelines(f"{t1}:{t2}\n")
            b = self.i
            self.i += 1

        with open('a.txt', 'a') as d:
            d.writelines(f"{t1}:{b}\n")

    def get(self, t1):
        with open("a.txt", 'r') as a:
            for line in a:
                if t1 in line:
                    parts = line.split(":")
                    if parts[0] == t1:
                        return int(parts[1].strip())
        return -1

    def get1(self, t1):
        getfile = self.get(t1)
        if getfile == -1:
            print("Key not found")
            return
        with open(f"a{getfile}.txt", 'r') as a:
            for line in a:
                if t1 in line:
                    print(line)
                    break

class GUI:
    def __init__(self, root):
        self.kv = KeyValue()
        self.root = root
        self.root.geometry('300x400')
        Label(root, text="key").grid(row=1, column=1)
        self.textbox1 = Entry(root)
        self.textbox1.grid(row=1, column=2)
        Label(root, text="value").grid(row=2, column=1)
        self.textbox2 = Entry(root)
        self.textbox2.grid(row=2, column=2)
        Button(root, text="set", command=self.set1).grid(row=3, column=1)
        Button(root, text="get1", command=self.get1).grid(row=3, column=2)

    def set1(self):
        t1 = self.textbox1.get()
        t2 = self.textbox2.get()
        self.kv.set1(t1, t2)

    def get1(self):
        t1 = self.textbox1.get()
        self.kv.get1(t1)

if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()
