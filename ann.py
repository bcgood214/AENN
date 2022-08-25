import math, random

class AND:
    def __init__(self, x1, x2, w1, w2, w3):
        self.x1 = x1
        self.x2 = x2
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

    def is_and(self):
        if self.x1 and self.x2:
            return 1
        return 0
    
    def run(self):
        sum = 0
        sum += self.x1 * self.w1
        sum += self.is_and() * self.w2
        sum += self.x2 * self.w3

        return sum

class EA:
    def __init__(self, gens, poolsize, mutrate):
        self.gens = gens
        self.mutrate = mutrate
        self.poolsize = poolsize
    
    def genind(self):
        whole = ['0' for x in range(5)]
        decimal = ['0' for x in range(5)]

        for i in range(len(whole)):
            if random.random() > 0.5:
                whole[i] = '1'
        
        for i in range(len(decimal)):
            if random.random() > 0.5:
                decimal[i] = '1'
        
        return [whole, decimal]
    
    def genpool(self):
        for i in range(self.poolsize):


    def run(self):
        self.pool = self.genpool()
