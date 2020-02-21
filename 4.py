import math
#task 1
class Tribonachi:
    def __init__(self):
        self.lst = [0,0,1]
    def __iter__(self):
        for i in range(0, 36):
            if i < 3:
                yield self.lst[i]
            else:
                self.lst.append((self.lst[i - 1] + self.lst[i - 2] + self.lst[i - 3]))
                yield self.lst[i]
#task2
class Leibnich:
    def __init__(self):
        self.sum = 0
        self.pi = round(math.pi/4,2)
        self.n = 1
        self.x = 0
    def __iter__(self):
        while self.sum !=self.pi:
            self.item = round(self.n/(2*self.x+1),2)
            self.sum+=self.item
            self.sum = round(self.sum,2)
            self.x+=1
            self.n = -1 if self.n == 1 else 1
            yield self.item
t = Tribonachi()
print("Числа Трибоначи")
for i in t:
    print(i)
l = Leibnich()
print("Ряд Лейбница: ")
for i in l:
    print(i)