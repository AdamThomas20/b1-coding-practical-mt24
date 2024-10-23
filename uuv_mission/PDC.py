class controller:
    def __init__(self):
          self.KP = 0.1
          self.KD = 0.75
    def control(self, e_t, e_t1):           
            u = self.KP*e_t + self.KD*(e_t-e_t1)
            return u