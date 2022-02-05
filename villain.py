class villain:
    def __init__(self,name,phase1hp,phase1atk,phase1sch,phase2hp,phase2atk,phase2sch):
        self.name = name
        self.health = phase1hp
        self.atk = phase1atk
        self.sch = phase1sch

        self.nexthp = phase2hp
        self.nextatk = phase2atk
        self.nextsch = phase2sch

        self.phase = 0

    def defeat(self):
        if self.phase == 0:
            self.phase+=1
            self.health = self.nexthp
            self.atk = self.nextatk
            self.sch = self.nextsch
        else:
            print("you win?")