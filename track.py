class track:
    def __init__(self, name, curr, max):
        self.name = name
        self.curr = curr
        self.max = max

    def add(self, num):
        self.curr += num
        if self.curr >= max:
            self.curr = max
            print(self.name, ": max has been reached.")

    def sub(self, num):
        self.curr -= num
        if self.curr <= 0:
            self.curr = 0
            print(self.name, ": min has been reached.")