import time, random, threading

class CPU:
    def __init__(self):
        pass
    def MULT(self, a, b):
        return a * b
    def DEVIDE(self, a, b):
        return a / b
    def ADD(self, a, b):
        return a + b
    def MINUS(self, a, b):
        return a - b

class GPU:
    def __init__(self, Y=10, X=10):
        self.Y = Y
        self.X = X
        self.lst = []
        for i in range(Y):
            self.lst.append([])
            for i1 in range(X):
                self.lst[i].append([255,255,255])
    # [
    # ["1" x0,"1" x1,"1" x2] - y0
    # ]

    def render(self, X=0, Y=0, rgblist=[255,255,255]):
        self.lst[self.Y][self.X] = rgblist
    def update(self):

        for i in range(self.Y):
            cars = 0
            for i1 in range(self.X):
                half1 = self.lst[i][cars]
                try: eth = half1[2]
                except: half1 = [255,255,255]
                cars+=1
                zeyt = f'\x1b[38;2;{half1[0]};{half1[1]};{half1[2]}m'
                if self.X != i1 and self.Y != i:
                    if len(self.lst[i]) > cars: print(f'{zeyt}█', end="")
                    else: print(f'{zeyt}█')
                else: print(f'{zeyt}█', end="")
    def AlwaysUpdate(self,fps=20):
        simp = 1/fps
        print(simp)
        while True:
            time.sleep(simp)
            ah.update()



ah = GPU(29, 120)
t1 = threading.Thread(target=ah.AlwaysUpdate, args=(1,))
t1.start()
from PIL import Image


im = Image.open(r'C:\\Users\\DemonNSK\\Desktop\\main.png')
px = im.load()
for i in range(29):
    for i1 in range(120):
        ah.lst[i][i1] = px[i1, i]
