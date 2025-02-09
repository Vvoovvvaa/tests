class Stack:
    def __init__(self, c):
        self.count = c
        self.ml = []

    def push(self, num):
        if len(self.ml) >= self.count:
            print("No space")
        else:
            self.ml.append(num)

    def pop(self):
        if not self.ml:
            print("No Element")
        else:
            return self.ml.pop(0)

    def __str__(self):
        return str(self.ml)

if __name__ == "__main__":
    s = Stack(3)
    s.push(10)
    s.push(12)
    s.push(15)
    s.pop()
    print(s)
