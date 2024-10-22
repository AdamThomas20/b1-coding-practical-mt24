class controller:
    def __init__(self):
          self.KP = 0.15
          self.KD = 0.6
    def control(self, e_t, e_t1):           
            u = self.KP*e_t + self.KD*(e_t-e_t1)
            return u